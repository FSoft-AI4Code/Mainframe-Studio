export const capitalize = (text: string) => {
  let arr = text.split(" ");
  arr = arr.map(o => o[0].toUpperCase() + o.slice(1));
  return arr.join(" ");
};

export const toLabelCase = (str: string): string => {
  return str
    .split("_")
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
};

export const toPascalCase = (str: string) => {
  return str
    .split("_")
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join(" ");
};

export const checkURL = (text: string) => {
  return /(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?/.test(
    text
  );
};

export function isJSON(str: string) {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
}

export const stripSlash = (key: string) => key.replace("/", "");

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const sanityCheck = (...sources: any[]) => {
  for (const source of sources) {
    if (typeof source !== "string") {
      throw new Error(`Expected string but got ${typeof source}`);
    }
  }
};

export const contains = (source: string, target: string, caseSensitive = true): number => {
  if (!source || typeof source !== "string") return -1;
  if (!target || typeof target !== "string") return -1;
  return (caseSensitive ? source : source.toLocaleLowerCase()).indexOf(
    caseSensitive ? target : target.toLocaleLowerCase()
  );
};

export const containsAnyIgnoreCase = (source: string, ...targets: string[]): boolean => {
  sanityCheck(source);
  let flag = false;
  for (const target of targets) {
    if (contains(source, target, false) !== -1) {
      flag = true;
      break;
    }
  }
  return flag;
};

export const cleanString = (str: string): string => str.replace(/["']/g, "").trim();
