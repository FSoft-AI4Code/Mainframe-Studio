import { useState, useLayoutEffect, useRef } from "react";

export function useAutosize(value: number) {
  const ref = useRef<HTMLTextAreaElement | null>(null);
  const [borderWidth, setBorderWidth] = useState<number>(0);

  useLayoutEffect(() => {
    if (!ref.current) return;

    const style = window.getComputedStyle(ref.current);
    setBorderWidth(
      (parseFloat(style?.borderTopWidth || "0") || 0) +
        (parseFloat(style?.borderBottomWidth || "0") || 0)
    );
  }, []);

  useLayoutEffect(() => {
    if (!ref.current) return;

    ref.current.style.height = "inherit";
    ref.current.style.height = `${ref.current.scrollHeight + borderWidth}px`;
  }, [value, borderWidth]);

  return ref;
}

export default useAutosize;
