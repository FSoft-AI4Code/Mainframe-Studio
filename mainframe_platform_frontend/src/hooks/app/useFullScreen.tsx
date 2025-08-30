import { FullscreenExitOutlined, FullscreenOutlined } from "@ant-design/icons";
import { useEffect, useState } from "react";

export const useFullScreen = (id: string) => {
  const [isFullScreen, setIsFullScreen] = useState(Boolean(document.fullscreenElement));

  const setFullScreen = (params?: { fullScreen?: boolean; elementId?: string }) => {
    const { elementId, fullScreen } = params || {};
    const elem: any = elementId ? document.getElementById(elementId) : document.documentElement;
    if (!elem) return;

    if (fullScreen !== false) {
      if (elem.requestFullscreen) {
        elem.requestFullscreen();
      } else if (elem.webkitRequestFullscreen) {
        /* Safari */
        elem.webkitRequestFullscreen();
      } else if (elem.msRequestFullscreen) {
        /* IE11 */
        elem.msRequestFullscreen();
      }
    } else if (document.fullscreenElement) {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if ((document as any).webkitExitFullscreen) {
        /* Safari */
        (document as any).webkitExitFullscreen();
      } else if ((document as any).msExitFullscreen) {
        /* IE11 */
        (document as any).msExitFullscreen();
      }
    }
  };

  const onClickFullScreen = () => {
    const nextState = !Boolean(document.fullscreenElement);
    setFullScreen({ fullScreen: nextState, elementId: id });
    setIsFullScreen(nextState);
  };

  const renderIcon = () => (isFullScreen ? <FullscreenExitOutlined /> : <FullscreenOutlined />);

  const handleFullscreenChange = () => {
    if (!document.fullscreenElement) {
      // Perform your desired action here when exiting fullscreen
      setIsFullScreen(false);
    }
  };

  useEffect(() => {
    document.addEventListener("fullscreenchange", handleFullscreenChange);
    document.addEventListener("webkitfullscreenchange", handleFullscreenChange);
    document.addEventListener("mozfullscreenchange", handleFullscreenChange);
    document.addEventListener("MSFullscreenChange", handleFullscreenChange);

    return () => {
      document.removeEventListener("fullscreenchange", handleFullscreenChange);
      document.removeEventListener("webkitfullscreenchange", handleFullscreenChange);
      document.removeEventListener("mozfullscreenchange", handleFullscreenChange);
      document.removeEventListener("MSFullscreenChange", handleFullscreenChange);
    };
  }, []);

  return {
    onClickFullScreen,
    renderIcon,
    isFullScreen
  };
};
