import { CaretDownOutlined, CaretUpOutlined, MinusOutlined, PlusOutlined } from "@ant-design/icons";
import { Card, Table } from "antd";
import { ColumnsType } from "antd/es/table";
import Input from "antd/es/input/Input";
import { useMemo, useState } from "react";

import { Button, Flex, Typography } from "@components";
import { allColors } from "@style";
import { ReverseCopybookData, Variable } from "@types";

import { FilterSection, ScrollableWrapper, TableWrapper } from "../styles";

// import { FilterSection, ScrollableWrapper, TableWrapper } from "../styles";

// import { FilterSection, ScrollableWrapper, TableWrapper } from "../../../data-asset/styles";

interface CopyBookReportProps {
  copybookData: ReverseCopybookData;
}

export interface VariableData extends Variable {
  children?: VariableData[];
  key?: string;
}

export const buildHierarchy = (variables: VariableData[]): VariableData[] => {
  const hierarchy: VariableData[] = [];
  const stack: VariableData[] = [];

  variables?.forEach(variable => {
    const newVariable: VariableData = { ...variable, children: [] };
    while (
      stack.length > 0 &&
      parseInt(stack[stack.length - 1].level) >= parseInt(newVariable.level)
    ) {
      stack.pop();
    }
    if (stack.length > 0) {
      stack[stack.length - 1].children?.push(newVariable);
    } else {
      hierarchy.push(newVariable);
    }
    stack.push(newVariable);
  });

  return hierarchy;
};
export const getAllKeys = (data: VariableData[]): string[] => {
  let keys: string[] = [];
  data.forEach(item => {
    keys.push(item?.key as string);
    if (item.children) {
      keys = keys.concat(getAllKeys(item.children));
    }
  });
  return keys;
};

export const convertToTableData = (variables: VariableData[], parentKey = ""): VariableData[] => {
  return variables?.map((item, index) => {
    const key = `${parentKey}${index}`;
    return {
      key,
      level: item?.level,
      name: item?.name,
      business_name: item?.business_name,
      length: item?.length,
      byte_length: item?.byte_length,
      data_type: item?.data_type,
      variable_position: item?.variable_position,
      remarks: item?.remarks,
      children: item?.children ? convertToTableData(item?.children, `${key}-`) : undefined
    };
  });
};

export default function CopyBookReport({ copybookData }: CopyBookReportProps) {
  const { output, name } = copybookData || {};
  const { copy_length: copyLength, variables_declaration: variablesDeclaration } = output || {};
  const [searchText, setSearchText] = useState("");
  const filteredData = useMemo(
    () =>
      variablesDeclaration?.filter((variable: VariableData) =>
        variable?.name?.toLowerCase()?.includes(searchText?.toLowerCase())
      ),
    [searchText]
  );

  const transformedData = buildHierarchy(filteredData);

  const columns: ColumnsType<VariableData> = [
    { title: "Level", dataIndex: "level", width: 200 },
    {
      title: "Name",
      dataIndex: "name"
    },
    {
      title: "Business Name",
      dataIndex: "business_name",
      render: (value: string) => value || "-"
    },
    {
      title: "Data Type",
      dataIndex: "data_type",
      render: (value: string) => value || "-"
    },
    { title: "Length", dataIndex: "length" },
    { title: "Byte Length", dataIndex: "byte_length" },
    { title: "Position", dataIndex: "variable_position" },
    {
      title: "Remarks",
      dataIndex: "remarks",
      render: (value: string) => value || "-"
    }
  ];

  const dataSource = convertToTableData(transformedData);
  const [expandedRowKeys, setExpandedRowKeys] = useState<React.Key[]>(getAllKeys(dataSource));

  // eslint-disable-next-line no-console
  console.log("expandedRowKeys", expandedRowKeys, getAllKeys(dataSource));
  const isExpanedAll = expandedRowKeys?.length === getAllKeys(dataSource)?.length;
  const handleExpandCollapse = () => {
    if (expandedRowKeys.length > 0) {
      setExpandedRowKeys([]);
    } else {
      setExpandedRowKeys(getAllKeys(dataSource));
    }
  };

  return (
    <ScrollableWrapper direction='column'>
      <Card
        title={
          <Typography level='title-24b' color='primary10'>
            Copybook Report: {name}
          </Typography>
        }
        style={{ background: allColors.neutral1, width: "100%" }}
      >
        <Flex direction='column' gap={24}>
          <Card title='Copy Length' style={{ background: allColors.neutral2 }}>
            <Typography level='body-16b' color='primary10'>
              {copyLength}
            </Typography>
          </Card>
          <Card title='Variables Declaration' style={{ background: allColors.neutral2 }}>
            <FilterSection>
              <Input
                placeholder='Search by Name'
                value={searchText}
                onChange={e => setSearchText(e.target.value)}
                style={{ flex: 1 }}
              />
              <Button
                type='primary'
                style={{
                  borderRadius: 4,
                  minWidth: 122
                }}
                icon={isExpanedAll ? <CaretUpOutlined /> : <CaretDownOutlined />}
                onClick={handleExpandCollapse}
              >
                {isExpanedAll ? "Collapse All" : "Expand All"}
              </Button>
            </FilterSection>
            <TableWrapper>
              <Table
                columns={columns}
                dataSource={dataSource}
                expandable={{
                  defaultExpandAllRows: false,
                  expandedRowKeys: expandedRowKeys,
                  indentSize: 30,
                  expandIcon: props => {
                    const children = props?.record?.children;
                    if (!children || children.length === 0)
                      return <MinusOutlined style={{ width: 25, opacity: 0 }} />;
                    if (children?.length > 0) {
                      if (props.expanded) {
                        return (
                          <Button
                            shape='circle'
                            type='text'
                            size='small'
                            style={{
                              marginRight: 4
                            }}
                            onClick={e => {
                              props.onExpand(props.record, e);
                            }}
                          >
                            <MinusOutlined />
                          </Button>
                        );
                      } else {
                        return (
                          <Button
                            shape='circle'
                            type='text'
                            size='small'
                            style={{
                              marginRight: 4
                            }}
                            onClick={e => {
                              props.onExpand(props.record, e);
                            }}
                          >
                            <PlusOutlined />
                          </Button>
                        );
                      }
                    }
                  },
                  onExpandedRowsChange: setExpandedRowKeys as never
                }}
                rowKey={"key"}
                pagination={{
                  pageSize: 10,
                  showSizeChanger: false,
                  showQuickJumper: false,
                  size: "small"
                }}
              />
            </TableWrapper>
          </Card>
        </Flex>
      </Card>
    </ScrollableWrapper>
  );
}
