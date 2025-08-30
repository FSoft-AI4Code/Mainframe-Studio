import styled from "@emotion/styled";

type FlexProps = {
  center?: boolean | "true" | "false" | "horizontal" | "vertical";
  justify?:
    | "space-around"
    | "space-between"
    | "space-evenly"
    | "flex-end"
    | "flex-start"
    | "center";
  direction?: "row" | "column";
  reverse?: boolean;
  gap?: number;
  align?: "center" | "flex-start" | "flex-end";
};

export const Flex = styled.div<FlexProps>`
  display: flex;
  flex-direction: ${({ direction, reverse }) => {
    if (reverse && direction) return `${direction}-reverse`;
    if (direction) return direction;
    return "initial";
  }};
  justify-content: ${({ center, justify }) => {
    const isCenter = center === true || center === "true" || center === "horizontal";
    const isJustify = justify;
    if (isCenter) return "center";
    if (isJustify) return justify;
    return "initial";
  }};
  align-items: ${({ center, align }) => {
    const isCenter = center === true || center === "true" || center === "vertical";
    return isCenter ? "center" : align ? align : "initial";
  }};
  gap: ${({ gap }) => gap}px;
`;
