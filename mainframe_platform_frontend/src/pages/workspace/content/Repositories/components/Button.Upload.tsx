import { Flex, Typography } from "@components";
import { CirclePlusSvg } from "@assets/svg";

import { ButtonWrapper } from "../styles";

export function UploadButton({ onClick, title }: { onClick: () => void; title: string }) {
  return (
    <ButtonWrapper align='center' gap={8} disabled={false} onClick={onClick}>
      <Flex center style={{ width: 28, height: 28 }}>
        <CirclePlusSvg />
      </Flex>
      <Typography style={{ whiteSpace: "nowrap" }} level='link-16m' color='neutral1'>
        {title}
      </Typography>
    </ButtonWrapper>
  );
}
