/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable unused-imports/no-unused-vars */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { AxiosError } from "axios";
import { useTranslation } from "react-i18next";
import { message as messageApi } from "antd";

import { RESPONSE_CODE, RESPONSE_MESSAGE } from "@defines";
import { useLogout } from "@services";

type Handle<T = unknown> = () => Promise<T>;

type Options = {
  onLoading?: (value: boolean) => void;
  onSuccess?: () => void;
  onError?: (error: unknown) => void;
  onDone?: () => void;
  notice?: {
    show?: boolean;
    ignoreCodes?: number[];
    fallbackMessage: string;
  };
};

export const useController = () => {
  const { mutate: logout } = useLogout();
  const { t } = useTranslation();

  const navigateUnauthen = (error: any) => {
    messageApi.error(error?.response?.data?.detail || t("error.unauthorized"));
    logout();
  };

  const controller = async <T = unknown>(
    handle: Handle<T>,
    options?: Options
  ): Promise<T | undefined> => {
    const { notice: noticeOptions, onDone, onSuccess, onError, onLoading } = options || {};
    const isShowNotice = noticeOptions?.show || false;
    const fallbackMessage = noticeOptions?.fallbackMessage;
    const noticeIgnoreCode = noticeOptions?.ignoreCodes || [];
    let result: T | undefined;

    try {
      if (onLoading) onLoading(true);
      result = await handle();
      if (onSuccess) onSuccess();
    } catch (error) {
      if (onError) onError(error);

      if (error instanceof AxiosError) {
        const { response } = error;
        // eslint-disable-next-line
        const status: number | undefined = response?.status;
        // eslint-disable-next-line
        const resCode: RESPONSE_CODE = response?.data?.message;
        debugger;
        if (
          status === 401
          // && token
          // || resCode === RESPONSE_CODE.TOKEN_EXPIRIED
        ) {
          navigateUnauthen(error);
          return;
        }
      }
      if (isShowNotice !== false) {
        let message = "";
        if (error instanceof AxiosError) {
          const errorCode = error?.response?.data?.message;
          // eslint-disable-next-line no-console
          const status: number | undefined = error?.response?.status;
          const messageResponse = (RESPONSE_MESSAGE as any)[errorCode];

          if (!errorCode || !noticeIgnoreCode?.includes(errorCode)) {
            if (errorCode && messageResponse) message = t(messageResponse);
            else if (status === 401) message = t("error.unauthorized");
            else message = error.message;
          }
          const detail = (error?.response?.data as any)?.detail;
          if (detail) {
            if (typeof detail === "string") message = detail;
            if (typeof detail === "object") message = detail?.message;
          }
        } else if (fallbackMessage) {
          message = fallbackMessage;
        } else if (error instanceof Error) {
          message = error.message;
        } else if (typeof error === "string") {
          message = error;
        } else message = t("unknow_error");
        if (message) messageApi.error(message);
      }
    } finally {
      if (onLoading) onLoading(false);
      if (onDone) onDone();
    }

    return result;
  };

  return { controller, navigateUnauthen };
};
