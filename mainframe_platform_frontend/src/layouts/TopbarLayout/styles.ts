import styled from "@emotion/styled";
import { Button, Layout, Progress as ProgressUI } from "antd";

export const Container = styled(Layout)`
  height: 100vh;
  overflow: hidden;

  .container-chart-search .wrap-button {
    width: 0 !important;
    margin: 0 !important;
    .ant-btn {
      opacity: 0;
    }
  }
`;

export const ButtonBack = styled(Button)``;

export const Progress = styled(ProgressUI)`
  margin: 0;
  padding: 0;
  line-height: 0;
`;
