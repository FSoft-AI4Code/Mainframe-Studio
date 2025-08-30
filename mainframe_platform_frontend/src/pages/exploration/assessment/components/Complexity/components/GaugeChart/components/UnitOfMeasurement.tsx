type UnitOfMeasurementProps = {
  value: string;
  disabled?: boolean;
  center: {
    x: number;
    y: number;
  };
  offsetText: number;
};

export const UnitOfMeasurement: React.FC<UnitOfMeasurementProps> = props => {
  const { value, disabled, center, offsetText, ...rest } = props;
  return (
    <text
      transform={`translate(${center.x + offsetText},${center.y + 50})`}
      opacity={disabled ? 0.4 : undefined}
      {...rest}
    >
      {value}
    </text>
  );
};
