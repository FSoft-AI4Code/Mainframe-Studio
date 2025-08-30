/* eslint-disable @typescript-eslint/no-explicit-any */
import { DEFAULT_QUERIES, ROUTERS } from "@defines";
import { PaginationQueries, PaginationSortItem } from "@types";

export const queriesToString = (options?: {
  defaultQueries?: boolean;
  currentQueries?: PaginationQueries;
}) => {
  const search = new URLSearchParams();
  const queries =
    options?.defaultQueries || !options?.currentQueries ? DEFAULT_QUERIES : options.currentQueries;
  Object.keys(queries).forEach(o => {
    const value = queries[o as keyof typeof queries];
    if (o === "sort") {
      if (
        typeof value === "object" &&
        Array.isArray(value) &&
        (value as PaginationSortItem[]).length
      ) {
        const sortItems = value as PaginationSortItem[];
        const sortString = [...sortItems].map(oo => `${oo.field},${oo.sort}`).join("|");
        search.append("sort", sortString);
      }
    } else if (o === "keyword") {
      if (value) search.append("keyword", value?.toString().trim().toLowerCase());
    } else if (o === "page") {
      search.append("page", (value + 1)?.toString());
    } else search.append(o, value?.toString());
  });
  return search;
};
export const getQueryParam = (param: string) => {
  const search = new URLSearchParams(location.search);
  return search.get(param);
};

export function generateUUID() {
  let dt = new Date().getTime();
  const uuid = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, c => {
    const r = (dt + Math.random() * 16) % 16 | 0;
    dt = Math.floor(dt / 16);
    return (c == "x" ? r : (r & 0x3) | 0x8).toString(16);
  });
  return uuid;
}

export const setFullScreen = (params?: { fullScreen?: boolean; elementId?: string }) => {
  const { elementId, fullScreen } = params || {};
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const elem: any = elementId ? document.getElementById(elementId) : document.documentElement;
  if (!elem) return;

  if (fullScreen !== false) {
    if (elem.requestFullscreen) {
      elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) {
      /* Safari */
      elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) {
      /* IE11 */
      elem.msRequestFullscreen();
    }
  } else if (document.fullscreenElement) {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if ((document as any).webkitExitFullscreen) {
      /* Safari */
      (document as any).webkitExitFullscreen();
    } else if ((document as any).msExitFullscreen) {
      /* IE11 */
      (document as any).msExitFullscreen();
    }
  }
};

export const roundToDecimalPlaces = (num: number, decimalPlaces: number) => {
  if (!num || !decimalPlaces) {
    return 0;
  }
  const factor = Math.pow(10, decimalPlaces);
  return Math.round(num * factor) / factor;
};

export const handleDownloadFile = (data: Blob, fileName?: string) => {
  const link = document.createElement("a");

  // Create a Blob URL for the downloaded file
  const blobUrl = URL.createObjectURL(data);

  // Set the link's href attribute to the Blob URL
  link.href = blobUrl;

  // Specify the suggested name for the file
  link.download = fileName || "downloaded";

  // Append the link to the document
  document.body.appendChild(link);

  // Trigger a click on the link to start the download
  link.click();

  // Remove the link from the document
  document.body.removeChild(link);
};

export const removeEmptyValuesInObject = (obj: object) => {
  return Object.entries(obj).reduce((acc: Record<string, unknown>, [key, value]) => {
    if (value !== null && value !== undefined) {
      acc[key] = value;
    }
    return acc;
  }, {});
};

export function redirectToLogin() {
  const search = new URLSearchParams(`redirect=${location.pathname}`);
  const queries = search.toString();
  const queriesDecode = decodeURIComponent(queries);
  const isSignInQuery = queriesDecode.includes(ROUTERS.LOGIN);
  window.location.replace(`${ROUTERS.LOGIN}${queries && !isSignInQuery ? `?${queries}` : ""}`);
}

export const addPropertiesToItems = <T, V>(
  items: T[] | undefined,
  getProperties: (item: T, index: number) => V,
  replace = false
): (T & V)[] | V[] => {
  return (
    items?.map((item, index) =>
      replace ? getProperties(item, index) : { ...item, ...getProperties(item, index) }
    ) || []
  );
};

export const generatePath = (path: string, params: Record<string, string>) => {
  return Object.entries(params).reduce((acc, [key, value]) => acc.replace(`:${key}`, value), path);
};

export const sleep = (ms: number) => new Promise(r => setTimeout(r, ms));

export const includesAny = (text: string, keywords: string[]): boolean =>
  keywords.some(keyword => text.includes(keyword));

export const getUniqueOptions = <T, K extends keyof T>(items: T[], key: K) => {
  return Array.from(
    new Map(
      items
        .filter(item => item[key] !== null && item[key] !== undefined)
        .map(item => [item[key], { value: item[key], label: String(item[key]) }])
    ).values()
  );
};

export const getUniqueOptionsMapper = <T, K extends keyof T, R>(
  items: T[],
  key: K,
  mapper: (item: T) => R
): R[] => {
  return Array.from(
    new Map(items.filter(item => item[key] != null).map(item => [item[key], mapper(item)])).values()
  );
};

const triggerDownload = (blob: Blob, fileName: string) => {
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = fileName;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
};

export const exportDataToCsv = (
  csvData: any,
  fileName = "data",
  fileType: "csv" | "xlsx" = "csv"
) => {
  const mimeTypes = {
    csv: "text/csv;charset=utf-8;",
    xlsx: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
  };

  const blob = new Blob([csvData], { type: mimeTypes[fileType] });
  triggerDownload(blob, `${fileName}.${fileType}`);
};

export const exportDataToZipFile = (fileData: BlobPart, fileName = "data") => {
  const blob = new Blob([fileData], { type: "application/zip" });
  triggerDownload(blob, `${fileName}.zip`);
};
