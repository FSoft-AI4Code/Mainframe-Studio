import {
  DeleteOutlined,
  EditOutlined,
  ExclamationCircleFilled,
  PlayCircleFilled
} from "@ant-design/icons";
import { Button, Input, Layout, message, Modal, Spin, Table, Typography as TypoAntd } from "antd";
import { ColumnType } from "antd/es/table";
import { useCallback, useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";

import { BigFolderSvg, DividerSvg, SearchSvg, SysAssessmentSvg } from "@assets/svg";
import { Flex, StatusLabel, Typography } from "@components";
import { ROUTERS } from "@defines";
import { TopbarLayout } from "@layouts/TopbarLayout";
import { HEADER_DASHBOARD_HEIGHT } from "@layouts/TopbarLayout/config";
import {
  useDeleteRepository,
  useGetRepositories,
  useProjectsQuery,
  useTriggerAssessment
} from "@services";
import { allColors } from "@style";
import { Repository } from "@types";
import { handleErrorMessage } from "@utils";

import { UploadButton, WrapperForm } from "./components";
import { UpdateRepoForm } from "./components/Update";

const { Header } = Layout;
const { confirm } = Modal;
const { Text } = TypoAntd;

function PageContent() {
  const [isUpdateModalOpen, setIsUpdateModalOpen] = useState(false);
  const [addNew, setAddNew] = useState(false);
  const [selectedRepo, setSelectedRepo] = useState<Repository>();
  const navigate = useNavigate();
  const [messageApi, contextHolder] = message.useMessage();

  const { mutate: deleteRepository } = useDeleteRepository();
  const { project, isLoading: loadingProject } = useProjectsQuery();

  const {
    repositories,
    isLoading: loadingRepositories,
    refetch: refetchRepository
  } = useGetRepositories({ limit: 100, skip: 0, enabled: !!project?.id });
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
                refetchRepository();
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
              refetchRepository();
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
    }
  };
  const columns: ColumnType<Repository>[] = [
    {
      title: "No",
      dataIndex: "no",
      key: "no",
      width: 60,
      render: value => {
        return <Flex center>{value}</Flex>;
      }
    },
    {
      title: "Name",
      dataIndex: "name",
      key: "name",
      width: 200
    },
    {
      title: "Description",
      dataIndex: "description",
      key: "description"
    },
    {
      title: "Status",
      dataIndex: "status",
      key: "status",
      width: 120,
      render: (_no, { status }) => <StatusLabel status={status} />
    },
    {
      title: "Action",
      dataIndex: "updated_at",
      key: "updated_at",
      width: 150,
      render(value, record) {
        return (
          <Flex gap={4}>
            <Button
              onClick={() => handleActions.onTriggerAssessment(record)}
              size='middle'
              icon={<PlayCircleFilled size={40} />}
              type='text'
              styles={{ icon: { color: allColors.primary6 } }}
            />
            <Button
              size='middle'
              styles={{ icon: { color: "#28C028" } }}
              onClick={() => {
                setSelectedRepo(record);
                setIsUpdateModalOpen(true);
              }}
              icon={<EditOutlined size={40} />}
              type='text'
            />
            <Button
              danger
              onClick={() => handleActions.deleteRepositoryById(record)}
              size='middle'
              icon={<DeleteOutlined size={40} />}
              type='text'
            />
          </Flex>
        );
      }
    }
  ];
  const [searchText, setSearchText] = useState<string>("");

  const searchRepositories = useMemo(
    () =>
      searchText ? repositories?.filter(repo => repo.name.includes(searchText)) : repositories,
    [searchText, repositories]
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
      {repositories && repositories?.length > 0 && (
        <Flex gap={32} direction='column' style={{ padding: 32, width: "100%" }}>
          <Flex align='center' gap={12} justify='space-between'>
            <Input
              placeholder='Search'
              value={searchText}
              onChange={e => setSearchText(e.target.value)}
              prefix={<SearchSvg />}
              style={{ height: 40, background: allColors.neutral1, width: 480 }}
              disabled={loadingProject}
            />
            <UploadButton title='Upload New' onClick={() => !loadingProject && setAddNew(true)} />
          </Flex>
          <Table
            bordered
            columns={columns}
            loading={loadingRepositories}
            dataSource={searchRepositories?.map((item, i) => ({ ...item, no: i + 1 }))}
            onRow={record => ({
              onClick: e => {
                const lastColumnIndex = columns.length - 1;
                const target = e.target as HTMLElement;
                if (target.closest("td")?.cellIndex !== lastColumnIndex) {
                  handleActions.openNewRepo(record.id);
                }
              }
            })}
            pagination={{
              position: ["bottomCenter"]
            }}
            scroll={{ x: "600px", y: "calc(100vh - 300px)" }}
            rowKey={"no"}
            sticky
          />
          <UpdateRepoForm
            key={selectedRepo?.id}
            repo={selectedRepo as Repository}
            setOpen={setIsUpdateModalOpen}
            open={isUpdateModalOpen}
            refetchRepository={refetchRepository}
          />
        </Flex>
      )}
      {(!projectId || repositories.length === 0) && (
        <>
          <Flex style={{ width: "100%", height: "100%" }} center>
            <Flex
              style={{
                width: 320,
                height: 320,
                borderRadius: "50%",
                background: allColors.neutral1
              }}
              center
              gap={24}
              direction='column'
            >
              <BigFolderSvg />
              {projectId && (
                <UploadButton
                  title='Upload Repository'
                  onClick={() => !loadingProject && setAddNew(true)}
                />
              )}
            </Flex>
          </Flex>
        </>
      )}
      {!!projectId && (
        <WrapperForm refetchRepository={refetchRepository} addNew={addNew} setAddNew={setAddNew} />
      )}
      {contextHolder}
    </>
  );
}
export const Repositories: React.FC = () => {
  const navigate = useNavigate();
  const onChangeSegmented = useCallback((value: string) => {
    navigate(`/${value}`);
  }, []);

  return (
    <Flex style={{ height: "100vh", width: "100%" }}>
      <TopbarLayout
        segmented={{
          options: [
            {
              label: "Repository List",
              key: ROUTERS.WORKSPACE_REPOSITORIES.replace("/", ""),
              icon: <SysAssessmentSvg />,
              breadcrumb: "List File"
            }
          ],
          onChange: onChangeSegmented,
          defaultValue: ROUTERS.WORKSPACE_REPOSITORIES.replace("/", ""),
          value: location.pathname.slice(1)
        }}
      >
        <Header
          style={{
            height: HEADER_DASHBOARD_HEIGHT,
            borderBottom: `1px solid ${allColors.neutral6}`,
            background: allColors.neutral4,
            padding: "0 32px "
          }}
        >
          <Flex style={{ padding: "24px 0 16px" }} gap={8} align='center'>
            <Typography level='title-24b' color='primary10'>
              Repository List
            </Typography>
            <Flex style={{ padding: "4px 8px 0" }}>
              <DividerSvg />
            </Flex>
            <Typography level='h6-body1r' color='primary6'>
              List File
            </Typography>
          </Flex>
        </Header>
        <PageContent />
      </TopbarLayout>
    </Flex>
  );
};
