import { Spin } from "antd";
import { useState } from "react";

import { Flex, Typography } from "@components";
import { useInventoryData } from "@hooks";

import {
  CmLOC,
  CountFileType,
  LOCDistribution,
  LOCFileType,
  TotalFile,
  TotalLOC
} from "./components";
import { LOCBByFileType } from "./components/LOCFileType";

export function InventoryPage() {
  const [dataset] = useState<never[]>([]);

  const {
    inventoryData,
    loadingInventory,
    loc,
    locFileType,
    locDistribution,
    comment,
    countFileType,
    distinctLabels
  } = useInventoryData();

  return inventoryData ? (
    <Flex direction='column' style={{ padding: 32, overflow: "auto", width: "100%" }} gap={24}>
      <Flex gap={24}>
        <TotalLOC totalLOC={loc} totalFile={inventoryData?.assessment?.length ?? 0} />
        <CmLOC title='Actual vs Comment Line of Codes' code={loc - comment} comment={comment} />
      </Flex>
      <LOCFileType data={locFileType as LOCBByFileType} labels={distinctLabels} />
      <Flex gap={24}>
        <TotalFile totalFile={dataset.length} />
        <CountFileType data={countFileType} labels={distinctLabels} />
      </Flex>
      <LOCDistribution data={locDistribution} />
    </Flex>
  ) : (
    <Flex center style={{ width: "100%", height: "100%" }}>
      {loadingInventory ? (
        <Spin />
      ) : (
        <Typography level='body-16r' color='primary10'>
          Assessment not performed
        </Typography>
      )}
    </Flex>
  );
}
