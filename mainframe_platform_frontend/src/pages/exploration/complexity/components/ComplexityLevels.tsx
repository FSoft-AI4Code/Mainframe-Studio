import { Bar } from "react-chartjs-2";

import { allColors } from "@style";
import { Flex, Typography } from "@components";
import { DotSvg } from "@assets/svg";

type ComplexityData = Record<"simple" | "medium" | "complex" | "veryComplex", number[]>;

export function ComplexityLevels({ data }: { data: ComplexityData }) {
  return (
    <Flex
      style={{ background: allColors.neutral1, padding: 16, borderRadius: "8px", flex: "1 1 0%" }}
      gap={16}
      direction='column'
      center
    >
      <Flex style={{ width: "100%" }}>
        <Typography level='body-16b' color='primary10'>
          Complexity Levels by File Types
        </Typography>
      </Flex>
      <Flex center style={{ width: "80%" }}>
        <Bar
          options={{
            aspectRatio: 4,
            interaction: {
              intersect: false,
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
            datasets: Object.entries(data).map(([key, value]) => ({
              data: value,
              backgroundColor:
                key === "simple"
                  ? allColors.brand1
                  : key === "medium"
                  ? allColors.brand2
                  : key === "complex"
                  ? allColors.brand3
                  : allColors.brand6,
              categoryPercentage: 0.4
            }))
          }}
        />
      </Flex>
      <Flex gap={15} center>
        <Flex center gap={3}>
          <DotSvg fill={allColors.brand1} />
          <Typography level='button-12m' color='primary10'>
            Low
          </Typography>
        </Flex>
        <Flex center gap={3}>
          <DotSvg fill={allColors.brand2} />
          <Typography level='button-12m' color='primary10'>
            Medium
          </Typography>
        </Flex>
        <Flex center gap={3}>
          <DotSvg fill={allColors.brand3} />
          <Typography level='button-12m' color='primary10'>
            Complex
          </Typography>
        </Flex>
        <Flex center gap={3}>
          <DotSvg fill={allColors.brand6} />
          <Typography level='button-12m' color='primary10'>
            Very Complex
          </Typography>
        </Flex>
      </Flex>
    </Flex>
  );
}
