import styled from "@emotion/styled";
import { useTranslation } from "react-i18next";
import { useNavigate } from "react-router-dom";

import { ArrowRightSvg } from "@assets/svg";
import { Button as AntdButton, Flex, Typography } from "@components";
import { ROUTERS } from "@defines";
import { RepoModel } from "@types";
import { formatDateUS } from "@utils";

import { CommonProps } from "./types";

const Button = styled(AntdButton)`
  background-color: ${({ theme }) => theme.colors.primary100}80;
`;

export const Information: React.FC<CommonProps & { data: RepoModel }> = ({ data, setIsOnEdit }) => {
  const navigate = useNavigate();
  const { t } = useTranslation();
  // const copyGraph = useSelector(repositorySelector.selectRepositoryCopyGraph);
  // const migrationData = useSelector(migrationRepositorySelector.selectMigrationRepositoryData);

  const onClickEdit = () => setIsOnEdit(true);

  const onClickGraph = () => {
    // if (copyGraph) navigate(ROUTERS.EXPLORATION_GRAPH);
    // else navigate(ROUTERS.EXPLORATION_FILE);
    navigate(ROUTERS.EXPLORATION_GRAPH);
  };

  // const onClickCopy = () => {
  //   try {
  //     if (migrationData?._id) {
  //       navigator.clipboard.writeText(
  //         location.origin +
  //           ROUTERS.SHARE_MIGRATION.replace(":projectId", String(data._id)).replace(
  //             ":matchingId",
  //             String(migrationData?._id)
  //           )
  //       );
  //     } else {
  //       navigator.clipboard.writeText(
  //         location.origin + ROUTERS.SHARE.replace(":projectId", data._id)
  //       );
  //     }
  //     messageApi.success("Copied shared project URL to clipboard!");
  //   } catch (error) {
  //     messageApi.error("Failed to copy");
  //   }
  // };

  return (
    <Flex direction='column' gap={24}>
      <Flex direction='column' gap={12} style={{ padding: "0 12px" }}>
        <div>
          <Typography level='h6-body1m' color='grey300'>
            {t("label.repo_name")}
          </Typography>
          <Typography level='h5-subtitles' color='primary100'>
            {data.name}
          </Typography>
        </div>
        <div>
          <Typography level='h6-body1m' color='grey300'>
            {t("label.url")}
          </Typography>
          <Typography level='h5-subtitles' color='primary100' ellipsis>
            {data.url}
          </Typography>
        </div>
        <div>
          <Typography level='h6-body1m' color='grey300'>
            {t("label.fetched_time")}
          </Typography>
          <Typography level='h5-subtitles' color='primary100'>
            {formatDateUS(data.created_at)}
          </Typography>
        </div>
      </Flex>
      <Flex gap={24}>
        <Button type='primary' onClick={onClickEdit}>
          {t("button.edit")}
        </Button>
        <Button type='primary' iconSuffix={<ArrowRightSvg />} onClick={onClickGraph}>
          {t("button.exploration")}
        </Button>
      </Flex>
    </Flex>
  );
};
