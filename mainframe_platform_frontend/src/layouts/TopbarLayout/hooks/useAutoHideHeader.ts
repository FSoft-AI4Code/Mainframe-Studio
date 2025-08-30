import { MouseEventHandler, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { appActions, appSelector } from "@store";

import { HEADER_HEIGHT } from "../config";

export type UseAutoHideHeaderProps = {
  autoHide?: boolean;
};

export const useAutoHideHeader = ({ autoHide }: UseAutoHideHeaderProps) => {
  const dispatch = useDispatch();
  const show = useSelector(appSelector.isTopBarShow);

  const setShow = (v: boolean) => dispatch(appActions.setTopBarShow(v));

  const onMouseMove: MouseEventHandler<HTMLDivElement> = e => {
    if (autoHide) {
      if (e.clientY <= HEADER_HEIGHT * 0.3) {
        if (!show) setShow(true);
      } else if (e.clientY > HEADER_HEIGHT * 2.5) {
        if (show) setShow(false);
      }
    }
  };

  useEffect(() => {
    setShow(autoHide ? false : true);
  }, [autoHide]);

  useEffect(() => {
    if (!show && !autoHide) setShow(true);
  }, [autoHide, show]);

  return { show, onMouseMove };
};
