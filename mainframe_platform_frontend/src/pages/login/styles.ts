import styled from "@emotion/styled";
import { Form } from "antd";

export const Container = styled.div`
  display: flex;
  flex-direction: row;
  padding: 61px 48px;
  border-radius: 24px;
  background: ${({ theme }) => theme.colors.primary200};

  & > *:not(:last-child) {
    margin-right: 70px;
  }
`;

export const FigSide = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;

  & > *:not(:last-child) {
    margin-bottom: 18px;
  }
`;

export const FormSide = styled.div`
  display: flex;
  align-items: center;
  gap: 24px;

  form {
    width: 400px;
  }
`;

export const WrapFig = styled.div`
  padding: 24px;
  border-radius: 100px 33px 39px 12px;
  background: ${({ theme }) => theme.colors.primary100};
`;

export const FormItemSubmit = styled(Form.Item)`
  display: flex;
  justify-content: end;

  .login-form-button {
    background-color: ${({ theme }) => theme.allColors.primary6};
  }
`;
