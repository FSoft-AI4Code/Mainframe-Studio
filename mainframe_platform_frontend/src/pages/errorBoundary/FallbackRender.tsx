/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable no-console */
import { Button } from "antd";
import type { FallbackProps } from "react-error-boundary";

import { Flex, Typography } from "@components";

export default function FallbackRender({ error, resetErrorBoundary }: FallbackProps) {
  console.log("fallback-render-error", error);
  return (
    <Flex
      direction='column'
      style={{
        justifyContent: "center",
        alignItems: "center",
        minHeight: "100vh"
      }}
    >
      <Typography level='h2' color={"primary1"} style={{ margin: 50 }}>
        Something went wrong!!!
      </Typography>
      <Typography level='h2' color={"primary1"} style={{ margin: 50 }}>
        {error.message}
      </Typography>
      <Flex gap={8}>
        <Button
          type='primary'
          onClick={() => {
            window.location.href = "/";
          }}
        >
          Back Home
        </Button>
        <Button type='primary' onClick={resetErrorBoundary}>
          Reload Page
        </Button>
      </Flex>
    </Flex>
  );
}
