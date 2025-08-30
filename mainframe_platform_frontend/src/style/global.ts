import { css } from "@emotion/react";

import { colors, v2Colors } from "./colors";
import { customStyle } from "./custom";
import { fontStyle } from "./fonts";

export const globalStyle = css`
  ${fontStyle}
  ${customStyle}
  * {
    box-sizing: border-box;
  }
  html {
    font-size: 16px;
  }
  body {
    font-family: SF Pro Text, sans-serif;
    line-height: 1.5rem;
    margin: 0;
    background-color: ${v2Colors.neutral1};
    color: ${colors.grey10};
  }

  .required::after {
    content: " *";
    color: red;
  }
`;
