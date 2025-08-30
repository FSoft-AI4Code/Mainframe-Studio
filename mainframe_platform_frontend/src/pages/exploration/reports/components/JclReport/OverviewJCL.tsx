import { ColumnsType } from "antd/es/table";
import { Tooltip } from "antd";
import { QuestionCircleOutlined } from "@ant-design/icons";

import { Flex, Typography } from "@components";
import { allColors } from "@style";
import { Overview } from "@types";

import { CustomTableVertial } from "./styles";
import { getCurrentJclDetail } from "./JCLReport";

interface OverviewJCLProps {
  overviewData: Overview | null;
  title?: string;
}

export default function OverviewJCL({ overviewData, title }: OverviewJCLProps) {
  const {
    job_name: jobName,
    class: classJCL,
    msgclass,
    notify,
    time: timeJCL,
    description
  } = overviewData || {};

  const dataSource = [
    { key: "jobName", field: "Job Name", value: jobName },
    { key: "Description", field: "Description", value: description },
    { key: "class", field: "Class", value: classJCL },
    { key: "mssclass", field: "MSGCLASS", value: msgclass },
    { key: "timeLimit", field: "Time Limit", value: timeJCL },
    { key: "notify", field: "Notify", value: notify }
  ];

  const columns: ColumnsType<Partial<{ key: string; field: string; value: string | undefined }>> = [
    {
      title: "Field",
      dataIndex: "field",
      key: "field",
      width: 140,
      onCell: () => {
        return {
          style: {
            border: `1px solid ${allColors.neutral7}`,
            background: `${allColors.neutral5}`
          }
        };
      },
      render: (value, { key }) => {
        // eslint-disable-next-line @typescript-eslint/no-shadow
        const { description, details = [] } = getCurrentJclDetail(key ?? "") || {};
        if (!description) return value || "None";

        return (
          <Flex gap={2} justify='space-between'>
            {value || "None"}{" "}
            <Tooltip
              trigger='click'
              rootClassName='default'
              title={
                <Flex direction='column' style={{ padding: 4 }}>
                  <Typography color='neutral10' level='body-14m'>
                    {description || ""}
                  </Typography>
                  <Flex direction='column'>
                    {details &&
                      details?.length > 0 &&
                      details?.map((item, i) => (
                        <Typography color='neutral10' level='body-14r' key={i}>
                          - {item}
                        </Typography>
                      ))}
                  </Flex>
                </Flex>
              }
            >
              <QuestionCircleOutlined style={{ width: 12 }} />
            </Tooltip>
          </Flex>
        );
      }
    },
    {
      title: "value",
      dataIndex: "value",
      key: "value",
      onCell: () => {
        return {
          style: {
            border: `1px solid ${allColors.neutral7}`
          }
        };
      },
      render: value => value || "None"
    }
  ];

  return (
    <Flex direction='column' gap={32}>
      {title && (
        <Typography level='body-16b' color='primary10'>
          {title}
        </Typography>
      )}
      <CustomTableVertial
        showHeader={false}
        tableLayout='fixed'
        columns={columns}
        rowKey='field'
        dataSource={dataSource}
        pagination={false}
        bordered
      />
    </Flex>
  );
}
