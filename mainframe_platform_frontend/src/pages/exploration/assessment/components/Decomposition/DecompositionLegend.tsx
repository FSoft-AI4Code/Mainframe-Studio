import { Tag, Space, Typography } from "antd";

import { EntryPointInput, LabelEnum } from "@types";
import { allColors } from "@style";

export const DecompositionTypeEnum = {
  JCL: LabelEnum.JCL,
  BMS: LabelEnum.BMS
};

export const decompositionColors: Record<string, string> = {
  JCL: allColors.brand1,
  BMS: allColors.brand5
};

export const DecompositionLegend = ({
  filters,
  setFilters
}: {
  filters: Partial<EntryPointInput>;
  setFilters: (val: Partial<EntryPointInput>) => void;
}) => {
  const currentType = filters?.type_filter;

  const handleClick = (type: string) => {
    setFilters({
      ...filters,
      skip: 0,
      type_filter: currentType === type ? undefined : type
    });
  };

  return (
    <Space size={6} wrap>
      <Typography>File Type:</Typography>
      {Object.entries(DecompositionTypeEnum).map(([key, value]) => (
        <Tag
          key={key}
          color={decompositionColors[key]}
          onClick={() => handleClick(value)}
          style={{
            cursor: "pointer",
            borderRadius: 999,
            padding: "4px 12px",
            fontWeight: 600,
            fontSize: 13,
            opacity: currentType && currentType !== value ? 0.4 : 1,
            transition: "opacity 0.3s"
          }}
        >
          {value}
        </Tag>
      ))}
    </Space>
  );
};
