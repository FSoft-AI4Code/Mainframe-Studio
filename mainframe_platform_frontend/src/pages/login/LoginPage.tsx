import { Button, Form, Input } from "antd";
import { lazy } from "react";
import { useTranslation } from "react-i18next";

import { LoginParams } from "@types";
import { FrameCoverSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { useLogin } from "@hooks";

import { FormItemSubmit, FormSide } from "./styles";

const AuthLayout = lazy(() => import("@layouts/AuthLayout"));

const LabelInput = ({ label }: { label: string }) => (
  <Typography color='primary10' level='body-14m'>
    {label}
  </Typography>
);

export const LoginPage = () => {
  const { t } = useTranslation();

  const { handleLogin, loading } = useLogin();

  const onClickLogin = (values: LoginParams) => {
    handleLogin(values);
  };

  return (
    <AuthLayout>
      <Flex
        style={{
          padding: 52,
          borderRadius: "16px",
          backgroundColor: "rgba(255, 255, 255, 0.5)",
          boxShadow: "0px 8px 16px 0px rgba(1, 12, 27, 0.1)"
        }}
        gap={52}
      >
        <Flex direction='column' gap={18} align='center'>
          <Typography level='h3s'>{t("page.signin.title")}</Typography>
          <FrameCoverSvg />
        </Flex>
        <FormSide>
          <Form
            name='normal_login'
            className='login-form'
            layout='vertical'
            initialValues={{
              remember: true
            }}
            onFinish={(values: LoginParams) => {
              // eslint-disable-next-line
              console.log("Received values of form: ", values);

              onClickLogin(values);
            }}
            style={{
              display: "flex",
              flexDirection: "column",
              gap: 24,
              justifyContent: "center"
            }}
            // onKeyUp={handleKeyUp}
          >
            <Form.Item name='username' label={<LabelInput label={t("email")} />}>
              <Input placeholder={t("your_email")} type='username' required />
            </Form.Item>
            <Form.Item name='password' label={<LabelInput label={t("password")} />}>
              <Input type='password' placeholder={t("your_password")} required />
            </Form.Item>

            <FormItemSubmit>
              <Button
                loading={loading}
                disabled={loading}
                type='primary'
                htmlType='submit'
                className='login-form-button'
              >
                <Typography color='neutral1' level='body-16m'>
                  {t("sign_in")}
                </Typography>
              </Button>
            </FormItemSubmit>
          </Form>
        </FormSide>
      </Flex>
    </AuthLayout>
  );
};
