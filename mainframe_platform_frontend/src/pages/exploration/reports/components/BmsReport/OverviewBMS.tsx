import { ColumnsType } from "antd/es/table";

import { addPropertiesToItems } from "@utils";
import { BMSRow } from "@types";
import { usePagination } from "@hooks";

import { CustomTable } from "./styles";

const columns: ColumnsType<Partial<BMSRow>> = [
  {
    title: "No.",
    dataIndex: "no",
    key: "no",
    width: 70,
    align: "center"
  },
  {
    title: "Name",
    dataIndex: "name",
    key: "name"
  },
  {
    title: "Type",
    dataIndex: "item_type",
    key: "item_type"
  },
  {
    title: "Pos",
    dataIndex: "position",
    key: "position",
    render(value) {
      return value?.join(", ");
    }
  },
  {
    title: "Length",
    dataIndex: "length",
    key: "length"
  },
  {
    title: "Properties",
    dataIndex: "properties",
    key: "properties",
    render(value, record) {
      return `${record.attribute} ${record.color}`;
    }
  },
  {
    title: "Initial Value",
    dataIndex: "initial_value",
    key: "initial_value"
  }
];

export default function OverviewBMS({ rows, loading }: { rows: BMSRow[]; loading?: boolean }) {
  const { handleChangeSize, pageSize } = usePagination({ defaultPageSize: 10 });
  return (
    <CustomTable
      columns={columns}
      loading={loading}
      dataSource={addPropertiesToItems(rows, (_, index) => ({
        no: index + 1
      }))}
      rowKey='no'
      pagination={{ pageSize, onChange: handleChangeSize }}
      scroll={{ x: 500 }}
    />
  );
}
