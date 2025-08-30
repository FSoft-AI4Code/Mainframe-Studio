import React, { lazy } from "react";
import { Button, Checkbox, Form, Input } from "antd";
import { useTranslation } from "react-i18next";

const AuthLayout = lazy(() => import("@layouts/AuthLayout"));

export const RegisterPage: React.FC = () => {
  const { t } = useTranslation();

  return (
    <AuthLayout>
      <Form name='register' layout='vertical'>
        <Form.Item name='name' validateFirst>
          <Input placeholder={t("your_name")} maxLength={100} />
        </Form.Item>
        <Form.Item name='email' validateFirst>
          <Input placeholder={t("your_email")} maxLength={100} />
        </Form.Item>
        <Form.Item name='password' required validateFirst>
          <Input.Password placeholder={t("your_password")} maxLength={20} />
        </Form.Item>
        <Form.Item dependencies={["password"]} name='confirmPassword' validateFirst>
          <Input.Password placeholder={t("re_enter_password")} maxLength={20} />
        </Form.Item>
        <Form.Item name='agreeAllTheTerm' valuePropName='checked' validateFirst>
          <Checkbox>{t("message.agreee_term_policy")}</Checkbox>
        </Form.Item>
        <Form.Item>
          <Button type='primary' htmlType='submit'>
            {t("create_account")}
          </Button>
        </Form.Item>
      </Form>
    </AuthLayout>
  );
};
