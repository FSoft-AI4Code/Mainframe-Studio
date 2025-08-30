import { useMemo } from "react";
import { useParams } from "react-router-dom";
import { Spin } from "antd";

import { useGetComplexitiesByRepository } from "@services";
import { Flex, Typography } from "@components";
import { useRepository } from "@hooks";

import { MeanComplexityData } from "./components/MeanComplexity";
import { ComplexityDistribution, ComplexityLevels, McCabe, MeanComplexity } from "./components";

const supportLabel = ["COBOL", "JCL_IBM", "JCL", "JCL_FUJITSU", "COPY", "SCREEN", "BSM"];

export type LabelComplexity =
  | "cobol"
  | "jcl"
  | "copybook"
  | "screen"
  | "jcl_ibm"
  | "jcl_fujitsu"
  | "copy"
  | "bms";

export function ComplexityPage() {
  const { repoId } = useParams();
  const { repository, loadingRepository } = useRepository();

  const { predictComplexity } = useGetComplexitiesByRepository({
    repoId: repoId as string,
    enabled: !!repository?.is_reversed
  });

  const complexityData = useMemo(
    () => predictComplexity.filter(({ label }) => supportLabel.includes(label)),
    [predictComplexity]
  );

  const meanComplexity: MeanComplexityData = useMemo(() => {
    const complexitySums: Record<string, number> = {};
    const counts: Record<string, number> = {};

    complexityData.forEach?.(file => {
      let label = file.label;
      const complexity = file.complexity;

      if (label === "JCL_IBM" || label === "JCL_FUJITSU") label = "JCL";
      if (label === "BMS") label = "SCREEN";

      if (!complexitySums[label]) {
        complexitySums[label] = 0;
        counts[label] = 0;
      }

      complexitySums[label] += complexity;
      counts[label] += 1;
    });

    const mean: Record<string, number> = {};

    for (const label in complexitySums) {
      mean[label] = complexitySums[label] / counts[label];
    }

    return {
      cobol: complexitySums.COBOL ?? 0,
      jcl: complexitySums.JCL ?? 0,
      screen: complexitySums.SCREEN ?? 0,
      copybook: complexitySums.COPY ?? 0
    };
  }, [complexityData]);

  const mcCabe = useMemo(
    () =>
      complexityData?.length
        ? complexityData.reduce((result, file) => (result += file.complexity), 0) /
          complexityData.length
        : 0,
    [complexityData]
  );

  const complexityLevel = useMemo(() => {
    const result = {
      simple: { cobol: 0, jcl: 0, copybook: 0, screen: 0 },
      medium: { cobol: 0, jcl: 0, copybook: 0, screen: 0 },
      complex: { cobol: 0, jcl: 0, copybook: 0, screen: 0 },
      veryComplex: { cobol: 0, jcl: 0, copybook: 0, screen: 0 }
    };

    complexityData.forEach?.(file => {
      const category = file.complexity_category.toLowerCase();
      let label = file.label.toLowerCase() as LabelComplexity;

      // Normalize specific labels
      if (label === "jcl_ibm" || label === "jcl_fujitsu") {
        label = "jcl";
      } else if (label === "copy") {
        label = "copybook";
      } else if (label === "bms") {
        label = "screen";
      }

      // Only consider valid labels (cobol, jcl, copybook, screen)
      if (["cobol", "jcl", "copybook", "screen"].includes(label)) {
        if (category === "simple") {
          result.simple[label]++;
        } else if (category === "medium") {
          result.medium[label]++;
        } else if (category === "complex") {
          result.complex[label]++;
        } else if (category === "very complex") {
          result.veryComplex[label]++;
        }
      }
    });

    return {
      simple: Object.values(result.simple),
      medium: Object.values(result.medium),
      complex: Object.values(result.complex),
      veryComplex: Object.values(result.veryComplex)
    };
  }, [complexityData]);

  return (
    <>
      {!repository || loadingRepository ? (
        <>
          <Flex center style={{ width: "100%", height: "100%" }}>
            <Spin size='default' />
          </Flex>
        </>
      ) : (
        <>
          {!!loadingRepository ? (
            <Flex
              direction='column'
              style={{ padding: 32, overflow: "auto", width: "100%" }}
              gap={24}
            >
              <McCabe mcCabe={mcCabe} />
              <MeanComplexity data={meanComplexity} />
              <ComplexityLevels data={complexityLevel} />
              <ComplexityDistribution data={complexityData} />
            </Flex>
          ) : (
            <Flex
              center
              style={{ width: "100%", background: "white", margin: "24px", borderRadius: "8px" }}
            >
              <Typography level='body-16b' color='primary10'>
                Reverse repository hasn't finished yet. Come back later
              </Typography>
            </Flex>
          )}
        </>
      )}
    </>
  );
}
