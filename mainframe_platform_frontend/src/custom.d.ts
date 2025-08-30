import "chart.js";

declare module "chart.js" {
  interface Element<T = AnyObject, O = AnyObject> {
    $context: Record<string, any>;
  }
}
