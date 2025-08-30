import styled from "@emotion/styled";

import { LogoSvg } from "@assets/svg";

const Icon = styled(LogoSvg)``;

export type LogoProps = {
  width?: number;
  height?: number;
};

export const Logo: React.FC<LogoProps> = ({ height, width }) => {
  const widthValue = width ? width : height ? (height / 48) * 46 : 46;
  const heightValue = height ? height : width ? (width / 46) * 48 : 48;
  return <Icon width={widthValue} height={heightValue} />;
};
