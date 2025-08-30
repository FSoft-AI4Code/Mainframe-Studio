import { Empty, Input, Select, Table, Typography as TypographyAntd } from "antd";
import { ColumnsType } from "antd/es/table";
import { useMemo } from "react";
import { useParams } from "react-router-dom";

import { Flex, Typography } from "@components";
import { useFilterGlobal } from "@hooks";
import { useCrudRepositoryQuery } from "@services";
import { allColors } from "@style";
import { CrudItem } from "@types";

import { FilterSection, TableWrapper } from "./styles";

const { Text } = TypographyAntd;

const permMap: Record<string, string> = {
  CREATE: "C",
  READ: "R",
  UPDATE: "U",
  DELETE: "D"
};

export function DatabasePage() {
  const { filterDatabase, setDatabaseFilter } = useFilterGlobal();
  const { searchText, type: typeFilter, page = 1, searchTable } = filterDatabase || {};
  const { repoId = "" } = useParams();

  const { crudItems, isLoading } = useCrudRepositoryQuery({ repository_id: repoId });

  const crudOptions = useMemo(() => {
    const permsSet = new Set<string>();
    crudItems?.forEach(item => {
      item.operations?.forEach(op => {
        const short = permMap[op];
        if (short) permsSet.add(short);
      });
    });
    return Array.from(permsSet)
      .sort((a, b) => Object.values(permMap)?.indexOf(a) - Object.values(permMap)?.indexOf(b))
      .map(p => ({ label: p, value: p }));
  }, [crudItems]);

  const allTables = useMemo(() => {
    const tables = new Set<string>();
    crudItems?.forEach(item => {
      if (item.table_name) {
        tables.add(item.table_name);
      }
    });
    return Array.from(tables);
  }, [crudItems, searchText, searchTable]);

  const placeholderColumns = Array.from({ length: 8 }, (_, i) => `Table ${i + 1}`);
  const currentTable = allTables?.length > 0 ? allTables : placeholderColumns;

  const filteredTablesMemo = useMemo(() => {
    if (!searchTable) return currentTable;
    return currentTable.filter(tableName =>
      tableName.toLowerCase().includes(searchTable.toLowerCase())
    );
  }, [currentTable, searchTable]);

  const filteredTables = filteredTablesMemo?.length > 0 ? filteredTablesMemo : ["Not Found"];

  const columns: ColumnsType<CrudItem> = useMemo(() => {
    return [
      {
        title: () => (
          <>
            <Flex
              style={{
                position: "absolute",
                background:
                  "linear-gradient(to right top, #ffffff 0%, #ffffff 49.9%, #BFBFBF 50%, #BFBFBF 51%, #ffffff 51.1%, #ffffff 100%)",
                clipPath: "polygon(0 0, 100% 0, 100% 100%)",
                height: "100%",
                width: "100%",
                top: 0,
                zIndex: 0
              }}
              direction='column'
            >
              <Text
                style={{
                  width: "100%",
                  textAlign: "end",
                  padding: "0px 12px",
                  color: allColors.neutral10,
                  fontWeight: 600,
                  fontSize: 16
                }}
              >
                Table
              </Text>
            </Flex>
            <Flex
              style={{
                position: "absolute",
                height: "100%",
                width: "100%",
                bottom: 0,
                zIndex: 1
              }}
              direction='column'
            >
              <Text
                style={{
                  padding: "0 12px",
                  marginTop: "auto",
                  color: allColors.neutral10,
                  fontWeight: 600,
                  fontSize: 16
                }}
              >
                Program
              </Text>
            </Flex>
          </>
        ),
        dataIndex: "program_name",
        key: "program_name",
        fixed: "left",
        width: 150,
        filteredValue: searchText ? [searchText] : null,
        onFilter: (_, record) => {
          return record?.program_name?.toLowerCase().includes(searchText.toLowerCase());
        },
        render: text => (
          <Text style={{ whiteSpace: "nowrap" }} strong>
            {text}
          </Text>
        )
      },
      ...filteredTables?.map((tableName: string) => ({
        title: (
          <Text style={{ whiteSpace: "nowrap" }} strong>
            {tableName}
          </Text>
        ),
        dataIndex: tableName,
        key: tableName,
        width: 200,
        render: (operations?: string[]) => {
          if (!operations || operations.length === 0) {
            return <Text type='secondary'>-</Text>;
          }
          const allowedOrder = ["C", "R", "U", "D"];
          const sortedOps = operations
            .map(op => op?.charAt(0)?.toUpperCase())
            .sort((a, b) => allowedOrder.indexOf(a) - allowedOrder.indexOf(b));
          return (
            <Flex gap={4}>
              {sortedOps.map(op => (
                <Typography level='title-20b' color={"primary6"} key={op}>
                  {op}
                </Typography>
              ))}
            </Flex>
          );
        }
      }))
    ];
  }, [filteredTables]);

  const processedData = useMemo(() => {
    const programMap: Record<
      string,
      {
        key: string[] | string;
        program_name: string;
        [tableName: string]: string[] | string;
      }
    > = {};

    crudItems?.forEach(item => {
      const key = item.program_name;
      if (!programMap[key]) {
        programMap[key] = {
          key,
          program_name: key
        };
      }

      if (item.table_name) {
        programMap[key][item.table_name] = item.operations || [];
      }
    });

    return Object.values(programMap);
  }, [crudItems]);

  const filteredData = useMemo(() => {
    if (!typeFilter || typeFilter.length === 0) return processedData;

    return processedData
      ?.map(item => {
        const newItem = { ...item };
        const keys = Object.keys(item).filter(k => k !== "program_name" && k !== "key");

        for (const table of keys) {
          const arrayRaw = item[table] as string[];
          const ops = arrayRaw?.map((op: string) => permMap[op]);
          const hasAll = typeFilter.every(t => ops.includes(t));
          if (!hasAll) {
            delete newItem[table];
          }
        }

        const remainingTables = Object.keys(newItem).filter(
          k => k !== "program_name" && k !== "key"
        );
        if (remainingTables.length === 0) return null;
        return newItem;
      })
      .filter(Boolean);
  }, [processedData, typeFilter]);

  return (
    <Flex style={{ padding: 24, width: "100%", height: "100%" }}>
      <Flex
        style={{
          width: "100%",
          height: "100%",
          background: allColors.neutral1,
          borderRadius: "8px"
        }}
        direction='column'
      >
        <Flex
          justify='space-between'
          align='center'
          style={{ padding: 20, borderBottom: `1px solid ${allColors.neutral6}` }}
        >
          <Typography color='primary10' level='body-16b'>
            Program & Table CRUD Relationships
          </Typography>
        </Flex>
        <Flex style={{ padding: "20px", flex: "1 1 0%" }} direction='column'>
          <FilterSection>
            <Input
              placeholder='Search Program'
              value={searchText}
              onChange={e => setDatabaseFilter({ searchText: e.target.value })}
              style={{ flex: 1 }}
            />
            <Input
              placeholder='Search Table'
              value={searchTable}
              onChange={e => setDatabaseFilter({ searchTable: e.target.value })}
              style={{ flex: 1 }}
            />
            <Select
              placeholder='CRUD Filter'
              mode='multiple'
              allowClear
              value={typeFilter}
              onChange={value => setDatabaseFilter({ type: value })}
              options={crudOptions}
              style={{ flex: 1 }}
            />
          </FilterSection>
          <TableWrapper>
            <Table
              columns={columns as never}
              showHeader={processedData.length > 0}
              dataSource={filteredData as never}
              loading={isLoading}
              pagination={{
                pageSize: 10,
                current: page,
                onChange: p => setDatabaseFilter({ page: p }),
                showTotal: () => `Total tables: ${filteredTablesMemo?.length}`
              }}
              rowKey='program_name'
              scroll={
                processedData && processedData?.length
                  ? { y: "calc(100vh - 360px)", x: "80vw" }
                  : undefined
              }
              locale={{
                emptyText: (
                  <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description='No data to display' />
                )
              }}
            />
          </TableWrapper>
        </Flex>
      </Flex>
    </Flex>
  );
}
