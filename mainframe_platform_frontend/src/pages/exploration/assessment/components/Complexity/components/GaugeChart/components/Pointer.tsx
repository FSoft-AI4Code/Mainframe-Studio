import { line, scaleLinear } from "d3";

type PointerProps = {
  width?: number;
  head?: number;
  tail?: number;
  value?: number;
  center: { x?: number; y: number };
  minAngle: number;
  maxAngle: number;
  disabled: boolean;
};

export const Pointer: React.FC<PointerProps> = props => {
  const {
    width = 10,
    head = 60,
    tail = 5,
    value = -10,
    center = { x: 125, y: 135 },
    minAngle,
    maxAngle,
    disabled
  } = props;

  const pointerLine = line()([
    [width / 2, 0],
    [0, -head],
    [-(width / 2), 0],
    [1, tail],
    [width / 2, 0]
  ]);
  const valueScale = scaleLinear().domain([0, 1]).range([minAngle, maxAngle]);
  const pointerValue = valueScale(value);

  return (
    <path
      d={String(pointerLine)}
      transform={`translate(${center.x}, ${center.y}) rotate(${pointerValue})`}
      fill={"#F54E4E"}
      opacity={disabled ? 0.3 : undefined}
    />
  );
};
