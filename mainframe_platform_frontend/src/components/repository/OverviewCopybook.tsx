import { Table } from "antd";
import { ColumnsType } from "antd/es/table";
import { useTranslation } from "react-i18next";

import { Flex, Typography } from "../ui";

import { WrapCol, WrapTable } from "./styles";

export function OverviewCopybook() {
  // COBOL_TODO: add data into this page
  // const data = useSelector(fileSelector.selectData);
  const { t } = useTranslation();

  const columns: ColumnsType<any> = [
    {
      title: t("page.file_explorer.copybook.overview.item_name"),
      dataIndex: "index",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.copybook.overview.item_level"),
      dataIndex: "name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.copybook.overview.item_data_type"),
      dataIndex: "physical_name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.copybook.overview.item_length"),
      dataIndex: "type",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.copybook.overview.item_default_value"),
      dataIndex: "crud",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.copybook.overview.item_comment"),
      dataIndex: "comment",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    }
  ];

  return (
    <Flex direction='column' gap={32}>
      <Flex direction='column' gap={8}>
        <Typography level='h6-body1m' color='primary100'>
          1. {t("page.file_explorer.copybook.overview.copy")}
        </Typography>
        <Flex direction='column'>
          <Typography level='h6-body1r' color='grey300'>
            {t("page.file_explorer.copybook.overview.name")}:CP 1ERR
          </Typography>
          <Typography level='h6-body1r' color='grey300'>
            {t("page.file_explorer.copybook.overview.subset")}:
          </Typography>
          <Typography level='h6-body1r' color='grey300'>
            {t("page.file_explorer.copybook.overview.superset")}:
          </Typography>
          <Typography level='h6-body1r' color='grey300'>
            {t("page.file_explorer.copybook.overview.related")}: src/cp1
          </Typography>
        </Flex>
      </Flex>
      <Flex direction='column' gap={16}>
        <Flex direction='column' gap={8}>
          <Typography level='h6-body1m' color='primary100'>
            2. {t("page.file_explorer.copybook.overview.data")}
          </Typography>
          <Typography level='h6-body1r' color='grey300'>
            {t("page.file_explorer.copybook.overview.data_description")}:
          </Typography>
        </Flex>
        <WrapTable>
          <Table columns={columns} />
        </WrapTable>
      </Flex>
    </Flex>
  );
}
