import { Divider, Select, SelectProps, Space } from "antd";
import React, { useState } from "react";

import { RangeFilterProps } from "./RangeSlider";
import { Typography } from "./Typography";
import { SliderWithInput } from "./SliderWithInput";

interface DropdowRangeFilterProps extends SelectProps, RangeFilterProps {
  label?: string;
}

export const DropdowSliderFilter: React.FC<DropdowRangeFilterProps> = ({
  min,
  max,
  label,
  placeholder,
  defaultOpen,
  value,
  defaultValue,
  popupMatchSelectWidth = false,
  onFilterChange,
  ...props
}) => {
  const [open, setOpen] = useState(defaultOpen);
  const handleFilterChange = (range: number | number[]) => {
    onFilterChange(range);
    setOpen(false);
  };
  const [curentValue, setCurentValue] = useState<number | null>(defaultValue);

  const updateValue = (newValue: number | null) => {
    setCurentValue(newValue);
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
      onClear={() => {
        updateValue(defaultValue);
        onFilterChange(0);
      }}
      dropdownRender={() => (
        <>
          <Space direction='vertical' size={0} style={{ padding: 8, width: "100%" }}>
            <Typography level={"body-14m"}>{label}</Typography>
            <Divider style={{ margin: "2px 0" }} />
            <SliderWithInput
              min={min}
              value={curentValue as number}
              max={max}
              defaultValue={defaultValue}
              onChange={updateValue}
              onFilterChange={handleFilterChange}
            />
          </Space>
        </>
      )}
    />
  );
};
