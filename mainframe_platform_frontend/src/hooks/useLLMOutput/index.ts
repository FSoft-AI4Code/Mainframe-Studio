// @llm-ui/react is support node16, bundler moduleResolution; which is conflict with current module resolution
// use our component for now
import { useCallback, useEffect, useMemo, useRef, useState } from "react";

import { defaultOptions, initialState } from "./constance";
import {
  BlockMatch,
  LLMOutputBlock,
  LLMOutputFallbackBlock,
  LLMOutputMatch,
  LLMOutputProps,
  MatchWithLLMOutput,
  ThrottleBasicOptions,
  ThrottleFunction,
  UseLLMOutputReturn
} from "./type";

const matchesToVisibleText = (matches: BlockMatch[]): string => {
  return matches.map(match => match.visibleText).join("");
};

const matchesToOutput = (matches: BlockMatch[]): string => {
  return matches.map(match => match.output).join("");
};

const calcPercentage = ({
  isBehind,
  adjustPercentage,
  isStreamFinished
}: {
  isBehind: boolean;
  adjustPercentage: number;
  isStreamFinished: boolean;
}) => {
  if (isStreamFinished) {
    return 1;
  }
  if (isBehind) {
    return 1 - adjustPercentage;
  }
  return 1 + adjustPercentage;
};

const getVisibleTextEveryNFrames = (
  lookbackFrameCount: number,
  windowLookBackCount: number,
  visibleTextLengthsAllOriginal: number[]
) => {
  const visibleTextLengthsAll = [0, ...visibleTextLengthsAllOriginal];
  const lookbackFrames = Math.min(lookbackFrameCount, visibleTextLengthsAll.length);
  const windowFrames = Math.min(windowLookBackCount, visibleTextLengthsAll.length);
  const recentVisibleTextLengths = visibleTextLengthsAll.slice(-1 * lookbackFrames);
  const textAddedCounts = [];
  if (windowFrames > 0) {
    for (let start = 0; start < recentVisibleTextLengths.length - windowFrames + 1; start++) {
      const end = start + windowFrames - 1;
      const textAddedCount = recentVisibleTextLengths[end] - recentVisibleTextLengths[start];
      textAddedCounts.push(textAddedCount);
    }
  }
  const avgTextAddedCount = textAddedCounts.reduce((a, b) => a + b, 0) / textAddedCounts.length;
  const result = avgTextAddedCount > 0 ? windowFrames / avgTextAddedCount : windowFrames;
  return result;
};

const throttleBasic = (userOptions: Partial<ThrottleBasicOptions> = {}): ThrottleFunction => {
  const { frameLookBackMs, targetBufferChars, readAheadChars, adjustPercentage, windowLookBackMs } =
    {
      ...defaultOptions,
      ...userOptions
    };

  return ({
    visibleText,
    isStreamFinished,
    visibleTextAll,
    visibleTextLengthsAll,
    frameCount,
    visibleTextIncrements,
    visibleTextLengthTarget,
    startStreamTime
  }) => {
    const timeSinceStartMs = performance.now() - startStreamTime;
    const timeSinceStartSec = timeSinceStartMs / 1e3;
    const fps = frameCount / timeSinceStartSec;
    const bufferSize = visibleTextAll.length - visibleTextLengthTarget;
    const lookbackFrameCount = Math.ceil(frameLookBackMs / (1e3 / fps));
    const windowLookBackCount = Math.ceil(windowLookBackMs / (1e3 / fps));
    const visibleTextEveryNFrames = getVisibleTextEveryNFrames(
      lookbackFrameCount,
      windowLookBackCount,
      visibleTextLengthsAll
    );
    let framesSinceLastIncrement = [...visibleTextIncrements].reverse().findIndex(inc => inc > 0);
    framesSinceLastIncrement =
      framesSinceLastIncrement === -1 ? frameCount : framesSinceLastIncrement;
    let visibleTextIncrement = 0;
    const targetBufferSize = readAheadChars + targetBufferChars;
    if (
      (!isStreamFinished &&
        (bufferSize < readAheadChars ||
          (visibleText.length === 0 && bufferSize < targetBufferSize))) ||
      visibleTextLengthTarget >= visibleTextAll.length
    ) {
      visibleTextIncrement = 0;
    } else {
      const targetBufferSize2 = readAheadChars + targetBufferChars;
      const isBehind = bufferSize > targetBufferSize2;
      const targetFrameEveryN =
        visibleTextEveryNFrames * calcPercentage({ adjustPercentage, isBehind, isStreamFinished });
      if (targetFrameEveryN > 1) {
        visibleTextIncrement = framesSinceLastIncrement >= targetFrameEveryN ? 1 : 0;
      } else {
        visibleTextIncrement = Math.round(1 / targetFrameEveryN);
      }
    }
    return {
      visibleTextIncrement
    };
  };
};

