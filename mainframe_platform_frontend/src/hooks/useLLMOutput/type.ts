type LLMOutputMatch = {
  startIndex: number;
  endIndex: number;
  outputRaw: string;
};
type BlockMatch = MatchBase & LLMOutputMatchWithLookBack;
type MatchBase = {
  block: LLMOutputFallbackBlock;
  priority: number;
  llmOutput: string;
  isComplete: boolean;
};
type MatchWithLLMOutput = MatchBase & { match: LLMOutputMatch };
type LLMOutputMatchWithLookBack = LLMOutputMatch & {
  output: string;
  visibleText: string;
  isVisible: boolean;
};
type MaybeLLMOutputMatch = LLMOutputMatch | undefined;
type LLMOutputComponent<Props = unknown> = React.FC<
  Props & {
    blockMatch: BlockMatch;
  }
>;
type LLMOutputMatcher = (llmOutput: string) => MaybeLLMOutputMatch;
type LookBack = {
  output: string;
  visibleText: string;
};
type LookBackFunctionParams = {
  output: string;
  isComplete: boolean;
  visibleTextLengthTarget: number;
  isStreamFinished: boolean;
};
type LookBackFunction = (params: LookBackFunctionParams) => LookBack;
type LLMOutputFallbackBlock = {
  component: LLMOutputComponent;
  lookBack: LookBackFunction;
};
type LLMOutputBlock = {
  findPartialMatch: LLMOutputMatcher;
  findCompleteMatch: LLMOutputMatcher;
} & LLMOutputFallbackBlock;
type ThrottleParams = {
  outputRaw: string;
  outputRendered: string;
  outputAll: string;
  visibleText: string;
  visibleTextAll: string;
  isStreamFinished: boolean;
  frameCount: number;
  frameTime: DOMHighResTimeStamp;
  frameTimePrevious: DOMHighResTimeStamp | undefined;
  startStreamTime: DOMHighResTimeStamp;
  finishStreamTime: DOMHighResTimeStamp | undefined;
  visibleTextLengthsAll: number[];
  outputLengths: number[];
  visibleTextIncrements: number[];
  visibleTextLengthTarget: number;
};
type ThrottleResponse = {
  visibleTextIncrement: number;
};
type ThrottleFunction = (params: ThrottleParams) => ThrottleResponse;

type LLMOutputProps = {
  llmOutput: string;
  blocks?: LLMOutputBlock[];
  fallbackBlock: LLMOutputFallbackBlock;
  isStreamFinished: boolean;
  throttle?: ThrottleFunction;
  onFinish?: () => void;
};
type UseLLMOutputReturn = {
  blockMatches: BlockMatch[];
  isFinished: boolean;
  finishCount: number;
  visibleText: string;
  restart: () => void;
};
declare const useLLMOutput: ({
  llmOutput,
  isStreamFinished,
  blocks,
  fallbackBlock,
  throttle,
  onFinish
}: LLMOutputProps) => UseLLMOutputReturn;

type TokenWithDelay = {
  token: string;
  delayMs: number;
};
type Probability = {
  prob: number;
};
type TokenProbability = {
  tokenChars: number;
} & Probability;
type DelayProbability = {
  delayMs: number;
} & Probability;
type ProbabilityOptions = {
  tokenCharsProbabilities: TokenProbability[];
  delayMsProbabilities: DelayProbability[];
};
type UseStreamWithProbabilitiesOptions = UseStreamTokenArrayOptions & ProbabilityOptions;
type UseStreamResponse = {
  output: string;
  reset: () => void;
  pause: () => void;
  start: () => void;
  isStreamStarted: boolean;
  isStreamFinished: boolean;
  isPlaying: boolean;
};
type UseStreamTokenArrayOptions = {
  autoStart: boolean;
  autoStartDelayMs: number;
  startIndex: number;
  delayMultiplier: number;
};

declare const stringToTokenArray: (
  llmOutput: string,
  { tokenCharsProbabilities, delayMsProbabilities }: ProbabilityOptions
) => TokenWithDelay[];

declare const useStreamTokenArrayOptionsDefaultOptions: UseStreamTokenArrayOptions;
declare const useStreamTokenArray: (
  tokenArray: TokenWithDelay[],
  userOptions?: Partial<UseStreamTokenArrayOptions>
) => UseStreamResponse;

declare const useStreamWithProbabilitiesDefaultOptions: UseStreamWithProbabilitiesOptions;
declare const useStreamWithProbabilities: (
  output: string,
  userOptions?: Partial<UseStreamWithProbabilitiesOptions>
) => UseStreamResponse;

type ThrottleBasicOptions = {
  readAheadChars: number;
  targetBufferChars: number;
  adjustPercentage: number;
  frameLookBackMs: number;
  windowLookBackMs: number;
};
declare const defaultOptions: ThrottleBasicOptions;
declare const throttleBasic: (userOptions?: Partial<ThrottleBasicOptions>) => ThrottleFunction;

export {
  stringToTokenArray,
  throttleBasic,
  defaultOptions as throttleBasicDefaultOptions,
  useLLMOutput,
  useStreamWithProbabilities as useStreamExample,
  useStreamTokenArray,
  useStreamTokenArrayOptionsDefaultOptions,
  useStreamWithProbabilities,
  useStreamWithProbabilitiesDefaultOptions,
  type BlockMatch,
  type DelayProbability,
  type LLMOutputBlock,
  type LLMOutputComponent,
  type LLMOutputFallbackBlock,
  type LLMOutputMatch,
  type LLMOutputMatcher,
  type LLMOutputProps,
  type LookBack,
  type LookBackFunction,
  type LookBackFunctionParams,
  type MaybeLLMOutputMatch,
  type Probability,
  type ProbabilityOptions,
  type ThrottleBasicOptions,
  type ThrottleFunction,
  type ThrottleParams,
  type ThrottleResponse,
  type TokenProbability,
  type TokenWithDelay,
  type UseLLMOutputReturn,
  type UseStreamResponse,
  type UseStreamTokenArrayOptions,
  type UseStreamWithProbabilitiesOptions,
  type MatchWithLLMOutput
};
