import { Badge } from "antd";
import { useTranslation } from "react-i18next";

import { ComplexityModel } from "@types";

import { GaugeChart } from "./components";
import { Title, WrapBadge, Wrapper } from "./style";

export const Complexity: React.FC<{ data: ComplexityModel }> = ({ data }) => {
  const { t } = useTranslation();
  // Low: 0-35 (%)
  // Medium: 35 -65 (%)
  // High: 65 - 100 (%)
  const arcSegments = [
    { min: 0, max: 0.35, color: "#306FFF" },
    { min: 0.35, max: 0.65, color: "#F7C034" },
    { min: 0.65, max: 1, color: "#FF3A29" }
  ];

  const mockDataBadges = [
    {
      color: "#306FFF",
      name: t("level.l")
    },
    {
      color: "#F7C034",
      name: t("level.md")
    },
    {
      color: "#FF3A29",
      name: t("level.h")
    }
  ];

  return (
    <Wrapper>
      <Title>{t("page.assessment.complexity")}</Title>
      <GaugeChart
        arcSegments={arcSegments}
        value={data?.C_sum ? Number(Math.floor(data?.C_sum)) : 0}
      />

      <WrapBadge>
        {mockDataBadges?.map(badge => (
          <Badge key={badge.name} status='success' text={badge.name} color={badge.color} />
        ))}
      </WrapBadge>
    </Wrapper>
  );
};
