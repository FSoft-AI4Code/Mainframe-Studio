/* eslint-disable @typescript-eslint/no-explicit-any */
import { Bar } from "react-chartjs-2";

import { allColors } from "@style";
import { Flex, Typography } from "@components";

export function LOCDistribution({ data }: { data: { log_frequencies: any[]; bins: any[] } }) {
  return (
    <Flex
      style={{ background: allColors.neutral1, padding: 16, borderRadius: "8px" }}
      gap={16}
      direction='column'
      center
    >
      <Flex style={{ width: "100%" }}>
        <Typography level='body-16b' color='primary10'>
          Lines of Code Distribution
        </Typography>
      </Flex>
      <Flex center style={{ width: "90%" }}>
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
            labels: data.bins.map(value => value.toFixed(0)),
            datasets: [
              {
                label: "Log Frequency",
                data: data.log_frequencies,
                backgroundColor: allColors.brand1
              }
            ]
          }}
        />
      </Flex>
      <Flex gap={15} center>
        <Typography level='caption-12m' color='primary10'>
          LoC
        </Typography>
      </Flex>
    </Flex>
  );
}
