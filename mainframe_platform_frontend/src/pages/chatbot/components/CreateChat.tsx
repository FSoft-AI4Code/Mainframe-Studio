import { BigChatSvg, CirclePlusSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { allColors } from "@style";

export function CreateChat() {
  return (
    <Flex
      center
      style={{ width: 320, height: 320, background: allColors.neutral1, borderRadius: "50%" }}
      gap={16}
      direction='column'
    >
      <BigChatSvg />
      <Flex
        center
        gap={6}
        style={{ borderRadius: "8px", background: allColors.primary6, padding: "6px 16px" }}
      >
        <CirclePlusSvg />
        <Typography color='neutral1' level='button-16s'>
          New Chat
        </Typography>
      </Flex>
    </Flex>
  );
}