const byMatchStartIndex = (match1: MatchWithLLMOutput, match2: MatchWithLLMOutput) =>
  match1.match.startIndex - match2.match.startIndex;

const fallbacksInGaps = ({
  blockMatches,
  llmOutput,
  fallbackPriority,
  fallbackBlock
}: {
  blockMatches: MatchWithLLMOutput[];
  llmOutput: string;
  fallbackPriority: number;
  fallbackBlock: LLMOutputFallbackBlock;
}) => {
  const fallbacks = blockMatches
    .map((match, index) => {
      const previousMatchEndIndex = index === 0 ? 0 : blockMatches[index - 1].match.endIndex;
      if (previousMatchEndIndex < match.match.startIndex) {
        const outputRaw = llmOutput.slice(previousMatchEndIndex, match.match.startIndex);
        return {
          block: fallbackBlock,
          match: {
            startIndex: previousMatchEndIndex,
            endIndex: match.match.startIndex,
            outputRaw
          },
          priority: fallbackPriority,
          llmOutput,
          isComplete: true
        };
      }
      return void 0;
    })
    .filter(match => match !== void 0);
  const lastMatchEndIndex =
    blockMatches.length > 0 ? blockMatches[blockMatches.length - 1].match.endIndex : 0;
  if (lastMatchEndIndex < llmOutput.length) {
    const outputRaw = llmOutput.slice(lastMatchEndIndex, llmOutput.length);
    fallbacks.push({
      block: fallbackBlock,
      match: {
        startIndex: lastMatchEndIndex,
        endIndex: llmOutput.length,
        outputRaw
      },
      priority: fallbackPriority,
      llmOutput,
      isComplete: false
    });
  }
  return fallbacks;
};

const isOverlapping = (match1: LLMOutputMatch, match2: LLMOutputMatch) => {
  return (
    (match1.startIndex >= match2.startIndex && match1.startIndex < match2.endIndex) || // match1 starts inside match2
    (match1.endIndex > match2.startIndex && match1.endIndex <= match2.endIndex) || // match1 ends inside match2
    (match2.startIndex >= match1.startIndex && match2.startIndex < match1.endIndex) || // match2 starts inside match1
    (match2.endIndex > match1.startIndex && match2.endIndex <= match1.endIndex)
  );
};

const highestPriorityNonOverlappingMatches = (
  matches: Array<MatchWithLLMOutput>
): Array<MatchWithLLMOutput> => {
  return matches.filter(match => {
    const higherPriorityMatches = matches.filter(m => m.priority < match.priority);
    return !higherPriorityMatches.some(m => isOverlapping(m.match, match.match));
  });
};

const completeMatchesForBlock = ({
  llmOutput,
  block,
  priority
}: {
  llmOutput: string;
  block: LLMOutputBlock;
  priority: number;
}): Array<MatchWithLLMOutput> => {
  const matches = [];
  let index = 0;
  while (index < llmOutput.length) {
    const nextMatch = block.findCompleteMatch(llmOutput.slice(index));
    if (nextMatch) {
      matches.push({
        block,
        match: {
          outputRaw: nextMatch.outputRaw,
          startIndex: index + nextMatch.startIndex,
          endIndex: index + nextMatch.endIndex
        },
        llmOutput,
        isComplete: true,
        priority
      });
      index += nextMatch.endIndex;
    } else {
      return matches;
    }
  }
  return matches;
};

const findPartialMatch = ({
  llmOutput,
  blocks,
  currentIndex
}: {
  llmOutput: string;
  blocks: LLMOutputBlock[];
  currentIndex: number;
}) => {
  for (const [priority, block] of Array.from(blocks.entries())) {
    const outputRaw = llmOutput.slice(currentIndex);
    const partialMatch = block.findPartialMatch(outputRaw);
    if (partialMatch) {
      return {
        block,
        match: {
          outputRaw: partialMatch.outputRaw,
          startIndex: partialMatch.startIndex + currentIndex,
          endIndex: partialMatch.endIndex + currentIndex
        },
        llmOutput,
        isComplete: true,
        priority
      };
    }
  }
  return void 0;
};

