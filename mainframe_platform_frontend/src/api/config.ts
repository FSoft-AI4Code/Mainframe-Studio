/* eslint-disable @typescript-eslint/no-explicit-any */
import { message as messageApi } from "antd";
import axios, { AxiosError, AxiosInstance, AxiosRequestConfig, AxiosResponse } from "axios";

import { backendURL } from "@configs";
import { RESPONSE_CODE, storage } from "@defines";
import { Response } from "@types";

function handleSuccessResponse(response: AxiosResponse) {
  return response.data;
}

function handleError(error: Error | AxiosError, api: Api) {
  // eslint-disable-next-line
  console.error("Error", (error as any)?.response?.data?.resCode);

  if (error instanceof AxiosError) {
    const { response } = error;
    const status: number | undefined = response?.status;
    const message: RESPONSE_CODE = response?.data?.message;
    // eslint-disable-next-line
    console.error("Axios error", status, message);

    if (status === 401) {
      messageApi.error(error?.response?.data?.detail || "Unauthenticated user");
      api.removeToken();
    }
  }
  throw error;
}

export class Api {
  public caller!: AxiosInstance;

  static instance?: Api;

  static getInstance() {
    if (!this.instance) this.instance = new Api();
    return this.instance;
  }

  constructor() {
    this.init();
  }

  private init() {
    this.caller = axios.create();
    // - Token
    const token = localStorage.getItem(storage.TOKEN) || sessionStorage.getItem(storage.TOKEN);
    // eslint-disable-next-line
    if (token) this.caller.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    // - Config
    this.caller.defaults.baseURL = backendURL;
    this.caller.defaults.timeout = 1000 * 60 * 5;
    this.caller.interceptors.response.use(handleSuccessResponse, error => handleError(error, this));
  }

  //> Handle
  public getAuthorizationToken = () => this.caller.defaults.headers.common.Authorization;

  public isAuthorization = () => Boolean(this.getAuthorizationToken());

  public setToken(token: string, options?: { saveToken?: boolean; pushChannel?: boolean }) {
    if (options?.saveToken) localStorage.setItem(storage.TOKEN, token);
    // eslint-disable-next-line
    if (token) this.caller.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  }

  public removeToken() {
    localStorage.removeItem(storage.TOKEN);
    // eslint-disable-next-line
    this.caller.defaults.headers.common["Authorization"] = "";
  }

  // COBOL: legacy code
  // > Controller
  // private controller: <T = any>(handle: () => Promise<AxiosResponse<Response<T>>>) => Promise<Response<T>> =
  //   async handle => {
  //     try {
  //       const response = await handle()
  //       return response.data
  //     } catch (error) {
  //       // eslint-disable-next-line
  //       console.log('Error', (error as any)?.response?.data?.resCode)

  //       if (error instanceof AxiosError) {
  //         const { response } = error
  //         const status: number | undefined = response?.status
  //         const message: RESPONSE_CODE = response?.data?.message
  //         // eslint-disable-next-line
  //         console.log('Axios error', status, message)
  //       }
  //       throw error
  //     }
  //   }

  // > Request
  public get<T = any, D = any>(
    url: string,
    apiConfig?: AxiosRequestConfig<D>
  ): Promise<Response<T>> {
    // eslint-disable-next-line
    // console.log("[GET]", url);
    return this.caller.get(url, apiConfig);
  }

  public delete<T = any, D = any>(
    url: string,
    apiConfig?: AxiosRequestConfig<D>
  ): Promise<Response<T>> {
    // eslint-disable-next-line
    console.log("[DELETE]", url);
    return this.caller.delete(url, apiConfig);
  }

  public post<T = any, D = any>(
    url: string,
    data?: D,
    apiConfig?: AxiosRequestConfig<D>
  ): Promise<Response<T>> {
    // eslint-disable-next-line
    // console.log("[POST]", url);
    return this.caller.post(url, data, apiConfig);
  }

  public put<T = any, D = any>(
    url: string,
    data?: D,
    apiConfig?: AxiosRequestConfig<D>
  ): Promise<Response<T>> {
    // eslint-disable-next-line
    console.log("[PUT]", url);
    return this.caller.put(url, data, apiConfig);
  }

  public patch<T = any, D = any>(
    url: string,
    data?: D,
    apiConfig?: AxiosRequestConfig<D>
  ): Promise<Response<T>> {
    // eslint-disable-next-line
    console.log("[PATCH]", url);
    return this.caller.patch(url, data, apiConfig);
  }
}

export const api = Api.getInstance();
