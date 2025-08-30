import { Suspense, lazy } from "react";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";

import { GlobalLoading } from "@components";
import { ROUTERS } from "@defines";

const LoginPage = lazy(() => import("@pages/login"));
const RegisterPage = lazy(() => import("@pages/register"));
const ForgotPasswordPage = lazy(() => import("@pages/forgotPassword"));
const VerifyPage = lazy(() => import("@pages/verify"));
const ResetPasswordPage = lazy(() => import("@pages/resetPassword"));
const NotFoundPage = lazy(() => import("@pages/notfound"));
const ServerErrorPage = lazy(() => import("@pages/serverError"));
const UnderMaintenancePage = lazy(() => import("@pages/underMaintenance"));
const PrivacyPolicyPage = lazy(() => import("@pages/privacyPolicy"));
const ThemePage = lazy(() => import("@pages/theme"));
const WorkspacePage = lazy(() => import("@pages/workspace"));
const AIAgentPage = lazy(() => import("@pages/ai-agent"));

const InventoryPage = lazy(() => import("@pages/exploration/inventory"));
const ComplexityPage = lazy(() => import("@pages/exploration/complexity"));
const DataAssetPage = lazy(() => import("@pages/exploration/data-asset"));
const EntryPointsPage = lazy(() => import("@pages/exploration/entrypoints"));
const DependencyGraphPage = lazy(() => import("@pages/exploration/dependencygraph"));
const ReportsPage = lazy(() => import("@pages/exploration/reports"));
const DatabasePage = lazy(() => import("@pages/exploration/database"));
const ReportDetailPage = lazy(() => import("@pages/exploration/reports/ReportDetailPage"));
const OverviewPage = lazy(() => import("@pages/exploration/overview"));
const UtilitiesPage = lazy(() => import("@pages/exploration/utilities"));
const DuplicatePage = lazy(() => import("@pages/exploration/duplicate"));
const Repositories = lazy(() => import("@pages/workspace/content/Repositories"));
const AssessmentPage = lazy(() => import("@pages/exploration/assessment/"));
const ExplorationPage = lazy(() => import("@pages/exploration/exploration"));
const ExplorationRouter = lazy(() => import("./ExplorationRouter"));

export const Router: React.FC = () => {
  return (
    <BrowserRouter>
      <Suspense fallback={<GlobalLoading />}>
        <Routes>
          <Route path={ROUTERS.LOGIN} element={<LoginPage />} />
          <Route path={ROUTERS.REGISTER} element={<RegisterPage />} />
          <Route path={ROUTERS.VERIFY} element={<VerifyPage />} />
          <Route path={ROUTERS.FORGOT_PASSWORD} element={<ForgotPasswordPage />} />
          <Route path={ROUTERS.RESET_PASSWORD} element={<ResetPasswordPage />} />
          <Route path={ROUTERS.NOT_FOUND} element={<NotFoundPage />} />
          <Route path={ROUTERS.SERVER_ERROR} element={<ServerErrorPage />} />
          <Route path={ROUTERS.UNDER_MAINTENANCE} element={<UnderMaintenancePage />} />
          <Route path={ROUTERS.PRIVACY_POLICY} element={<PrivacyPolicyPage />} />
          <Route path={ROUTERS.THEME} element={<ThemePage />} />
          <Route element={<WorkspacePage />}>
            <Route path={ROUTERS.WORKSPACE_REPOSITORIES} element={<Repositories />} />
            <Route path={ROUTERS.EXPLORATION_AI_AGENT} element={<AIAgentPage />} />
            <Route path={ROUTERS.EXPLORATION_WITH_REPOSITORY_ID} element={<ExplorationRouter />}>
              <Route path={ROUTERS.EXPLORATION_OVERVIEW} element={<OverviewPage />} />
              <Route path={ROUTERS.EXPLORATION_ASSESSMENT} element={<AssessmentPage />} />
              <Route path={ROUTERS.EXPLORATION_EXPLORATION}>
                <Route path={ROUTERS.EXPLORATION_UTILITIES} element={<UtilitiesPage />} />
                <Route path={ROUTERS.EXPLORATION_DUPLICATE} element={<DuplicatePage />} />
                <Route path={ROUTERS.EXPLORATION_DATABASE} element={<DatabasePage />} />
                <Route path={ROUTERS.EXPLORATION_ENTRYPOINTS} element={<ExplorationPage />} />
                <Route path={ROUTERS.EXPLORATION_DATASET} element={<DataAssetPage />} />
              </Route>
              <Route path={ROUTERS.EXPLORATION_ASSETS}>
                <Route path={ROUTERS.EXPLORATION_INVENTORY} element={<InventoryPage />} />
                <Route path={ROUTERS.EXPLORATION_COMPLEXITY} element={<ComplexityPage />} />
                <Route path={ROUTERS.EXPLORATION_DATASET} element={<DataAssetPage />} />
                <Route
                  path={ROUTERS.CATCH_ALL_ROUTE}
                  element={<Navigate to={ROUTERS.EXPLORATION_INVENTORY} replace />}
                />
              </Route>
              <Route path={ROUTERS.EXPLORATION_REPORTS} element={<ReportsPage />} />
              <Route path={ROUTERS.EXPLORATION_REPORTS_DETAIL} element={<ReportDetailPage />} />
              <Route path={ROUTERS.EXPLORATION_REVERSE}>
                <Route path={ROUTERS.EXPLORATION_GRAPH} element={<DependencyGraphPage />} />
                <Route path={ROUTERS.EXPLORATION_ENTRYPOINTS} element={<EntryPointsPage />} />
                <Route path={ROUTERS.CATCH_ALL_ROUTE} element={<Navigate to='graph' replace />} />
              </Route>
            </Route>
          </Route>
          <Route
            path={ROUTERS.WORKSPACE_HOME}
            element={<Navigate to={ROUTERS.WORKSPACE_REPOSITORIES} />}
          />
          <Route path={ROUTERS.CATCH_ALL_ROUTE} element={<Navigate to={ROUTERS.NOT_FOUND} />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
};
