import { MenuProps } from "antd";
import { useTranslation } from "react-i18next";
import { useSelector } from "react-redux";
import { useLocation, useNavigate } from "react-router-dom";

import { CobolListSvg, MigrationSvg, RepositorySvg } from "@assets/svg";
import { IconCircle } from "@components";
import { repositorySelector } from "@store";

export const useMenu: () => MenuProps = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const repositoryId = useSelector(repositorySelector.selectRepositoryId);
  const location = useLocation();
  const subWorkspace = location.pathname.split("/").at(-1);
  const onClickItem = (category: string) => {
    navigate(`/workspace/${category}`);
  };

  const items = [
    ...(repositoryId
      ? [
          {
            getIcon: (active: boolean) => (
              <IconCircle icon={<RepositorySvg />} size={32} active={active} />
            ),
            label: t("component.menu.cobol_repo"),
            category: "repository"
          }
        ]
      : []),
    {
      getIcon: (active: boolean) => (
        <IconCircle icon={<CobolListSvg />} size={32} active={active} isStroke />
      ),
      label: t("component.menu.cobol_list"),
      category: "repositories"
    },
    // ...(isShowExploration === true
    //   ? [
    //       {
    //         getIcon: (active: boolean) => <IconCircle icon={<MigrationSvg />} size={32} active={active} />,
    //         label: 'Exploration file level',
    //         category: 'exploration'
    //       }
    //     ]
    //   : []),
    {
      getIcon: (active: boolean) => (
        <IconCircle icon={<MigrationSvg />} size={32} active={active} />
      ),
      label: t("component.menu.cobol_migration"),
      category: "migration"
    }
  ].map(({ getIcon, ...o }) => ({
    ...o,
    key: o.category,
    icon: getIcon(o.category === subWorkspace),
    onClick: () => onClickItem(o.category)
  }));

  return {
    items,
    selectedKeys: subWorkspace ? [subWorkspace] : items[0]?.key ? [String(items[0].key)] : []
  };
};
