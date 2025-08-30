import { Button, Checkbox, Divider, theme } from "antd";
import { memo, useMemo, forwardRef } from "react";

interface FilterLevelMenuProps {
  nodeLevels: number[];
  selectedLevels: number[];
  onLevelChange: (levels: number[]) => void;
  onMouseEnter: () => void;
  onMouseLeave: () => void;
}

// Using forwardRef to properly handle refs from Dropdown component
const FilterLevelMenu = memo(
  forwardRef<HTMLDivElement, FilterLevelMenuProps>(
    ({ nodeLevels, selectedLevels, onLevelChange, onMouseEnter, onMouseLeave }, ref) => {
      const { token } = theme.useToken();

      // Calculate whether all levels are selected
      const allSelected = selectedLevels.length === nodeLevels.length;

      // Calculate a descriptive status text
      const levelCount = `${selectedLevels.length} of ${nodeLevels.length} levels selected`;

      // Sort the levels numerically
      const sortedLevels = useMemo(() => [...nodeLevels].sort((a, b) => a - b), [nodeLevels]);

      // Handlers for the filter actions
      const handleSelectAll = () => onLevelChange([...nodeLevels]);
      const handleClearAll = () => onLevelChange([]);
      const handleLevelToggle = (level: number, isChecked: boolean) => {
        if (isChecked) {
          onLevelChange([...selectedLevels, level]);
        } else {
          onLevelChange(selectedLevels.filter(l => l !== level));
        }
      };

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
            <strong style={{ fontSize: 14 }}>Filter by Level</strong>
          </div>

          {/* Status indicator */}
          <div style={{ fontSize: 12, color: token.colorTextSecondary, marginBottom: 8 }}>
            {levelCount}
          </div>

          {/* Action buttons */}
          <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
            <Button
              size='small'
              type={allSelected ? "default" : "primary"}
              onClick={handleSelectAll}
              disabled={allSelected}
              style={{ flex: 1 }}
            >
              Select All
            </Button>
            <Button
              size='small'
              danger
              onClick={handleClearAll}
              disabled={selectedLevels.length === 0}
              style={{ flex: 1 }}
            >
              Clear
            </Button>
          </div>

          <Divider style={{ margin: "4px 0 12px" }} />

          {/* Level checkboxes */}
          <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
            {sortedLevels.map(level => (
              <Checkbox
                key={level}
                checked={selectedLevels.includes(level)}
                onChange={e => handleLevelToggle(level, e.target.checked)}
              >
                Level {level}
              </Checkbox>
            ))}
          </div>
        </div>
      );
    }
  )
);

export default FilterLevelMenu;
