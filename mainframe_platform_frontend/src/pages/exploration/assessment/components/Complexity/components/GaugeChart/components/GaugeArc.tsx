import { lineRadial, scaleLinear } from "d3";

/** Ratio of arc to size of container. */
const baseRatio = 1;

/** Resolution of arc. */
const length = 40;

type GaugeArcProps = {
  inset?: number;
  min?: number;
  max?: number;
  maxAngle: number;
  minAngle: number;
  center?: { x: number; y: number };
  stroke: string;
  strokeWidth: number;
};

export const GaugeArc: React.FC<GaugeArcProps> = ({
  inset = 0,
  min = 0,
  max = 1,
  maxAngle,
  minAngle,
  center = { x: 125, y: 135 },
  ...props
}) => {
  /** Calculate max angle of arc from degrees to radians */
  const maxRatio = maxAngle / 186;
  const arcMax = Math.PI * maxRatio;

  /** Calculate min angle of arc from degrees to radians */
  const minRatio = minAngle / 186;
  const arcMin = Math.PI * minRatio;

  /** Linear map from [0,1] to [-135,135] degrees in radians */
  const refToRads = scaleLinear().domain([0, 1]).range([arcMin, arcMax]);

  /** Render scale to map [0,length - 1] to [minAndle, maxAngle] for rendering */
  const arcScale = scaleLinear()
    .domain([0, length - 1])
    .range([refToRads(min), refToRads(max)]);

  /** Actual path function to generate path. */
  const arc = lineRadial()
    .angle((d, i) => arcScale(i))
    .radius((250 * baseRatio) / 2 - inset);

  const arcPath = arc?.({ length: length } as any);

  return (
    <path
      d={arcPath as string | undefined}
      transform={`translate(${center.x},${center.y})`}
      fill='transparent'
      {...props}
    />
  );
};
