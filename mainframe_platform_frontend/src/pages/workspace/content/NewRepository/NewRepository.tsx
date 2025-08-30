import { useState } from "react";
import { useSelector } from "react-redux";

import { repositorySelector } from "@store";

import { ModalSuccess } from "../Repository/components";

import { InputContent } from "./InputContent";

export const NewRepository: React.FC = () => {
  const data = useSelector(repositorySelector.selectRepositoryData);
  const [isOnEdit, setIsOnEdit] = useState(false);
  const commonProps = { isOnEdit, setIsOnEdit, data: data as any };
  const [repositoryId, setRepositoryId] = useState<string>();

  return (
    <>
      <InputContent {...commonProps} setRepositoryId={setRepositoryId} />
      <ModalSuccess repositoryId={repositoryId} />
    </>
  );
};
