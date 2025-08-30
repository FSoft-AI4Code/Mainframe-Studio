export enum SortOrderENum {
  desc = -1,
  asc = 1
}

export const sortBy = <T>(
  data: T[] | undefined,
  keys: (keyof T)[],
  orders: (keyof typeof SortOrderENum)[]
): T[] => {
  if (!data) return [];
  return [...data].sort((a, b) => {
    for (let i = 0; i < keys.length; i++) {
      const key = keys[i];
      const order = SortOrderENum[orders[i]];
      if (a[key] < b[key]) return SortOrderENum.desc * order;
      if (a[key] > b[key]) return SortOrderENum.asc * order;
    }
    return 0;
  });
};
