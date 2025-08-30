import { LineCustom, PercentSucess, WrapLine, WrapProcessMultilSteps } from "./styles";

type ProcessMultilStepsProps = {
  percents?: number[];
  colors?: string[];
};

export const ProcessMultilSteps: React.FC<ProcessMultilStepsProps> = ({ percents, colors }) => {
  return (
    <WrapProcessMultilSteps>
      <WrapLine>
        {percents?.map((percent, index) => (
          <LineCustom
            key={String(index)}
            className='line'
            percent={Number(percent) || 0}
            color={colors?.[index]}
          />
        ))}
      </WrapLine>
      <PercentSucess>{percents?.[0] || 0}%</PercentSucess>
    </WrapProcessMultilSteps>
  );
};
