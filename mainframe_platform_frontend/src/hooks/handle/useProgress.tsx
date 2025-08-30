import styled from "@emotion/styled";
import { ProgressProps, Progress as ProgressUI } from "antd";
import { useEffect, useRef, useState } from "react";
import { useSelector } from "react-redux";

import { repositorySelector } from "@store";

export const Progress = styled(ProgressUI)`
  margin: 0;
  padding: 0;
  line-height: 0;
`;

export const useProgress = (): ProgressProps | undefined => {
  const refTimeout = useRef<NodeJS.Timeout>();

  const repositoryId = useSelector(repositorySelector.selectRepositoryId);
  const treeView = useSelector(repositorySelector.selectRepositoryTreeView);
  const copyGraph = useSelector(repositorySelector.selectRepositoryCopyGraph);
  const cluster = useSelector(repositorySelector.selectRepositoryCluster);
  const [percent, setPercent] = useState<number>();
  const [percentLive, setPercentLive] = useState<number>();

  const clearRefTimeout = () => {
    if (refTimeout.current) {
      clearTimeout(refTimeout.current);
      refTimeout.current = undefined;
    }
  };

  const caculatePercent = () => {
    const totalTask = [treeView, copyGraph, cluster, repositoryId];
    const doneTask = totalTask.filter(o => o);
    const percentValue = (doneTask.length / totalTask.length) * 100;
    const percentNext =
      ((percentValue < 100 ? doneTask.length + 1 : totalTask.length) / totalTask.length) * 100 -
      (percentValue < 100 ? 1 : 0);
    return { percentValue, percentNext };
  };

  useEffect(() => {
    const { percentValue } = caculatePercent();
    if (percentValue === 100) setPercentLive(undefined);
    else setPercentLive(0);
  }, []);

  useEffect(() => {
    const { percentNext } = caculatePercent();
    setPercent(percentNext);
  }, [treeView, copyGraph, cluster, repositoryId]);

  useEffect(() => {
    clearRefTimeout();
    if (typeof percentLive !== "number" || typeof percent !== "number" || percentLive === percent)
      return;
    const sub = percent - percentLive;
    if (Math.abs(sub) < 0.02) {
      if (percent !== 100) setPercentLive(percent);
      else setPercentLive(undefined);
    } else {
      refTimeout.current = setTimeout(() => {
        clearRefTimeout();
        setPercentLive(percentLive + sub / 20);
      }, 1000 / 30);
    }
  }, [percent, percentLive]);

  return percentLive ? { percent: percentLive } : undefined;
};
