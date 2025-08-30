import { ColumnType } from "antd/es/table";
import { Empty } from "antd";

import { Flex } from "@components";
import { addPropertiesToItems } from "@utils";
import { AccessOperation, DataSetInfo } from "@types";

import { CustomTable } from "../../styles";

type DataItem = DataSetInfo;
type Pagination = {
  page: number;
  onChange?: (page: number, pageSize: number) => void;
  pageSize: number;
  total: number;
};

export function JobviewSubTab({
  data,
  loading,
  pagination
}: {
  pagination: Pagination;
  loading?: boolean;
  data: Array<DataItem>;
}) {
  const { pageSize, page, onChange, total } = pagination || {};

  const columns: ColumnType<Partial<DataItem>>[] = [
    {
      title: "JCL Name",
      dataIndex: "jcl_name",
      key: "jcl_name",
      width: 120
    },
    {
      title: "Step",
      dataIndex: "step",
      key: "step",
      width: 100
    },
    {
      title: "Exec Program",
      dataIndex: "exec_program_id",
      key: "exec_program_id",
      width: 150
    },
    {
      title: "Physical File",
      dataIndex: "dataset_name",
      key: "dataset_name",
      width: 200
    },
    {
      title: "Assign Name",
      dataIndex: "ddname",
      key: "ddname",
      width: 120
    },
    {
      title: "File Type",
      dataIndex: "dataset_type",
      key: "dataset_type",
      width: 120
    },
    {
      title: "Open Mode",
      dataIndex: "access_operations",
      key: "open_mode",
      render: access_operations =>
        access_operations?.map((op: AccessOperation) => op.open_mode).join(", "),
      width: 150
    }
  ];

  return (
    <Flex style={{ marginTop: 12 }} direction='column'>
      <CustomTable
        bordered
        loading={loading}
        showHeader={total > 0 ? true : false}
        tableLayout={"auto"}
        columns={columns}
        rowKey={"no"}
        dataSource={addPropertiesToItems(data, (_, i) => ({ no: i + 1 }))}
        pagination={{
          position: ["bottomRight"],
          current: page,
          total,
          pageSize,
          showTotal: () => `Total files: ${total}`,
          onChange
        }}
        scroll={data && data?.length ? { x: "70vw" } : undefined}
        locale={{
          emptyText: <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description='No data to display' />
        }}
      />
    </Flex>
  );
}
