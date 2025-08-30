import styled from "@emotion/styled";
import { BreadcrumbProps, Space, Typography } from "antd";
import { FunctionComponent, ReactNode, useMemo } from "react";
import { useTranslation } from "react-i18next";
import { Link, useParams } from "react-router-dom";

import { CobolListSvg, MigrationSvg, RepositorySvg } from "@assets/svg";
import { IconCircle } from "@components";
import { workspace } from "@defines";

type Item = {
  router?: string;
  title: ReactNode;
};

const populateCategory = (cate: string) => cate.replace(/\//g, "");

const BreadcrumbText = styled(Typography)`
  font-weight: 700;
  font-size: 16px;
  line-height: 24px;
  color: ${({ theme }) => theme.colors.primary100};
`;

const genBreadcrumbItem = (Icon: FunctionComponent, title: string): ReactNode => {
  return (
    <Space style={{ gap: 6 }}>
      <IconCircle icon={<Icon />} size={24} />
      <BreadcrumbText>{title}</BreadcrumbText>
    </Space>
  );
};

const getItems: (params: { items?: Item[] }) => Required<BreadcrumbProps>["items"][number][] = ({
  items
}) =>
  (
    [
      // {
      //   router: ROUTERS.WORKSPACE_HOME,
      //   title: 'Workspace'
      // },
      ...(items || [])
    ] as Item[]
  ).map(o => ({
    ...o,
    href: o.router,
    title: o.router ? <Link to={o.router}>{o.title}</Link> : o.title
  }));

export const useBreadcrumb: () => BreadcrumbProps = () => {
  const { workspaceCategory } = useParams();
  const { t } = useTranslation();

  const categories = [
    {
      category: populateCategory(workspace.WORKSPACE_REPOSITORY),
      title: t("component.breadcrumb.cobol_repo"),
      icon: RepositorySvg
    },
    {
      category: populateCategory(workspace.WORKSPACE_REPOSITORIES),
      title: t("component.breadcrumb.cobol_list"),
      icon: CobolListSvg
    },
    // {
    //   category: populateCategory(workspace.WORKSPACE_EXPLORATION),
    //   title: 'Exploration file level'
    // },
    {
      category: populateCategory(workspace.WORKSPACE_MIGRATION_REPOSITORY),
      title: t("component.breadcrumb.cobol_migration"),
      icon: MigrationSvg
    }
  ];

  const currentBreadcrumb = useMemo(() => {
    const currentCategory = categories.find(({ category }) => category === workspaceCategory);

    return {
      items: getItems({
        items: currentCategory
          ? [
              {
                title: currentCategory.icon
                  ? genBreadcrumbItem(currentCategory.icon, currentCategory.title)
                  : currentCategory.title
              }
            ]
          : []
      })
    };
  }, [workspaceCategory]);

  return currentBreadcrumb;
};
