import { Badge, Col, Progress, Row } from "antd";
import { useState } from "react";
import { useTranslation } from "react-i18next";

import { Typography } from "@components";
import { ComplexityModel } from "@types";
import { roundToDecimalPlaces } from "@utils";

import {
  AnalysisBlock,
  ProcessItem,
  ProcessName,
  Title,
  TitleHightLight,
  WrapAnalysisBlock,
  WrapBadge,
  WrapperCobolCode,
  WrapperProcess
} from "./style";

const LIST_TABS = [
  {
    name: "COBOL",
    value: "Cobol"
  },
  {
    name: "JCL",
    value: "JCL"
  },
  {
    name: "ASM",
    value: "ASM"
  }
  // {
  //   name: 'ONLINE',
  //   value: 'ONLINE'
  // },
  // {
  //   name: 'DATA',
  //   value: 'DATA'
  // }
];

export const CobolCode: React.FC<{ complexity: ComplexityModel }> = ({ complexity }) => {
  const { t } = useTranslation();
  const [activeTab, setTab] = useState(LIST_TABS[0]);

  const getValueProgress = (defaultKey: string): number => {
    return roundToDecimalPlaces(
      (complexity as any)?.[defaultKey?.replace("defaultKey", activeTab?.value)] || 0,
      2
    );
  };

  const dataProgess = [
    {
      color: "#FFB200",
      trailColor: "#FFF5CC",
      name: t("page.assessment.avg_loc"),
      maxName: t("page.assessment.max_loc"),
      defaultKey: "avg_defaultKey_LOCs"
    },
    // {
    //   color: '#9BF9BB',
    //   trailColor: '#DAD7FE',
    //   name: t("page.assessment.no_files"),
    //   defaultKey: 'num_defaultKey_files'
    // },
    {
      color: "#02A0FC",
      trailColor: "#CCF8FE",
      name: t("page.assessment.avg_cyc_level"),
      maxName: t("page.assessment.max_cyc_level"),
      defaultKey: "avg_defaultKey_Cyc"
    },
    {
      color: "#A129FF",
      trailColor: "#FFE5D3",
      name: t("page.assessment.avg_no_tokens"),
      maxName: t("page.assessment.max_no_tokens"),
      defaultKey: "avg_defaultKey_n_tokens"
    },
    {
      color: "#FF453A",
      trailColor: "#FFE5D3",
      name: t("page.assessment.avg_no_op"),
      maxName: t("page.assessment.max_no_op"),
      defaultKey: "avg_defaultKey_n_operators"
    }
  ];

  return (
    <WrapperCobolCode>
      <Title>
        {LIST_TABS?.map((tab, index) => {
          const isLast = LIST_TABS?.length === index + 1;
          if (tab.value === activeTab.value) {
            return (
              <TitleHightLight onClick={() => setTab(tab)}>
                {tab.name} {!isLast && "/"}{" "}
              </TitleHightLight>
            );
          }
          return (
            <span onClick={() => setTab(tab)}>
              {tab.name} {!isLast && "/"}{" "}
            </span>
          );
        })}
      </Title>
      <WrapBadge align='flex-start'>
        {dataProgess?.map(badge => (
          <Badge key={badge.name} status='success' text={badge.name} color={badge.color} />
        ))}
      </WrapBadge>
      <Row>
        <WrapAnalysisBlock span={8}>
          <AnalysisBlock>
            <Typography level='h7-body2M' color='grey10'>
              {t("page.assessment.no_files")}
            </Typography>
            <Typography level='h4-titles' color='primary100'>
              {getValueProgress("num_defaultKey_files")}
            </Typography>
          </AnalysisBlock>
          {/* <AnalysisBlock>
            <Typography level='h7-body2M' color='grey10'>{t("page.assessment.code_complexity")}</Typography>
            <Typography level='h4-titles' color='primary100'>
              {roundToDecimalPlaces(
                (complexity as any)?.['C_cobol'?.replace('cobol', String(activeTab?.value).toLocaleLowerCase())] || 0,
                2
              )}
            </Typography>
          </AnalysisBlock> */}
        </WrapAnalysisBlock>
        <Col span={16}>
          <WrapperProcess>
            {dataProgess?.map(item => {
              const avg = getValueProgress(item?.defaultKey);
              const max = getValueProgress(item?.defaultKey?.replace("avg", "max"));
              return (
                <ProcessItem key={item.name} strokeColor={item.color}>
                  <ProcessName>
                    {item.name} / {item.maxName}
                  </ProcessName>
                  <Progress
                    percent={(avg / max) * 100}
                    format={() => `${avg} / ${max}`}
                    trailColor={item?.trailColor || "#FFF5CC"}
                  />
                </ProcessItem>
              );
            })}
          </WrapperProcess>
        </Col>
      </Row>
    </WrapperCobolCode>
  );
};
