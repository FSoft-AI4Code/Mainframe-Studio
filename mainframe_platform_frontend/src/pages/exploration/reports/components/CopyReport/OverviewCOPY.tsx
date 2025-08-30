import { ColumnsType } from "antd/es/table";

import { Flex } from "@components";
import { CopySession } from "@types";

import { CustomTable } from "../styles";

const columns: ColumnsType<Partial<CopySession>> = [
  {
    title: "No",
    dataIndex: "index",
    key: "index",
    width: 70,
    align: "center"
  },
  {
    title: "Level",
    dataIndex: "level",
    key: "level"
  },
  {
    title: "Variable Name",
    dataIndex: "name",
    key: "name"
  },
  {
    title: "Data Types",
    dataIndex: "picture_clause",
    key: "picture_clause"
  },
  {
    title: "Redefined Variable",
    dataIndex: "redefine",
    key: "redefine"
  },
  {
    title: "Default Value",
    dataIndex: "default_value",
    key: "default_value"
  },
  {
    title: "Mapping Data Type",
    dataIndex: "data_type",
    key: "data_type"
  }
];

export default function OverviewCOPY({ data }: { data: CopySession[] | null }) {
  return data ? (
    <Flex direction='column' gap={32}>
      <CustomTable
        columns={columns}
        dataSource={data.map((step, id) => ({ ...step, index: id + 1 }))}
        pagination={false}
        scroll={{ y: "calc(100vh - 400px)" }}
      />
    </Flex>
  ) : null;
}
