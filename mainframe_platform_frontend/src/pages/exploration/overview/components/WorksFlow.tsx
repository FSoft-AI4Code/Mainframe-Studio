import { Row } from "antd";
import { useParams } from "react-router-dom";

import { CustomCard, Flex, Typography } from "@components";
import { useComplexitiesDistributionQuery, useDeadCodeFile, useReverseCoverage } from "@services";
import { v2CommonColors } from "@style";
import { roundToDecimalPlaces } from "@utils";

export function WorksFlow() {
  const { repoId = "" } = useParams();
  const { totalCoverage, isLoading } = useReverseCoverage({ repoId });
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { deadAndTotal } = useDeadCodeFile({ repoId, limit: 100, skip: 0 });
  const { averageComplexity } = useComplexitiesDistributionQuery({
    repoId,
    reprocess: false
  });
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { dead = 0, total = 0 } = deadAndTotal || {};
  const worksFlow = [
    {
      title: "Assessment",
      items: [
        { label: "Coverage", value: `${roundToDecimalPlaces(totalCoverage, 2)}%` },
        { label: "Complexity", value: `${roundToDecimalPlaces(averageComplexity, 2)}` },
        { label: "Deadcode", value: `${roundToDecimalPlaces((dead / total) * 100, 2)}%` }
      ]
    },
    {
      title: "Explorer",
      items: [
        { label: "Entrypoint", value: "0" },
        { label: "Verification", value: "0%" },
        { label: "Feedback", value: "0" }
      ]
    },
    {
      title: "Migrations",
      items: [
        { label: "Test coverage", value: "0%" },
        { label: "Rewrite", value: "0%" },
        { label: "Docs coverage", value: "0%" }
      ]
    }
  ];

  return (
    <Row gutter={[24, 0]}>
      <CustomCard
        title={
          <Typography level='body-16b' color='primary10'>
            Workflow
          </Typography>
        }
        colProps={{ xs: 24, style: { width: "100%" } }}
      >
        <Row wrap gutter={[24, 24]}>
          {worksFlow?.map(({ title, items }) => (
            <CustomCard
              key={title}
              loading={isLoading}
              title={
                <>
                  <Typography level='body-16b' color='primary10'>
                    {title}
                  </Typography>
                </>
              }
              bodyStyle={{ padding: "6px 24px 24px 24px" }}
              style={{ background: v2CommonColors.neutral3 }}
              colProps={{ style: { width: "100%" }, xs: 24, lg: 8 }}
            >
              {items.map(({ label, value }, key) => (
                <Flex key={`${label}${key}`} justify='space-between' align='center'>
                  <Typography level='button-14m' color='primary10'>
                    {label}
                  </Typography>
                  <Typography level='body-16b' color='primary6'>
                    {value}
                  </Typography>
                </Flex>
              ))}
            </CustomCard>
          ))}
        </Row>
      </CustomCard>
    </Row>
  );
}
