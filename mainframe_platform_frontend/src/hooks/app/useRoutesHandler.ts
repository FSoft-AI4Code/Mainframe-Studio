import { useDispatch, useSelector } from "react-redux";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import { useCallback, useEffect } from "react";

import { routesActions, routeSelector } from "@store"; // Sửa lại `routeSelcector` thành `routeSelector`
import { ROUTERS } from "@defines";

export const routeMap: Record<string, string> = {
  inventory: "Inventory",
  complexity: "Complexity",
  dataset: "Dataset Assignment",
  graph: "Dependency Graph",
  entrypoints: "Entrypoints",
  reports: "Reports",
  overview: "Overview",
  assessment: "Assessment",
  exploration: "Exploration",
  database: "Database & Table",
  utilities: "Utilities",
  duplication: "Duplication"
};

export function useRoutesHandler() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const recentRoutes = useSelector(routeSelector.recentRoutes); // Sửa lỗi selector
  const { repoId } = useParams();

  const { pathname, search } = useLocation();

  const mapRoute = useCallback((route: keyof typeof routeMap) => routeMap[route] || "", []);

  const setRecentRoute = (routes: { key: string; path: string }) =>
    dispatch(routesActions.setRecentRoute(routes));

  const clearRoutes = () => dispatch(routesActions.clearRoutes());

  const updateRoutes = (route: string) => dispatch(routesActions.updateRoutes(route));

  const getRoutes = (path: string, defautValue: string) =>
    path?.split("/")?.at(-1) || path?.split("/")?.at(-2) || defautValue;

  const keyValue = getRoutes(pathname, ROUTERS.EXPLORATION_OVERVIEW);
  const route = search ? "reverse" : keyValue;

  useEffect(() => {
    const keyRoute = mapRoute(route);
    if (keyRoute) {
      setRecentRoute({
        key: keyRoute,
        path: `${pathname}${search}`
      });
    }
  }, [dispatch, route, pathname, search, mapRoute]);

  const onChangeSegmented = useCallback(
    (value: string) => {
      if (!repoId) return;
      const key = getRoutes(value, "assets");
      const newRoute = `/exploration/${repoId}/${value}`;
      const keyRoute = mapRoute(key);
      navigate(newRoute);
      if (keyRoute) {
        setRecentRoute({
          key: keyRoute,
          path: `${newRoute}`
        });
      }
    },
    [repoId, navigate, dispatch, mapRoute]
  );

  return {
    route,
    navigate,
    setRecentRoute,
    recentRoutes,
    updateRoutes,
    clearRoutes,
    onChangeSegmented,
    pathname,
    search
  };
}
