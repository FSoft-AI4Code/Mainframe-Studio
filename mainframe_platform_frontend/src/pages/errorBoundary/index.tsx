/* eslint-disable no-console */
import React from "react";
import { ErrorBoundary as ErrorBoundaryProvider } from "react-error-boundary";

import FallbackRender from "./FallbackRender";

interface ErrorBoundaryProps {
  children: React.ReactNode;
}
const logError = (error: Error, info: { componentStack: string }) => {
  console.log("logError", { error, info });
  // Do something with the error, e.g. log to an external API
};
export default function ErrorBoundary({ children }: ErrorBoundaryProps) {
  return (
    <ErrorBoundaryProvider
      onReset={details => {
        console.log({ details });
        window.location.reload();
      }}
      onError={logError}
      fallbackRender={FallbackRender}
    >
      {children}
    </ErrorBoundaryProvider>
  );
}
