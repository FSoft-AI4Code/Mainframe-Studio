import { UIEventHandler, useRef, useState } from "react";
import { useDispatch } from "react-redux";
import { message } from "antd";

import { Pagination, PaginationQueries } from "@types";
import { DEFAULT_QUERIES } from "@defines";
import { queriesToString } from "@utils";

import { useDebounce } from "./useDebounce";

type Params<RecordType> = {
  fetch: (search: URLSearchParams) => Promise<Pagination<RecordType> | undefined>;
};

export const useInfiniteScroll = <RecordType extends object>(params: Params<RecordType>) => {
  const dispatch = useDispatch<AppDispatch>();
  const [loading, setLoading] = useState(true);
  const refQueries = useRef<PaginationQueries>(Object.assign({}, DEFAULT_QUERIES));
  const { debounce } = useDebounce();
  const [data, setData] = useState<Pagination<RecordType>>({
    items: null,
    pagination: { totalPages: 1, currentPage: 1, totalRecords: 1 }
  });

  const fetch = async () => {
    try {
      setLoading(true);
      const response = await params.fetch(queriesToString({ currentQueries: refQueries.current }));
      if (response && !data.items) setData(response);
      return response;
    } catch (error) {
      dispatch(
        message.error(
          error instanceof Error
            ? error.message
            : typeof error === "string"
            ? error
            : "error.unknow"
        )
      );
    } finally {
      setLoading(false);
    }
  };

  const init = () => {
    return debounce(async () => {
      refQueries.current = Object.assign({}, DEFAULT_QUERIES);
      const response = await fetch();
      if (response) setData(response);
      return response;
    });
  };

  const onScroll: UIEventHandler<HTMLElement> = async e => {
    const element = e.target as HTMLElement;
    if (
      !loading &&
      (element?.scrollTop || element?.offsetTop) + element.offsetHeight + 1 >=
        element.scrollHeight &&
      data.pagination.currentPage < data.pagination.totalPages
    ) {
      element.scrollTo(0, element.scrollHeight);
      refQueries.current.page++;
      const response = await fetch();
      if (response)
        setData(state => {
          return {
            items: [...(state.items || []), ...(response.items || [])],
            pagination: response.pagination
          };
        });
    }
  };

  return {
    data,
    loading,
    fetch,
    onScroll,
    init
  };
};
