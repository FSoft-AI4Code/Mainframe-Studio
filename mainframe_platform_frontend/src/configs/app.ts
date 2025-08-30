export const enabledSSL = process.env.REACT_APP_ENABLED_SSL === "true";
export const apiURL = process.env.REACT_APP_API_URL ?? "beta-api.mainframe-studio.fpt-aic.com";

export const backendURL = `${enabledSSL ? "https" : "http"}://${apiURL}`;
export const wsURL = `${enabledSSL ? "wss" : "ws"}://${apiURL}`;
