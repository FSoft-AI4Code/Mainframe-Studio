export const defaultOptions = {
  readAheadChars: 15,
  targetBufferChars: 15,
  adjustPercentage: 0.2,
  frameLookBackMs: 1e4,
  windowLookBackMs: 2e3
};

export const initialState = {
  blockMatches: [],
  isFinished: false,
  visibleText: ""
};
