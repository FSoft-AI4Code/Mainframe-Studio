import { Bar } from "react-chartjs-2";

import { allColors } from "@style";
import { Flex, Typography } from "@components";

export type LOCBByFileType = Record<"cobol" | "jcl" | "copybook" | "screen" | "unknown", number>;

export function LOCFileType({ data, labels }: { data: LOCBByFileType; labels: string[] }) {
  return (
    <Flex
      style={{ background: allColors.neutral1, padding: 32, borderRadius: "8px" }}
      gap={16}
      direction='column'
    >
      <Flex style={{ width: "100%" }}>
        <Typography level='body-16b' color='primary10'>
          Lines of Code by File Type
        </Typography>
      </Flex>
      <Flex center>
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
            labels: labels,
            datasets: [
              {
                data: Object.values(data),
                backgroundColor: [
                  allColors.brand1,
                  allColors.brand2,
                  allColors.brand3,
                  allColors.brand4,
                  allColors.brand5
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
    </Flex>
  );
}
