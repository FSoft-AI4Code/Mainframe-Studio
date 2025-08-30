import styled from "@emotion/styled";
import { Table, Tooltip } from "antd";
import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { dracula } from "react-syntax-highlighter/dist/esm/styles/prism";

import { blobApi } from "@api";
import { getCblCommonTableColumns } from "@pages/exploration/file/config";
import { Container } from "@pages/exploration/file/styles";
import { fileSelector } from "@store";
import { colors } from "@style";
import { Reference } from "@types";
import { formatDateNoTime } from "@utils";

import { Flex, Typography } from "../ui";

import { WrapTable } from "./styles";

const Header = styled.div`
  padding: 10px 16px;
  text-align: center;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  background: ${({ theme }) => theme.colors.primary100};
  color: ${({ theme }) => theme.colors.grey900};
`;

const Content = styled.div`
  display: flex;
  border: ${({ theme }) => `solid 1px ${theme.colors.grey500}`};
  padding: 24px 16px;
  gap: 24px;
  flex-direction: column;
`;

export const References = () => {
  const { t } = useTranslation();
  const data = useSelector(fileSelector.selectData);
  const { fileId } = useParams();
  const [references, setReferences] = useState<Array<Reference> | null>(null);
  const dataResources = [
    {
      name: data?.name,
      title: "AIC",
      creation_date: formatDateNoTime(data?.created_at || ""),
      update_date: formatDateNoTime(data?.updated_at || "")
    }
  ];

  useEffect(() => {
    const fetchReferences = async () => {
      if (!fileId) return;

      const response = await blobApi.getFileReferences(fileId);

      if (!response?.data) return;
      setReferences(response.data);
    };

    fetchReferences();
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
      <WrapTable>
        <Header>{`Cobol source code reference & explanation (${data?.path})`}</Header>
        <Content>
          {references?.map(reference => (
            <Flex direction='column' key={reference.command} style={{ width: "100%" }}>
              <Tooltip title={reference.explain} placement='bottomLeft'>
                <Typography
                  level='h6-body1r'
                  style={{ backgroundColor: colors.secondary100, padding: "0 8px", height: 24 }}
                >
                  {reference.command}
                </Typography>
              </Tooltip>
              {reference.sub_commands ? (
                <Flex gap={0} direction='column'>
                  {reference.sub_commands.map(subCommand => (
                    <Tooltip
                      title={subCommand.explain}
                      key={subCommand.command}
                      placement='bottomLeft'
                    >
                      <SyntaxHighlighter
                        language='cobol'
                        style={dracula}
                        customStyle={{ margin: "0", borderRadius: "initial", padding: "5px 15px" }}
                      >
                        {subCommand.command}
                      </SyntaxHighlighter>
                    </Tooltip>
                  ))}
                </Flex>
              ) : null}
            </Flex>
          ))}
        </Content>
      </WrapTable>
    </Container>
  );
};
