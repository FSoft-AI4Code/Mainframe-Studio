import { Button, Result } from "antd";
import React from "react";
import { useTranslation } from "react-i18next";
import { useLocation, useNavigate } from "react-router-dom";

export const ServerErrorPage: React.FC = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const location = useLocation();
  const { message } = location.state || {};

  const onClick = () => navigate("/");

  return (
    <Result
      status='500'
      title='500'
      subTitle={message ? message : t("message.server_error")}
      extra={
        <Button onClick={onClick} type='primary'>
          {t("message.back_home")}
        </Button>
      }
    />
  );
};
