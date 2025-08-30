import { Table } from "antd";
import { useTranslation } from "react-i18next";

import { Inputtable } from "@types";

import { WrapCol, WrapTable } from "../styles";

export function OutputTable({ data }: { data?: Inputtable[] }) {
  const { t } = useTranslation();

  const dataResourcesOutput =
    data?.map(i => ({
      name: i?.item_name,
      level: i?.cobol_level,
      cobol_type: i?.cobol_dtype,
      length: i?.length,
      access_mode: i?.access_mode,
      data_type: i?.dtype,
      default_value: i?.default_value,
      remarks: i?.remarks
    })) || [];

  const columnsOutput = [
    {
      title: t("page.file_explorer.cobol.io_params.name"),
      dataIndex: "name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.io_params.level"),
      dataIndex: "level",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.io_params.type"),
      dataIndex: "cobol_type",
      render: (e: string) => <WrapCol mw={150}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.io_params.length"),
      dataIndex: "length",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.io_params.mode"),
      dataIndex: "access_mode",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.io_params.data_type"),
      dataIndex: "date_type",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.io_params.default_value"),
      dataIndex: "default_value",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.io_params.remarks"),
      dataIndex: "remarks",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    }
  ];

  return (
    <WrapTable>
      <Table columns={columnsOutput} dataSource={dataResourcesOutput} pagination={false} />
    </WrapTable>
  );
}
