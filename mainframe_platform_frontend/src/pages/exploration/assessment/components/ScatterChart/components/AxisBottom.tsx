import { useEffect, useState } from "react";
import { ScaleLinear } from "d3";

import { colors } from "@style";

type AxisBottomProps = {
  xScale: ScaleLinear<number, number>;
  pixelsPerTick: number;
  height: number;
};

// tick length
const TICK_LENGTH = 10;

export const AxisBottom = ({ xScale, pixelsPerTick, height }: AxisBottomProps) => {
  const range = xScale.range();
  const [ticks, setTicks] = useState<
    {
      value: number;
      xOffset: number;
    }[]
  >();

  useEffect(() => {
    const width = range[1] - range[0];
    const numberOfTicksTarget = Math.floor(width / pixelsPerTick);

    const result = xScale.ticks(numberOfTicksTarget).map(value => ({
      value,
      xOffset: xScale(value)
    }));
    setTicks(result);
  }, [xScale]);

  return (
    <>
      {/* Ticks and labels */}
      {ticks?.map(({ value, xOffset }: { [key: string]: string | number }) => (
        <g key={value} transform={`translate(${xOffset}, 0)`} shapeRendering={"crispEdges"}>
          <line
            y1={TICK_LENGTH}
            y2={-height - TICK_LENGTH}
            stroke={colors.colorYellow100}
            strokeWidth={0.5}
          />
          <text
            key={value}
            style={{
              fontSize: "10px",
              textAnchor: "middle",
              transform: "translateY(20px)",
              fill: colors.colorWhite00
            }}
          >
            {value}
          </text>
        </g>
      ))}
    </>
  );
};
