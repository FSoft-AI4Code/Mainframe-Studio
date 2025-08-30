import { Edge, Node } from "@types";
export interface Filters {
  nodeLimit: number;
  complexity: number;
  pageNumber: number;
  pageLimit: number;
  loc: number;
}
export interface GraphState extends Filters {
  selectedEntry: string | null;
  selectedGroup: string[];
  selectedEntries: Record<string, never | unknown | string>;
  showNode: Record<string, boolean>;
  selectedType: "jcl" | "bms" | null;
  entries: { value: string; type: string; id: string }[];
  selectedGraph: { nodes: Node[]; edges: Edge[] };
}

export type State = GraphState;
