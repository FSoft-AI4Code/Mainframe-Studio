import { Fragment } from "react";

import { Flex, Typography } from "@components";
import { useMessages } from "@pages/workspace/WorkspacePage";

import { ParagraphLevel } from "../fake/blob";

const ProgramCall = ({ text }: { text: string }) => {
  // Regular expression to match text and multiple [label]<value> pairs
  const regex = /(.*?)\s*\[(.*?)\]<([^>]+)>/g;
  const matches = [...text.matchAll(regex)];

  // Extract the last piece of text after the final match
  const lastMatch = matches[matches.length - 1];
  const lastTextIndex = lastMatch ? (lastMatch.index ?? 0) + lastMatch[0].length : 0;
  const trailingText = text.slice(lastTextIndex).trim();

  return matches.length > 0 ? (
    <div style={{ whiteSpace: "normal" }}>
      {/* Loop over each match to render the extracted parts */}
      {matches.map((match, index) => (
        <Fragment key={index}>
          {/* Display the preceding text */}
          <Typography level='body-16r' color='primary10' style={{ display: "inline" }}>
            {match[1]}
          </Typography>{" "}
          {/* Display the label with an onClick event */}
          <Typography
            level='body-16r'
            color='primary6'
            onClick={() => {
              const session = document.getElementById(match[3]);

              session?.scrollIntoView({ behavior: "smooth" });
            }}
            style={{ cursor: "pointer", display: "inline" }}
          >
            {match[2]}
          </Typography>{" "}
        </Fragment>
      ))}

      {/* Display any remaining text after the last [label]<value> pair */}
      {trailingText && (
        <Typography level='body-16r' color='primary10' style={{ display: "inline" }}>
          {trailingText}
        </Typography>
      )}
    </div>
  ) : (
    <Typography level='body-16r' color='primary10'>
      {text}
    </Typography>
  );
};

const ProgramBlock = ({ block }: { block: ParagraphLevel | null }) => {
  const displayedLogic = block?.paragraph_logic ?? [];
  const { setMessages } = useMessages();

  return block ? (
    <Flex gap={8} direction='column' id={block.paragraph_name}>
      <Flex
        align='center'
        justify='space-between'
        style={{ cursor: "pointer" }}
        onClick={() => {
          setMessages(prev => [
            { role: "user", content: `\`\`\`cobol\n ${block.paragraph_code}\`\`\`` },
            ...prev
          ]);
        }}
      >
        <Typography level='body-16m' color='neutral10'>
          {block.paragraph_name}
        </Typography>
      </Flex>
      <Flex direction='column' style={{ padding: "0 16px" }} gap={8}>
        {displayedLogic.map(logic => (
          <Flex key={logic} align='center' justify='space-between'>
            <ProgramCall text={logic} />
          </Flex>
        ))}
      </Flex>
    </Flex>
  ) : null;
};

const ProgramProcessLogicPage = ({
  programLogic
}: {
  programLogic: Record<string, ParagraphLevel>;
}) => {
  return (
    <Flex gap={8} direction='column'>
      {Object.values(programLogic).map((block, index) => (
        <ProgramBlock block={block} key={`${block.paragraph_name}-${index}`} />
      ))}
    </Flex>
  );
};

export default ProgramProcessLogicPage;
