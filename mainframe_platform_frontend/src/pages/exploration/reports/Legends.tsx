import Tag from "antd/es/tag";
import { Node } from "@xyflow/react";
import { CSSProperties, Fragment } from "react";
import "@xyflow/react/dist/style.css";

import { Flex, Typography } from "@components";
import { allColors } from "@style";

export type NodeBase = { label: string; children: NodeBase[] } & Node;
export type TreeNode = {
  id: string;
  label: string;
  type?: string;
  children?: TreeNode[];
  name?: string;
  section?: string;
  isRoot: boolean;
  level?: number;
};

type Legend = {
  label: string;
  id: string | number;
  style: CSSProperties;
};
interface LegendsProps {
  style?: CSSProperties;
  variant?: "primary" | "secondary";
  data: Legend[];
}
const Legends = ({ data: legends, style, variant = "primary" }: LegendsProps) => {
  return (
    <Flex
      style={{
        width: "fit-content",
        position: "absolute",
        right: 12,
        top: 70,
        background: allColors.neutral1,
        padding: 8,
        borderRadius: 4,
        boxShadow: "rgba(0, 0, 0, 0.24) 0px 3px 8px",
        ...style
      }}
      direction='column'
      gap={8}
    >
      {legends?.map(({ id, label, style: { color, ...itemStyle } }) => (
        <Fragment key={id}>
          {variant === "primary" ? (
            <Tag
              style={{
                borderRadius: 2,
                width: "100%",
                padding: "4px 8px",
                color: allColors.primary10,
                textTransform: "capitalize",
                ...itemStyle
              }}
              key={id}
              color={color}
            >
              {label}
            </Tag>
          ) : (
            <Flex align='center'>
              <Tag
                style={{
                  borderRadius: 2,
                  width: 24,
                  height: 24,
                  color: allColors.primary10,
                  textTransform: "capitalize",
                  ...itemStyle
                }}
                key={id}
                color={color}
              ></Tag>
              <Typography level={"caption-12m"}>{label}</Typography>
            </Flex>
          )}
        </Fragment>
      ))}
    </Flex>
  );
};

export default Legends;
