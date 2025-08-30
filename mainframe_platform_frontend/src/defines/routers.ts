import { stripSlash } from "@utils";

export type KeyWorkSpace = keyof typeof workspace;
export type KeyExploration = keyof typeof exploration;
export type KeyMigration = keyof typeof migration;
// > Workspace
export const workspace = {
  WORKSPACE: "/:workspaceCategory?",
  WORKSPACE_HOME: "/",
  WORKSPACE_REPOSITORY: "/repository",
  WORKSPACE_REPOSITORIES: "/repositories",
  WORKSPACE_EXPLORATION: "/exploration",
  WORKSPACE_MIGRATION_REPOSITORY: "/migration"
};

export const workspaceCategories: Record<
  keyof Pick<
    typeof workspace,
    | "WORKSPACE_REPOSITORY"
    | "WORKSPACE_EXPLORATION"
    | "WORKSPACE_MIGRATION_REPOSITORY"
    | "WORKSPACE_REPOSITORIES"
  >,
  string
> = {
  WORKSPACE_REPOSITORY: workspace.WORKSPACE_REPOSITORY.replace("/", ""),
  WORKSPACE_REPOSITORIES: workspace.WORKSPACE_REPOSITORIES.replace("/", ""),
  WORKSPACE_EXPLORATION: workspace.WORKSPACE_EXPLORATION.replace("/", ""),
  WORKSPACE_MIGRATION_REPOSITORY: workspace.WORKSPACE_MIGRATION_REPOSITORY.replace("/", "")
};

export const workspaceRouters = {} as Record<KeyWorkSpace, string>;
Object.keys(workspace).forEach(
  key => (workspaceRouters[key as KeyWorkSpace] = `${workspace[key as KeyWorkSpace]}`)
);

// > Exploration
export const exploration = {
  EXPLORATION: "/:explorationCategory?/*",
  EXPLORATION_HOME: "/",
  EXPLORATION_EXPLORATION: "/exploration",
  EXPLORATION_AI_AGENT: "/ai-agent/:repoId",
  EXPLORATION_GRAPH: "/graph",
  EXPLORATION_REVERSE: "/reverse",
  EXPLORATION_ENTRYPOINTS: "/entrypoints",
  EXPLORATION_REPORTS: "/reports",
  EXPLORATION_REPORTS_DETAIL: "/reports/detail/:type/:name",
  EXPLORATION_PROGRAMS_REPORTS: "/programs-reports",
  EXPLORATION_PROGRAMS_REPORTS_DETAIL: "/programs-reports/detail/:type/:name",
  EXPLORATION_DATABASE: "/database",
  EXPLORATION_FILE: "/file",
  EXPLORATION_ASSESSMENT: "/assessment",
  EXPLORATION_ASSETS: "/assets",
  EXPLORATION_INVENTORY: "/inventory",
  EXPLORATION_COMPLEXITY: "/complexity",
  EXPLORATION_DATASET: "/dataset",
  EXPLORATION_FILE_WITH_ID: "/file/:fileId",
  EXPLORATION_WITH_REPOSITORY_ID: "/exploration/:repoId",
  EXPLORATION_OVERVIEW: "/overview",
  EXPLORATION_FILE_WITH_ID_CATEGORY: "/file/:fileId/:fileCategory?",
  EXPLORATION_UTILITIES: "/utilities",
  EXPLORATION_DUPLICATE: "/duplication"
};

export const migration = {
  MIGRATION: "/:migrationCategory?/*",
  MIGRATION_HOME: "/",
  MIGRATION_GRAPH: "/graph",
  MIGRATION_FILE: "/file",
  MIGRATION_ASSESSMENT: "/assessment",
  MIGRATION_FILE_WITH_ID: "/file/:fileId",
  MIGRATION_FILE_WITH_ID_CATEGORY: "/file/:fileId/:fileCategory?",
  MIGRATION_FILE_MATCHING: "/file/:fileId/matching"
};

