import { UserModel } from "@types";

export type State = {
  data?: UserModel;
  isAuthorized: boolean;
};
