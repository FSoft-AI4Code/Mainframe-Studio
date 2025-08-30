import { useRef } from "react";

export const useDebounce = (options?: { timeout?: number }) => {
  const refTimeout = useRef<NodeJS.Timeout>();

  const clearRefTimeout = () => {
    if (refTimeout.current) {
      clearTimeout(refTimeout.current);
      refTimeout.current = undefined;
    }
  };

  const debounce = <RecordType>(handle: () => Promise<RecordType>): Promise<RecordType> => {
    clearRefTimeout();
    return new Promise<RecordType>(res => {
      refTimeout.current = setTimeout(async () => {
        const response = await handle();
        clearRefTimeout();
        res(response);
      }, options?.timeout || 500);
    });
  };

  return {
    debounce
  };
};
