import { Bar } from "react-chartjs-2";

import { allColors } from "@style";
import { Flex, Typography } from "@components";

export type MeanComplexityData = Record<"cobol" | "jcl" | "copybook" | "screen", number>;

export function MeanComplexity({ data }: { data: MeanComplexityData }) {
  return (
    <Flex
      style={{ background: allColors.neutral1, padding: 16, borderRadius: "8px" }}
      gap={16}
      direction='column'
      center
    >
      <Flex style={{ width: "100%" }}>
        <Typography level='body-16b' color='primary10'>
          Total Complexity by File Type
        </Typography>
      </Flex>
      <Flex center style={{ width: "70%" }}>
        <Bar
          options={{
            interaction: {
              mode: "index"
            },
            plugins: {
              tooltip: {
                padding: { top: 4, right: 8, bottom: 4, left: 8 },
                cornerRadius: 4,
                backgroundColor: allColors.primary3,
                bodyColor: allColors.primary10,
                callbacks: {
                  title: () => ""
                }
              }
            }
          }}
          data={{
            labels: ["COBOL", "JCL", "COPYBOOK", "SCREEN"],
            datasets: [
              {
                data: Object.values(data).map(value => value.toFixed(2)),
                backgroundColor: [
                  allColors.brand1,
                  allColors.brand2,
                  allColors.brand3,
                  allColors.brand4
                ],
                borderColor: allColors.secondary10,
                borderWidth: 1,
                hoverBorderColor: allColors.secondary9,
                borderRadius: { topLeft: 6, topRight: 6, bottomLeft: 6, bottomRight: 6 },
                borderSkipped: false,
                barThickness: 50
              }
            ]
          }}
        />
      </Flex>
      {/* <Flex gap={15} center>
        <Flex center gap={3}>
          <DotSvg fill={allColors.brand1} />
          <Typography level='button-12m' color='primary10'>
            COBOL
          </Typography>
        </Flex>
        <Flex center gap={3}>
          <DotSvg fill={allColors.brand2} />
          <Typography level='button-12m' color='primary10'>
            JCL
          </Typography>
        </Flex>
        <Flex center gap={3}>
          <DotSvg fill={allColors.brand3} />
          <Typography level='button-12m' color='primary10'>
            COPYBOOK
          </Typography>
        </Flex>
        <Flex center gap={3}>
          <DotSvg fill={allColors.brand4} />
          <Typography level='button-12m' color='primary10'>
            SCREEN
          </Typography>
        </Flex>
      </Flex> */}
    </Flex>
  );
}
