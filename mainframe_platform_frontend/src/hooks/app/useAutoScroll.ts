import { useEffect, useRef } from "react";

export function useAutoScroll(dependencies: string[]) {
  const scrollContentRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    if (!scrollContentRef.current) return;

    const container = scrollContentRef.current;
    container.scrollTo({
      top: container.scrollHeight,
      behavior: "smooth"
    });
  }, dependencies);

  return scrollContentRef;
}
