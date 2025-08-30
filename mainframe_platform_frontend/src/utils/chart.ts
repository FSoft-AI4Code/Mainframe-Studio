import { colors } from "@style";

const colorMap = [
  colors.primary100,
  "#F44336",
  "#E91E63",
  "#9C27B0",
  "#673AB7",
  "#3F51B5",
  "#2196F3",
  "#03A9F4",
  "#00BCD4",
  "#009688",
  "#4CAF50",
  "#8BC34A",
  "#CDDC39",
  "#FFEB3B",
  "#FFC107",
  "#FF9800",
  "#FF5722",
  "#795548",
  "#9E9E9E",
  "#607D8B"
];

export const getFillColor = (group: string | number) => {
  return colorMap[group as number] || colors.primary100;
};

export const getColorsWithOpacity = (colorsBase: number[][], colorIndex = 0, opacity = 1) => {
  const [r, g, b] = colorsBase[colorIndex % colorsBase?.length] || colorsBase[0];
  return `rgba(${r}, ${g}, ${b}, ${opacity})`;
};
