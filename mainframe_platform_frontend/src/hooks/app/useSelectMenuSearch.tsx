import { Empty, SelectProps } from "antd";
import { MutableRefObject, useEffect, useRef, useState } from "react";

type Option = { label: string; value: string };

type Output = SelectProps & {
  setValue: (v?: string) => void;
  refValue: MutableRefObject<string | undefined>;
};

export const useSelectMenuSearch = <RecordType extends object>(
  data: RecordType,
  getOptions: (data: RecordType) => Option[]
): Output => {
  const refValue = useRef<string>();
  const [value, setValue] = useState<string>();
  const [options, setOptions] = useState<Option[]>([]);
  const [optionsTotal, setOptionsTotal] = useState<typeof options>([]);

  const onSearch: SelectProps["onSearch"] = v => {
    const reg = new RegExp(`.*${v}.*`, "i");
    setOptions(optionsTotal.filter(o => o.label.match(reg)));
  };

  const onChange: SelectProps["onChange"] = d => {
    refValue.current = d?.value;
    setValue(d?.value);
  };

  useEffect(() => {
    const opts = getOptions(data);
    setOptions(opts);
    setOptionsTotal(opts);
  }, [data]);

  return {
    labelInValue: true,
    showSearch: true,
    allowClear: true,
    filterOption: false,
    options,
    onSearch,
    onChange,
    notFoundContent: <Empty />,
    value,
    refValue,
    setValue
  };
};
