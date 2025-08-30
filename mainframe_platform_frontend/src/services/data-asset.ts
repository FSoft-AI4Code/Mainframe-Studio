import { useQuery } from "@tanstack/react-query";

import { dataAssetApi } from "@api";

export const useGetDataAssets = ({ repoId }: { repoId: string }) => {
  const { data, isLoading } = useQuery({
    queryKey: ["get-data-asesets"],
    queryFn: () => dataAssetApi.getDataAsset(),
    enabled: !!repoId
  });
  return {
    dataAsesets: data ?? [],
    isLoading
  };
};
