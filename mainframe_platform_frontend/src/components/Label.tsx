import { allColors } from "@style";
import { DotSvg } from "@assets/svg";
import { RepositoryStatusEnum } from "@types";

import { Flex, Typography } from "./ui";

export function StatusLabel({ status }: { status: keyof typeof RepositoryStatusEnum }) {
  const colors = [
    "rgba(191, 90, 242, 1)",
    "lime",
    "yellow",
    "blue",
    "cyan",
    "blue",
    "green",
    "blue",
    "geekblue",
    "magenta",
    "volcano",
    "gold"
  ];
  const currentColor = colors[RepositoryStatusEnum[status]] || colors[0];

  return (
    <Flex
      style={{
        width: "max-content",
        height: 24,
        padding: "4px",
        background: allColors.neutral3,
        borderRadius: "24px"
      }}
      gap={6}
      align='center'
    >
      <DotSvg width={12} height={11} fill={currentColor} />
      <Typography level='caption-12r' color='primary10'>
        {`${status.charAt(0).toUpperCase()}${status.slice(1)}`}
      </Typography>
    </Flex>
  );
}
