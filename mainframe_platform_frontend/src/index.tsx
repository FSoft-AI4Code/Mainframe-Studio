import { Global as GlobalStyle, ThemeProvider } from "@emotion/react";
import { ConfigProvider } from "antd";
import {
  ArcElement,
  BarController,
  BarElement,
  CategoryScale,
  Chart,
  Filler,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip
} from "chart.js";
import ReactDOM from "react-dom/client";
import { Provider } from "react-redux";
import { PersistGate } from "redux-persist/integration/react";

import ErrorBoundary from "@pages/errorBoundary";
// eslint-disable-next-line import/order
import { QueryClientProvider } from "@providers";
import "./lang";

import { persistor, store } from "@store";
import { antdTheme, globalStyle, theme } from "@style";
Chart.register([
  ArcElement,
  CategoryScale,
  LinearScale,
  BarController,
  BarElement,
  PointElement,
  LineElement,
  Filler,
  Tooltip
]);

import App from "./App";
import reportWebVitals from "./reportWebVitals";

import "./lang/language";

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(
  <ErrorBoundary>
    <GlobalStyle styles={globalStyle} />
    <ThemeProvider theme={theme}>
      <ConfigProvider theme={antdTheme}>
        <Provider store={store}>
          <PersistGate persistor={persistor}>
            <QueryClientProvider>
              <App />
            </QueryClientProvider>
          </PersistGate>
        </Provider>
      </ConfigProvider>
    </ThemeProvider>
  </ErrorBoundary>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
