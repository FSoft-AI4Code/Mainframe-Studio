export class Dimension {
  private value: number;

  constructor(val: number) {
    this.value = val;
  }

  public get number() {
    return this.value;
  }

  public get string() {
    return `${this.value}px`;
  }
}
