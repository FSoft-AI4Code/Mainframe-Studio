import { Dimension } from "@class";

class Breakpoint {
  private val: number;

  constructor(val: number) {
    this.val = val;
  }

  public get min() {
    return new Dimension(this.val + 0.02);
  }

  public get max() {
    return new Dimension(this.val - 0.02);
  }

  public get value() {
    return new Dimension(this.val);
  }
}

export const breakpoints = {
  xs: new Breakpoint(480),
  sm: new Breakpoint(576),
  md: new Breakpoint(768),
  lg: new Breakpoint(992),
  xl: new Breakpoint(1200),
  xxl: new Breakpoint(1600)
};
