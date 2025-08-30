import React from "react";
import { Button, Result } from "antd";
import { useLocation, useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";

export const NotFoundPage: React.FC = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const location = useLocation();
  const { message } = location.state || {};

  const onClick = () => navigate("/");

  return (
    <Result
      status='404'
      title='404'
      subTitle={message ? message : t("message.not_found")}
      extra={
        <Button onClick={onClick} type='primary'>
          {t("back_home")}
        </Button>
      }
    />
  );
};
