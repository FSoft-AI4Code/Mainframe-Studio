import styled from "@emotion/styled";
import { Tooltip } from "antd";
import { CSSProperties, PropsWithChildren } from "react";

import { ColorsDefinesKey } from "@style";

const config = {
  h1: `
    font-family: SF Pro Text;
    font-size: 60px;
    font-weight: 590;
    line-height: 68px;
  `,
  h2: `
    font-family: SF Pro Text;
    font-size: 48px;
    font-weight: 590;
    line-height: 56px;
    text-align: left;
  `,
  h3: `
    font-family: SF Pro Text;
    font-size: 36px;
    font-weight: 590;
    line-height: 44px;
    text-align: left;
  `,
  "body-16b": `
    font-family: SF Pro Text;
    font-size: 16px;
    font-weight: 700;
    line-height: 22px;
    text-align: left;
  `,
  "body-16m": `
    font-family: SF Pro Text;
    font-size: 16px;
    font-weight: 510;
    line-height: 22px;
    text-align: left;
  `,
  "body-16r": `
    font-family: SF Pro Text;
    font-size: 16px;
    font-weight: 400;
    line-height: 22px;
    text-align: left;
  `,
  "body-14b": `
    font-family: SF Pro Text;
    font-size: 14px;
    font-weight: 700;
    line-height: 20px;
    text-align: left;
  `,
  "body-14m": `
    font-family: SF Pro Text;
    font-size: 14px;
    font-weight: 510;
    line-height: 20px;
    text-align: left;
  `,
  "body-14r": `
    font-family: SF Pro Text;
    font-size: 14px;
    font-weight: 400;
    line-height: 20px;
    text-align: left;
  `,
  "body-code-14r": `
    font-family: Courier;
    font-size: 14px;
    font-weight: 400;
    line-height: 20px;
    text-align: left;
  `,
  "title-32b": `
    font-family: SF Pro Text;
    font-size: 32px;
    font-weight: 700;
    line-height: 40px;
    text-align: left;
  `,
  "title-24b": `
    font-family: SF Pro Text;
    font-size: 24px;
    font-weight: 700;
    line-height: 32px;
    text-align: left;
  `,
  "title-20b": `
    font-family: SF Pro Text;
    font-size: 20px;
    font-weight: 700;
    line-height: 28px;
    text-align: left;
  `,
  "title-18b": `
    font-family: SF Pro Text;
    font-size: 18px;
    font-weight: 700;
    line-height: 110%;
    text-align: left;
  `,
  "subtitle-20s": `
    font-family: SF Pro Text;
    font-size: 20px;
    font-weight: 590;
    line-height: 28px;
    text-align: left;
  `,
  "button-16s": `
    font-family: SF Pro Text;
    font-size: 16px;
    font-weight: 590;
    line-height: 24px;
    text-align: left;
  `,
  "button-14m": `
    font-family: SF Pro Text;
    font-size: 14px;
    font-weight: 510;
    line-height: 20px;
    text-align: left;
  `,
  "button-12m": `
    font-family: SF Pro Text;
    font-size: 12px;
    font-weight: 510;
    line-height: 14px;
    text-align: left;
  `,
  "link-16m": `
    font-family: SF Pro Text;
    font-size: 16px;
    font-weight: 510;
    line-height: 24px;
    text-align: left;
  `,
  "link-14m": `
    font-family: SF Pro Text;
    font-size: 14px;
    font-weight: 510;
    line-height: 20px;
    text-align: left;
  `,
  "caption-12m": `
    font-family: SF Pro Text;
    font-size: 12px;
    font-weight: 510;
    line-height: 16px;
    text-align: left;
  `,
  "caption-12r": `
    font-family: SF Pro Text;
    font-size: 12px;
    font-weight: 400;
    line-height: 16px;
    text-align: left;
  `,
  "caption-10s": `
    font-family: SF Pro Text;
    font-size: 10px;
    font-weight: 590;
    line-height: 12px;
    text-align: left;
  `,
  "caption-8s": `
    font-family: SF Pro Text;
    font-size: 8px;
    font-weight: 590;
    line-height: 12px;
    text-align: left;
  `,
  h1s: `
    font-family: SF Pro Text;
    font-size: 60px;
    font-weight: 600;
    line-height: 68px;
    letter-spacing: 0em;
  `,
  h2s: `
    font-family: SF Pro Text;
    font-size: 48px;
    font-weight: 600;
    line-height: 56px;
    letter-spacing: 0em;
  `,
  h3s: `
    font-family: SF Pro Text;
    font-size: 36px;
    font-weight: 600;
    line-height: 44px;
    letter-spacing: 0em;
  `,
  "h4-titles": `
    font-family: SF Pro Text;
    font-size: 24px;
    font-weight: 600;
    line-height: 32px;
    letter-spacing: 0em;
  `,
  "h5-subtitles": `
    font-family: SF Pro Text;
    font-size: 20px;
    font-weight: 600;
    line-height: 28px;
    letter-spacing: 0em;
  `,
  "h6-body1m": `
    font-family: SF Pro Text;
    font-size: 16px;
    font-weight: 500;
    line-height: 24px;
    letter-spacing: 0em;
  `,
  "h6-body1r": `
    font-family: SF Pro Text;
    font-size: 16px;
    font-weight: 400;
    line-height: 24px;
    letter-spacing: 0.01em;
  `,
  "h7-body2M": `
    font-family: SF Pro Text;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    letter-spacing: 0em;
  `,
  "h7-body2r": `
    font-family: SF Pro Text;
    font-size: 14px;
    font-weight: 400;
    line-height: 20px;
    letter-spacing: 0.02em;
  `,
  "h8-captions": `
    font-family: SF Pro Text;
    font-size: 12px;
    font-weight: 600;
    line-height: 14px;
    letter-spacing: 0em;
  `,
  "h8-captionm": `
    font-family: SF Pro Text;
    font-size: 12px;
    font-weight: 500;
    line-height: 14px;
    letter-spacing: 0em;
  `
};

const getEllipsisCss = (width?: string) => `
  ${width ? `max-width: ${width};` : ""}
  white-space: nowrap;
  overflow: hidden !important;
  text-overflow: ellipsis;
`;

type LevelType = keyof typeof config;
type WrapperProps = {
  level: LevelType;
  color?: ColorsDefinesKey;
  ellipsis?: { width?: string } | boolean;
};
type Props = PropsWithChildren &
  WrapperProps & { className?: string; style?: CSSProperties; onClick?: () => void };

const Wrapper = styled.p<WrapperProps>`
  ${({ level }) => config[level]}
  ${({ ellipsis }) =>
    Boolean(ellipsis)
      ? getEllipsisCss(typeof ellipsis === "boolean" ? undefined : ellipsis?.width)
      : ""}
  word-wrap: break-word;
  color: ${({ theme, color }) => (color ? theme.allColors[color] : "")};
  margin: 0;
`;

export const Typography: React.FC<Props> = props => {
  if (props.ellipsis)
    return (
      <Tooltip title={props.children}>
        <Wrapper {...props} />
      </Tooltip>
    );
  return <Wrapper {...props} />;
};
