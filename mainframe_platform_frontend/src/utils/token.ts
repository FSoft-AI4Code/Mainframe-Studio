import { storage } from "@defines";

export const getAuthToken = () => {
  if (typeof window === undefined) {
    return null;
  }
  return localStorage.getItem(storage.TOKEN);
};

export function setAuthToken(token: string) {
  localStorage.setItem(storage.TOKEN, token);
}

export function removeAuthToken() {
  localStorage.removeItem(storage.TOKEN);
}

export function checkHasAuthToken() {
  const token = getAuthToken();
  if (!token) return false;
  return true;
}
