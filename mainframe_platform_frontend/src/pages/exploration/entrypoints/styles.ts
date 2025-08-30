import styled from "@emotion/styled";
import { Table } from "antd";

import { allColors } from "@style";

export const CustomTable = styled(Table)`
  .ant-table-thead {
    .ant-table-cell {
      background: ${allColors.neutral5};
      border-color: ${allColors.neutral7};
      border-radius: none;
    }
  }

  .ant-table-tbody {
    .ant-table-cell {
      vertical-align: top;
    }
  }
`;

export const CustomTableVertial = styled(Table)`
  .ant-table-thead {
    .ant-table-cell {
      background: ${allColors.neutral5};
      border-color: ${allColors.neutral7};
      border-radius: none;
    }
  }
  .ant-table {
    // border-left: 1px solid ${allColors.neutral7};
    border-radius: 0;
    .ant-table-cell {
      border: 0;
      color: ${allColors.neutral10};
      font-size: 16px;
      font-weight: 510;
      padding: 8px 16px;
    }
  }
`;
