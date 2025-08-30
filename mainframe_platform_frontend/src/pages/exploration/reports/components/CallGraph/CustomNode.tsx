/* eslint-disable unused-imports/no-unused-vars */
import { Handle, Position } from "@xyflow/react";
import { Tooltip, Dropdown } from "antd";
import { memo, useCallback } from "react";
import {
  MoreOutlined,
  FullscreenOutlined,
  CaretDownOutlined,
  CaretRightOutlined,
  InfoCircleOutlined
} from "@ant-design/icons";

import { Flex, Typography } from "@components";
import { allColors } from "@style";
import { SummarizationValue } from "@types";

import { CustomNodeData } from "./SectionCallGraph";

const { Left, Right } = Position;

type DataNodeProps = {
  id: string;
  data: CustomNodeData;
  style?: React.CSSProperties;
  isConnectable: boolean;
  onToggleExpand?: (nodeId: string) => void;
  isCollapsed?: boolean;
};

interface InformationToolTipProps {
  summarization?: SummarizationValue;
  name: string;
}

export const InformationToolTip = memo(({ summarization, name }: InformationToolTipProps) => {
  return (
    <Flex
      style={{
        padding: 16,
        borderRadius: "16px",
        border: `1px solid ${allColors.neutral6}`,
        background: allColors.neutral1,
        width: 326,
        minHeight: 180,
        maxHeight: 240
      }}
      direction='column'
      gap={8}
    >
      <Typography style={{ padding: "0 10px" }} level='subtitle-20s' color='primary10'>
        {name}
      </Typography>
      <Flex
        direction='column'
        style={{
          overflow: "auto"
        }}
      >
        <Flex gap={8} align='flex-start'>
          <Typography level='button-16s' color='primary10'>
            {summarization &&
            summarization.paragraph_logic &&
            Array.isArray(summarization.paragraph_logic) &&
            summarization.paragraph_logic.length > 0 ? (
              <Flex gap={3} direction='column'>
                {summarization.paragraph_logic.map((paragraph, i) => (
                  <Typography level='body-14r' color='primary10' key={i}>
                    - {paragraph?.trim()}
                  </Typography>
                ))}
              </Flex>
            ) : (
              <Typography level='body-14r' color='primary10'>
                No detailed summary available for this component.
              </Typography>
            )}
          </Typography>
        </Flex>
      </Flex>
    </Flex>
  );
});