const matchesWithLookback = ({
  matches,
  visibleTextLengthTarget,
  isStreamFinished
}: {
  matches: any[];
  visibleTextLengthTarget: number;
  isStreamFinished: boolean;
}): BlockMatch[] => {
  return matches.reduce((acc: BlockMatch[], match, index) => {
    const visibleTextSoFar = acc.map(m => m.visibleText.length).reduce((a, b) => a + b, 0);
    const localVisibleTextLengthTarget = Math.max(visibleTextLengthTarget - visibleTextSoFar, 0);
    const isLastMatch = index === matches.length - 1;
    const isComplete = !isLastMatch || isStreamFinished;
    const { output, visibleText } = match.block.lookBack({
      isComplete,
      visibleTextLengthTarget: localVisibleTextLengthTarget,
      isStreamFinished,
      output: match.match.outputRaw
    });
    const matchWithLookback = {
      ...match.match,
      isComplete,
      block: match.block,
      priority: match.priority,
      llmOutput: match.llmOutput,
      output,
      visibleText,
      isVisible: visibleText.length > 0
    };
    return [...acc, matchWithLookback];
  }, []);
};

const matchBlocks = ({
  llmOutput,
  blocks,
  fallbackBlock,
  isStreamFinished,
  visibleTextLengthTarget = Number.MAX_SAFE_INTEGER
}: {
  llmOutput: string;
  blocks: LLMOutputBlock[];
  fallbackBlock: LLMOutputFallbackBlock;
  isStreamFinished: boolean;
  visibleTextLengthTarget?: number;
}) => {
  const allCompleteMatches = blocks.flatMap((block, priority) =>
    completeMatchesForBlock({
      llmOutput,
      block,
      priority
    })
  );
  const matches = highestPriorityNonOverlappingMatches(allCompleteMatches);
  matches.sort(byMatchStartIndex);
  const lastMatchEndIndex = matches.length > 0 ? matches[matches.length - 1].match.endIndex : 0;
  const partialMatch = !isStreamFinished
    ? findPartialMatch({
        llmOutput,
        currentIndex: lastMatchEndIndex,
        blocks
      })
    : void 0;
  if (partialMatch) {
    matches.push(partialMatch);
  }
  const fallBacks = fallbacksInGaps({
    blockMatches: matches,
    llmOutput,
    fallbackPriority: blocks.length,
    fallbackBlock
  });
  for (const fallBack of fallBacks) {
    if (!fallBack) continue;
    matches.push(fallBack);
  }
  matches.sort(byMatchStartIndex);
  return matchesWithLookback({
    matches,
    isStreamFinished,
    visibleTextLengthTarget
  });
};

