import { ArrowGaugeSvg } from "@assets/svg";

import { GaugeArc, UnitOfMeasurement } from "./components";
import { ArrowGauge, CustomGaugeChart, GaugeBaseSvgStyled, GaugePercent, WrapGauge } from "./style";

const defaultSize = 170;

type ArcSegment = {
  min: number;
  max: number;
  color: string;
  node?: (disable?: boolean) => boolean;
};

type GaugeChartProps = {
  height?: number;
  width?: number;
  disabled?: boolean;
  maxAngle?: number;
  minAngle?: number;
  arcSegments?: ArcSegment[];
  uom?: string;
  uomProps?: {
    offsetText: number;
  };
  value: number;
};

export const GaugeChart: React.FC<GaugeChartProps> = ({
  height,
  width,
  disabled,
  maxAngle = 135,
  minAngle = -135,
  arcSegments = [{ min: 0, max: 1, color: "skyblue" }],
  uom = "",
  uomProps = {
    offsetText: -7.5
  },
  value,
  ...props
}) => {
  const gaugeOrigin = {
    x: 140,
    y: 140
  };

  const startDeg = -134;
  const endDeg = 129;
  const degPointed = ((endDeg - startDeg) / 100) * value + startDeg;

  const renderBaseGauge = () => {
    return (
      <svg
        width={width ? width : height ? height : defaultSize}
        height={height ? height : width ? width : defaultSize}
        viewBox={"0 0 280 280"}
        {...props}
      >
        {arcSegments.map((item: ArcSegment, idx: number) => (
          <g key={`arcsegment-${idx}`}>
            {typeof item.node === "function" ? item.node(disabled) : item.node}
            <GaugeArc
              key={`gauge-arcsegment-${idx}`}
              inset={12}
              min={item.min}
              max={item.max}
              stroke={
                disabled && !item.node
                  ? `rgba(${idx * 15},${idx * 15},${idx * 15}, ${idx * 0.1 + 0.1})`
                  : item.color
              }
              strokeWidth={15}
              center={gaugeOrigin}
              maxAngle={maxAngle}
              minAngle={minAngle}
            />
          </g>
        ))}
        <UnitOfMeasurement value={uom} disabled={disabled} center={gaugeOrigin} {...uomProps} />
      </svg>
    );
  };

  return (
    <CustomGaugeChart>
      <GaugeBaseSvgStyled />
      <WrapGauge>{renderBaseGauge()}</WrapGauge>
      <ArrowGauge degPointed={degPointed}>
        <ArrowGaugeSvg />
      </ArrowGauge>
      <GaugePercent>{value}%</GaugePercent>
    </CustomGaugeChart>
  );
};
