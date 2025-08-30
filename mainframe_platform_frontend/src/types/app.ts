import { RESPONSE_CODE } from "@defines";

export type Response<ResBody> = {
  message: RESPONSE_CODE;
  data: ResBody;
};
