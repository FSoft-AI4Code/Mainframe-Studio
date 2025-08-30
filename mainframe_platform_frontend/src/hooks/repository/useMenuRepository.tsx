import { MenuProps } from "antd";
import { useCallback, useEffect, useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import { FolderSvg, RootSvg } from "@assets/svg";
import { IconCircle } from "@components";
import { File, Folder, TreeView } from "@types";

export type MenuEvent = (info: { key?: string }) => void;

export type MenuRepositoryProps = {
  tree: TreeView | null | undefined;
  menuEvent?: MenuEvent;
  additionalKeys?: string[];
};

export const useMenuRepository: ({ tree, additionalKeys }: MenuRepositoryProps) => MenuProps = ({
  tree,
  menuEvent,
  additionalKeys
}) => {
  const { repoId, fileId } = useParams();
  const navigate = useNavigate();
  const [openKeys, setOpenKeys] = useState<Array<string>>([]);

  const onOpenChange: MenuProps["onOpenChange"] = useCallback((keys: Array<string>) => {
    setOpenKeys(keys);
  }, []);

  const items = useMemo(() => {
    if (!tree) return [];
    const analyze = (dir: File | Folder): Required<MenuProps>["items"][number] => {
      if (dir.type === "tree") {
        return {
          key: dir.id,
          label: dir.name,
          icon: <IconCircle icon={dir.path === "" ? <RootSvg /> : <FolderSvg />} size={32} />,
          children: dir.children?.map?.(analyze)
        };
      } else {
        return {
          key: dir.id,
          label: dir.name,
          onClick: menuEvent
            ? menuEvent
            : info => {
                navigate(`/exploration/${repoId}/file/${info.key}`);
              }
        };
      }
    };

    return tree.map(analyze);
  }, [tree]);

  useEffect(() => {
    if (items?.[0]?.key) setOpenKeys([items[0].key.toString()]);
  }, [items]);

  const selectedKeys = useMemo(() => {
    if (!additionalKeys?.length && !fileId) {
      return undefined;
    }
    return ([fileId, ...(additionalKeys || [])]?.filter(i => i) as string[]) || undefined;
  }, [additionalKeys, fileId]);

  return {
    items,
    openKeys,
    onOpenChange,
    selectedKeys
  };
};