export const useLLMOutput = ({
  llmOutput,
  isStreamFinished,
  blocks = [],
  fallbackBlock,
  throttle = throttleBasic(),
  onFinish = () => null
}: LLMOutputProps): UseLLMOutputReturn => {
  const startTime = useRef(performance.now());
  const lastRenderTime = useRef(performance.now());
  const renderLoopRef = useRef<FrameRequestCallback>();
  const frameRef = useRef<number>();
  const frameCountRef = useRef(0);
  const finishTimeRef = useRef<number>();
  const previousFrameTimeRef = useRef<number>();
  const visibleTextAllLengthsRef = useRef<number[]>([]);
  const outputLengthsRef = useRef<number[]>([]);
  const visibleTextIncrementsRef = useRef<number[]>([]);
  const visibleTextLengthTargetRef = useRef(0);
  const memoMatchBlocks = useMemo(() => {
    return matchBlocks({
      llmOutput,
      blocks,
      fallbackBlock,
      isStreamFinished
    });
  }, [llmOutput, isStreamFinished]);
  const [{ blockMatches, ...state }, setState] = useState({
    ...initialState,
    finishCount: 0,
    blockMatches: memoMatchBlocks
  });
  const reset = useCallback(() => {
    setState(state2 => ({ ...state2, ...initialState }));
    startTime.current = performance.now();
    finishTimeRef.current = void 0;
    previousFrameTimeRef.current = void 0;
    visibleTextAllLengthsRef.current = [];
    outputLengthsRef.current = [];
    visibleTextIncrementsRef.current = [];
    visibleTextLengthTargetRef.current = 0;
    frameCountRef.current = 0;
    if (frameRef.current) {
      cancelAnimationFrame(frameRef.current);
      frameRef.current = void 0;
    }
  }, [setState]);
  const restart = useCallback(() => {
    reset();
    setTimeout(() => {
      if (renderLoopRef.current) {
        frameRef.current = requestAnimationFrame(renderLoopRef.current);
      }
    }, 10);
  }, [reset]);
  const renderLoop = (frameTime: number) => {
    if (!renderLoopRef.current) {
      return;
    }
    const allMatches = matchBlocks({
      llmOutput,
      blocks,
      fallbackBlock,
      isStreamFinished
    });
    const visibleText = matchesToVisibleText(blockMatches);
    const outputRendered = matchesToOutput(blockMatches);
    const visibleTextAll = matchesToVisibleText(allMatches);
    const outputAll = matchesToOutput(allMatches);
    if (!isStreamFinished) {
      visibleTextAllLengthsRef.current.push(visibleTextAll.length);
      outputLengthsRef.current.push(outputAll.length);
    }
    const isFinished = visibleText === visibleTextAll && isStreamFinished;
    if (isFinished) {
      frameRef.current = void 0;
      setState(state2 => ({
        ...state2,
        blockMatches,
        isFinished,
        finishCount: state2.finishCount + 1,
        visibleText
      }));
      onFinish();
      return;
    }
    const visibleTextLengthsAll = isStreamFinished
      ? [...visibleTextAllLengthsRef.current, visibleTextAll.length]
      : visibleTextAllLengthsRef.current;
    const outputLengths = isStreamFinished
      ? [...outputLengthsRef.current, outputAll.length]
      : outputLengthsRef.current;
    const { visibleTextIncrement } = throttle({
      outputRaw: llmOutput,
      outputRendered,
      outputAll,
      visibleText,
      visibleTextAll,
      startStreamTime: startTime.current,
      isStreamFinished,
      frameCount: frameCountRef.current,
      frameTime,
      frameTimePrevious: previousFrameTimeRef.current,
      finishStreamTime: finishTimeRef.current,
      visibleTextLengthsAll,
      outputLengths,
      visibleTextIncrements: visibleTextIncrementsRef.current,
      visibleTextLengthTarget: visibleTextLengthTargetRef.current
    });
    if (visibleTextIncrement < 0) {
      throw new Error("throttle returned negative visibleTextIncrement");
    }
    visibleTextIncrementsRef.current.push(visibleTextIncrement);
    visibleTextLengthTargetRef.current = visibleTextLengthTargetRef.current + visibleTextIncrement;
    if (visibleTextLengthTargetRef.current > visibleText.length) {
      const matches = matchBlocks({
        llmOutput,
        blocks,
        fallbackBlock,
        isStreamFinished,
        visibleTextLengthTarget: visibleTextLengthTargetRef.current
      });
      const updatedVisibleText = matchesToVisibleText(matches);
      lastRenderTime.current = performance.now();
      setState(state2 => ({
        ...state2,
        blockMatches: matches,
        isFinished,
        visibleText: updatedVisibleText
      }));
    }
    frameRef.current = requestAnimationFrame(renderLoopRef.current);
    previousFrameTimeRef.current = frameTime;
    frameCountRef.current = frameCountRef.current + 1;
  };
  useEffect(() => {
    renderLoopRef.current = renderLoop;
  });
  useEffect(() => {
    renderLoopRef.current = renderLoop;
    if (!frameRef.current && llmOutput && llmOutput.length > 0) {
      frameRef.current = requestAnimationFrame(renderLoopRef.current);
    } else if (
      // reset the render loop if user clears the llmOutput
      visibleTextIncrementsRef.current.length > 0 &&
      llmOutput.length === 0
    ) {
      reset();
    }
  }, [llmOutput]);
  useEffect(() => {
    // eslint-disable-next-line @typescript-eslint/no-unused-expressions
    () => {
      if (frameRef.current) {
        cancelAnimationFrame(frameRef.current);
      }
    };
  }, []);
  useEffect(() => {
    if (!finishTimeRef.current && isStreamFinished) {
      finishTimeRef.current = performance.now();
    }
  }, [isStreamFinished]);
  return { blockMatches, restart, ...state };
};
