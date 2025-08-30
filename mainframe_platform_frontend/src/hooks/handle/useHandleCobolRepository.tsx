import { useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";

import { storage } from "@defines";
import {
  migrationRepositoryActions,
  repositoryActions,
  repositorySelector,
  userSelector
} from "@store";

export const useHandleCobolRepository = () => {
  // const refQueue = useRef<NodeJS.Timeout>();
  // const { t } = useTranslation();
  const dispatch = useDispatch();
  const refId = useRef<string>();
  // const repositoryData = useSelector(repositorySelector.selectRepositoryData);
  const repositoryId = useSelector(repositorySelector.selectRepositoryId);
  // const treeView = useSelector(repositorySelector.selectRepositoryTreeView);
  // const copyGraph = useSelector(repositorySelector.selectRepositoryCopyGraph);
  // const cluster = useSelector(repositorySelector.selectRepositoryCluster);
  // const done = useSelector(repositorySelector.selectRepositoryDone);
  // const complexity = useSelector(repositorySelector.selectComplexity);
  const userData = useSelector(userSelector.selectData);
  // const token = localStorage.getItem(storage.TOKEN);
  // const { navigateUnauthen } = useController();

  // const clearRefQueue = () => {
  //   if (refQueue.current) {
  //     clearTimeout(refQueue.current);
  //     refQueue.current = undefined;
  //   }
  // };

  const initialize = () => {
    const repo = localStorage.getItem(storage.REPO);
    dispatch(repositoryActions.setRepositoryData(repo ? JSON.parse(repo) : undefined));
    const migrationRepo = localStorage.getItem(storage.MIGRATION_REPO);
    dispatch(
      migrationRepositoryActions.setMigrationRepositoryData(
        migrationRepo ? JSON.parse(migrationRepo) : undefined
      )
    );
  };

  // const tryFetch = async (handle: () => Promise<void>, options?: { time?: number }) => {
  //   let success = false;
  //   try {
  //     await handle();
  //     success = true;
  //   } catch (error: any) {
  //     if (error?.response?.status === 401) {
  //       success = true;
  //       navigateUnauthen(error);
  //     }
  //     // eslint-disable-next-line no-console
  //     console.log(error);
  //   } finally {
  //     if (!success) {
  //       clearRefQueue();
  //       refQueue.current = setTimeout(() => {
  //         clearRefQueue();
  //         tryFetch(handle, options);
  //       }, options?.time || 1000);
  //     }
  //   }
  // };

  // const fetchFileDetailRequest = (id: string) => {
  //   tryFetch(async () => {
  //     const res = (await repositoryApi.getRepositoryRequest(id)) as any as RepoModel;
  //     if (res.tree_view) {
  //       dispatch(repositoryActions.setTreeView(res.tree_view));
  //       if (!done) {
  //         dispatch(
  //           appActions.setNotificationData({
  //             message: "Network Diagram initialization in progress.",
  //             type: "pending"
  //           })
  //         );
  //       }
  //     } else throw new Error();
  //   });
  // };

  // const fetchNetworkingGraph = async (id: string) => {
  //   tryFetch(
  //     async () => {
  //       const res = await repositoryApi.getGraphChartDataRequest(id);
  //       if (res.data) {
  //         dispatch(repositoryActions.setCopyGraph(res.data));
  //         if (!done) {
  //           dispatch(
  //             appActions.setNotificationData({
  //               message: "Graph Clustering initialization in progress.",
  //               type: "pending"
  //             })
  //           );
  //         }
  //       } else throw new Error();
  //     },
  //     { time: 5000 }
  //   );
  // };

  // const fetchScatterPlotGraph = async (id: string) => {
  //   tryFetch(
  //     async () => {
  //       const res = await repositoryApi.getClusterChartDataRequest(id);
  //       if (res.data) {
  //         dispatch(repositoryActions.setClusters(res.data));
  //         if (!done) {
  //           dispatch(
  //             appActions.setNotificationData({
  //               message: "Graph Clustering initialized successfully.",
  //               type: "pending",
  //               timeout: 5000
  //             })
  //           );
  //         }
  //       } else throw new Error();
  //     },
  //     { time: 5000 }
  //   );
  // };

  useEffect(() => {
    initialize();
  }, [userData]);

  useEffect(() => {
    refId.current = repositoryId;
  }, [repositoryId]);

  // useEffect(() => {
  //   if (!done && repositoryId)
  //     dispatch(
  //       appActions.setNotificationData({
  //         message: t("notification.git_in_progress"),
  //         type: "pending",
  //         timeout: 5000
  //       })
  //     );
  // }, [repositoryId]);

  // useEffect(() => {
  //   if (!treeView && repositoryId) fetchFileDetailRequest(repositoryId);
  // }, [treeView, repositoryId]);

  // useEffect(() => {
  //   if (treeView && !copyGraph && repositoryId && token) fetchNetworkingGraph(repositoryId);
  // }, [repositoryId, treeView]);

  // useEffect(() => {
  //   if (copyGraph && !cluster && refId.current) fetchScatterPlotGraph(refId.current);
  // }, [copyGraph, cluster]);

  // const fetchComplexityRequest = async () => {
  //   tryFetch(
  //     async () => {
  //       const res = await repositoryApi.getComplexityDataRequest(String(repositoryId));
  //       if (res.data) {
  //         dispatch(repositoryActions.setComplexity(res?.data));
  //       } else throw new Error();
  //     },
  //     { time: 5000 }
  //   );
  // };

  // useEffect(() => {
  //   if (!complexity && repositoryId && done && token) fetchComplexityRequest();
  // }, [complexity, repositoryId, userData, done]);

  // useEffect(() => {
  //   if (treeView && copyGraph && cluster && !done) {
  //     // eslint-disable-next-line @typescript-eslint/naming-convention
  //     const { copy_graph, tree_view, clusters, ...storageData } = repositoryData;
  //     localStorage.setItem(storage.REPO, JSON.stringify({ ...storageData, done: true }));
  //     dispatch(
  //       appActions.setNotificationData({
  //         message: t("notification.all_done"),
  //         type: "success",
  //         timeout: 5000
  //       })
  //     );
  //   }
  // }, [treeView, copyGraph, cluster, repositoryData, done]);
};
