import { Form, InputNumber, Slider } from "antd";
import { FilterDropdownProps } from "antd/es/table/interface";
import { useState } from "react";

import { Button, Flex } from "@components";

interface RangeFilterProps extends FilterDropdownProps {
  min: number;
  max: number;
  label?: string;
}
export const RangeFilter = ({
  setSelectedKeys,
  selectedKeys,
  confirm,
  clearFilters,
  min,
  max,
  label
}: RangeFilterProps) => {
  const [range, setRange] = useState<number[]>(() => {
    if (selectedKeys.length && Array.isArray(selectedKeys[0])) {
      return selectedKeys[0] as number[];
    }
    return [min, max];
  });

  return (
    <Form
      onFinish={() => {
        setSelectedKeys([range] as never);
        confirm();
      }}
      style={{ width: 320, padding: 24 }}
    >
      <Form.Item label={label}>
        <Slider
          range
          min={min}
          max={max}
          value={range as [number, number]}
          onChange={setRange}
          style={{ width: "100%" }}
        />
      </Form.Item>
      <Flex gap={12} justify='space-between'>
        <Form.Item label='Min'>
          <InputNumber
            min={min}
            max={max - 1}
            value={range[0]}
            onChange={val => setRange([val as number, range[1]])}
          />
        </Form.Item>
        <Form.Item label='Max'>
          <InputNumber
            min={range[0] + 1}
            max={max}
            value={range[1]}
            onChange={val => setRange([range[0], val as number])}
          />
        </Form.Item>
      </Flex>
      <Flex
        style={{
          marginTop: 16
        }}
        gap={12}
      >
        <Button htmlType='submit' type='primary' style={{ width: "100%", borderRadius: 6 }}>
          Confirm
        </Button>
        <Button
          onClick={() => {
            setSelectedKeys([]);
            clearFilters?.();
            setRange([min, max]);
            confirm();
          }}
          style={{ width: "100%", borderRadius: 6 }}
        >
          Reset
        </Button>
      </Flex>
    </Form>
  );
};
