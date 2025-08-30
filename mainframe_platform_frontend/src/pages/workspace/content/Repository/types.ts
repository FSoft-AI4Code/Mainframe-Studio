import { RepoModel } from "@types";

export type CommonProps = {
  data: RepoModel;
  isOnEdit: boolean;
  setIsOnEdit: (v: boolean) => void;
};
