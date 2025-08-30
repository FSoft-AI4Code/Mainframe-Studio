import { Flex, Typography } from "@components";
import { allColors } from "@style";

import { useIncrementalNumber } from "../../../../hooks/app";

export function TotalFile({ totalFile }: { totalFile: number }) {
  const incrementalNumber = useIncrementalNumber(totalFile);

  return (
    <Flex
      gap={16}
      style={{
        padding: 16,
        background: allColors.neutral1,
        width: "25%",
        borderRadius: 8
      }}
      direction='column'
    >
      <Typography level='body-16b' color='primary10'>
        Total Datasets
      </Typography>
      <Flex
        style={{
          borderRadius: 8,
          background: allColors.neutral3,
          padding: "16px 20px",
          height: 64
        }}
        center
      >
        <Typography level='title-24b' color='primary6'>
          {incrementalNumber.toLocaleString()}
        </Typography>
      </Flex>
    </Flex>
  );
}
