import { persistor, store } from "@store";
import { AuthTokens } from "@types";
import { removeAuthToken } from "@utils";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class UserApi {
  static doLoginRequest = (params: FormData) => {
    return HttpClient.post<AuthTokens>(API_ENPOINTS.LOGIN, params, {
      headers: { "Content-Type": "multipart/form-data" }
    });
  };

  static cleanStore = async () => {
    await persistor.flush();
    await persistor.purge();
    store.dispatch({ type: "GLOBAL_RESET", payload: null });
  };

  static doLogoutRequest = async () => {
    removeAuthToken();
    await this.cleanStore();
  };
}
