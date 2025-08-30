import { OverflowEmpty } from "@components";
import { LLMResponse } from "@pages/chatbot/components/LLMResponse";

export default function ScreenLayoutBMS({
  screen_string,
  loading
}: {
  screen_string: string;
  loading?: boolean;
}) {
  if (loading || !screen_string) return <OverflowEmpty />;
  return (
    <LLMResponse key={screen_string} response={`\`\`\`cobol\n${screen_string}`} isStreamFinished />
  );
}
