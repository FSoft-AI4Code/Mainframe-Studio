export const formatDateUS = (date: string) => {
  if (!date) {
    return "";
  }
  return new Date(date).toLocaleDateString("en-US", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric"
  });
};

export const formatDateUS2 = (date: string) => {
  if (!date) {
    return "";
  }
  return new Date(date)
    ?.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric"
    })
    ?.replace(/,/g, "");
};

export const formatDateNoTime = (date: string) => {
  if (!date) {
    return "";
  }
  return new Date(date)?.toLocaleDateString("en-CA", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit"
  });
};
