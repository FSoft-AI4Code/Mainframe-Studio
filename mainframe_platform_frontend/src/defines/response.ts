/*eslint-disable */
export enum RESPONSE_CODE {
  INTERNAL_SERVER_ERROR = 50000
}

export const RESPONSE_MESSAGE: Record<string, string> = {
  [RESPONSE_CODE.INTERNAL_SERVER_ERROR]: "response_code.internal_server_error"
};
/* eslint-enable */
