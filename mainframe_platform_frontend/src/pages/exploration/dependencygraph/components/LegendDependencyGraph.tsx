import { Image } from "antd";

import diamondDarkImg from "@assets/svg/diamond-dark.svg";
import octagonDarkImg from "@assets/svg/octagon-dark.svg";
import ellipseDarkImg from "@assets/svg/ellipse-dark.svg";
import diamondImg from "@assets/svg/diamond.svg";
import ellipseImg from "@assets/svg/ellipse.svg";
import octagonImg from "@assets/svg/octagon.svg";
import polygonImg from "@assets/svg/polygon.svg";
import rectangleImg from "@assets/svg/rectangle.svg";
import starImg from "@assets/svg/star.svg";
import polygonDarkImg from "@assets/svg/polygon-dark.svg";
import rectangleDarkImg from "@assets/svg/rectangle-dark.svg";
import pentagonImg from "@assets/svg/pentagon.svg";
import pentagonDarkImg from "@assets/svg/pentagon-dark.svg";
import starDarkImg from "@assets/svg/star-dark.svg";
import { Flex, Typography } from "@components";
import { allColors } from "@style";
import { Node } from "@types";

export const legendsGraph = {
  COPY: {
    key: "COPY",
    label: "CPY",
    color: allColors.support09,
    img: diamondImg,
    missingImg: diamondDarkImg
  },
  COBOL: {
    key: "COBOL",
    label: "COBOL",
    color: allColors.support05,
    img: ellipseImg,
    missingImg: ellipseDarkImg
  },
  JCL: {
    key: "JCL",
    label: "JCL",
    color: allColors.support03,
    img: rectangleImg,
    missingImg: rectangleDarkImg
  },
  BMS: {
    key: "BMS",
    label: "BMS",
    color: allColors.support02,
    img: polygonImg,
    missingImg: polygonDarkImg
  },
  UTILITY: {
    key: "UTILITY",
    label: "Utility",
    color: allColors.support06,
    img: starImg,
    missingImg: starDarkImg
  },
  WFL: {
    key: "WFL",
    label: "WFL",
    color: allColors.support07,
    img: pentagonImg,
    missingImg: pentagonDarkImg
  },
  OTHER: {
    key: "OTHER",
    label: "Other",
    color: allColors.support08,
    img: octagonImg,
    missingImg: octagonDarkImg
  }
};

type KeyType = keyof typeof legendsGraph;

interface LegendGraphProps {
  nodes: Node[];
}

export default function LegendDependencyGraph({ nodes }: LegendGraphProps) {
  const getCount = (key: KeyType) =>
    nodes?.filter(({ label }) =>
      key === "JCL" ? ["JCL_IBM", "JCL_FUJITSU", "JCL"].includes(label) : label === key
    ).length;
  const uniqueNodesByType = Array.from(
    new Map(nodes?.map(node => [node.label, { status: node.status, label: node.label }])).values()
  );

  return (
    <Flex gap={12} style={{ alignItems: "center", justifyContent: "end", flexWrap: "wrap" }}>
      <Flex style={{ alignItems: "center" }} gap={10}>
        <Typography level={"caption-12m"}>Mising:</Typography>
        <Flex style={{ width: 30, height: 10, background: allColors.neutral9 }}></Flex>
      </Flex>
      <Flex
        gap={10}
        style={{ flexWrap: "wrap", marginLeft: "auto" }}
        align='center'
        justify='flex-end'
      >
        {uniqueNodesByType.map(({ label }) => {
          const img = (legendsGraph[label as keyof typeof legendsGraph] || legendsGraph.OTHER).img;
          return (
            <Flex
              key={label}
              gap={4}
              style={{
                padding: "4px 8px",
                borderRadius: "50px",
                border: `1px solid ${allColors.neutral6}`,
                alignItems: "end"
              }}
            >
              <Flex center>
                <Image preview={false} src={img} alt={label} />
              </Flex>
              <Typography level='h7-body2M' color='primary10'>
                {label}
              </Typography>
              <Typography level='h7-body2M' color='primary10'>
                {getCount(label as keyof typeof legendsGraph)}
              </Typography>
            </Flex>
          );
        })}
      </Flex>
    </Flex>
  );
}
