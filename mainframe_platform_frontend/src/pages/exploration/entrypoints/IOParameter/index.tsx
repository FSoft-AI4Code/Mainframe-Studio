import { ColumnsType } from "antd/es/table";

import { Flex, Typography } from "@components";

import { CustomTable } from "../styles";
import { IOParams } from "../fake/blob";

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
    title: "Cobol Level",
    dataIndex: "cobol_level",
    key: "cobol_level",
    width: 150
  },
  {
    title: "Cobol Data Type",
    dataIndex: "dtype",
    key: "dtype"
  },
  {
    title: "Redefined Variables",
    dataIndex: "var",
    key: "var"
  },
  {
    title: "Default value",
    dataIndex: "default_value",
    key: "default_value"
  },
  {
    title: "Remarks",
    dataIndex: "remarks",
    key: "remarks"
  }
];

export default function IOParameter({ ioData }: { ioData: IOParams | null }) {
  return ioData ? (
    <Flex gap={16} direction='column'>
      <Flex gap={4} direction='column'>
        <Typography level='body-16b'>1. Input Parameter Definitions</Typography>
        <Typography level='body-16r'>{ioData.input_note}</Typography>
      </Flex>
      <CustomTable
        columns={columns}
        dataSource={ioData.input_table.map((item, index) => ({ ...item, index: index + 1 }))}
        pagination={false}
        scroll={{ y: 400 }}
      />

      <Flex gap={4} direction='column'>
        <Typography level='body-16b'>2. Output Parameter Definitions</Typography>
        <Typography level='body-16r'>{ioData.output_note}</Typography>
      </Flex>
      <CustomTable
        columns={columns}
        dataSource={ioData.output_table.map((item, index) => ({ ...item, index: index + 1 }))}
        pagination={false}
        scroll={{ y: 400 }}
      />

      <Flex gap={4} direction='column'>
        <Typography level='body-16b'>3. Linkage Parameter Definitions</Typography>
      </Flex>
      <CustomTable columns={columns} dataSource={[]} pagination={false} scroll={{ y: 400 }} />
    </Flex>
  ) : null;
}
