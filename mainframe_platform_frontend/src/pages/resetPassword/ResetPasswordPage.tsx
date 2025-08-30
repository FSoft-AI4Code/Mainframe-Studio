import React, { lazy } from "react";
import { Button, Form, Input } from "antd";

import { Flex } from "@components";
const AuthLayout = lazy(() => import("@layouts/AuthLayout"));

export const ResetPasswordPage: React.FC = () => {
  return (
    <AuthLayout>
      <Form layout='vertical'>
        <Form.Item name='password' label='New Password' validateFirst>
          <Input.Password placeholder='Your New Password' maxLength={20} />
        </Form.Item>
        <Form.Item name='confirm-password' label='Re- Enter Password' validateFirst>
          <Input.Password placeholder='Confirm Password' maxLength={20} />
        </Form.Item>
        <Flex justify='flex-end'>
          <Button htmlType='submit'>Submit</Button>
        </Flex>
      </Form>
    </AuthLayout>
  );
};
