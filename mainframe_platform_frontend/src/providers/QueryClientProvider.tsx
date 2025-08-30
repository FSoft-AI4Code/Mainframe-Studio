import { QueryClient, QueryClientProvider as QueryProvider } from "@tanstack/react-query";
import { PropsWithChildren } from "react";

const queryClient = new QueryClient({
  defaultOptions: { queries: { retry: 1, refetchOnWindowFocus: false } }
});

export function QueryClientProvider({ children }: PropsWithChildren) {
  return <QueryProvider client={queryClient}>{children}</QueryProvider>;
}
