import { ColumnsType } from "antd/es/table";
import Markdown from "react-markdown";

import { Flex, Typography } from "@components";

import { CustomTable } from "../styles";
import { OverviewProgram } from "../fake/blob";

const columns: ColumnsType<any> = [
  {
    title: "No",
    dataIndex: "index",
    key: "index",
    width: 70,
    align: "center"
  },
  {
    title: "Item Name",
    dataIndex: "item_name",
    key: "item_name"
  },
  {
    title: "Physical Name",
    dataIndex: "physical_name",
    key: "physical_name"
  },
  {
    title: "Type",
    dataIndex: "type",
    key: "type"
  },
  {
    title: "CRUD Operation",
    dataIndex: "crud_op",
    key: "crud_op"
  },
  {
    title: "Remarks",
    dataIndex: "notes",
    key: "notes"
  }
];

export default function OverviewPage({ overviewData }: { overviewData: OverviewProgram | null }) {
  return (
    <Flex gap={16} direction='column'>
      <Flex gap={4} direction='column'>
        <Typography level='body-16b'>1. Program Overview</Typography>
        <Markdown>{overviewData?.summarization}</Markdown>
      </Flex>
      <Flex gap={4} direction='column'>
        <Typography level='body-16b'>2. Input/Output Data (IO)</Typography>
        <Typography level='body-16r'>
          The table below shows the IO data used in this program
        </Typography>
      </Flex>
      <CustomTable
        columns={columns}
        dataSource={overviewData?.io_table}
        pagination={false}
        scroll={{ y: "calc(100vh - 400px)" }}
      />
    </Flex>
  );
}
