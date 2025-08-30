import { Table } from "antd";
import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import { blobApi } from "@api";
import { getCblCommonTableColumns } from "@pages/exploration/file/config";
import { Container } from "@pages/exploration/file/styles";
import { fileSelector } from "@store";
import { IoParamsDef } from "@types";
import { formatDateNoTime } from "@utils";

import { Flex, Typography } from "../../ui";
import { WrapTable } from "../styles";

import { InputTable } from "./InputTable";
import { OutputTable } from "./OutputTable";

export const IoParameter = () => {
  const { t } = useTranslation();
  const { fileId } = useParams();
  const data = useSelector(fileSelector.selectData);
  const [iOParams, setIOParams] = useState<IoParamsDef | null>(null);

  const dataResources = [
    {
      name: data?.name,
      title: "AIC",
      creation_date: formatDateNoTime(data?.created_at || ""),
      update_date: formatDateNoTime(data?.updated_at || "")
    }
  ];

  useEffect(() => {
    const fetchIOParamsData = async () => {
      if (!fileId) return;
      const response = await blobApi.getFileIOParams(fileId);

      if (!response?.data) return;
      setIOParams(response.data);
    };

    fetchIOParamsData();
  }, [fileId]);

  return (
    <Container direction='column' gap={24}>
      <WrapTable>
        <Table
          columns={getCblCommonTableColumns(t)}
          dataSource={dataResources}
          pagination={false}
        />
      </WrapTable>
      <Flex gap={8} direction='column'>
        <Typography level='h6-body1m' color='primary100'>
          1. {t("page.file_explorer.cobol.io_params.title")}
        </Typography>
        <Typography level='h6-body1r' color='grey300'>
          {t("page.file_explorer.cobol.io_params.input_description")}
        </Typography>
        <InputTable data={iOParams?.input_table} />
        <p>
          {t("page.file_explorer.cobol.io_params.note")}: {iOParams?.input_note || "-"}
        </p>
      </Flex>
      <Flex gap={8} direction='column'>
        <Typography level='h6-body1m' color='primary100'>
          2. {t("page.file_explorer.cobol.io_params.output")}
        </Typography>
        <Typography level='h6-body1r' color='grey300'>
          {t("page.file_explorer.cobol.io_params.output_description")}
        </Typography>
        <OutputTable data={iOParams?.output_table} />
        <p>
          {t("page.file_explorer.cobol.io_params.note")}: {iOParams?.output_note || "-"}
        </p>
      </Flex>
    </Container>
  );
};
