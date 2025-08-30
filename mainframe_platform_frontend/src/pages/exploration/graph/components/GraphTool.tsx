import { CheckOutlined, CloseOutlined } from "@ant-design/icons";
import styled from "@emotion/styled";
import { Select, Switch } from "antd";
import { useMemo, useState } from "react";
import { useTranslation } from "react-i18next";

import { SearchSvg, ZoomInSvg } from "@assets/svg";
import { Flex } from "@components";
import { NetworkingDataType } from "@types";

import { ToolWrapper } from "../styles";

import { ApplicationStat, CopyStat, DatabaseStat } from "./Stats";

type GraphToolProps = {
  onClickZoomIn: () => void;
  isDeadCode?: boolean;
  onChangeDeadCode: () => void;
  searchProps: any;
  chartData: NetworkingDataType;
};

const Wrapper = styled.div`
  position: relative;

  .prefix-icon-wrapper {
    position: absolute;
    z-index: 1;
    width: 3rem;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  && .ant-select {
    font-size: 14px;
    line-height: 20px;
    input {
      margin-left: 30px !important;
    }
    .ant-select-selection-placeholder,
    .ant-select-selection-item {
      margin-left: 27px !important;
    }
  }
`;

export function GraphTool({
  onClickZoomIn,
  searchProps,
  isDeadCode,
  onChangeDeadCode,
  chartData
}: GraphToolProps) {
  const { t } = useTranslation();
  const [clickSearch, setClickSearch] = useState(false);

  const handleBlurInput = () => {
    if (searchProps.value) return;
    setClickSearch(false);
  };
  const stats = useMemo(
    () =>
      chartData.nodes.reduce(
        (result, node) => {
          switch (node.group) {
            case "COBOL":
              result.cobol += 1;
              break;
            case "DB":
              result.db += 1;
              break;
            case "COPY":
              result.cpb += 1;
              break;
            default:
              break;
          }
          return result;
        },
        {
          cobol: 0,
          cpb: 0,
          db: 0
        }
      ),
    [chartData]
  );

  return (
    <ToolWrapper justify='space-between' align='center'>
      <Flex justify='space-between' gap={12} align='center'>
        <ZoomInSvg onClick={onClickZoomIn} style={{ cursor: "pointer" }} />
        {clickSearch ? (
          <Wrapper className={"search-input"}>
            <div className='prefix-icon-wrapper'>
              <SearchSvg />
            </div>
            <Select
              {...searchProps}
              placeholder={t("component.input.search_blob")}
              onBlur={handleBlurInput}
              size='large'
              autoFocus={true}
            />
          </Wrapper>
        ) : (
          <SearchSvg style={{ cursor: "pointer" }} onClick={() => setClickSearch(true)} />
        )}
        <Switch
          size='small'
          checkedChildren={<CheckOutlined />}
          unCheckedChildren={<CloseOutlined />}
          checked={isDeadCode}
          onChange={onChangeDeadCode}
        />
      </Flex>
      <Flex justify='space-between' gap={16} align='center'>
        <ApplicationStat content={`${stats.cobol} ${stats.cobol > 1 ? "Programs" : "Program"}`} />
        <DatabaseStat content={`${stats.db} ${stats.db > 1 ? "Databases" : "Database"}`} />
        <CopyStat content={`${stats.cpb} ${stats.cpb > 1 ? "Copybooks" : "Copybook"}`} />
      </Flex>
    </ToolWrapper>
  );
}
