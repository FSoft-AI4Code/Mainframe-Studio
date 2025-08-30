import { Bar } from "react-chartjs-2";

import { Flex, XYChartSkeleton } from "@components";
import { allColors } from "@style";
import { DistComplexity } from "@types";
interface ComplexityDistributionProps {
  data: DistComplexity;
  loading?: boolean;
}

export function ComplexityDistribution({ data, loading }: ComplexityDistributionProps) {
  const { bins, frequencies } = data || {};
  return (
    <Flex
      style={{
        background: allColors.neutral1,
        borderRadius: "8px"
      }}
      gap={16}
      direction='column'
      center
    >
      {!data || loading ? (
        <Flex style={{ width: "100%" }} center>
          <XYChartSkeleton
            style={{
              maxHeight: 400,
              width: "auto"
            }}
          />
        </Flex>
      ) : (
        <Flex center style={{ width: "100%" }}>
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
                  displayColors: true,
                  callbacks: {
                    title: item => item?.[0]?.label || ""
                  }
                }
              },
              scales: {
                x: {
                  type: "linear",
                  position: "bottom",
                  title: {
                    display: true,
                    color: allColors.primary10,
                    text: "Complexity",
                    padding: {
                      bottom: 10,
                      top: 20
                    }
                  }
                },
                y: {
                  title: {
                    display: true,
                    color: allColors.primary10,
                    text: "Frequencies",
                    padding: {
                      bottom: 20
                    }
                  }
                }
              }
            }}
            data={{
              labels: bins?.map(value => value.toFixed(0)),
              datasets: [
                {
                  label: "Frequencies",
                  data: frequencies,
                  backgroundColor: allColors.brand1
                }
              ]
            }}
          />
        </Flex>
      )}
    </Flex>
  );
}
