import { ColumnType } from "antd/es/table";
import { useMemo } from "react";
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

export function FileViewSubTab({
  data,
  loading,
  pagination
}: {
  pagination: Pagination;
  loading?: boolean;
  data: Array<DataItem>;
}) {
  const { pageSize, page, onChange, total } = pagination || {};

  const columns: ColumnType<Partial<DataItem>>[] = useMemo(
    () => [
      {
        title: "File Name",
        dataIndex: "dataset_name",
        key: "dataset_name",
        width: 150
      },
      {
        title: "Assign Name",
        dataIndex: "ddname",
        key: "ddname"
      },
      {
        title: "File Type",
        dataIndex: "dataset_type",
        key: "dataset_type"
      },
      {
        title: "Open Mode",
        dataIndex: "access_operations",
        key: "open_mode",
        render: access_operations =>
          access_operations?.map((op: AccessOperation) => op.open_mode).join(", "),
        width: 150
      },
      {
        title: "Job Name",
        dataIndex: "jcl_name",
        key: "jcl_name"
      },
      {
        title: "Step Name",
        dataIndex: "step",
        key: "step"
      },
      {
        title: "Program Name",
        dataIndex: "exec_program_id",
        key: "exec_program_id"
      }
    ],
    []
  );

  return (
    <Flex style={{ marginTop: 12 }} direction='column'>
      <CustomTable
        bordered
        loading={loading}
        tableLayout={"auto"}
        showHeader={total > 0 ? true : false}
        columns={columns}
        rowKey={"no"}
        dataSource={addPropertiesToItems(data, (_, i) => ({ no: i + 1 }))}
        pagination={{
          position: ["bottomRight"],
          current: page,
          total,
          pageSize,
          onChange,
          showTotal: () => `Total files: ${total}`
        }}
        scroll={data && data?.length ? { x: "70vw" } : undefined}
        locale={{
          emptyText: <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description='No data to display' />
        }}
      />
    </Flex>
  );
}
