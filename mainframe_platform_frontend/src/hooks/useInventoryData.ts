import { useMemo } from "react";
import { useParams } from "react-router-dom";

import { CountBByFileType } from "@pages/exploration/inventory/components/CountFileType";
import { useGetAssessmentRepository } from "@services";

type AccumulatorType = { [key: string]: number };

export function useInventoryData() {
  const { repoId = "" } = useParams();
  const { inventoryData, isLoading: loadingInventory } = useGetAssessmentRepository({ repoId });

  const loc = useMemo(
    () =>
      inventoryData
        ? inventoryData.assessment?.reduce?.((result, item) => result + item.code + item.comment, 0)
        : 0,
    [inventoryData]
  );

  const comment = useMemo(
    () =>
      inventoryData
        ? inventoryData.assessment?.reduce?.((result, item) => result + item.comment, 0)
        : 0,
    [inventoryData]
  );

  const locFileType =
    useMemo(() => {
      // Get distinct labels first
      const distinctLabels = [...new Set(inventoryData?.assessment?.map(item => item.label) || [])];

      // Define type for the accumulator

      // Create initial accumulator with 0 for each label
      const initial: AccumulatorType = distinctLabels.reduce(
        (acc, label) => ({
          ...acc,
          [label.toLowerCase()]: 0
        }),
        {}
      );

      // Reduce the assessment data using dynamic labels
      return inventoryData?.assessment?.reduce?.(
        (result, item) => ({
          ...result,
          [item.label.toLowerCase()]: result[item.label.toLowerCase()] + item.code
        }),
        initial
      );
    }, [inventoryData]) || {};

  const distinctLabels = useMemo(() => {
    return [...new Set(inventoryData?.assessment?.map(item => item.label) || [])];
  }, [inventoryData]);

  const countFileType = useMemo(() => {
    // Get distinct labels first
    // eslint-disable-next-line @typescript-eslint/no-shadow
    const distinctLabels = [...new Set(inventoryData?.assessment?.map(item => item.label) || [])];

    // Create initial accumulator with 0 for each label
    const initial: AccumulatorType = distinctLabels.reduce(
      (acc, label) => ({
        ...acc,
        [label.toLowerCase()]: 0
      }),
      {}
    );

    // Reduce the assessment data using dynamic labels
    return inventoryData?.assessment?.reduce?.(
      (result, item) => ({
        ...result,
        [item.label.toLowerCase()]: result[item.label.toLowerCase()] + 1
      }),
      initial
    );
  }, [inventoryData]) as CountBByFileType;

  const locDistribution = useMemo(() => {
    if (!inventoryData?.code_dist) return { log_frequencies: [], bins: [] };
    const { bins, frequencies } = inventoryData.code_dist;
    return {
      log_frequencies: frequencies,
      bins
    };
  }, [inventoryData]);

  return {
    loc,
    comment,
    distinctLabels,
    locFileType,
    countFileType,
    locDistribution,
    loadingInventory,
    inventoryData
  };
}
