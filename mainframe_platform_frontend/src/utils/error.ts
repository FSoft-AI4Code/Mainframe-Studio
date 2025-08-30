/* eslint-disable @typescript-eslint/no-non-null-assertion */
import { AxiosError, HttpStatusCode } from "axios";
import { message as messageApi } from "antd";

export type ErrorResolverBackEndDataType = {
  detail?: string | Record<string, string>;
};

export type ErrorResolverBackEndType = {
  code: number;
  detail: string;
};

export type ResolvePromiseOptions = {
  show?: boolean;
  fallbackMessage?: string;
  ignoreCodes?: number[];
};

export const getErrorMessage = (
  detail: string | Record<string, string>,
  statusText: string
): string => {
  if (typeof detail === "string") return detail;
  if (Array.isArray(detail)) return detail?.[0]?.msg || statusText;
  if (detail && typeof detail === "object") return detail?.message || statusText;
  return statusText;
};

export const resolveErrorBackEnd = (
  error: AxiosError<ErrorResolverBackEndDataType>,
  options: ResolvePromiseOptions = {}
): ErrorResolverBackEndType => {
  const errorCode = error?.response?.status;
  if (options?.ignoreCodes?.includes(errorCode!)) {
    return { code: errorCode!, detail: "" };
  }
  if (error?.response) {
    const detail = error?.response?.data.detail;
    return {
      code: error?.response?.status,
      detail: getErrorMessage(detail!, error?.response?.statusText)
    };
  } else if (error?.request) {
    return {
      code: HttpStatusCode.InternalServerError,
      detail: "The request was made but no response was received"
    };
  } else {
    return {
      code: HttpStatusCode.InternalServerError,
      detail: "Something happened in setting up the request"
    };
  }
};

export const showErrorMessage = (
  errorDetail: ErrorResolverBackEndType,
  options: ResolvePromiseOptions
) => {
  if (options.show !== false && errorDetail.detail) {
    messageApi.error({
      content: errorDetail.detail
    });
  }
};

export const handleErrorMessage = (
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  error: AxiosError<ErrorResolverBackEndDataType> | any,
  options: ResolvePromiseOptions
) => {
  if (error.isAxiosError) {
    debugger;
  }
  const errorDetail = resolveErrorBackEnd(error, options);
  // eslint-disable-next-line no-console
  console.log({ errorDetail, error });
  showErrorMessage(errorDetail, options);
};