export const explorationCategories: Record<
  keyof Pick<
    typeof exploration,
    | "EXPLORATION_GRAPH"
    | "EXPLORATION_FILE"
    | "EXPLORATION_ASSESSMENT"
    | "EXPLORATION_UTILITIES"
    | "EXPLORATION_OVERVIEW"
    | "EXPLORATION_ASSETS"
    | "EXPLORATION_INVENTORY"
    | "EXPLORATION_COMPLEXITY"
    | "EXPLORATION_DATASET"
    | "EXPLORATION_REVERSE"
    | "EXPLORATION_ENTRYPOINTS"
    | "EXPLORATION_REPORTS"
    | "EXPLORATION_REPORTS_DETAIL"
    | "EXPLORATION_EXPLORATION"
    | "EXPLORATION_AI_AGENT"
    | "EXPLORATION_DATABASE"
    | "EXPLORATION_DUPLICATE"
  >,
  string
> = {
  EXPLORATION_GRAPH: stripSlash(exploration.EXPLORATION_GRAPH),
  EXPLORATION_FILE: stripSlash(exploration.EXPLORATION_FILE),
  EXPLORATION_ASSESSMENT: stripSlash(exploration.EXPLORATION_ASSESSMENT),
  EXPLORATION_OVERVIEW: stripSlash(exploration.EXPLORATION_OVERVIEW),
  EXPLORATION_ASSETS: stripSlash(exploration.EXPLORATION_ASSETS),
  EXPLORATION_INVENTORY: stripSlash(exploration.EXPLORATION_INVENTORY),
  EXPLORATION_COMPLEXITY: stripSlash(exploration.EXPLORATION_COMPLEXITY),
  EXPLORATION_DATASET: stripSlash(exploration.EXPLORATION_DATASET),
  EXPLORATION_REVERSE: stripSlash(exploration.EXPLORATION_REVERSE),
  EXPLORATION_ENTRYPOINTS: stripSlash(exploration.EXPLORATION_ENTRYPOINTS),
  EXPLORATION_REPORTS: stripSlash(exploration.EXPLORATION_REPORTS),
  EXPLORATION_REPORTS_DETAIL: stripSlash(exploration.EXPLORATION_REPORTS_DETAIL),
  EXPLORATION_DATABASE: stripSlash(exploration.EXPLORATION_DATABASE),
  EXPLORATION_EXPLORATION: stripSlash(exploration.EXPLORATION_EXPLORATION),
  EXPLORATION_AI_AGENT: stripSlash(exploration.EXPLORATION_AI_AGENT),
  EXPLORATION_UTILITIES: stripSlash(exploration.EXPLORATION_UTILITIES),
  EXPLORATION_DUPLICATE: stripSlash(exploration.EXPLORATION_DUPLICATE)
};

export const explorationRouters = {} as Record<KeyExploration, string>;
Object.keys(exploration).forEach(
  key => (explorationRouters[key as KeyExploration] = `${exploration[key as KeyExploration]}`)
);

export const migrationRouters = {} as Record<KeyMigration, string>;

Object.keys(migration).forEach(
  key =>
    (migrationRouters[key as KeyMigration] = `${workspace.WORKSPACE_MIGRATION_REPOSITORY}${
      migration[key as KeyMigration]
    }`)
);

const mainRouters = {
  LOGIN: "/signin",
  REGISTER: "/register",
  VERIFY: "/verify",
  FORGOT_PASSWORD: "/forgot-password",
  RESET_PASSWORD: "/resetpwd",
  UNAUTHORIZED: "/401",
  NOT_FOUND: "/404",
  SERVER_ERROR: "/500",
  CATCH_ALL_ROUTE: "*",
  UNDER_MAINTENANCE: "/under-maintenance",
  PRIVACY_POLICY: "/privacy-and-policy",
  COMMING_SOON: "/coming-soon",
  THEME: "/theme",
  SHARE: "/share/:projectId",
  SHARE_MIGRATION: "/share/:projectId?matchingId=:matchingId"
};

export const ROUTERS = {
  ...mainRouters,
  ...workspaceRouters,
  ...explorationRouters,
  ...migrationRouters,
  ...explorationCategories
};

export const ROUTERS_GUARD = [ROUTERS.WORKSPACE, ROUTERS.EXPLORATION];
