import { GlobalLoading } from "@components";
import { useApp, useHandle, useShowNotification } from "@hooks";
import { Router } from "@router";

function App() {
  const { inited } = useApp();
  useHandle();
  const contextHolder = useShowNotification();

  if (!inited) return <GlobalLoading />;

  return (
    <>
      <Router />
      {contextHolder}
    </>
  );
}

export default App;
