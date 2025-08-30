import { css } from "@emotion/react";

export const fontStyle = css`
  @font-face {
    font-family: "SF Pro Text";
    font-style: normal;
    font-weight: 400;
    src: url("/static/fonts/SFPRODISPLAYREGULAR.OTF") format("opentype");
  }
  @font-face {
    font-family: "SF Pro Text";
    font-style: normal;
    font-weight: 500;
    src: url("/static/fonts/SFPRODISPLAYREGULAR.OTF") format("opentype");
  }

  @font-face {
    font-family: "SF Pro Text";
    font-style: normal;
    font-weight: 600;
    src: url("/static/fonts/SFPRODISPLAYMEDIUM.OTF") format("opentype");
  }

  @font-face {
    font-family: "SF Pro Text";
    font-style: normal;
    font-weight: 700;
    src: url("/static/fonts/SFPRODISPLAYBOLD.OTF") format("opentype");
  }
`;
