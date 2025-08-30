import { Button, Divider, theme, Typography } from "antd";
import { memo, forwardRef } from "react";
import { NodeExpandOutlined, NodeCollapseOutlined, ControlOutlined } from "@ant-design/icons";

interface ExpandCollapseMenuProps {
  nodeLevels: number[];
  onExpandAll: () => void;
  onCollapseAll: () => void;
  onLevelControl: (level: number) => void;
  onMouseEnter: () => void;
  onMouseLeave: () => void;
}

// Using forwardRef to properly handle refs from Dropdown component
const ExpandCollapseMenu = memo(
  forwardRef<HTMLDivElement, ExpandCollapseMenuProps>(
    (
      { nodeLevels, onExpandAll, onCollapseAll, onLevelControl, onMouseEnter, onMouseLeave },
      ref
    ) => {
      const { token } = theme.useToken();

      // Sort the levels numerically
      const sortedLevels = [...nodeLevels].sort((a, b) => a - b);

      return (
        <div
          ref={ref}
          style={{
            backgroundColor: token.colorBgElevated,
            padding: 12,
            borderRadius: token.borderRadiusLG,
            boxShadow: token.boxShadow,
            minWidth: 200,
            maxHeight: 350,
            overflowY: "auto"
          }}
          onMouseEnter={onMouseEnter}
          onMouseLeave={onMouseLeave}
        >
          {/* Header with title */}
          <div style={{ marginBottom: 8 }}>
            <strong style={{ fontSize: 14 }}>Expand/Collapse Nodes</strong>
          </div>

          {/* Global actions */}
          <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
            <Button
              size='small'
              type='primary'
              icon={<NodeExpandOutlined />}
              onClick={onExpandAll}
              style={{ flex: 1 }}
            >
              Expand All
            </Button>
            <Button
              size='small'
              danger
              icon={<NodeCollapseOutlined />}
              onClick={onCollapseAll}
              style={{ flex: 1 }}
            >
              Collapse All
            </Button>
          </div>

          <Divider style={{ margin: "4px 0 12px" }} />

          {/* Simplified level-specific actions with clearer labels */}
          <Typography.Text type='secondary' style={{ display: "block", marginBottom: 8 }}>
            Set visibility level:
          </Typography.Text>

          <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
            {sortedLevels.map(level => (
              <Button
                key={level}
                size='small'
                onClick={() => onLevelControl(level)}
                style={{ width: "100%", fontSize: 13 }}
                icon={<ControlOutlined />}
              >
                Expand to Level {level}
              </Button>
            ))}
          </div>
        </div>
      );
    }
  )
);

export default ExpandCollapseMenu;