const CustomNode = memo(
  ({ id, data, style, isConnectable, onToggleExpand, isCollapsed = false }: DataNodeProps) => {
    const { label, isRoot, hasChildren, summarization, type } = data || {};

    // Handlers for node actions
    const handleFocusNode = useCallback(() => {
      // Implement focus on this node functionality
    }, []);

    const handleToggleExpand = useCallback(
      (e: React.MouseEvent) => {
        e.stopPropagation();
        if (onToggleExpand && hasChildren && typeof id === "string") {
          onToggleExpand(id);
        }
      },
      [id, hasChildren, onToggleExpand]
    );

    // Menu items for dropdown
    const menuItems = [
      {
        key: "focus",
        label: "Focus on this node",
        onClick: handleFocusNode
      },
      {
        key: "expand",
        label: isCollapsed ? "Expand children" : "Collapse children",
        onClick: () => {
          if (onToggleExpand && typeof id === "string") {
            onToggleExpand(id);
          }
        },
        disabled: !hasChildren
      }
    ];

    // Determine if the node has actual summarization data
    const hasSummarizationData = !!(
      summarization &&
      summarization.paragraph_logic &&
      Array.isArray(summarization.paragraph_logic) &&
      summarization.paragraph_logic.length > 0
    );

    return (
      <div
        style={{
          padding: "2px 6px",
          borderRadius: "6px",
          maxWidth: "100%",
          overflow: "hidden",
          position: "relative",
          // Add blue border for collapsed nodes instead of changing background
          border:
            isCollapsed && hasChildren
              ? `1.5px solid ${allColors.primary6}`
              : style?.border || "1px solid transparent"
        }}
      >
        {/* Header with icons */}
        <Flex
          justify='space-between'
          align='center'
          style={{
            borderBottom: `1px solid ${
              isCollapsed && hasChildren ? allColors.warning : allColors.neutral5
            }`,
            padding: "4px 2px",
            marginBottom: "4px"
          }}
        >
          {/* Type label and info button */}
          <Flex align='center' style={{ flexGrow: 1, gap: "6px" }}>
            {/* Info Button - Now integrated in the header for better UX */}
            {hasSummarizationData && (
              <Tooltip
                rootClassName='entrypoint'
                title={
                  <InformationToolTip
                    name={label || "Component Info"}
                    summarization={summarization}
                  />
                }
                arrow={true}
                placement='top'
              >
                <InfoCircleOutlined
                  style={{
                    fontSize: "14px",
                    color: hasSummarizationData ? allColors.primary8 : allColors.primary6,
                    cursor: "pointer"
                  }}
                />
              </Tooltip>
            )}

            {/* Type label */}
            {type && (
              <div
                style={{
                  fontSize: "9px",
                  opacity: 0.75,
                  textTransform: "uppercase",
                  fontWeight: 600,
                  color: allColors.neutral8,
                  letterSpacing: "0.5px"
                }}
              >
                {type}
              </div>
            )}
          </Flex>

          {/* Node action buttons */}
          <Flex gap={4}>
            {/* Focus on node button */}
            <Tooltip title='Focus on this node'>
              <FullscreenOutlined
                onClick={handleFocusNode}
                style={{
                  fontSize: "14px",
                  color: allColors.primary8,
                  cursor: "pointer"
                }}
              />
            </Tooltip>

            {/* Expand/Collapse button with clear visual indicators */}
            {hasChildren && (
              <Tooltip title={isCollapsed ? "Expand children" : "Collapse children"}>
                {isCollapsed ? (
                  <CaretRightOutlined
                    onClick={handleToggleExpand}
                    style={{
                      fontSize: "14px",
                      color: allColors.warning,
                      cursor: "pointer",
                      fontWeight: "bold"
                    }}
                  />
                ) : (
                  <CaretDownOutlined
                    onClick={handleToggleExpand}
                    style={{
                      fontSize: "14px",
                      color: allColors.primary8,
                      cursor: "pointer"
                    }}
                  />
                )}
              </Tooltip>
            )}

            {/* Menu dropdown */}
            <Dropdown menu={{ items: menuItems }} trigger={["click"]} placement='bottomRight'>
              <MoreOutlined
                style={{
                  fontSize: "14px",
                  color: allColors.primary8,
                  cursor: "pointer"
                }}
              />
            </Dropdown>
          </Flex>
        </Flex>

        {/* Node label styling */}
        <div
          style={{
            fontSize: "11px",
            fontWeight: isCollapsed ? 600 : 500, // Make text slightly bolder when collapsed
            lineHeight: "1.3",
            wordBreak: "break-word",
            overflow: "hidden",
            textOverflow: "ellipsis",
            padding: "2px 0 4px"
          }}
        >
          {label}
        </div>

        {/* Show collapsed indicator */}
        {hasChildren && isCollapsed && (
          <div
            style={{
              position: "absolute",
              bottom: 2,
              right: 2,
              background: allColors.warning,
              borderRadius: "50%",
              width: 8,
              height: 8,
              border: `1px solid ${allColors.warning}`,
              zIndex: 10
            }}
          />
        )}

        {/* HANDLE STYLING - these are the connection points for edges */}
        {!isRoot && (
          <Handle
            type='target'
            position={Left}
            style={{
              width: 8,
              height: 8,
              background: allColors.primary6,
              border: `1px solid ${allColors.primary10}`,
              zIndex: 5
            }}
            id={"target-handle"}
            isConnectable={isConnectable}
          />
        )}
        {hasChildren && (
          <Handle
            type='source'
            position={Right}
            style={{
              width: 8,
              height: 8,
              background: allColors.primary6,
              border: `1px solid ${allColors.primary10}`,
              zIndex: 5
            }}
            id={"source-handle"}
            isConnectable={isConnectable}
          />
        )}
      </div>
    );
  }
);

export default CustomNode;
