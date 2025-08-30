import { useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, chatApi } from "@api";

export const useGetChatProject = ({
  projectId,
  enabled = true
}: {
  projectId: string;
  enabled?: boolean;
}) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.CHAT_PROJECTS, projectId],
    queryFn: () => chatApi.getChatProject(projectId),
    enabled: !!projectId && enabled
  });
  return { chatProject: data?.data, isLoading };
};
