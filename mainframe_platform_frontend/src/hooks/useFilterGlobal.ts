import { useDispatch, useSelector } from "react-redux";

import { filterActions, filterSelector, ReportFilter, DatabaseFilterState } from "@store";

export function useFilterGlobal() {
  const filterReports = useSelector(filterSelector.filterReports);
  const filterDatabase = useSelector(filterSelector.filterDatabase);
  const dispatch = useDispatch();
  const setReportsFilter = (filter: Partial<ReportFilter>) =>
    dispatch(filterActions.setReportsFilter(filter));
  const resetReportsFilter = () => dispatch(filterActions.resetReportsFilter());
  const setDatabaseFilter = (filter: Partial<DatabaseFilterState>) =>
    dispatch(filterActions.setDatabaseFilter(filter));
  const resetDatabaseFilter = () => dispatch(filterActions.resetDatabaseFilter());
  return {
    filterReports,
    filterDatabase,
    setReportsFilter,
    resetReportsFilter,
    setDatabaseFilter,
    resetDatabaseFilter
  };
}
