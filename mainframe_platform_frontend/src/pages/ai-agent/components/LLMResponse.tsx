import { codeBlockLookBack, findCompleteCodeBlock, findPartialCodeBlock } from "@llm-ui/code";
// import { useLLMOutput } from "@llm-ui/react";
import { markdownLookBack } from "@llm-ui/markdown";

import { useLLMOutput } from "../../../hooks/useLLMOutput";

import { CodeBlock } from "./CodeBlock";
import { MarkdownComponent } from "./MarkdownComponent";

export const LLMResponse = ({
  response,
  isStreamFinished = false
}: {
  response: string;
  isStreamFinished?: boolean;
}) => {
  const { blockMatches } = useLLMOutput({
    llmOutput: response,
    fallbackBlock: {
      component: MarkdownComponent, // from Step 1
      lookBack: markdownLookBack()
    },
    blocks: [
      {
        component: CodeBlock, // from Step 2
        findCompleteMatch: findCompleteCodeBlock(),
        findPartialMatch: findPartialCodeBlock(),
        lookBack: codeBlockLookBack()
      }
    ],
    isStreamFinished
  });

  return (
    <>
      {blockMatches.map((blockMatch, index) => {
        const Component = blockMatch.block.component;
        return <Component key={index} blockMatch={blockMatch} />;
      })}
    </>
  );
};
