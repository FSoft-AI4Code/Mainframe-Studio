import { DatabaseOutlined, FileOutlined } from "@ant-design/icons";
import { Dispatch, SetStateAction, useState } from "react";
import { useParams } from "react-router-dom";

import { Flex, Tabs } from "@components";
import { useDatasetsQuery } from "@services";
import { DatasetsInput, ViewExportType } from "@types";

import { FileViewSubTab } from "./file-view.subtab";
import FilterPanel from "./filter-panel";
import { JobviewSubTab } from "./job-view.subtab";

interface TableViewTabProps {
  filter: Partial<DatasetsInput & { view: ViewExportType }>;
  setFilter: Dispatch<SetStateAction<Partial<DatasetsInput>>>;
}

export function TableViewTab({ filter, setFilter }: TableViewTabProps) {
  const [activeTab, setActiveTab] = useState<string>("job");
  const { repoId = "" } = useParams();
  const [limit, setLimit] = useState(20);
  const [page, setPage] = useState(1);
  const skip = (page - 1) * limit;

  // eslint-disable-next-line unused-imports/no-unused-vars
  const { view, ...filterTable } = filter || {};

  const { datasetAssignments, total, isLoading } = useDatasetsQuery({
    repository_id: repoId,
    enabled: !!repoId,
    skip,
    ...filterTable,
    limit
  });

  const handleFilter = (values: Partial<DatasetsInput>) => {
    const cleaned = Object.fromEntries(
      Object.entries(values).map(([key, value]) => [key, value === "All" ? null : value])
    );
    setFilter(prev => ({ ...prev, ...cleaned }));
    setPage(1);
  };

  const handleChangePagination = (currentPage: number, pageSize: number) => {
    setPage(currentPage);
    setLimit(pageSize);
  };

  const items = [
    {
      key: "job",
      label: "Job View",
      children: (
        <>
          {total > 0 && <FilterPanel key={1} filter={filter} onFilter={handleFilter} />}
          <JobviewSubTab
            pagination={{ page, total, pageSize: limit, onChange: handleChangePagination }}
            loading={isLoading}
            data={datasetAssignments}
          />
        </>
      ),
      icon: <DatabaseOutlined />
    },
    {
      key: "file",
      label: "File View",
      children: (
        <>
          {total > 0 && <FilterPanel key={1} filter={filter} onFilter={handleFilter} />}
          <FileViewSubTab
            pagination={{ page, total, pageSize: limit, onChange: handleChangePagination }}
            loading={isLoading}
            data={datasetAssignments}
          />
        </>
      ),
      icon: <FileOutlined />
    }
  ];

  return (
    <Flex style={{ marginTop: 24 }} gap={24} direction='column'>
      <Tabs
        activeKey={activeTab}
        onChange={key => {
          setActiveTab(key);
          setFilter(prev => ({ ...prev, view: key }));
        }}
        items={items}
      />
    </Flex>
  );
}
