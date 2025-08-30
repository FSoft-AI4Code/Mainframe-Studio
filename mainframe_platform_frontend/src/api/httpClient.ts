import { message as messageApi } from "antd";
import axios, { AxiosError, AxiosRequestConfig, AxiosResponse, HttpStatusCode } from "axios";

import { backendURL } from "@configs";
import {
  ErrorResolverBackEndDataType,
  getAuthToken,
  redirectToLogin,
  removeAuthToken
} from "@utils";

import { API_ENPOINTS } from "./endpoints";

function handleSuccessResponse(response: AxiosResponse) {
  return response;
}
function handleError(error: AxiosError<ErrorResolverBackEndDataType, unknown>) {
  if (error.response && error.response.status === HttpStatusCode.Unauthorized) {
    if (!API_ENPOINTS.LOGIN.includes(error?.response.config.url as string)) {
      messageApi.error((error?.response?.data?.detail as string) || "Unauthenticated user");
      removeAuthToken();
      redirectToLogin();
    }
  }
  return Promise.reject(error);
}

const Axios = axios.create({
  baseURL: backendURL,
  timeout: 1000 * 60 * 5,
  headers: {
    "Content-Type": "application/json"
  }
});
Axios.interceptors.request.use(
  config => {
    const token = getAuthToken();
    if (token) config.headers.Authorization = `Bearer ${token}`;
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

Axios.interceptors.response.use(handleSuccessResponse, handleError);

export class HttpClient {
  static async get<T>(url: string, params?: unknown, options?: AxiosRequestConfig) {
    const response = await Axios.get<T>(url, { params, ...options });
    return response.data;
  }

  static async post<T>(url: string, data: unknown, options?: AxiosRequestConfig) {
    const response = await Axios.post<T>(url, data, options);
    return response.data;
  }

  static async put<T>(url: string, data: unknown) {
    const response = await Axios.put<T>(url, data);
    return response.data;
  }

  static async delete<T>(url: string) {
    const response = await Axios.delete<T>(url);
    return response.data;
  }
}
