import { useDispatch, useSelector } from "react-redux";

import { filterGraphActions, filterGraphSelector, GraphState } from "@store";

export function useFilterGraph() {
  const filterState = useSelector(filterGraphSelector.graphFilterStore);

  const dispatch = useDispatch();

  const setSelectedGroup = (group: string[]) =>
    dispatch(filterGraphActions.setSelectedGroup(group));

  const setSelectedEntry = (entry: string) => dispatch(filterGraphActions.setSelectedEntry(entry));

  const setSelectedEntries = (entries: Record<string, never | unknown | string>) =>
    dispatch(filterGraphActions.setSelectedEntries(entries));

  const setSelectedType = (type: "jcl" | "bms" | null) =>
    dispatch(filterGraphActions.setSelectType(type));

  const setShowNode = (nodeShow: Record<string, boolean>) =>
    dispatch(filterGraphActions.setShowNode(nodeShow));

  const setNodeLimit = (nodes: number) => dispatch(filterGraphActions.setNodeLimit(nodes));
  const setGraphFilter = (payload: Partial<GraphState>) =>
    dispatch(filterGraphActions.setGraphFilters(payload));

  return {
    ...filterState,
    setSelectedGroup,
    setSelectedType,
    setSelectedEntry,
    setShowNode,
    setSelectedEntries,
    setNodeLimit,
    setGraphFilter
  };
}
