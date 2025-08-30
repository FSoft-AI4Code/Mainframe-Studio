import { type ColumnsType } from "antd/es/table";

import { Flex, Typography } from "@components";
import { JCLStep } from "@types";

import { CustomTable } from "../../../entrypoints/styles";

type ColumnData = JCLStep & { index: number };

const columns: ColumnsType<Partial<ColumnData>> = [
  {
    title: "No",
    dataIndex: "index",
    key: "index",
    width: 70,
    align: "center"
  },
  {
    title: "Step Name",
    dataIndex: "step_name",
    key: "step_name"
  },
  {
    title: "Program Executed",
    dataIndex: "program_executed",
    key: "program_executed"
  },
  {
    title: "Input/Output",
    dataIndex: "io_statements",
    key: "io_statements",
    render(value: string[]) {
      return value.map(str => <div key={str}>{str}</div>);
    }
  },
  {
    title: "Properties",
    dataIndex: "property",
    key: "property"
  }
];

export default function StepJCL({ steps }: { steps: JCLStep[] | null }) {
  return steps ? (
    <Flex direction='column' gap={32}>
      <Typography level='body-16b' color='primary10'>
        JCL Step List
      </Typography>

      <CustomTable
        columns={columns}
        rowKey='index'
        dataSource={steps?.map((step, id) => ({ ...step, index: id + 1 }))}
        pagination={false}
        scroll={{ y: "calc(100vh - 400px)" }}
      />
    </Flex>
  ) : null;
}
