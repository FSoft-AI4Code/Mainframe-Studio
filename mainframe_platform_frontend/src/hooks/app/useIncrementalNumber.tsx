import { useState, useEffect } from "react";

export const useIncrementalNumber = (targetNumber: number, duration = 1000) => {
  const [currentValue, setCurrentValue] = useState(0);

  useEffect(() => {
    let start = 0;
    const increment = targetNumber / (duration / 10);

    const timer = setInterval(() => {
      start += increment;
      if (start >= targetNumber) {
        start = targetNumber;
        clearInterval(timer);
      }
      setCurrentValue(Math.round(start));
    }, 10);

    return () => clearInterval(timer);
  }, [targetNumber, duration]);

  return currentValue;
};
