import { useMemo, useRef, useState } from "react";
import Select from "antd/es/select";

import { DoubleChevronInSvg } from "@assets/svg";
import { DropdowSliderFilter, Flex, Typography } from "@components";
import { useBreakpoint, useEntryPoint, useFilterGraph, useMessages } from "@hooks";
import { allColors } from "@style";
import { addPropertiesToItems } from "@utils";

import { EntriesWrapper, FileWrapper } from "./styles";

export function ListEntries() {
  const { entries, loadingGraph } = useEntryPoint();
  const { xl } = useBreakpoint();
  const { elementViews } = useMessages();
  const isAIAgentPage = elementViews === "EXPLORATION";

  const {
    selectedEntry,
    setSelectedEntry,
    selectedType,
    setSelectedType,
    setGraphFilter,
    loc: locFilter,
    complexity
  } = useFilterGraph();
  const entriesWrapperRef = useRef<HTMLDivElement>(null);
  const [showMore, setShowMore] = useState(false);

  const displayedEntries = useMemo(
    () => (selectedType ? entries?.filter(({ type }) => type === selectedType) : entries),
    [selectedType, entries]
  );

  // eslint-disable-next-line no-console
  console.log({ displayedEntries, selectedEntry });

  const [showFilter, setShowFilter] = useState(false);
  // eslint-disable-next-line unused-imports/no-unused-vars, @typescript-eslint/no-unused-vars
  const handleFilter = () => setShowFilter(!showFilter);
  // eslint-disable-next-line unused-imports/no-unused-vars, @typescript-eslint/no-unused-vars

  const entryByTypes = [
    { label: "EntryBMS", type: "bms", bgColor: allColors.brand1 },
    { label: "EntryJCL", type: "jcl", bgColor: allColors.brand5 }
  ];
  return (
    <Flex
      style={{
        position: "relative",
        background: allColors.neutral1,
        borderRadius: "8px 8px 0 0",
        borderBottom: `1px solid ${allColors.neutral6}`
      }}
      gap={24}
      direction='column'
    >
      <Flex align='flex-start' gap={16} direction='column' style={{ padding: "16px 24px 0" }}>
        <Typography level='body-16b' color='primary10'>
          List Entry Point
        </Typography>
        <Flex
          justify='flex-end'
          style={{ flexWrap: xl && !isAIAgentPage ? "nowrap" : "wrap", width: "100%" }}
          gap={8}
        >
          <Flex gap={8} justify='flex-end' style={{ width: "100%" }}>
            <DropdowSliderFilter
              dropdownStyle={{ width: 300 }}
              style={{ width: 150 }}
              placeholder='Loc'
              label='Loc filter'
              value={locFilter ? locFilter : null}
              min={0}
              max={10000}
              defaultValue={0}
              onFilterChange={value =>
                setGraphFilter({
                  loc: value as number
                })
              }
            />
            <DropdowSliderFilter
              dropdownStyle={{ width: 300 }}
              style={{ width: 150 }}
              placeholder='Complexity'
              label='Complexity filter'
              value={complexity ? complexity : null}
              min={0}
              max={1000}
              defaultValue={0}
              onFilterChange={value =>
                setGraphFilter({
                  complexity: value as number
                })
              }
            />
            <Select
              style={{ width: 150 }}
              placeholder='Search'
              options={addPropertiesToItems(
                entries,
                ({ value, id }) => ({
                  value: `${id}-${value}`,
                  label: value
                }),
                true
              )}
              showSearch
              loading={loadingGraph}
              allowClear
              value={!!selectedEntry ? selectedEntry : null}
              onChange={setSelectedEntry}
            />
            <Select
              style={{ width: 150 }}
              options={[
                { value: "jcl", label: "JCL" },
                { value: "bms", label: "BMS" }
              ]}
              value={selectedType}
              onChange={setSelectedType}
              placeholder='Choose type'
              allowClear
            />
          </Flex>
          <Flex gap={8} style={{ marginLeft: "auto" }}>
            {entryByTypes?.map(({ label, type, bgColor }) => (
              <Flex
                key={type}
                gap={6}
                style={{
                  padding: "6px 16px",
                  height: 30,
                  background: bgColor,
                  borderRadius: "100px"
                }}
                center
              >
                <Typography level='h7-body2M' color='neutral1'>
                  {label}
                </Typography>
                <Flex
                  style={{
                    padding: "0px 4px",
                    borderRadius: "8px",
                    background: allColors.neutral1
                  }}
                >
                  <Typography level='h7-body2M' color='secondary10'>
                    {entries?.filter(({ type: entryType }) => entryType === type).length}
                  </Typography>
                </Flex>
              </Flex>
            ))}
          </Flex>
        </Flex>
      </Flex>
      <EntriesWrapper showMore={showMore} ref={entriesWrapperRef} scrollHeight={0}>
        {displayedEntries?.map(({ value, type, id }) => (
          <FileWrapper
            type={type as "bms" | "jcl"}
            gap={6}
            center
            onClick={() => setSelectedEntry(`${id}-${value}`)}
            key={id}
          >
            <Typography level='h7-body2M' color='neutral1'>
              {value}
            </Typography>
          </FileWrapper>
        ))}
      </EntriesWrapper>
      <Flex
        center
        style={{
          width: 28,
          height: 28,
          position: "absolute",
          bottom: 2,
          right: 16,
          transform: showMore ? "translateY(50%) rotate(180deg)" : "translateY(50%) rotate(0deg)",
          cursor: "pointer",
          transition: "all 0.2s 0.2s",
          border: `1px solid ${allColors.neutral6}`,
          borderRadius: "8px",
          zIndex: 1000,
          background: allColors.neutral1
        }}
        onClick={() => setShowMore(value => !value)}
      >
        <DoubleChevronInSvg />
      </Flex>
    </Flex>
  );
}
