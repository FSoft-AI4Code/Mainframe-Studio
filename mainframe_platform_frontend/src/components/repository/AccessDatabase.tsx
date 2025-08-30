import { Table } from "antd";
import { ColumnsType } from "antd/es/table";
import { useTranslation } from "react-i18next";

import { Flex, Typography } from "../ui";

import { WrapCol, WrapTable } from "./styles";

export function AccessDatabase() {
  const { t } = useTranslation();

  const columns: ColumnsType<object> = [
    {
      title: t("page.file_explorer.database.access.file_name"),
      dataIndex: "index",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.access.nallable"),
      dataIndex: "name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    },
    {
      title: t("page.file_explorer.database.access.file_name"),
      dataIndex: "physical_name",
      render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
    }
  ];

  return (
    <Flex direction='column' gap={16}>
      <Typography level='h6-body1r' color='grey300'>
        {t("page.file_explorer.database.access.description")}
      </Typography>
      <WrapTable>
        <Table columns={columns} />
      </WrapTable>
    </Flex>
  );
}
