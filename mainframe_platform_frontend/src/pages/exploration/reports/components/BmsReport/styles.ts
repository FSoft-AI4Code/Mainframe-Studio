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
