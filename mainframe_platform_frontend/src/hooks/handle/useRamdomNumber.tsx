import { useState, useEffect } from "react";

export const useRamdomNumber = () => {
  const [randomNumber, setRandomNumber] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      const newRandomNumber = Math.floor(Math.random() * 101); // Generate a random number between 0 and 100
      setRandomNumber(newRandomNumber);
    }, 500); // 500 milliseconds (0.5 seconds)

    // Clean up the interval when the component unmounts
    return () => {
      clearInterval(interval);
    };
  }, []); // Empty dependency array to run the effect only once

  return randomNumber;
};
