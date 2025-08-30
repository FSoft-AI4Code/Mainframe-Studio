import styled from "@emotion/styled";
import { Divider, Form, InputNumber, Slider, Table } from "antd";
import { ColumnsType } from "antd/es/table";
import { FilterDropdownProps, FilterValue, TablePaginationConfig } from "antd/es/table/interface";
import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import { Button, Flex, Typography } from "@components";
import { useFilterGraph } from "@hooks";
import { useEntryPointByRepository } from "@services";
import { allColors } from "@style";
import { Criticality, DistributionEntryPoint, EntryPointInput } from "@types";
import { addPropertiesToItems } from "@utils";

import { decompositionColors, DecompositionLegend } from "./DecompositionLegend";

const CustomTable = styled(Table)`
  .ant-table-thead {
    .ant-table-cell {
      background: ${allColors.neutral5};
      border-color: ${allColors.neutral7};
      border-radius: none;
    }
  }

  .ant-table-tbody {
    .ant-table-cell {
      vertical-align: top;
    }
    /* Row background theo type */
    .row-type-jcl > .ant-table-cell {
      background-color: ${allColors.brand1};
    }

    .row-type-bms > .ant-table-cell {
      background-color: ${allColors.brand5};
    }
  }
`;

interface RangeFilterProps extends FilterDropdownProps {
  min: number;
  max: number;
  defaultValue: number;
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
export const SliderFilter = ({
  setSelectedKeys,
  selectedKeys,
  confirm,
  clearFilters,
  defaultValue,
  min,
  max,
  label
}: RangeFilterProps) => {
  const [value, setValue] = useState<number>(
    selectedKeys.length && selectedKeys[0] ? (selectedKeys[0] as number) : defaultValue || min
  );
  return (
    <Form
      onFinish={() => {
        setSelectedKeys([value] as never);
        confirm();
      }}
      style={{ width: 320, padding: 24 }}
    >
      <Typography level={"body-14m"}>{label}</Typography>
      <Divider style={{ margin: "2px 0" }} />
      <Flex align='center' gap={16}>
        <Slider min={min} max={max} value={value} onChange={setValue} style={{ width: "100%" }} />
        <InputNumber
          min={min}
          max={max}
          value={value}
          controls={false}
          onChange={val => setValue(val as number)}
          style={{ width: "100px" }}
        />
      </Flex>
      <Flex style={{ marginTop: 16 }} gap={12}>
        <Button htmlType='submit' type='primary' style={{ width: "100%", borderRadius: 6 }}>
          Confirm
        </Button>
        <Button
          onClick={() => {
            setSelectedKeys([]);
            clearFilters?.();
            setValue(min);
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

export function DecompositionsComponent() {
  const { repoId = "" } = useParams();

  const navigate = useNavigate();
  const limit = 20;
  const [page, setPage] = useState(1);
  const [filters, setFilters] = useState<Partial<EntryPointInput>>();
  const skip = (page - 1) * limit;
  const { entryPoints, isLoading, total } = useEntryPointByRepository({
    repoId,
    limit,
    skip,
    ...filters
  });
  const { setSelectedEntry } = useFilterGraph();

  const columns: ColumnsType<Partial<DistributionEntryPoint>> = [
    {
      title: "No.",
      dataIndex: "no",
      key: "no",
      width: 80
    },
    {
      title: "EntryPoint",
      dataIndex: "name",
      key: "name"
    },
    {
      title: "LoC",
      dataIndex: "line_of_code",
      filteredValue: [filters?.loc_filter as number],
      key: "line_of_code",
      filterDropdown: props => (
        <SliderFilter defaultValue={0} label='LoC filter' {...props} min={0} max={10000} />
      )
    },
    {
      title: "Complexity",
      dataIndex: "complexity",
      key: "complexity",
      filteredValue: [filters?.complexity_filter as number],
      filterDropdown: props => (
        <SliderFilter defaultValue={0} label='Complexity filter' {...props} min={0} max={1000} />
      )
    },
    {
      title: "Files",
      dataIndex: "number_of_files",
      key: "number_of_files",
      filteredValue: [filters?.number_of_files_filter as number],
      filterDropdown: props => (
        <SliderFilter defaultValue={1} label='Files filter' {...props} min={0} max={1000} />
      )
    },
    {
      title: "Critical",
      dataIndex: "criticality",
      key: "criticality",
      filterMultiple: false,
      filteredValue: [filters?.criticality_filter as string],
      filters: [
        { value: "LOW", text: "Low" },
        { value: "MEDIUM", text: "Medium" },
        { value: "HIGH", text: "High" }
      ]
    }
  ];
  const handleTableChange = (
    _: TablePaginationConfig,
    filtersValue: Record<string, FilterValue | null>
  ) => {
    // eslint-disable-next-line @typescript-eslint/naming-convention
    const { line_of_code, criticality, complexity, number_of_files, label } = filtersValue || {};

    setFilters({
      loc_filter: line_of_code?.[0] as number,
      criticality_filter: criticality?.[0] as Criticality,
      complexity_filter: complexity?.[0] as number,
      number_of_files_filter: number_of_files?.[0] as number,
      type_filter: label?.[0] as string
    });
  };

  const handleRowClick = ({ name, _id }: DistributionEntryPoint) => {
    setSelectedEntry(`${_id}-${name}`);
    navigate(`/exploration/${repoId}/exploration/entrypoints`, {
      replace: false
    });
  };

  return (
    <>
      <DecompositionLegend filters={filters as Partial<EntryPointInput>} setFilters={setFilters} />
      <CustomTable
        onChange={handleTableChange}
        columns={columns}
        dataSource={
          addPropertiesToItems(entryPoints, (_, index) => ({
            no: index + 1 + skip
          })) as DistributionEntryPoint[]
        }
        loading={isLoading}
        pagination={{
          pageSize: limit,
          showTitle: true,
          current: skip / limit + 1,
          showSizeChanger: false,
          total: total,
          showQuickJumper: false,
          size: "small",
          onChange(curentPage) {
            setPage(curentPage);
          }
        }}
        rowClassName={record =>
          (record as DistributionEntryPoint).label
            ? `row-type-${(record as DistributionEntryPoint).label.toLowerCase()}`
            : ""
        }
        onRow={record => ({
          onClick: e => {
            e.preventDefault();
            handleRowClick(record as DistributionEntryPoint);
          },
          style: {
            background: `${
              decompositionColors[(record as DistributionEntryPoint)?.label as never] ||
              decompositionColors.BMS
            }!important`
          }
        })}
        rowKey='_id'
        scroll={{ y: "550px" }}
      />
    </>
  );
}
