import { ThemeConfig } from "antd";

import { allColors, colors } from "./colors";

export const antdTheme: ThemeConfig = {
  token: {
    ...colors,
    fontSizeHeading1: 60,
    lineHeightHeading1: 68,
    fontSizeHeading2: 48,
    lineHeightHeading2: 56,
    fontSizeHeading3: 36,
    lineHeightHeading3: 1.25,
    fontSizeHeading4: 24,
    lineHeightHeading4: 1.3,
    fontSizeHeading5: 20,
    lineHeightHeading5: 1.4,
    fontFamily: "SF Pro Text, sans-serif",
    borderRadius: 8
  },
  components: {
    Button: {
      colorBgContainerDisabled: colors.grey500,
      colorPrimaryHover: allColors.primary5,
      colorPrimaryBgHover: allColors.primary5,
      colorTextDisabled: colors.grey900,
      borderRadius: 99,
      fontSizeLG: 16,
      lineHeightLG: 24,
      fontSizeSM: 12,
      lineHeightSM: 14,
      fontSize: 14
    },
    Tabs: {
      horizontalItemPadding: "0 0 18px"
    },
    Slider: {
      handleSize: 12,
      railSize: 10
    }
  }
};
