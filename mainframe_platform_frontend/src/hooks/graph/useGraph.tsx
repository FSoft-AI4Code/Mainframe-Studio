import { ReactComponent as ArrowLeftOutlineSvg } from "@assets/svg/arrow-left-outline.svg";
import { ReactComponent as CircleOutlineSvg } from "@assets/svg/circle-outline.svg";
import applicationImg from "@assets/svg/application-stat.svg";
import databaseImg from "@assets/svg/database-stat.svg";
import batchChainImg from "@assets/svg/batch-chain-stat.svg";
import { ReactComponent as StarSvg } from "@assets/svg/star-ouline.svg";
import { ReactComponent as RectangleSvg } from "@assets/svg/rectangle-outline.svg";
import starImg from "@assets/svg/star.svg";
import { ReactComponent as TritangleSvg } from "@assets/svg/tritangle-outline.svg";
import { ReactComponent as UnknowSvg } from "@assets/svg/unknow-outline.svg";
import tritangleImg from "@assets/svg/tritangle.svg";
import unknowImg from "@assets/svg/unknow-icon.svg";
import appGrImg from "@assets/svg/application.svg";
import dbGrImg from "@assets/svg/db-group.svg";
import chainGrImg from "@assets/svg/chain.svg";
import { colors } from "@style";

const ICON_WIDTH = 37;
const ICON_HEIGHT = 12;

export const useGraph = () => {
  const LEGENDS = [
    {
      id: "program",
      icon: <RectangleSvg />,
      iconLink: applicationImg,
      name: "Program",
      backgroundColor: colors.orange,
      width: ICON_WIDTH,
      height: ICON_HEIGHT
    },
    {
      id: "copy",
      icon: <StarSvg />,
      iconLink: starImg,
      name: "Copy",
      backgroundColor: colors.pink
    },
    {
      id: "db",
      icon: <CircleOutlineSvg />,
      iconLink: databaseImg,
      name: "Database",
      backgroundColor: colors.orange,
      width: ICON_WIDTH,
      height: ICON_HEIGHT
    },
    {
      id: "screen",
      icon: <TritangleSvg />,
      iconLink: tritangleImg,
      name: "Screen",
      backgroundColor: colors.blue
    },
    {
      id: "link",
      icon: <ArrowLeftOutlineSvg />,
      iconLink: batchChainImg,
      name: "Arrow",
      backgroundColor: colors.primary100,
      width: ICON_WIDTH,
      height: ICON_HEIGHT
    },
    {
      id: "db-group",
      width: 20,
      height: 20,
      x: -10.5,
      y: -10.5,
      type: "group",
      icon: <ArrowLeftOutlineSvg />,
      iconLink: dbGrImg,
      name: "Arrow",
      backgroundColor: colors.primary100
    },
    {
      id: "app-group",
      type: "group",
      width: 20,
      height: 20,
      x: -10.5,
      y: -10.5,
      icon: <ArrowLeftOutlineSvg />,
      iconLink: appGrImg,
      name: "Arrow",
      backgroundColor: colors.primary100
    },
    {
      id: "chain-group",
      type: "group",
      width: 20,
      height: 20,
      x: -10.5,
      y: -10.5,
      icon: <ArrowLeftOutlineSvg />,
      iconLink: chainGrImg,
      name: "Arrow",
      backgroundColor: colors.primary100
    },
    {
      id: "",
      icon: <UnknowSvg />,
      iconLink: unknowImg,
      name: "Unknown",
      backgroundColor: colors.red
    }
  ];

  return {
    legend: LEGENDS
  };
};
