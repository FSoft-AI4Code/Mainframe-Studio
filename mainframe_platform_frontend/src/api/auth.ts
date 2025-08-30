import { Api, api } from "./config";

class Auth {
  instance: Api;

  constructor(params: Api) {
    this.instance = params;
  }

  public verifyToken = () => {
    return this.instance.post("/auth/verify");
  };
}

export const authApi = new Auth(api);
