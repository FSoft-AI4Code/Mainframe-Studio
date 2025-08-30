import { Flex, Typography } from "@components";
import { allColors } from "@style";

import { useIncrementalNumber } from "../../../../hooks/app";

export function TotalLOC({ totalLOC, totalFile }: { totalLOC: number; totalFile: number }) {
  const incTotalLOC = useIncrementalNumber(totalLOC);
  const incTotalFile = useIncrementalNumber(totalFile);

  return (
    <Flex
      style={{
        padding: 24,
        background: allColors.neutral1,
        borderRadius: 8,
        flex: 1
      }}
      direction='column'
      gap={20}
    >
      <Flex gap={16} direction='column'>
        <Typography level='body-16b' color='primary10'>
          Total Lines of Code
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
            {incTotalLOC.toLocaleString()}
          </Typography>
        </Flex>
      </Flex>
      <Flex gap={16} direction='column'>
        <Typography level='body-16b' color='primary10'>
          Total File Source
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
            {incTotalFile.toLocaleString()}
          </Typography>
        </Flex>
      </Flex>
    </Flex>
  );
}
