import { allColors, colors, v2Colors } from "./colors";

export const theme = {
  colors,
  v2Colors,
  allColors
};

type ThemeType = typeof theme;
declare module "@emotion/react" {
  // eslint-disable-next-line @typescript-eslint/no-empty-interface
  export interface Theme extends ThemeType {}
}
