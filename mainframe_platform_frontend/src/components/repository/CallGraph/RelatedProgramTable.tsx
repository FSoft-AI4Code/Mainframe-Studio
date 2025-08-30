import Table, { ColumnsType } from "antd/es/table";
import { useTranslation } from "react-i18next";

import { Program } from "@types";

import { WrapCol, WrapTable } from "../styles";

export function RelatedProgramTable({ data }: { data?: Program[] }) {
  const { t } = useTranslation();

  const dataResourcesRelated =
    data?.map((row, index) => ({
      index: index,
      program_id: row.program_id,
      program_type: row.program_type,
      program_name: row.program_name,
      call_type: row.call_type,
      note: row.notes,
      locations: row.locations
    })) || [];

  const columnsRelated: ColumnsType<any> = [
    {
      title: "#",
      dataIndex: "index",
      align: "center",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.call_graph.id"),
      dataIndex: "program_id",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.call_graph.type"),
      dataIndex: "program_type",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.call_graph.name"),
      dataIndex: "program_name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.call_graph.call_type"),
      dataIndex: "call_type",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.call_graph.notes"),
      dataIndex: "notes",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.cobol.call_graph.locations"),
      dataIndex: "locations",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    }
  ];

  return (
    <WrapTable>
      <Table columns={columnsRelated} dataSource={dataResourcesRelated} pagination={false} />
    </WrapTable>
  );
}
