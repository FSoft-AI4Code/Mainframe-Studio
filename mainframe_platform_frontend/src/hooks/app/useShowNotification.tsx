import { CheckOutlined, LoadingOutlined } from "@ant-design/icons";
import styled from "@emotion/styled";
import { notification } from "antd";
import { useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";

import { appActions, appSelector } from "@store";

const Wrapper = styled.div`
  display: flex;

  & > *:not(:last-child) {
    margin-right: 10px;
  }
`;

const WrapperIcon = styled.div``;

const WrapperContent = styled.div``;

const KEY = "notification";

export const useShowNotification = () => {
  const dispatch = useDispatch();
  const notificationData = useSelector(appSelector.selectNotificationData);
  const refTimeout = useRef<NodeJS.Timeout>();
  const [api, contextHolder] = notification.useNotification();

  const clearTimeRefTimeout = () => {
    if (refTimeout.current) {
      clearTimeout(refTimeout.current);
      refTimeout.current = undefined;
    }
  };

  useEffect(() => {
    if (notificationData)
      api.open({
        message: (
          <Wrapper>
            {notificationData.type && (
              <WrapperIcon>
                {notificationData.type === "pending" ? <LoadingOutlined /> : <CheckOutlined />}
              </WrapperIcon>
            )}
            <WrapperContent>{notificationData.message}</WrapperContent>
          </Wrapper>
        ),
        placement: "bottomRight",
        role: "status",
        duration: -1,
        key: KEY,
        className: "cobol-notification",
        closeIcon: false
      });
    else api.destroy(KEY);
  }, [notificationData]);

  useEffect(() => {
    clearTimeRefTimeout();
    if (notificationData?.timeout) {
      refTimeout.current = setTimeout(() => {
        clearTimeRefTimeout();
        dispatch(appActions.setNotificationData());
      }, notificationData.timeout);
    }
  }, [notificationData?.timeout]);

  return contextHolder;
};
