import styled from "@emotion/styled";

import { colors } from "@style";

import { Typography } from "./ui";

const Wrap = styled.div`
  display: flex;
  align-items: center;
  position: relative;
  z-index: 1002;
`;

const WrapLegend = styled.div<{
  background?: string;
  highLight?: boolean;
  size?: "small" | "large";
}>`
  display: flex;
  align-items: center;
  padding: ${({ size }) => {
    if (size === "small") {
      return "7.5px 6.5px";
    }
    return "8px 16px";
  }};
  color: ${({ theme }) => theme.colors.white};
  background-color: ${({ theme, background }) => background || theme.colors.primary100};
  margin-right: 16px;
  border-radius: 8px;
  position: relative;
  opacity: ${({ highLight }) => {
    if (highLight === false) {
      return 0.5;
    }
    return 1;
  }};
  z-index: ${({ highLight }) => (highLight ? 1000 : 100)};

  .icon {
    width: ${({ size }) => {
      if (size === "small") {
        return "12px";
      }
      return "16px";
    }};
    height: ${({ size }) => {
      if (size === "small") {
        return "12px";
      }
      return "16px";
    }};
    margin-right: 8px;
    display: flex;
    align-items: center;
  }
`;

export const Legend: React.FC<{
  data: {
    icon?: JSX.Element;
    name: string;
    backgroundColor?: string;
  }[];
  highLight?: string;
  size?: "small" | "large";
}> = ({ data, highLight, size }) => {
  return (
    <Wrap>
      {data.sort().map(item => {
        return (
          <WrapLegend
            size={size}
            highLight={highLight ? item?.backgroundColor === highLight : undefined}
            key={item?.name}
            background={item.backgroundColor || colors.colorWhite00}
          >
            {!!item.icon && <div className='icon'>{item.icon}</div>}
            <Typography level={size === "small" ? "h8-captions" : "h7-body2M"}>
              {item.name}
            </Typography>
          </WrapLegend>
        );
      })}
    </Wrap>
  );
};
