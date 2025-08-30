import React, { lazy } from "react";
import { Button, Form, Input } from "antd";
import { useTranslation } from "react-i18next";

import { Flex } from "@components";

const AuthLayout = lazy(() => import("@layouts/AuthLayout"));

export const ForgotPasswordPage: React.FC = () => {
  const { t } = useTranslation();

  return (
    <AuthLayout>
      <Form name='forgot' layout='vertical'>
        <Form.Item name='email'>
          <Input placeholder={t("email")} maxLength={100} />
        </Form.Item>
        <Flex center='vertical' justify='space-between'>
          <Button type='primary' htmlType='submit'>
            {t("reset")}
          </Button>
        </Flex>
      </Form>
    </AuthLayout>
  );
};
