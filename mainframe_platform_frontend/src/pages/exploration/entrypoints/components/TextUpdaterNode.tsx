import styled from "@emotion/styled";
import { Tooltip } from "antd";
import { useNavigate, useParams } from "react-router-dom";
import { Handle, Position } from "reactflow";

import { ArrowRightSvg, CodeSvg, EyeSvg, GitBranchInSvg, InfoInSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { ROUTERS } from "@defines";
import { useRoutesHandler } from "@hooks";
import { allColors } from "@style";
import { FileGroup } from "@types";
import { cleanString, generatePath } from "@utils";

const ButtonWrapper = styled(Flex)`
  padding: 6px 16px;
  border-radius: 100px;
  border: 1px solid ${({ theme }) => theme.allColors.primary6};
  color: ${({ theme }) => theme.allColors.primary6};
  width: 100%;
  cursor: pointer;

  &:hover {
    background: ${({ theme }) => theme.allColors.primary6};
    color: ${({ theme }) => theme.allColors.neutral1};

    svg {
      stroke: ${({ theme }) => theme.allColors.neutral1};
    }
  }
`;

interface ITextUpdaterToolTip {
  id: string;
  setExpand: () => void;
  expand: boolean | null;
  name: string;
  complexity?: number | null;
  line_of_code?: number | null;
  status?: string;
  onAction?: () => void;
}

function TextUpdaterToolTip({
  id,
  setExpand,
  expand,
  name,
  complexity,
  line_of_code,
  status,
  onAction
}: ITextUpdaterToolTip) {
  const { setRecentRoute, pathname, navigate } = useRoutesHandler();

  const handleActions = () => {
    if (onAction) return onAction();
    setRecentRoute({ key: `Reverse ${name}`, path: `${pathname}?fileId=${id}` });
    navigate({
      pathname: window.location.pathname,
      search: `?fileId=${id}`
    });
  };
  const isMissing = status === "MISSING";
  return (
    <Flex
      style={{
        padding: 24,
        borderRadius: "16px",
        border: `1px solid ${allColors.neutral6}`,
        background: allColors.neutral1,
        width: 380
      }}
      direction='column'
      gap={16}
    >
      <Typography level='subtitle-20s' color='primary10'>
        Details for {name}
      </Typography>
      <Flex gap={8} align='center'>
        <CodeSvg />
        <Typography level='button-16s' color='primary10'>
          {`Lines of Code: ${line_of_code ?? "Unknown"}`}
        </Typography>
      </Flex>
      <Flex gap={8} align='center'>
        <GitBranchInSvg />
        <Typography level='button-16s' color='primary10'>
          {`Complexity: ${complexity ?? "Unknown"}`}
        </Typography>
      </Flex>
      {!isMissing && (
        <ButtonWrapper center gap={6} onClick={handleActions}>
          <Typography level='body-16m'>Review</Typography>
          <EyeSvg stroke={allColors.primary6} />
        </ButtonWrapper>
      )}
      {expand !== null ? (
        <ButtonWrapper center gap={6} onClick={() => setExpand()}>
          <Typography level='body-16m'>Child Nodes</Typography>
          <ArrowRightSvg stroke={allColors.primary6} />
        </ButtonWrapper>
      ) : null}
    </Flex>
  );
}

export function TextUpdaterNode({
  data
}: {
  data: {
    fileType: FileGroup;
    name: string;
    complexity?: number | null;
    line_of_code?: number | null;
    status: string;
    id: string;
    index: number;
    expand: boolean | null;
    expandAll: boolean;
    setExpand: () => void;
    setExpandAll: () => void;
    label: string;
  };
}) {
  // eslint-disable-next-line @typescript-eslint/naming-convention
  const { label, id, expand, setExpand, name, line_of_code, complexity, fileType, status } =
    data || {};
  const navigate = useNavigate();
  const { repoId } = useParams();
  const onAction = () => {
    navigate(
      generatePath(`/exploration/${repoId}/${ROUTERS.EXPLORATION_REPORTS_DETAIL}`, {
        type: cleanString(fileType),
        name: cleanString(name)
      })
    );
  };

  return (
    <Flex center gap={6}>
      <Handle type='source' position={Position.Right} />
      <Handle type='target' position={Position.Left} />
      <Flex style={{ position: "relative" }}>
        <Tooltip
          rootClassName='entrypoint'
          title={
            <TextUpdaterToolTip
              name={name}
              line_of_code={line_of_code}
              complexity={complexity}
              id={id}
              status={status}
              setExpand={setExpand}
              expand={expand}
              onAction={onAction}
            />
          }
          arrow={false}
        >
          {fileType !== "UTILITY" && status !== "MISSING" && (
            <Flex
              style={{
                position: "absolute",
                top: 0,
                left: 0,
                transform: "translate(-70%, -40%)",
                zIndex: 1000
              }}
            >
              <InfoInSvg />
            </Flex>
          )}
        </Tooltip>
        <Typography level='body-16m' color='neutral1'>
          {label}
        </Typography>
      </Flex>
    </Flex>
  );
}
