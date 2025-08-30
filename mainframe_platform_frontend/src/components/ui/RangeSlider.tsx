import { Divider, Form, InputNumber, Slider } from "antd";
import { useState } from "react";

import { Button, Flex } from "@components";

export interface RangeFilterProps {
  min: number;
  max: number;
  onFilterChange: (range: number | number[]) => void;
}

export const RangeSliderFilter = ({ min, max, onFilterChange }: RangeFilterProps) => {
  const [range, setRange] = useState<[number, number]>([min, max]);

  const updateRange = (newRange: [number, number]) => {
    setRange(newRange);
  };

  return (
    <Form onFinish={() => onFilterChange(range)} style={{ width: "100%" }}>
      <Slider range min={min} max={max} value={range} onChange={updateRange} />
      <Flex gap={12} justify='space-between'>
        <InputNumber
          min={min}
          max={range[1] - 1}
          value={range[0]}
          onChange={val => updateRange([val as number, range[1]])}
        />
        <InputNumber
          min={range[0] + 1}
          max={max}
          value={range[1]}
          onChange={val => updateRange([range[0], val as number])}
        />
      </Flex>
      <Divider style={{ margin: "12px 0" }} />
      <Flex justify='space-between' gap={12}>
        <Button htmlType='submit' type='primary' style={{ width: "100px", borderRadius: 6 }}>
          Apply
        </Button>
        <Button onClick={() => updateRange([min, max])} style={{ width: "100px", borderRadius: 6 }}>
          Reset
        </Button>
      </Flex>
    </Form>
  );
};
