import { ColumnsType } from "antd/es/table";
import { ReactNode } from "react";

import {
  // AccessDatabase,
  CallGraph,
  IoParameter,
  Overview,
  // OverviewCopybook,
  // OverviewDatabase,
  ProcessingLogic,
  References,
  Typography
} from "@components";
import { FileGroup } from "@types";

import { WrapCol } from "../../../components/repository/styles";

export const DEFAULT_TAB = "overview";

export const genTabItemsRender = (
  t: any
): Record<FileGroup, Record<string, { label: ReactNode; render: () => ReactNode }>> => ({
  COBOL: {
    overview: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.cobol.overview.tab")}</Typography>
      ),
      render: () => <Overview />
    },
    "io-params": {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.cobol.io_params.tab")}</Typography>
      ),
      render: () => <IoParameter />
    },
    "processing-logic": {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.cobol.process_logic.tab")}</Typography>
      ),
      render: () => <ProcessingLogic />
    },
    "call-graph": {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.cobol.call_graph.tab")}</Typography>
      ),
      render: () => <CallGraph />
    },
    reference: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.cobol.reference.tab")}</Typography>
      ),
      render: () => <References />
    }
  },
  JCL: {
    overview: {
      label: <Typography level='h6-body1m'>{t("page.file_explorer.jcl.overview.tab")}</Typography>,
      render: () => t("message.coming_soon")
    }
  },
  JCL_IBM: {
    overview: {
      label: <Typography level='h6-body1m'>{t("page.file_explorer.jcl.overview.tab")}</Typography>,
      render: () => t("message.coming_soon")
    }
  },
  JCL_FUJITSU: {
    overview: {
      label: <Typography level='h6-body1m'>{t("page.file_explorer.jcl.overview.tab")}</Typography>,
      render: () => t("message.coming_soon")
    }
  },
  COPY: {
    overview: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.copybook.overview.tab")}</Typography>
      ),
      // render: () => <OverviewCopybook />
      render: () => t("message.coming_soon")
    }
  },
  DB: {
    overview: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.database.overview.tab")}</Typography>
      ),
      // render: () => <OverviewDatabase />
      render: () => t("message.coming_soon")
    },
    access: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.database.access.tab")}</Typography>
      ),
      // render: () => <AccessDatabase />
      render: () => t("message.coming_soon")
    }
  },
  SQL: {
    overview: {
      label: <Typography level='h6-body1m'>{t("page.file_explorer.sql.overview.tab")}</Typography>,
      render: () => t("message.coming_soon")
    }
  },
  SCREEN: {
    overview: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.screen.overview.tab")}</Typography>
      ),
      render: () => t("message.coming_soon")
    }
  },
  OTHER: {
    overview: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.other.overview.tab")}</Typography>
      ),
      render: () => t("message.coming_soon")
    }
  },
  BMS: {
    overview: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.other.overview.tab")}</Typography>
      ),
      render: () => t("message.coming_soon")
    }
  },
  UTILITY: {
    overview: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.other.overview.tab")}</Typography>
      ),
      render: () => t("message.coming_soon")
    }
  },
  CSD: {
    overview: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.other.overview.tab")}</Typography>
      ),
      render: () => t("message.coming_soon")
    }
  },
  PLI: {
    overview: {
      label: (
        <Typography level='h6-body1m'>{t("page.file_explorer.other.overview.tab")}</Typography>
      ),
      render: () => t("message.coming_soon")
    }
  }
});

export const getCblCommonTableColumns = (t: any): ColumnsType<any> => [
  {
    title: t("page.file_explorer.cobol.table.project_name"),
    dataIndex: "name",
    align: "center",
    render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
  },
  {
    title: t("page.file_explorer.cobol.table.document_title"),
    dataIndex: "title",
    align: "center",
    render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
  },
  {
    title: t("page.file_explorer.cobol.table.creator"),
    dataIndex: "created_by",
    align: "center",
    render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
  },
  {
    title: t("page.file_explorer.cobol.table.created_at"),
    dataIndex: "creation_date",
    align: "center",
    render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
  },
  {
    title: t("page.file_explorer.cobol.table.updated_by"),
    dataIndex: "updated_by",
    align: "center",
    render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
  },
  {
    title: t("page.file_explorer.cobol.table.updated_at"),
    dataIndex: "update_date",
    align: "center",
    render: (e: string) => <WrapCol mw={100}>{e}</WrapCol>
  }
];
