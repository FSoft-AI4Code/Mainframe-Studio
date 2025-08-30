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
import { colors } from "@style";
import { formatDateNoTime } from "@utils";

import { Flex, Typography } from "../ui";

import { WrapTable } from "./styles";

const listItemRegExp = /^\d+\./;

const Content = styled.div`
  ul {
    padding-left: 0px;
    list-style: none;
  }
`;

export const ProcessingLogic = () => {
  const { t } = useTranslation();
  const data = useSelector(fileSelector.selectData);
  const { fileId } = useParams();

  const [processLogic, setProcessLogic] = useState<Array<string> | null>(null);
  const dataResources = [
    {
      name: data?.name,
      title: "AIC",
      creation_date: formatDateNoTime(data?.created_at || ""),
      update_date: formatDateNoTime(data?.updated_at || "")
    }
  ];

  useEffect(() => {
    const fetchProcessLogic = async () => {
      if (!fileId) return;

      const response = await blobApi.getFileProcessLogic(fileId);

      if (!response?.data) return;
      setProcessLogic(response.data);
    };

    fetchProcessLogic();
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
          {t("page.file_explorer.cobol.process_logic.title")}
        </Typography>
        <Content>
          <ul>
            {processLogic?.map(i => (
              <li key={i}>
                <Typography
                  level={listItemRegExp.test(i) ? "h6-body1r" : "h6-body1m"}
                  color={listItemRegExp.test(i) ? "grey300" : "white"}
                  style={{ backgroundColor: listItemRegExp.test(i) ? "" : colors.primary100 }}
                >
                  {i}
                </Typography>
              </li>
            ))}
          </ul>
        </Content>
      </Flex>
    </Container>
  );
};
