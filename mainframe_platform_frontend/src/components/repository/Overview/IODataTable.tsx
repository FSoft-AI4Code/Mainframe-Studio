import { Table } from "antd";
import { ColumnsType } from "antd/es/table";
import { useTranslation } from "react-i18next";

import { OverviewBlob } from "@types";

import { WrapCol, WrapTable } from "../styles";

export function IODataTable({ data }: { data: OverviewBlob | null }) {
  const { t } = useTranslation();
  const dataResourcesIo =
    data?.io_table?.map(i => ({
      index: i.index,
      name: i.item_name,
      physical_name: i?.physical_name,
      type: i?.type || "File",
      crud: i?.crud_op,
      access_mode: i?.access_mode,
      note: i?.notes
    })) || [];

  const columnsIo: ColumnsType<object> = [
    {
      title: "#",
      dataIndex: "index",
      align: "center",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.overview.io_data_item_name"),
      dataIndex: "name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.overview.io_data_physical_name"),
      dataIndex: "physical_name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.overview.io_data_type"),
      dataIndex: "type",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.overview.io_data_crud"),
      dataIndex: "crud",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.overview.io_data_access_mode"),
      dataIndex: "access_mode",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.overview.io_data_notes"),
      dataIndex: "note",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    }
  ];

  return (
    <WrapTable>
      <Table columns={columnsIo} dataSource={dataResourcesIo} pagination={false} />
    </WrapTable>
  );
}
