import { Table } from "antd";
import { ColumnsType } from "antd/es/table";
import { useTranslation } from "react-i18next";

import { Flex, Typography } from "../ui";

import { WrapCol, WrapTable } from "./styles";

export function OverviewDatabase() {
  const { t } = useTranslation();

  const columns: ColumnsType<any> = [
    {
      title: t("page.file_explorer.database.overview.data_item_name"),
      dataIndex: "index",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.overview.data_type"),
      dataIndex: "name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.overview.data_nallable"),
      dataIndex: "physical_name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.overview.data_cobol_item_name"),
      dataIndex: "type",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.overview.data_cobol_level"),
      dataIndex: "crud",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.overview.data_cobol_data_type"),
      dataIndex: "crud",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.overview.data_length"),
      dataIndex: "crud",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.overview.data_default_value"),
      dataIndex: "crud",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.overview.data_comment"),
      dataIndex: "crud",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    }
  ];

  return (
    <Flex direction='column' gap={32}>
      <Flex direction='column' gap={8}>
        <Typography level='h6-body1m' color='primary100'>
          1. {t("page.file_explorer.database.overview.title")}
        </Typography>
        <Flex direction='column'>
          <Typography level='h6-body1r' color='grey300'>
            {t("page.file_explorer.database.overview.name")}: DHSACTBL (the name declared in the
            "EXEC SQL DECLARE..." statement).
          </Typography>
          <Typography level='h6-body1m' color='grey300'>
            {t("page.file_explorer.database.overview.file")}: The file name contains the "declare"
            command \(there may be multiple tables declared in one file, each table needing a
            separate report\)
          </Typography>
          <Typography level='h6-body1r' color='grey300'>
            {t("page.file_explorer.database.overview.related_pgms")}:
            JDHSB354_HPC1_JSYS.ENDV.HON.IMPORT.PGMBLIB
          </Typography>
        </Flex>
      </Flex>
      <Flex direction='column' gap={16}>
        <Flex direction='column' gap={8}>
          <Typography level='h6-body1m' color='primary100'>
            2. {t("page.file_explorer.database.overview.data")}
          </Typography>
          <Typography level='h6-body1r' color='grey300'>
            {t("page.file_explorer.database.overview.data_description")}
          </Typography>
        </Flex>
        <WrapTable>
          <Table columns={columns} />
        </WrapTable>
      </Flex>
    </Flex>
  );
}
