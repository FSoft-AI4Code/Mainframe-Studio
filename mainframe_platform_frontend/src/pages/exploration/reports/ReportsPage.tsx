import { Button, Input, Select, Table } from "antd";
import { ColumnsType } from "antd/es/table";
import { useNavigate, useParams } from "react-router-dom";
import { useState } from "react";
import { EditOutlined } from "@ant-design/icons";

import { Flex, Typography } from "@components";
import { useFilterGlobal } from "@hooks";
import { useListReverses } from "@services";
import { allColors } from "@style";
import { ReverseItem, ReverseTypeEnum } from "@types";
import { addPropertiesToItems, cleanString, getUniqueOptions, toPascalCase } from "@utils";

import { FilterSection, TableWrapper, warning } from "./styles";
import { CreateUtilityModal } from "./components/CreateUtilityModal";
export function ReportsPage() {
  const { filterReports, setReportsFilter } = useFilterGlobal();
  const { searchText, status: statusFilter, type: typeFilter, page = 1 } = filterReports || {};
  const { repoId = "" } = useParams();
  const navigate = useNavigate();
  const {
    files,
    isLoading: loadingFiles,
    refetch
  } = useListReverses({
    repoId: repoId || "",
    type: typeFilter as ReverseTypeEnum
  });

  const [isUpdateModalOpen, setIsUpdateModalOpen] = useState(false);
  const [selectedReport, setSelectedReport] = useState<ReverseItem>();
  const columns: ColumnsType<ReverseItem> = [
    {
      title: "NAME",
      dataIndex: "name",
      key: "name",
      sorter: (a, b) => a?.name.localeCompare(b?.name),
      filteredValue: searchText ? [searchText] : null,
      showSorterTooltip: false,
      onFilter: (_, record) => {
        return record.name.toLowerCase().includes(searchText.toLowerCase());
      }
    },
    {
      title: "TYPE",
      dataIndex: "type",
      key: "type",
      filteredValue: typeFilter ? [typeFilter] : null,
      onFilter: (_, record) => !typeFilter || record.type === typeFilter
    },
    {
      title: "STATUS",
      dataIndex: "status",
      key: "status",
      render: (value: string) => <Typography level='body-16r'>{toPascalCase(value)}</Typography>,
      filteredValue: statusFilter ? [statusFilter] : null,
      onFilter: (_, record) => !statusFilter || record.status === statusFilter
    },
    {
      title: "Action",
      dataIndex: "updated_at",
      key: "updated_at",
      width: 150,
      onCell: () => ({
        onClick: e => {
          e.preventDefault();
          e.stopPropagation();
        }
      }),
      render(value, record) {
        return (
          <Button
            size='middle'
            styles={{ icon: { color: "#28C028" } }}
            onClick={e => {
              e.stopPropagation();
              setSelectedReport(record);
              setIsUpdateModalOpen(true);
            }}
            icon={<EditOutlined size={40} />}
            type='text'
          />
        );
      }
    }
  ];

  const handleRowClick = (record: ReverseItem) => {
    // eslint-disable-next-line @typescript-eslint/naming-convention
    const { type: typeFile, name, is_reversed } = record || {};
    if (!is_reversed) {
      return warning({
        title: "The report file is empty!",
        closable: true
      });
    }

    return navigate(`detail/${cleanString(typeFile)}/${cleanString(name)}`, {
      state: { searchText, statusFilter, typeFilter },
      replace: false
    });
  };

  const typeOptions = getUniqueOptions<ReverseItem, "type">(files, "type");
  const statusOptions = getUniqueOptions<ReverseItem, "status">(files, "status");

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
            Reverse Engineering File Manager
          </Typography>
        </Flex>
        <Flex style={{ padding: "20px", flex: "1 1 0%" }} direction='column'>
          <FilterSection>
            <Input
              placeholder='Search by Name'
              value={searchText}
              onChange={e => {
                const value = e.target.value;
                setReportsFilter({
                  searchText: value as string
                });
              }}
              style={{ flex: 1 }}
            />
            <Select
              placeholder='Filter by Type'
              allowClear
              value={typeFilter}
              onChange={value => {
                setReportsFilter({
                  type: value as string
                });
              }}
              loading={loadingFiles}
              options={typeOptions}
            />
            <Select
              placeholder='Filter by Status'
              allowClear
              value={statusFilter}
              loading={loadingFiles}
              dropdownStyle={{ textTransform: "capitalize" }}
              style={{ textTransform: "capitalize" }}
              onChange={value => {
                setReportsFilter({
                  status: value as string
                });
              }}
              options={addPropertiesToItems(statusOptions, ({ label }) => ({
                label: toPascalCase(label)
              }))}
            />
          </FilterSection>
          <TableWrapper>
            <Table
              columns={columns}
              dataSource={Array.isArray(files) ? files : []}
              pagination={{
                pageSize: 10,
                showSizeChanger: false,
                showQuickJumper: false,
                current: page,
                onChange(currnetPage) {
                  setReportsFilter({
                    page: currnetPage
                  });
                },
                size: "small"
              }}
              rowKey='name'
              loading={loadingFiles}
              scroll={{ y: "calc(100vh - 360px)" }}
              onRow={record => ({
                onClick: e => {
                  e.preventDefault();
                  handleRowClick(record);
                }
              })}
            />
          </TableWrapper>
        </Flex>
      </Flex>
      <CreateUtilityModal
        key={(selectedReport as ReverseItem)?.name + (selectedReport as ReverseItem)?.type}
        data={selectedReport as ReverseItem}
        setOpen={setIsUpdateModalOpen}
        open={isUpdateModalOpen}
        refetchReport={refetch}
      />
    </Flex>
  );
}
