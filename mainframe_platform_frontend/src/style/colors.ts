import { AliasToken, SeedToken } from "antd/es/theme/internal";

const v2DarkColors = {
  glassmorphism100: "rgba(26, 26, 28, 0.16)",
  glassmorphism200: "rgba(26, 26, 28, 0.32)",
  glassmorphism300: "rgba(26, 26, 28, 0.64)",
  glassmorphism400: "rgba(26, 26, 28, 0.6)"
};

const v2LightColors = {
  glassmorphism100: "rgba(242, 242, 242, 0.16)",
  glassmorphism200: "rgba(242, 242, 242, 0.32)",
  glassmorphism300: "rgba(242, 242, 242, 0.64)",
  glassmorphism400: "rgba(242, 242, 242, 0.6)"
};

export const v2CommonColors = {
  neutral1: "#FFFFFF",
  neutral2: "#FAFAFA",
  neutral3: "#F5F5F5",
  neutral4: "#F0F0F0",
  neutral5: "#D9D9D9",
  neutral6: "#BFBFBF",
  neutral7: "#8C8C8C",
  neutral8: "#595959",
  neutral9: "#434343",
  neutral10: "#262626",
  neutral11: "#1F1F1F",
  neutral12: "#141414",
  neutral13: "#000000",
  neutral14: "#dbdade",
  primary1: "#E6F7FF",
  primary2: "#BAE7FF",
  primary3: "#91D5FF",
  primary4: "#69C0FF",
  primary5: "#40A9FF",
  primary6: "#1890FF",
  primary7: "#096DD9",
  primary8: "#0050B3",
  primary9: "#003A8C",
  primary10: "#002766",
  secondary1: "#F0F5FF",
  secondary2: "#D6E4FF",
  secondary3: "#ADC6FF",
  secondary4: "#85A5FF",
  secondary5: "#597EF7",
  secondary6: "#2F54EB",
  secondary7: "#1D39C4",
  secondary8: "#10239E",
  secondary9: "#061178",
  secondary10: "#030852",
  info: "#2B8EFF",
  success: "#32D74B",
  warning: "#FFB441",
  error: "#FF453A",
  support00: "linear-gradient(#1890FF, #2F54EB)",
  support01: "#2F98E8",
  support02: "#FF5879",
  support03: "#42B8B8",
  support04: "#FF9538",
  support05: "#FFC64C",
  support06: "#8E5BFF",
  support07: "#C2C4C8",
  support08: "#EB2F96",
  support09: "#A0D911",
  support10: "#1791D7",
  brand1: "rgba(47, 152, 232, 1)",
  hBrand1: "rgba(47, 152, 232, 0.8)",
  mBrand1: "rgba(47, 152, 232, 0.6)",
  blurredBrand1: "rgba(47, 152, 232, 0.2)",
  brand2: "rgba(255, 88, 121, 1)",
  mBrand2: "rgba(255, 88, 121, 0.6)",
  blurredBrand2: "rgba(255, 88, 121, 0.2)",
  brand3: "rgba(66, 184, 184, 1)",
  brand4: "rgba(255, 149, 56, 1)",
  brand5: "rgba(142, 91, 255, 1)",
  hBrand5: "rgba(142, 91, 255, 0.8)",
  brand6: "rgba(255, 198, 76, 1)",
  brand7: "rgba(235, 227, 20, 1)",
  brand8: "rgba(235, 47, 150, 1)",
  brand9: "rgba(160, 217, 17, 1)",
  brand10: "rgba(210, 66, 37, 1)"
};

export const v2Colors = {
  ...v2CommonColors,
  elevation200: {
    border: "1px solid rgba(229, 229, 234, 1)",
    boxShadow: "0px 8px 16px 0px rgba(1, 12, 27, 0.1)"
  },
  elevation300: {
    border: "1px solid rgba(229, 229, 234, 1)",
    boxShadow: "0px 12px 24px 0px rgba(1, 12, 27, 0.1)"
  },
  elevation400: {
    border: "1px solid rgba(229, 229, 234, 1)",
    boxShadow: "0px 18px 28px 0px rgba(1, 12, 27, 0.1)"
  },
  elevation500: {
    border: "1px solid rgba(229, 229, 234, 1)",
    boxShadow: "0px 24px 64px 0px rgba(1, 12, 27, 0.1"
  }
};

export const v2Light = { ...v2Colors, ...v2LightColors };

export const v2Dark = { ...v2Colors, ...v2DarkColors };

export const colorsDefines = {
  primary100: "#F6D053",
  primary200: "#292e30",
  secondary100: "#879CB3",
  secondary200: "#E7ECEF",
  neutral: "#3f3f3f",
  grey: "#000000",
  grey900: "#1A1A1C",
  grey800: "#3A3A3C",
  grey700: "#48484A",
  grey600: "#636366",
  grey500: "#8E8E93",
  grey400: "#AEAEB2",
  grey300: "#C7C7CC",
  grey200: "#D1D1D6",
  grey100: "#F5F5F5",
  grey50: "#F2F2F7",
  grey10: "#FFFFFF",
  grey11: "#C2C2C2",
  info: "#00D3F6",
  success: "#27FB82",
  actionSucess: "#34B53A",
  green: "#3ea04d",
  actionDanger: "#FF3A29",
  warning: "#FDBE16",
  danger: "#FF453A",
  placeholder: "#E9EDF2",
  skeleton: "#F0F1F1",
  backgroundlight: "#F2F2F250",
  backgrounddark: "#F0F1F150",
  divider: "#F0F1F1",
  blur400: "#F2F2F2",
  blur300: "#F2F2F2",
  blur200: "#F2F2F2",
  blur100: "#F2F2F2",
  blur400dark: "#1A1A1C",
  blur300dark: "#1A1A1C",
  blur200dark: "#1A1A1C",
  blur100dark: "#1A1A1C",
  "palettes1.1": "#4A55A2",
  "palettes1.2": "#7895CB",
  "palettes1.3": "#A0BFE0",
  "palettes1.4": "#C5DFF8",
  "palettes2.1": "#645CBB",
  "palettes2.2": "#A084DC",
  "palettes2.3": "#BFACE2",
  "palettes2.4": "#EBC7E6",
  "palettes3.1": "#6096B4",
  "palettes3.2": "#93BFCF",
  "palettes3.3": "#BDCDD6",
  "palettes3.4": "#EEE9DA",
  black: "#000",
  white: "#fff",
  purple: "#9747FF",
  pink: "#FFA5CB",
  orange: "#EF8636",
  blue: "#539FEC",
  red: "#BB1910"
};

export const colors: typeof colorsDefines &
  Partial<SeedToken> &
  Partial<AliasToken> &
  Record<string, string> = {
  ...colorsDefines,
  colorPrimary: v2Colors.primary6,
  colorInfo: v2Colors.info,
  colorSuccess: v2Colors.success,
  colorWarning: v2Colors.warning,
  colorError: v2Colors.error,
  colorBorder: colorsDefines.grey400,
  colorBgSpotlight: v2Colors.primary6,
  colorTextBase: v2Colors.primary10,
  colorTextPlaceholder: colorsDefines.grey600,
  colorLink: `${v2Colors.primary6}50`,
  colorLinkHover: `${v2Colors.primary6}`,
  colorLinkActive: `${v2Colors.primary6}`
};

export const allColors = { ...colorsDefines, ...v2Colors };

export const colorsNodeByStatus = {
  MISSING: allColors.warning
  // DEAD: allColors.danger
  // ALIVE: allColors.primary10
};
export type ColorsDefinesKey = keyof typeof allColors;
