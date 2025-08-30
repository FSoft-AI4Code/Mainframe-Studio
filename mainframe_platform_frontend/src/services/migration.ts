import { useMutation, useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, migrationApi } from "@api";
import { MigrationFileContentQuery, MigrationStructureQuery, MigrationTriggerQuery } from "@types";
import { exportDataToZipFile, handleErrorMessage } from "@utils";

export const useStructureMigrationQuery = ({
  enabled = true,
  ...params
}: MigrationStructureQuery) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [API_ENPOINTS.MIGRATION_STRUCTURE, params],
    queryFn: () => migrationApi.getRepositoryStructure(params),
    enabled: !!params.bms_file_name && !!params.repository_id && enabled
  });
  return {
    bmsFileName: data?.bms_file_name,
    repositoryId: data?.repository_id,
    migrationStructure: data?.structure,
    loading: isLoading,
    refetch
  };
};
export const useFileContentQuery = (params: MigrationFileContentQuery) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [API_ENPOINTS.MIGRATION_FILE_CONTENT, params],
    queryFn: () => migrationApi.getFileContent(params),
    enabled: !!params.bms_file_name && !!params.repository_id && !!params.file_path
  });

  return {
    fileContent: data?.content,
    filePath: data?.file_path,
    loading: isLoading,
    refetch
  };
};

export const useTriggerBmsMigration = () =>
  useMutation({
    mutationFn: migrationApi.triggerBmsMigration
  });

export const useTriggerBmsMigrationQuery = ({
  enabled = true,
  ...params
}: MigrationTriggerQuery & { enabled?: boolean }) => {
  return useQuery({
    queryKey: [API_ENPOINTS.MIGRATION_BMS, params.bms_file_name, params.repository_id],
    queryFn: () => migrationApi.triggerBmsMigration(params),
    enabled: !!params.bms_file_name && !!params.repository_id && enabled
  });
};

export const useDownloadMigrationMutation = () =>
  useMutation({
    mutationFn: migrationApi.downloadMigration,
    onSuccess(data) {
      exportDataToZipFile(data as BlobPart, "migrations");
    },
    onError(error) {
      handleErrorMessage(error, { show: true });
    }
  });
