import { useState } from "react";
import { Doughnut } from "react-chartjs-2";

import { DotSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { allColors } from "@style";

type ActiveState = { label: "comment" | "code"; value: number } | null;
interface CmLocProps {
  comment: number;
  code: number;
  title?: string;
  width?: number;
  height?: number;
  options?: {
    cutout?: number;
  };
}

export function CmLOC({ comment, code, title, width = 120, height = 120, options }: CmLocProps) {
  const { cutout = 32 } = options || {};
  const [active, setActive] = useState<ActiveState>(null);

  return (
    <Flex
      direction='column'
      style={{
        // padding: 16,
        justifyContent: "center",
        background: allColors.neutral1,
        borderRadius: 8,
        flex: 1
      }}
      gap={16}
    >
      {title && (
        <Typography style={{ textAlign: "center" }} level='body-16b' color='primary10'>
          {title}
        </Typography>
      )}
      <Flex gap={16} justify='space-between' align='center' direction='column'>
        <Flex style={{ width, height, position: "relative" }} center>
          <Doughnut
            data={{
              labels: ["comment", "code"],
              datasets: [
                {
                  label: "My First Dataset",
                  data: [comment, code],
                  backgroundColor:
                    active?.label === "comment"
                      ? [allColors.mBrand2, allColors.blurredBrand1]
                      : active?.label === "code"
                      ? [allColors.blurredBrand2, allColors.mBrand1]
                      : [allColors.mBrand2, allColors.mBrand1],
                  hoverOffset: 4
                }
              ]
            }}
            options={{
              cutout: cutout,
              onHover: (_, activeElements, chart) => {
                if (activeElements[0]) {
                  const ctx = activeElements[0].element.$context;
                  const label = chart.data.labels?.[ctx.dataIndex] as "comment" | "code";
                  const value = chart.data.datasets[0].data[ctx.dataIndex] as number;

                  if (active?.label !== label) setActive({ label, value });
                } else {
                  setActive(null);
                }
              },
              interaction: {
                mode: "index"
              },
              plugins: {
                tooltip: { enabled: false }
              }
            }}
            onMouseLeave={() => setActive(null)}
          />
          <Typography
            level='body-16b'
            color='primary6'
            style={{
              position: "absolute",
              left: "50%",
              top: "50%",
              transform: "translate(-50%, -50%)"
            }}
          >
            {active ? active.value : "100 %"}
          </Typography>
        </Flex>
        <Flex direction='column' center gap={12}>
          <Flex
            justify='space-between'
            align='center'
            style={{
              width: 120,
              borderRadius: "8px",
              padding: "1px 5px 1px 0",
              background: active?.label === "code" ? allColors.primary3 : "inherit"
            }}
          >
            <Flex align='center' gap={2}>
              <Flex center style={{ width: 16, height: 16 }}>
                <DotSvg fill={allColors.mBrand1} />
              </Flex>
              <Typography level='button-12m' color='primary10'>
                Code
              </Typography>
            </Flex>
            <Typography level='caption-12r' color='primary10'>{`${(code + comment
              ? (code * 100) / (code + comment)
              : 0
            ).toFixed(2)}%`}</Typography>
          </Flex>
          <Flex
            justify='space-between'
            align='center'
            style={{
              width: 120,
              borderRadius: "8px",
              padding: "1px 5px 1px 0",
              background: active?.label === "comment" ? allColors.primary3 : "inherit"
            }}
          >
            <Flex align='center' gap={2} style={{ padding: 2 }}>
              <Flex center style={{ width: 16, height: 16 }}>
                <DotSvg fill={allColors.mBrand2} />
              </Flex>
              <Typography level='button-12m' color='primary10'>
                Comment
              </Typography>
            </Flex>
            <Typography level='caption-12r' color='primary10'>{`${(code + comment
              ? (comment * 100) / (code + comment)
              : 0
            ).toFixed(2)}%`}</Typography>
          </Flex>
        </Flex>
      </Flex>
    </Flex>
  );
}
