import { useState, useEffect, useCallback, useMemo } from "react";
import { Card, Input, Space, Button, Dropdown, Tooltip, theme } from "antd";
import {
  SearchOutlined,
  FullscreenOutlined,
  FilterOutlined,
  DownOutlined,
  MenuFoldOutlined,
  DashboardOutlined,
  BranchesOutlined
} from "@ant-design/icons";
import { Node } from "@xyflow/react";

import FilterLevelMenu from "./FilterLevelMenu";
import SearchResultCounter from "./SearchResultCounter";
import ExpandCollapseMenu from "./ExpandCollapseMenu";

interface ControlPanelProps {
  programId: string;
  searchText: string;
  selectedLevels: number[];
  nodeLevels: number[];
  filteredNodes: Node[];
  isPanelCollapsed: boolean;
  onSearch: (text: string) => void;
  onLevelChange: (levels: number[]) => void;
  onFitView: () => void;
  onTogglePanel: () => void;
  onExpandAll: () => void;
  onCollapseAll: () => void;
  onLevelControl: (level: number) => void;
}

const ControlPanel = ({
  programId,
  searchText,
  selectedLevels,
  nodeLevels,
  filteredNodes,
  isPanelCollapsed,
  onSearch,
  onLevelChange,
  onFitView,
  onTogglePanel,
  onExpandAll,
  onCollapseAll,
  onLevelControl
}: ControlPanelProps) => {
  const { token } = theme.useToken();

  // Local state
  const [filterDropdownVisible, setFilterDropdownVisible] = useState(false);
  const [expandDropdownVisible, setExpandDropdownVisible] = useState(false);
  const [filterMouseOver, setFilterMouseOver] = useState(false);
  const [expandMouseOver, setExpandMouseOver] = useState(false);
  const [isExpanded, setIsExpanded] = useState(false);
  const [isInitialRender, setIsInitialRender] = useState(true);

  // Only sync state after first render
  useEffect(() => {
    if (isInitialRender) {
      setIsInitialRender(false);
    } else {
      setIsExpanded(!isPanelCollapsed);
    }
  }, [isPanelCollapsed, isInitialRender]);

  // Auto-close dropdowns when mouse leaves
  useEffect(() => {
    if (!filterMouseOver && filterDropdownVisible) {
      const timer = setTimeout(() => setFilterDropdownVisible(false), 200);
      return () => clearTimeout(timer);
    }
  }, [filterMouseOver, filterDropdownVisible]);

  useEffect(() => {
    if (!expandMouseOver && expandDropdownVisible) {
      const timer = setTimeout(() => setExpandDropdownVisible(false), 200);
      return () => clearTimeout(timer);
    }
  }, [expandMouseOver, expandDropdownVisible]);

  // Event handlers
  const handleFilterMouseEvents = useCallback((isOver: boolean) => {
    setFilterMouseOver(isOver);
  }, []);

  const handleExpandMouseEvents = useCallback((isOver: boolean) => {
    setExpandMouseOver(isOver);
  }, []);

  const handleDropdownVisibility = useCallback((visible: boolean, type: "filter" | "expand") => {
    if (type === "filter") {
      setFilterDropdownVisible(visible);
    } else {
      setExpandDropdownVisible(visible);
    }
  }, []);

  const handleToggle = useCallback(() => {
    // For first click, don't use animation delay
    if (isPanelCollapsed) {
      setIsExpanded(true);
      onTogglePanel();
    } else {
      setIsExpanded(false);
      // Only add delay for closing animation
      setTimeout(() => {
        onTogglePanel();
      }, 150);
    }
  }, [isPanelCollapsed, onTogglePanel]);

  const handleSearch = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      onSearch(e.target.value);
    },
    [onSearch]
  );

  // Derived state
  const hasSearchResults = useMemo(
    () => searchText.trim() && filteredNodes.length > 0,
    [searchText, filteredNodes]
  );

  const levelFilterText = useMemo(() => {
    if (selectedLevels.length === 0) return "Filter by Level";
    if (selectedLevels.length === nodeLevels.length) return "All Levels";
    return `Levels (${selectedLevels.length}/${nodeLevels.length})`;
  }, [selectedLevels, nodeLevels]);

  // Lazy-loaded content - only render full card contents when panel is expanded
  const renderCardContent = () => {
    if (!isExpanded && isPanelCollapsed) return null;

    return (
      <Space direction='vertical' size={token.marginSM} style={{ width: "100%" }}>
        <div style={{ position: "relative" }}>
          <Input
            placeholder='Search nodes...'
            prefix={<SearchOutlined />}
            allowClear
            value={searchText}
            size='large'
            onChange={handleSearch}
            style={{ borderRadius: token.borderRadiusSM, fontSize: token.fontSizeLG }}
          />

          {searchText.trim() && <SearchResultCounter count={filteredNodes.length} />}
        </div>

        <div
          style={{
            display: "flex",
            gap: token.marginSM,
            width: "100%",
            marginTop: hasSearchResults ? 8 : 0
          }}
        >
          <Button
            type='default'
            icon={<FullscreenOutlined />}
            onClick={onFitView}
            style={{ flex: 1 }}
          >
            Fit View
          </Button>

          <Dropdown
            open={expandDropdownVisible}
            onOpenChange={visible => handleDropdownVisibility(visible, "expand")}
            trigger={["click"]}
            placement='bottom'
            dropdownRender={() => (
              <ExpandCollapseMenu
                nodeLevels={nodeLevels}
                onExpandAll={onExpandAll}
                onCollapseAll={onCollapseAll}
                onLevelControl={onLevelControl}
                onMouseEnter={() => handleExpandMouseEvents(true)}
                onMouseLeave={() => handleExpandMouseEvents(false)}
              />
            )}
          >
            <Button
              type='default'
              icon={<BranchesOutlined />}
              onClick={() => setExpandDropdownVisible(!expandDropdownVisible)}
              onMouseEnter={() => handleExpandMouseEvents(true)}
              onMouseLeave={() => handleExpandMouseEvents(false)}
              style={{ flex: 1 }}
            >
              Expand/Collapse
            </Button>
          </Dropdown>
        </div>

        <Dropdown
          open={filterDropdownVisible}
          onOpenChange={visible => handleDropdownVisibility(visible, "filter")}
          trigger={["click"]}
          placement='bottomLeft'
          dropdownRender={() => (
            <FilterLevelMenu
              nodeLevels={nodeLevels}
              selectedLevels={selectedLevels}
              onLevelChange={onLevelChange}
              onMouseEnter={() => handleFilterMouseEvents(true)}
              onMouseLeave={() => handleFilterMouseEvents(false)}
            />
          )}
        >
          <Button
            type={
              selectedLevels.length > 0 && selectedLevels.length < nodeLevels.length
                ? "primary"
                : "default"
            }
            icon={<FilterOutlined />}
            onClick={() => setFilterDropdownVisible(!filterDropdownVisible)}
            onMouseEnter={() => handleFilterMouseEvents(true)}
            onMouseLeave={() => handleFilterMouseEvents(false)}
            style={{
              width: "100%",
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between"
            }}
          >
            <span>{levelFilterText}</span>
            <DownOutlined />
          </Button>
        </Dropdown>
      </Space>
    );
  };

  return (
    <>
      <style>
        {`
          @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
          }
          @keyframes slideOut {
            from { opacity: 1; transform: translateX(0); }
            to { opacity: 0; transform: translateX(-20px); }
          }
          .panel-container {
            transition: all 0.25s ease;
            position: relative;
          }
          .panel-expanded {
            opacity: 1;
            transform: translateX(0);
            animation: slideIn 0.25s;
          }
          .panel-collapsed {
            opacity: 0;
            transform: translateX(-20px);
            animation: slideOut 0.25s;
            pointer-events: none;
          }
        `}
      </style>

      {isPanelCollapsed && (
        <Tooltip title='Show Controls' placement='right'>
          <Button
            type='primary'
            shape='circle'
            icon={<DashboardOutlined />}
            onClick={handleToggle}
            style={{
              position: "absolute",
              top: 10,
              left: 10,
              zIndex: 10,
              boxShadow: token.boxShadowSecondary,
              width: 40,
              height: 40
            }}
          />
        </Tooltip>
      )}

      <div className={`panel-container ${isExpanded ? "panel-expanded" : "panel-collapsed"}`}>
        <Card
          title={`Program: ${programId}`}
          extra={
            <Button
              type='text'
              icon={<MenuFoldOutlined style={{ fontSize: 16 }} />}
              onClick={handleToggle}
              style={{ marginRight: -12 }}
            />
          }
          style={{
            maxWidth: 350,
            boxShadow: token.boxShadowSecondary
          }}
        >
          {renderCardContent()}
        </Card>
      </div>
    </>
  );
};

export default ControlPanel;
