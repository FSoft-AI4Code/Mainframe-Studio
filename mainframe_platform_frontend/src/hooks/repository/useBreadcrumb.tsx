import styled from "@emotion/styled";
import { BreadcrumbProps } from "antd";
import { useEffect, useState } from "react";

import { FolderSvg, RootSvg } from "@assets/svg";
import { IconCircle } from "@components";
import { File, RepoModel } from "@types";

const Title = styled.span`
  display: flex;
  align-items: center;

  & > *:not(:last-child) {
    margin-right: 10px;
  }
`;

const Text = styled.span<{ type?: "folder" | "file" }>`
  font-size: 16px;
  font-weight: 600;
  line-height: 24px;
  letter-spacing: 0em;
  color: ${({ theme, type }) => (type === "folder" ? theme.colors.primary100 : "white")};
  text-decoration: ${({ type }) => (type === "folder" ? "underline" : "none")};
`;

type Props = {
  project: Partial<RepoModel>;
  treeFileSelected: File | undefined;
};

export const useBreadcrumb: ({ project, treeFileSelected }: Props) => BreadcrumbProps = ({
  project,
  treeFileSelected
}) => {
  const [paths, setPaths] = useState<string[]>();
  const [items, setItems] = useState<BreadcrumbProps["items"]>([]);

  useEffect(() => {
    setPaths(treeFileSelected ? treeFileSelected.path.split("/") : undefined);
  }, [treeFileSelected]);

  useEffect(() => {
    if (!paths) setItems(undefined);
    else {
      setItems([
        {
          title: (
            <Title>
              <IconCircle icon={<RootSvg />} size={24} />
              <Text type='folder'>{project.name}</Text>
            </Title>
          )
        },
        ...paths.map((o, i) => ({
          title: (
            <Title>
              {i !== paths.length - 1 && <IconCircle icon={<FolderSvg />} size={24} />}
              <Text type={i === paths.length - 1 ? "file" : "folder"}>{o}</Text>
            </Title>
          )
        }))
      ]);
    }
  }, [paths]);

  return {
    items
  };
};
