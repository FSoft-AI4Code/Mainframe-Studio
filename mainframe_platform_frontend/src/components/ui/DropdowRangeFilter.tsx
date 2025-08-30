/* eslint-disable @typescript-eslint/no-unused-vars */
import { Divider, Select, SelectProps, Space } from "antd";
import React, { useState } from "react";

import { RangeSliderFilter, RangeFilterProps } from "./RangeSlider";
import { Typography } from "./Typography";

interface DropdowRangeFilterProps extends SelectProps, RangeFilterProps {
  label?: string;
}

export const DropdowRangeFilter: React.FC<DropdowRangeFilterProps> = ({
  min,
  max,
  label,
  placeholder,
  value,
  popupMatchSelectWidth = false,
  onFilterChange,
  ...props
}) => {
  const [open, setOpen] = useState(false);
  const handleFilterChange = (range: number | number[]) => {
    onFilterChange(range);
    setOpen(false);
  };

  return (
    <Select
      allowClear
      {...props}
      onDropdownVisibleChange={setOpen}
      popupMatchSelectWidth={popupMatchSelectWidth}
      open={open}
      value={value}
      placeholder={placeholder}
      placement='bottomRight'
      dropdownRender={() => (
        <>
          <Space direction='vertical' size={0} style={{ padding: 8, width: "100%" }}>
            <Typography level={"body-14m"}>{label}</Typography>
            <Divider style={{ margin: "2px 0" }} />
            <RangeSliderFilter min={min} max={max} onFilterChange={handleFilterChange} />
          </Space>
        </>
      )}
    />
  );
};
