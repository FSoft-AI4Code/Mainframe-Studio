import { Scatter } from "react-chartjs-2";

import { allColors } from "@style";
import { Flex, Typography } from "@components";
import { DotSvg } from "@assets/svg";

export function ComplexityDistribution({ data }: { data: any[] }) {
  return (
    <Flex
      style={{ background: allColors.neutral1, padding: 16, borderRadius: "8px", flex: "1 1 0%" }}
      gap={16}
      direction='column'
      center
    >
      <Flex style={{ width: "100%" }}>
        <Typography level='body-16b' color='primary10'>
          Complexity per Lines of Code
        </Typography>
      </Flex>
      <Flex center direction='column' style={{ width: "80%" }}>
        <Scatter
          options={{
            interaction: {
              mode: "nearest"
            },
            plugins: {
              tooltip: {
                padding: { top: 4, right: 8, bottom: 4, left: 8 },
                cornerRadius: 4,
                backgroundColor: allColors.primary3,
                bodyColor: allColors.primary10,
                callbacks: {
                  title: files => files[0].dataset.label ?? ""
                }
              }
            },
            scales: {
              x: {
                type: "linear",
                position: "bottom"
              },
              y: {
                title: {
                  display: true,
                  color: allColors.primary10,
                  text: "Complexity",
                  padding: {
                    bottom: 20
                  }
                }
              }
            }
          }}
          data={{
            datasets: data.map(({ label, complexity, code, name }: any) => ({
              data: [{ x: code, y: complexity, name }],
              label: name,
              pointRadius: 4,
              hoverRadius: 5,
              backgroundColor:
                label === "COBOL"
                  ? allColors.brand1
                  : label === "JCL_IBM" || label === "JCL_FUJITSU" || label === "JCL"
                  ? allColors.brand2
                  : label === "COPY"
                  ? allColors.brand3
                  : allColors.brand4
            }))
          }}
        />
        <Typography level='caption-12m' color='primary10'>
          LoC
        </Typography>
      </Flex>
      <Flex gap={15} center>
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
      </Flex>
    </Flex>
  );
}
