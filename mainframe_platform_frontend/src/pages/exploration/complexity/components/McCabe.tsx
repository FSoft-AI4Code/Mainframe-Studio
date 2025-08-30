import { Slider } from "antd";
import styled from "@emotion/styled";

import { DotSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { allColors } from "@style";

import { useIncrementalNumber } from "../../../../hooks/app";

// Helper function to map one range to another
function mapValue(value: number, fromLow: number, fromHigh: number, toLow: number, toHigh: number) {
  return ((value - fromLow) * (toHigh - toLow)) / (fromHigh - fromLow) + toLow;
}

function mapRange(input: number) {
  if (input < 0 || input > 10000) {
    throw new Error("Input must be between 0 and 100000");
  }

  let output;

  if (input <= 100) {
    // Map from range 0-100 to range 0-25
    output = mapValue(input, 0, 100, 0, 25);
  } else if (input <= 500) {
    // Map from range 100-500 to range 25-50
    output = mapValue(input, 100, 500, 25, 50);
  } else if (input <= 1000) {
    // Map from range 500-1000 to range 50-75
    output = mapValue(input, 500, 1000, 50, 75);
  } else {
    // Map from range 1000-10000 to range 75-100
    output = mapValue(input, 1000, 10000, 75, 100);
  }

  return output;
}

const CustomSlider = styled(Slider)`
  height: 20px;
  .ant-slider-rail {
    background: ${({ theme }) => theme.allColors.neutral6};
    border-radius: 8px;
  }

  .ant-slider-track {
    border-radius: 8px;
    background-image: linear-gradient(
      to right,
      ${({ theme }) => theme.allColors.brand1} 125px,
      ${({ theme }) => theme.allColors.brand3} 125px,
      ${({ theme }) => theme.allColors.brand3} 250px,
      ${({ theme }) => theme.allColors.brand4} 250px,
      ${({ theme }) => theme.allColors.brand4} 375px,
      ${({ theme }) => theme.allColors.brand8} 375px,
      ${({ theme }) => theme.allColors.brand8} 500px
    );
  }
`;

export function McCabe({ mcCabe }: { mcCabe: number }) {
  // const [level, setLevel] = useState<"simple" | "medium" | "high">("high");
  const incrementalNumber = useIncrementalNumber(mcCabe);

  return (
    <Flex
      gap={24}
      style={{
        padding: 16,
        background: allColors.neutral1,
        borderRadius: 8
      }}
      direction='column'
    >
      <Typography level='body-16b' color='primary10'>
        Total Complexity
      </Typography>
      <Flex gap={10} center direction='column'>
        <Typography
          level='title-24b'
          color={
            mcCabe <= 100
              ? "brand1"
              : mcCabe <= 500
              ? "brand3"
              : mcCabe <= 1000
              ? "brand4"
              : "brand8"
          }
        >
          {mcCabe <= 100
            ? "Simple"
            : mcCabe <= 500
            ? "Medium"
            : mcCabe <= 1000
            ? "Complex"
            : "Very Complex"}
        </Typography>
        <CustomSlider
          value={mapRange(incrementalNumber)}
          style={{ width: "100%", maxWidth: 500 }}
          className='table'
          min={0}
          max={100}
          rootClassName='center'
          tooltip={{
            formatter: () => (
              <Typography style={{ textAlign: "center" }} level={"link-14m"}>
                {mcCabe.toFixed(0)}
              </Typography>
            )
          }}
        />
        <Flex justify='space-between' align='center' style={{ width: "100%", maxWidth: 500 }}>
          <Flex style={{ width: 0 }} center>
            <Typography color='neutral13' level='caption-12r' style={{ whiteSpace: "nowrap" }}>
              0
            </Typography>
          </Flex>
          <Flex style={{ width: 0 }} center>
            <Typography color='neutral13' level='caption-12r' style={{ whiteSpace: "nowrap" }}>
              100
            </Typography>
          </Flex>
          <Flex style={{ width: 0 }} center>
            <Typography color='neutral13' level='caption-12r' style={{ whiteSpace: "nowrap" }}>
              500
            </Typography>
          </Flex>
          <Flex style={{ width: 0 }} center>
            <Typography color='neutral13' level='caption-12r' style={{ whiteSpace: "nowrap" }}>
              1000
            </Typography>
          </Flex>
          <Typography
            color='neutral13'
            level='caption-12r'
            style={{ whiteSpace: "nowrap" }}
          ></Typography>
        </Flex>
      </Flex>
      <Flex gap={12} center>
        <Flex center style={{ minWidth: 65 }}>
          <Flex center style={{ width: 16, height: 16 }}>
            <DotSvg fill={allColors.brand1} />
          </Flex>
          <Typography level='button-12m' color='primary10'>
            Simple
          </Typography>
        </Flex>
        <Flex center style={{ minWidth: 65 }}>
          <Flex center style={{ width: 16, height: 16 }}>
            <DotSvg fill={allColors.brand3} />
          </Flex>
          <Typography level='button-12m' color='primary10'>
            Medium
          </Typography>
        </Flex>
        <Flex center style={{ minWidth: 65 }}>
          <Flex center style={{ width: 16, height: 16 }}>
            <DotSvg fill={allColors.brand4} />
          </Flex>
          <Typography level='button-12m' color='primary10'>
            Complex
          </Typography>
        </Flex>
        <Flex center style={{ minWidth: 65 }}>
          <Flex center style={{ width: 16, height: 16 }}>
            <DotSvg fill={allColors.brand8} />
          </Flex>
          <Typography level='button-12m' color='primary10'>
            Very Complex
          </Typography>
        </Flex>
      </Flex>
    </Flex>
  );
}
