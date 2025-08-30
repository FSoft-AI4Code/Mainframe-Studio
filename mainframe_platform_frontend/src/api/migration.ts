import queryString from "query-string";

import {
  MigrationDownloadQuery,
  MigrationFileContentData,
  MigrationFileContentQuery,
  MigrationStructureQuery,
  MigrationStructureResponse,
  MigrationTriggerQuery
} from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class MigrationApi {
  static getRepositoryStructure = ({ repository_id, ...params }: MigrationStructureQuery) => {
    const queryStr = queryString.stringify(params, { skipEmptyString: true, skipNull: true });
    return HttpClient.get<MigrationStructureResponse>(
      `${API_ENPOINTS.MIGRATION_STRUCTURE}/${repository_id}?${queryStr}`
    );
  };

  static getFileContent = ({ repository_id, ...params }: MigrationFileContentQuery) => {
    const queryStr = queryString.stringify(params, { skipEmptyString: true, skipNull: true });
    return HttpClient.get<MigrationFileContentData>(
      `${API_ENPOINTS.MIGRATION_FILE_CONTENT}/${repository_id}?${queryStr}`
    );
  };

  static triggerBmsMigration = ({ repository_id, bms_file_name }: MigrationTriggerQuery) => {
    return HttpClient.post(`${API_ENPOINTS.MIGRATION_BMS}/${repository_id}/${bms_file_name}`, {});
  };

  static downloadMigration = ({ repository_id, ...params }: MigrationDownloadQuery) => {
    const queryStr = queryString.stringify(params, { skipEmptyString: true, skipNull: true });

    return HttpClient.get(`${API_ENPOINTS.MIGRATION_DOWNLOAD}/${repository_id}?${queryStr}`, null, {
      responseType: "blob"
    });
  };
}
