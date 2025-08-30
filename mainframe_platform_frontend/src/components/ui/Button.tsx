import styled from "@emotion/styled";
import { ButtonProps, Button as ButtonUI } from "antd";

type Props = ButtonProps & { iconSuffix?: ButtonProps["icon"]; iconPrefix?: ButtonProps["icon"] };

const WrapperFullSizeChildren = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;

  & > :not(:last-child) {
    margin-right: 6px;
  }
`;

export const Button: React.FC<Props> = ({ children, iconSuffix, iconPrefix, ...props }) => {
  const renderChildren = () => {
    if (iconSuffix || iconPrefix) {
      return (
        <WrapperFullSizeChildren>
          {iconPrefix}
          <span>{children}</span>
          {iconSuffix}
        </WrapperFullSizeChildren>
      );
    }
    return children;
  };

  return <ButtonUI {...props}>{renderChildren()}</ButtonUI>;
};
