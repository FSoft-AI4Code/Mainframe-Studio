import { ReactNode, useState } from "react";
import { Tooltip as TooltipUI, TooltipProps } from "antd";
import styled from "@emotion/styled";

import { NetworkingDataType } from "@types";

type NodeType = NetworkingDataType["nodes"][number];

const Tooltip = styled(TooltipUI)``;

export const useChartTooltip = (): {
  onHoverInNode: (e: MouseEvent, d: NodeType) => void;
  onHoverOutNode: (e: MouseEvent, d: NodeType) => void;
  render: () => ReactNode;
} => {
  const [tooltipProps, setTooltipProps] = useState<TooltipProps>({});

  const toggleTooltip = (e: MouseEvent, d: NodeType, open: boolean) => {
    setTooltipProps({
      open,
      title: d.short_description || d.name,
      overlayStyle: {
        top: e.y + 20,
        left: e.x - 20
      }
    });
  };

  return {
    onHoverInNode: (e: MouseEvent, d: NodeType) => toggleTooltip(e, d, true),
    onHoverOutNode: (e: MouseEvent, d: NodeType) => toggleTooltip(e, d, false),
    render: () => (
      <Tooltip rootClassName='chartTooltip' arrow={false} placement='bottom' {...tooltipProps} />
    )
  };
};
