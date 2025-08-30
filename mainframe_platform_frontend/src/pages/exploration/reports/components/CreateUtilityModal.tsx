import { Button, Form, Input, message, Select, Switch } from "antd";
import { Dispatch, SetStateAction } from "react";
import { useParams } from "react-router-dom";

import { Flex, Typography } from "@components";
import { ReverseItem, CreateUtilityRequest, LabelEnum, FormField } from "@types";
import {
  useCategoryUtilityQuery,
  useCreateUtility,
  useFieldsUtilitiesByTypeQuery
} from "@services";
import { handleErrorMessage, toLabelCase } from "@utils";

import { WrapModal } from "./styles";

export const DynamicField = ({ field, loading }: DynamicFeildProps) => {
  const { name: fieldName, inputType, required, options, mode } = field || {};
  const rules = required
    ? [{ required: true, message: `${toLabelCase(fieldName)} is required` }]
    : [];

  const commonProps = {
    placeholder: `Enter ${fieldName}`
  };

  const renderMap: Record<string, React.ReactNode> = {
    input: <Input style={{ height: 40 }} {...commonProps} />,
    textarea: <Input.TextArea {...commonProps} autoSize={{ minRows: 3 }} />,
    select: (
      <Select
        loading={loading}
        {...commonProps}
        allowClear
        mode={mode === "multiple" ? "multiple" : undefined}
        placeholder={`Select ${fieldName}`}
        options={options?.map((opt: string) => ({ label: opt, value: opt }))}
      />
    ),
    switch: <Switch />
  };

  const component = renderMap[inputType];
  const currentInputType = inputType === "switch" ? "checked" : "value";

  if (!component) return null;

  return (
    <Form.Item
      key={fieldName}
      name={fieldName}
      label={`${toLabelCase(fieldName)}`}
      rules={rules}
      valuePropName={currentInputType}
    >
      {component}
    </Form.Item>
  );
};

export function CreateUtilityModal({
  setOpen,
  open,
  data,
  refetchReport
}: Readonly<{
  setOpen: Dispatch<SetStateAction<boolean>>;
  open: boolean;
  data: ReverseItem;
  refetchReport: () => void;
}>) {
  const [messageApi, contextHolder] = message.useMessage();
  const { name, type } = data || {};
  const { repoId = "" } = useParams();
  const [form] = Form.useForm();

  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { categoryUtility, loading: loadingCategory } = useCategoryUtilityQuery({ repoId });
  const { mutate: createUtitity } = useCreateUtility();
  const { fieldsUtility, loading: loadingFields } = useFieldsUtilitiesByTypeQuery(
    type as LabelEnum
  );

  const handleCancel = () => setOpen(false);

  const handleUpdate = (formData: CreateUtilityRequest & Record<string, any>) => {
    if (!repoId) return;

    // eslint-disable-next-line no-console
    console.log("formData,", formData);
    createUtitity(
      {
        ...formData,
        repository_id: repoId,
        file_name: name,
        label: type
      },
      {
        onSuccess() {
          refetchReport();
          handleCancel();
          messageApi.success("Created successfully!");
        },
        onError(error) {
          handleErrorMessage(error as never, { show: true });
        }
      }
    );
  };

  return (
    <WrapModal
      footer={false}
      centered
      closable
      open={open}
      onCancel={handleCancel}
      bodyStyle={{ background: "white" }}
    >
      <Flex style={{ marginBottom: "16px" }} center>
        <Typography color='primary10' level='title-24b'>
          Create Utilities
        </Typography>
      </Flex>
      <Form
        form={form}
        onFinish={handleUpdate}
        initialValues={{
          repository_id: repoId,
          file_name: name,
          label: type
        }}
        layout='vertical'
        style={{ display: "flex", flexDirection: "column", gap: 8 }}
      >
        {/* Static fields */}
        <Form.Item name='repository_id' label='Repository ID'>
          <Input placeholder='Enter repository id' style={{ height: 40 }} readOnly />
        </Form.Item>
        <Form.Item name='file_name' label='File Name'>
          <Input placeholder='Enter file name' style={{ height: 40 }} readOnly />
        </Form.Item>
        <Form.Item name='label' label='Label'>
          <Input placeholder='Enter label' style={{ height: 40 }} readOnly />
        </Form.Item>
        {/* Dynamic fields */}
        {Array.isArray(fieldsUtility) &&
          fieldsUtility?.map(field => (
            <DynamicField key={field.name} field={field} loading={loadingFields} />
          ))}

        <Flex justify='flex-end' style={{ marginTop: 12 }} gap={10}>
          <Button onClick={handleCancel} size='large' type='default'>
            Cancel
          </Button>
          <Button size='large' type='primary' htmlType='submit'>
            Submit
          </Button>
        </Flex>

        {contextHolder}
      </Form>
    </WrapModal>
  );
}

type DynamicFeildProps = {
  field: FormField;
  loading?: boolean;
};
