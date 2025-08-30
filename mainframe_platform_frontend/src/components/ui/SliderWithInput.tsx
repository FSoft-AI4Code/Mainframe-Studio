import { Divider, Form, InputNumber, Slider } from "antd";

import { Button, Flex } from "@components";

export interface RangeFilterProps {
  min: number;
  max: number;
  value: number;
  defaultValue?: number;
  onFilterChange: (value: number) => void;
  onChange: (value: number | null) => void;
}

export const SliderWithInput = ({
  min,
  max,
  onFilterChange,
  value,
  onChange,
  defaultValue
}: RangeFilterProps) => {
  return (
    <Form onFinish={() => onFilterChange(value)} style={{ width: "100%" }}>
      <Flex align='center' gap={16}>
        <Slider min={min} style={{ width: "100%" }} max={max} value={value} onChange={onChange} />
        <InputNumber
          min={min}
          controls={false}
          max={max}
          style={{
            width: "100px",
            maxHeight: "30px"
          }}
          value={value}
          onChange={onChange}
        />
      </Flex>
      <Divider style={{ margin: "0 0 12px 0px" }} />
      <Flex justify='space-between' gap={12}>
        <Button htmlType='submit' type='primary' style={{ width: "100px", borderRadius: 6 }}>
          Apply
        </Button>
        <Button
          onClick={() => onChange(defaultValue as number)}
          style={{ width: "100px", borderRadius: 6 }}
        >
          Reset
        </Button>
      </Flex>
    </Form>
  );
};
