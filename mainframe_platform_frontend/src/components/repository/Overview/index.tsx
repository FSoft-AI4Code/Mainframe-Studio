import styled from "@emotion/styled";
import { Table } from "antd";
import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import { blobApi } from "@api";
import { getCblCommonTableColumns } from "@pages/exploration/file/config";
import { Container } from "@pages/exploration/file/styles";
import { fileSelector } from "@store";
import { OverviewBlob } from "@types";
import { formatDateNoTime } from "@utils";

import { Flex, Typography } from "../../ui";
import { WrapTable } from "../styles";

import { IODataTable } from "./IODataTable";

const HightLight = styled.span`
  font-weight: 500;
  color: ${({ theme }) => theme.colors.primary100};
`;

export const Overview = () => {
  const { t } = useTranslation();
  const { fileId } = useParams();
  const data = useSelector(fileSelector.selectData);
  const [overview, setOverview] = useState<OverviewBlob | null>(null);
  const dataResources = [
    {
      name: data?.name,
      title: "AIC",
      creation_date: formatDateNoTime(data?.created_at || ""),
      update_date: formatDateNoTime(data?.updated_at || "")
    }
  ];

  useEffect(() => {
    const fetchOverviewData = async () => {
      if (!fileId) return;
      const response = await blobApi.getFileOverview(fileId);

      if (!response?.data) return;
      setOverview(response.data);
    };

    fetchOverviewData();
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
      <Typography level='h6-body1r' color='grey300'>
        {data?.name ? (
          <>
            <div>
              <Typography level='h6-body1m' color='primary100'>
                1. {t("page.file_explorer.cobol.overview.title")}
              </Typography>
            </div>
            {t("page.file_explorer.cobol.overview.program_name")}: {data?.name}
          </>
        ) : null}
        {overview?.io_files.length ? (
          <div>
            {t("page.file_explorer.cobol.overview.program_io_file")}:{" "}
            {overview?.io_files?.join(", ")}
          </div>
        ) : null}
        {overview?.db_accesses.length ? (
          <div>
            <HightLight>{t("page.file_explorer.cobol.overview.program_db_access")}: </HightLight>{" "}
            {t("page.file_explorer.cobol.overview.program_db_access_content", {
              tb_nums: overview?.db_accesses?.length ?? 0
            })}{" "}
            {overview?.db_accesses?.map(access => access.name)?.join(", ")}
          </div>
        ) : null}
        {overview?.copy_files.length ? (
          <div>
            <HightLight>{t("page.file_explorer.cobol.overview.program_copy_using")}: </HightLight>{" "}
            {overview?.copy_files?.join(", ")}
          </div>
        ) : null}
        {overview?.call_files.length ? (
          <div>
            <HightLight>{t("page.file_explorer.cobol.overview.program_related_pgm")}: </HightLight>
            {t("page.file_explorer.cobol.overview.program_related_pgm_content")}{" "}
            {overview?.call_files?.join(", ")}
          </div>
        ) : null}
        {overview?.summarization ? (
          <>
            <div>
              <HightLight>
                {t("page.file_explorer.cobol.overview.program_summarization")}:{" "}
              </HightLight>
            </div>
            {overview?.summarization}
          </>
        ) : null}
      </Typography>
      <Flex gap={8} direction='column'>
        <Typography level='h6-body1m' color='primary100'>
          2. {t("page.file_explorer.cobol.overview.io_data")}
        </Typography>
        <Typography level='h6-body1r' color='grey300'>
          {t("page.file_explorer.cobol.overview.io_data_description")}:
        </Typography>
        <IODataTable data={overview} />
      </Flex>
    </Container>
  );
};
