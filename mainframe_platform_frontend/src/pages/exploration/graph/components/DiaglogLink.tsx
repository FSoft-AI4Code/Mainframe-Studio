import { ReactComponent as XIcon } from "@assets/svg/x.svg";
import { DialogChartData } from "@components";
import { NetworkingDataType } from "@types";

import { NODE_BY_TYPE } from "../config";

import { WrapAction, WrapContent, WrapInfo } from "./styles";

type NodeType = NetworkingDataType["nodes"][number];
type LinkType = NetworkingDataType["links"][number];

type Props = {
  colorByType?: string;
  close: () => void;
  nodes: NodeType[];
  linkSelected: LinkType | undefined;
};

export const DialogLink: React.FC<Props> = ({ nodes, linkSelected, colorByType, close }) => {
  const dataSource = nodes?.find(node => node.id === (linkSelected?.source as any)?.id);
  const dataTarget = nodes?.find(node => node.id === (linkSelected?.target as any)?.id);

  return (
    <DialogChartData
      width={541}
      height={350}
      open={Boolean(linkSelected)}
      onCancel={close}
      borderColor={colorByType}
      closeIcon={
        <WrapAction onClick={close}>
          <XIcon />
        </WrapAction>
      }
      left={
        <div>
          <WrapInfo>Source: {dataSource?.display_name}</WrapInfo>
          <WrapInfo>
            Source type:{" "}
            {(NODE_BY_TYPE as any)?.[dataSource?.type || ""]
              ? (NODE_BY_TYPE as any)?.[dataSource?.type || ""]
              : dataSource?.type}
          </WrapInfo>
          <WrapInfo>Target: {dataTarget?.display_name}</WrapInfo>
          <WrapInfo>
            Target type:{" "}
            {(NODE_BY_TYPE as any)?.[dataTarget?.type || ""]
              ? (NODE_BY_TYPE as any)?.[dataTarget?.type || ""]
              : dataTarget?.type}
          </WrapInfo>
          {linkSelected?.content ? (
            <WrapContent thumbColor={colorByType}>
              <div className='content'>
                <div> {linkSelected?.content}</div>
              </div>
            </WrapContent>
          ) : null}
        </div>
      }
    />
  );
};
