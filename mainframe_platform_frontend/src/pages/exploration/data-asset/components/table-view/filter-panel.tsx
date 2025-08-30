/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable unused-imports/no-unused-imports */
/* eslint-disable @typescript-eslint/no-unused-vars */
import type React from "react";
import { useEffect, useState } from "react";
import { Button, Card, Form, Input, Select, Space } from "antd";
import { FilterOutlined, UpOutlined, DownOutlined } from "@ant-design/icons";
import { useParams } from "react-router-dom";

import { useDebounce } from "@hooks";
import { Flex } from "@components";
import { DatasetsInput, ViewExportType } from "@types";
import { useAvailabledFilterDatasetsQuery } from "@services";

interface FilterPanelProps {
  onFilter?: (values: Partial<DatasetsInput>) => void;
  filter: Partial<DatasetsInput & { view: ViewExportType }>;
}

const FilterPanel: React.FC<FilterPanelProps> = ({ onFilter, filter }) => {
  const [visible, setVisible] = useState(false);
  const [form] = Form.useForm();
  const { debounce } = useDebounce({ timeout: 300 });
  const { repoId = "" } = useParams();
  const { datasetType, openMode, isLoading } = useAvailabledFilterDatasetsQuery({
    repository_id: repoId
  });

  const toggleFilterPanel = () => {
    setVisible(!visible);
  };

  const handleFinish = (values: Partial<DatasetsInput>) => {
    debounce(async () => onFilter?.(values));
  };

  useEffect(() => {
    form.setFieldsValue(filter);
  }, [filter]);

  return (
    <Flex style={{ marginTop: 16 }} direction='column'>
      <Button
        onClick={toggleFilterPanel}
        style={{ borderRadius: 4, width: 150 }}
        shape='default'
        icon={<FilterOutlined />}
      >
        {visible ? "Hide Filters" : "Show Filters"}
        {visible ? <UpOutlined /> : <DownOutlined />}
      </Button>
      {visible && (
        <Card className='filter-panel' style={{ marginTop: 16 }}>
          <Form
            form={form}
            layout='vertical'
            onValuesChange={(changed, allValues) => {
              const cleaned = Object.fromEntries(
                Object.entries(allValues).map(([key, value]) => [
                  key,
                  value === "All" ? null : value
                ])
              );
              debounce(async () => onFilter?.(cleaned));
            }}
            onFinish={handleFinish}
          >
            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))",
                gap: 16
              }}
            >
              <Form.Item label='File Name' name='file_name'>
                <Input allowClear placeholder='Filter by File Name' />
              </Form.Item>

              <Form.Item label='Job Name' name='job_name'>
                <Input allowClear placeholder='Filter by Job Name' />
              </Form.Item>

              <Form.Item label='Program Name' name='program_name'>
                <Input allowClear placeholder='Filter by Program Name' />
              </Form.Item>

              <Form.Item label='Step Name' name='step_name'>
                <Input allowClear placeholder='Filter by Step Name' />
              </Form.Item>

              <Form.Item label='Assign Name' name='assign_name'>
                <Input allowClear placeholder='Filter by Assign Name' />
              </Form.Item>

              <Form.Item label='File Type' name='file_type' initialValue='All'>
                <Select loading={isLoading}>
                  <Select.Option value='All'>All</Select.Option>
                  {datasetType?.map(type => (
                    <Select.Option key={type} value={type}>
                      {type?.toUpperCase()}
                    </Select.Option>
                  ))}
                </Select>
              </Form.Item>

              <Form.Item label='Open Mode' name='open_mode' initialValue='All'>
                <Select loading={isLoading}>
                  <Select.Option value='All'>All</Select.Option>
                  {openMode?.map(mode => (
                    <Select.Option key={mode} value={mode}>
                      {mode?.toUpperCase()}
                    </Select.Option>
                  ))}
                </Select>
              </Form.Item>
            </div>

            {/* <Space>
              <Button type='primary' htmlType='submit'>
                Apply Filters
              </Button>
              <Button onClick={handleReset}>Reset</Button>
            </Space> */}
          </Form>
        </Card>
      )}
    </Flex>
  );
};

export default FilterPanel;
