import {
  CloseCircleOutlined,
  DeleteFilled,
  DownloadOutlined,
  EditOutlined,
  ExclamationCircleFilled,
  SaveOutlined
} from "@ant-design/icons";
import type { PaginationProps, TableProps } from "antd";
import {
  Form,
  Input,
  InputNumber,
  message,
  Modal,
  Popconfirm,
  Select,
  Spin,
  Table,
  Typography as TypoAntd,
  Typography as TypographyAntd
} from "antd";
import React, { useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import { SearchSvg } from "@assets/svg";
import { Button, Flex, Typography } from "@components";
import {
  useCategoryUtilityQuery,
  useDeleteRepository,
  useDeleteUtility,
  useExportUtilitiesReport,
  useProjectsQuery,
  useTriggerAssessment,
  useUpdateUtility,
  useUtilitiesFileQuery
} from "@services";
import { allColors, v2CommonColors } from "@style";
import { Repository, UtilityFile } from "@types";
import { addPropertiesToItems, handleErrorMessage } from "@utils";

import { WrapperForm } from "./components";

export interface Option {
  value?: string;
  label?: string;
}

const { confirm } = Modal;
const { Text } = TypoAntd;

interface EditableCellProps extends React.HTMLAttributes<HTMLElement> {
  editing: boolean;
  dataIndex: string;
  title: string;
  inputType: "number" | "text" | "select";
  record: UtilityFile;
  index: number;
  required?: boolean;
  options: Option[];
}

const EditableCell: React.FC<React.PropsWithChildren<EditableCellProps>> = ({
  editing,
  dataIndex,
  title,
  inputType,
  required,
  children,
  options,
  ...restProps
}) => {
  let inputNode: React.ReactNode;

  if (inputType === "number") {
    inputNode = <InputNumber />;
  } else if (inputType === "select") {
    inputNode = (
      <Select>
        {options?.map(opt => (
          <Select.Option key={opt.value} value={opt.label}>
            {opt.label}
          </Select.Option>
        ))}
      </Select>
    );
  } else {
    inputNode = <Input />;
  }

  return (
    <td {...restProps}>
      {editing ? (
        <Form.Item
          name={dataIndex}
          style={{ margin: 0 }}
          rules={[{ required: !!required, message: `Please input ${title}` }]}
        >
          {inputNode}
        </Form.Item>
      ) : (
        children
      )}
    </td>
  );
};

function PageContent() {
  const [form] = Form.useForm();

  const [editingKey, setEditingKey] = useState("");
  const [pagination, setPagination] = useState({ current: 1, pageSize: 10 });
  const [addNew, setAddNew] = useState(false);
  const navigate = useNavigate();
  const [messageApi, contextHolder] = message.useMessage();
  const { mutate: deleteUtility } = useDeleteUtility();
  const { mutate: udpateUtility } = useUpdateUtility();

  const { repoId = "" } = useParams();
  const { mutate: deleteRepository } = useDeleteRepository();
  const { project, isLoading: loadingProject } = useProjectsQuery();

  const { mutate: exportReport, isPending: loadingExport } = useExportUtilitiesReport();

  const { utilitiesFile, loading, total, refetchUtilitiesFile } = useUtilitiesFileQuery({
    repoId,
    skip: (pagination.current - 1) * pagination.pageSize,
    limit: pagination.pageSize
  });

  const handleTableChange = (paginationInfo: PaginationProps) => {
    setPagination({
      current: paginationInfo.current as number,
      pageSize: paginationInfo.pageSize as number
    });
  };

  const { categoryUtility } = useCategoryUtilityQuery({ repoId });

  const optionsCategory = Object.entries(categoryUtility)?.map(([key, value]) => ({
    label: key,
    value
  }));

  const isEditing = (record: UtilityFile) => record?._id?.toString() === editingKey;

  const edit = (record: Partial<UtilityFile>) => {
    form.setFieldsValue({ name: "", age: "", address: "", ...record });
    setEditingKey(record?._id?.toString() as string);
  };

  const cancel = () => {
    setEditingKey("");
  };

  const save = async (id: string) => {
    try {
      const row = (await form.validateFields()) as UtilityFile;

      if (!row) return;
      udpateUtility(
        {
          utility_id: id,
          comment: row?.comment,
          category: row?.category?.toString(),
          updated_at: row?.updated_at,
          description: row?.description
        },
        {
          onSuccess() {
            refetchUtilitiesFile();
            setEditingKey("");
          },
          onError(error) {
            handleErrorMessage(error, { show: true });
          }
        }
      );
    } catch (errInfo) {
      handleErrorMessage(errInfo, { show: true });
    }
  };

  const onDeleteRow = (id: string) => {
    if (!id) return;
    deleteUtility(id, {
      onError(error) {
        handleErrorMessage(error, { show: true });
      },
      onSuccess() {
        refetchUtilitiesFile();
      }
    });
  };

  const columns = [
    { title: "No", dataIndex: "no", key: "no", width: 80 },
    { title: "Id", dataIndex: "_id", key: "_id", width: 80 },
    { title: "Name", dataIndex: "name", key: "name" },
    {
      title: "Category",
      dataIndex: "category",
      key: "category",
      editable: true,
      options: optionsCategory,
      inputType: "select"
    },
    { title: "Description", dataIndex: "description", key: "description", editable: true },
    { title: "Comment", dataIndex: "comment", key: "comment", editable: true },
    {
      title: "Action",
      dataIndex: "actions",
      render: (_: unknown, record: UtilityFile) => {
        const editable = isEditing(record);
        return editable ? (
          <Flex>
            <Popconfirm title='Sure to update?' onConfirm={() => save(record._id)}>
              <Button size='small' shape='circle' type='ghost'>
                <SaveOutlined
                  style={{
                    color: "blue",
                    fontSize: 16
                  }}
                />
              </Button>
            </Popconfirm>
            <Popconfirm title='Sure to cancel?' onConfirm={cancel}>
              <Button size='small' shape='circle' type='ghost'>
                <CloseCircleOutlined
                  style={{
                    color: "red",
                    fontSize: 16
                  }}
                />
              </Button>
            </Popconfirm>
          </Flex>
        ) : (
          <Flex gap={4}>
            <TypographyAntd.Link disabled={editingKey !== ""} onClick={() => edit(record)}>
              <EditOutlined
                style={{
                  color: "green"
                }}
              />
            </TypographyAntd.Link>
            <Popconfirm title='Sure to delete?' onConfirm={() => onDeleteRow(record._id)}>
              <Button size='small' shape='circle' type='ghost'>
                <DeleteFilled
                  style={{
                    color: "red",
                    fontSize: 16
                  }}
                />
              </Button>
            </Popconfirm>
          </Flex>
        );
      }
    }
  ];

  const mergedColumns: TableProps<UtilityFile>["columns"] = columns.map(col => {
    if (!col.editable) {
      return col;
    }
    return {
      ...col,
      onCell: (record: UtilityFile) => ({
        record,
        inputType: col.inputType ?? "text",
        options: col?.options ?? [],
        dataIndex: col.dataIndex,
        title: col.title,
        editing: isEditing(record)
      })
    };
  });

  const { mutate: triggerAssessment, isPending } = useTriggerAssessment();
  const handleActions = {
    openNewRepo: (id: string) => {
      navigate(`/exploration/${id}/overview`);
    },
    deleteRepositoryById: (repo: Repository) => {
      if (!repo?.id) return;
      confirm({
        title: (
          <>
            Are you sure you want to delete the repository{" "}
            <Text strong style={{ fontWeight: 700, fontSize: 16, color: "blue" }}>
              {repo.name}
            </Text>
            ?
          </>
        ),
        icon: <ExclamationCircleFilled />,
        closable: false,
        async onOk() {
          if (!repo.id) return;
          deleteRepository(
            { repository_id: repo.id },
            {
              onSuccess() {
                // refetchRepository();
                messageApi.open({
                  type: "success",
                  content: "Deleted repository!"
                });
              },
              onError(error) {
                handleErrorMessage(error as never, { show: true });
              }
            }
          );
        },
        onCancel() {
          // eslint-disable-next-line no-console
          console.log("Cancel");
        }
      });
    },
    onTriggerAssessment: (repo: Repository) => {
      if (!repo?.id) return;
      confirm({
        title: (
          <>
            Are you sure you want to start the repository{" "}
            <Text strong style={{ fontWeight: 700, fontSize: 16, color: "blue" }}>
              {repo.name}
            </Text>
            ?
          </>
        ),
        icon: <ExclamationCircleFilled />,
        closable: false,
        okButtonProps: { loading: isPending },
        async onOk() {
          if (!repo.id) return;
          triggerAssessment(repo.id, {
            onSuccess() {
              // refetchRepository();
              messageApi.open({
                type: "success",
                content: "Repository has been started!"
              });
            },
            onError(error) {
              handleErrorMessage(error as never, { show: true });
            }
          });
        },
        onCancel() {
          // eslint-disable-next-line no-console
          console.log("Cancel");
        }
      });
    },
    exportExcelReport: () => {
      if (!repoId) return;
      exportReport(repoId);
    }
  };

  const [searchText, setSearchText] = useState<string>("");

  const searchUtilitiesData = useMemo(
    () =>
      searchText ? utilitiesFile?.filter(file => file?.name.includes(searchText)) : utilitiesFile,
    [searchText, utilitiesFile]
  );

  const { id: projectId } = project || {};
  if (loadingProject)
    return (
      <Flex style={{ height: "100%" }} center direction='column'>
        <Spin />
      </Flex>
    );

  return (
    <>
      <Flex
        gap={24}
        direction='column'
        style={{
          padding: 24,
          height: "100%",
          width: "100%"
        }}
      >
        <Flex
          justify='space-between'
          style={{ background: v2CommonColors.neutral1, padding: 24, borderRadius: 8 }}
          align='center'
          gap={12}
        >
          <Flex direction='column'>
            <Typography style={{ fontWeight: 700 }} level='h5-subtitles' color='primary10'>
              Utilities Used in the System
            </Typography>
            <Typography color='primary10' level='body-14b'>
              Manage the utilities used in the system
            </Typography>
          </Flex>

          <Button
            style={{
              height: 36,
              borderRadius: 8,
              width: 135
            }}
            loading={loadingExport}
            shape='default'
            type='primary'
            onClick={handleActions.exportExcelReport}
            icon={<DownloadOutlined />}
          >
            Export Report
          </Button>
        </Flex>

        <Flex
          style={{ background: v2CommonColors.neutral1, padding: 24, borderRadius: 8 }}
          gap={24}
          direction='column'
        >
          <Flex align='center' gap={12} justify='space-between'>
            <Input
              placeholder='Search'
              value={searchText}
              onChange={e => setSearchText(e.target.value)}
              prefix={<SearchSvg />}
              style={{ height: 40, background: allColors.neutral1, width: 480 }}
              disabled={loadingProject}
            />

            {/* <Button
              style={{
                height: 36,
                borderRadius: 8,
                width: 135
              }}
              onClick={() => !loadingProject && setAddNew(true)}
              shape='default'
              type='primary'
              icon={<PlusCircleOutlined />}
            >
              Add New
            </Button> */}
          </Flex>
          <Form form={form} component={false}>
            <Table<UtilityFile>
              components={{
                body: { cell: EditableCell }
              }}
              loading={loading}
              bordered
              dataSource={
                addPropertiesToItems(searchUtilitiesData, (_, i) => ({
                  no: (pagination.current - 1) * pagination.pageSize + (i + 1)
                })) as UtilityFile[]
              }
              columns={mergedColumns as never}
              rowClassName='editable-row'
              pagination={{
                position: ["bottomCenter"],
                onChange: cancel,
                current: pagination.current,
                pageSize: pagination.pageSize,
                total
              }}
              onChange={handleTableChange}
              scroll={{ x: "500px" }}
              rowKey={"id"}
            />
          </Form>
        </Flex>
      </Flex>

      {!!projectId && (
        <WrapperForm
          refetchRepository={refetchUtilitiesFile}
          addNew={addNew}
          setAddNew={setAddNew}
        />
      )}
      {contextHolder}
    </>
  );
}
export const Utilities: React.FC = () => {
  return (
    <Flex direction='column' style={{ width: "100%", overflowY: "auto", marginBottom: 24 }}>
      <PageContent />
    </Flex>
  );
};
