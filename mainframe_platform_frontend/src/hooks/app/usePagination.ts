import { useState } from "react";

interface Pagination {
  defaultPageSize?: number;
}
export function usePagination({ defaultPageSize = 10 }: Pagination) {
  const [pageSize, setPageSize] = useState(defaultPageSize);
  const handleChangeSize = (_: number, size: number) => setPageSize(size);
  return { pageSize, handleChangeSize };
}
