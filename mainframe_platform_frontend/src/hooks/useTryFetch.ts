import { useRef } from "react";

export function useTryFetch() {
  const refQueue = useRef<NodeJS.Timeout>();

  const clearRefQueue = () => {
    if (refQueue.current) {
      clearTimeout(refQueue.current);
      refQueue.current = undefined;
    }
  };

  const tryFetch = async (handle: () => Promise<void>, options?: { time?: number }) => {
    let success = true;

    try {
      await handle();
    } catch (error: any) {
      if (error?.response?.status !== 401) success = false;
      // eslint-disable-next-line no-console
      console.error(error);
    } finally {
      if (success) return;

      clearRefQueue();
      refQueue.current = setTimeout(() => {
        clearRefQueue();
        tryFetch(handle, options);
      }, options?.time || 1000);
    }
  };

  return { tryFetch, clearRefQueue };
}
