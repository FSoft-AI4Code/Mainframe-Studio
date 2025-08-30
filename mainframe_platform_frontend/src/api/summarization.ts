import { ModernizationInput, ModernizationResponse, SummarizationBmsInput } from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class SummarizationApi {
  static inferenceModernization = (params: ModernizationInput) => {
    return HttpClient.post<ModernizationResponse>(API_ENPOINTS.INFERENCE_MODERNIZATION, params);
  };

  static striggerSummarizationBMS = ({ repository_id, file_name }: SummarizationBmsInput) => {
    return HttpClient.post<ModernizationResponse>(
      `${API_ENPOINTS.SUMMARIZATION_BMS}/${repository_id}/files/${file_name}`,
      {}
    );
  };
}
