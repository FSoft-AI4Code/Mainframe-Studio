import { Button, Table } from "antd";
import type { ColumnsType, TableProps } from "antd/es/table";

import { ArrowHighPrioritySvg } from "@assets/svg";

import { ProcessMultilSteps } from "./components";
import { GroupPriority, TestCaseProcess, TestCaseWrap, Title, Wrapper } from "./styles";

// TODO integrate api
type DataType = {
  no: string;
  test: string;
  priority: string;
  status: string;
};

const columns: ColumnsType<DataType> = [
  {
    title: "No.",
    dataIndex: "no",
    render: text => <Wrapper>{text}</Wrapper>
  },
  {
    title: "Test",
    dataIndex: "test",
    render: text => <Wrapper>{text}</Wrapper>
  },
  {
    title: "Priority",
    dataIndex: "priority",
    render: text => (
      <GroupPriority>
        <ArrowHighPrioritySvg />
        {text}
      </GroupPriority>
    )
  },
  {
    title: "Status",
    dataIndex: "status",
    render: text => <Button type='primary'>{text}</Button>
  }
];

const data = [
  {
    no: "1",
    test: "John Brown",
    priority: "John Brown",
    status: "John Brown"
  },
  {
    no: "2",
    test: "John Brown",
    priority: "John Brown",
    status: "John Brown"
  }
];

const onChange: TableProps<DataType>["onChange"] = (pagination, filters, sorter, extra) => {
  // eslint-disable-next-line
  console.log("params", pagination, filters, sorter, extra);
};

export const TestCaseContent: React.FC = () => {
  return (
    <TestCaseWrap>
      <Title>Test</Title>
      <TestCaseProcess>
        <ProcessMultilSteps percents={[50, 20]} colors={["#32D74B", "#FF453A"]} />
      </TestCaseProcess>
      <Table columns={columns} dataSource={data} onChange={onChange} />
    </TestCaseWrap>
  );
};
