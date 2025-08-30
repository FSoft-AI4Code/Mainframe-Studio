import i18next from "i18next";
import { initReactI18next } from "react-i18next";

import * as langEn from "./en.json";
import * as langJa from "./ja.json";
import * as langVi from "./vi.json";

const defaultLang = process.env.REACT_APP_DEFAULT_LANG || "en";

i18next
  // .use(languageDetector)
  .use(initReactI18next)
  .init({
    compatibilityJSON: "v3",
    lng: defaultLang,
    fallbackLng: "en",
    debug: false,
    resources: {
      en: { translation: langEn },
      vi: { translation: langVi },
      ja: { translation: langJa }
    }
  });
