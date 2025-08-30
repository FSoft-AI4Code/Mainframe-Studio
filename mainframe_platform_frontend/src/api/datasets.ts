import queryString from "query-string";

import {
  AvailableFilterParams,
  AvailableFilterResponse,
  DatasetResponse,
  DatasetsInput,
  ExportDatasetsInput,
  StatisticDatasetsResponse
} from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class DatasetsApi {
  static getDatasets = (params: DatasetsInput) => {
    const queryStr = queryString.stringify(params, { skipEmptyString: true, skipNull: true });
    return HttpClient.get<DatasetResponse>(`${API_ENPOINTS.DATASETS}?${queryStr}`);
  };

  static getStatisticDatasets = (params: DatasetsInput) => {
    const queryStr = queryString.stringify(params, { skipEmptyString: true, skipNull: true });
    return HttpClient.get<StatisticDatasetsResponse>(
      `${API_ENPOINTS.DATASETS_STATISTIC}?${queryStr}`
    );
  };

  static exportDataset = (params: ExportDatasetsInput) => {
    const queryStr = queryString.stringify(params, { skipEmptyString: true, skipNull: true });
    return HttpClient.get<StatisticDatasetsResponse>(`${API_ENPOINTS.DATASETS_EXPORT}?${queryStr}`);
  };

  static getListAvailabeFilterDataset = (params: AvailableFilterParams) => {
    return HttpClient.get<AvailableFilterResponse>(
      `${API_ENPOINTS.DATASETS_AVAILABLE_FILTER}`,
      params
    );
  };
}
