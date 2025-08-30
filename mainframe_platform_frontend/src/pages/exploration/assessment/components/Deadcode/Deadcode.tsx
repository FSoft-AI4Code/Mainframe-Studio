import styled from "@emotion/styled";
import { Table } from "antd";
import { ColumnsType } from "antd/es/table";

import { allColors } from "@style";
import { addPropertiesToItems } from "@utils";
import { FileDeadCode } from "@types";

export const CustomTable = styled(Table)`
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
  }
`;

interface DeadcodeProps {
  data: FileDeadCode[];
  loading?: boolean;
}
export function Deadcode({ data: files, loading: isLoading }: DeadcodeProps) {
  const columns: ColumnsType<Partial<FileDeadCode>> = [
    {
      title: "No.",
      dataIndex: "no",
      key: "no"
    },

    {
      title: "File Name",
      dataIndex: "file_name",
      key: "file_name"
    },
    {
      title: "Type",
      dataIndex: "type",
      key: "type"
    },
    {
      title: "LoC",
      dataIndex: "lines_of_code",
      key: "lines_of_code"
    },
    {
      title: "Complexity",
      dataIndex: "complexity",
      key: "complexity"
    }
  ];

  return (
    <>
      <CustomTable
        columns={columns}
        dataSource={addPropertiesToItems(files, (_, i) => ({
          no: i + 1
        }))}
        loading={isLoading}
        pagination={{
          pageSize: 10,
          showSizeChanger: false,
          showQuickJumper: false,
          size: "small"
        }}
        rowKey='no'
        scroll={{ y: "calc(100vh - 400px)" }}
      />
    </>
  );
}
