import { Button, Form, Input, message, Modal, ModalProps } from "antd";
import { Dispatch, SetStateAction, useCallback } from "react";
import styled from "@emotion/styled";
import FormItem from "antd/es/form/FormItem";

import { Flex, Typography } from "@components";
import { Repository, UpdateReponsitoryInput } from "@types";
import { useUpdateRepository } from "@services";
import { handleErrorMessage } from "@utils";

const WrapModal = styled(Modal)<ModalProps>`
  .ant-modal-content {
    padding: 16px 24px;
    border-radius: 12px;
    background-color: white !important;
    position: relative;
  }
  .ant-modal-close {
    position: absolute;
    top: 16px;
    right: 16px;
  }
  .ant-modal-footer {
    background: white;
  }
`;

export function UpdateRepoForm({
  setOpen,
  open,
  repo,
  refetchRepository
}: {
  setOpen: Dispatch<SetStateAction<boolean>>;
  open: boolean;
  repo: Repository;
  refetchRepository: () => void;
}) {
  const [messageApi, contextHolder] = message.useMessage();
  // eslint-disable-next-line @typescript-eslint/naming-convention
  const { name, url, id, status, is_assessed, is_reversed, description } = repo || {};

  const [form] = Form.useForm();
  const handleCancel = () => {
    setOpen(false);
  };
  const { mutate: updateRepository } = useUpdateRepository();
  const handleUpdate = useCallback(
    (value: UpdateReponsitoryInput) => {
      updateRepository(
        {
          repository_id: id,
          url: value?.url,
          token: value?.token,
          name: value?.name,
          description: value?.description,
          is_assessed,
          is_reversed,
          status: status
        },
        {
          onSuccess() {
            refetchRepository();
            handleCancel();
            messageApi.open({
              type: "success",
              content: "Update repository success!"
            });
          },
          onError(error) {
            handleErrorMessage(error as never, { show: true });
          }
        }
      );
    },
    [id]
  );

  return (
    <WrapModal
      footer={false}
      centered
      closable
      open={open}
      okText='Save Change'
      onCancel={handleCancel}
      bodyStyle={{
        background: "white"
      }}
    >
      <Flex style={{ marginBottom: "16px" }} center>
        <Typography color='primary10' level='title-24b'>
          Update repository
        </Typography>
      </Flex>
      <Form
        form={form}
        onFinish={handleUpdate}
        initialValues={{
          name,
          url,
          description
        }}
        style={{
          display: "flex",
          flexDirection: "column",
          gap: 8
        }}
        layout='vertical'
      >
        <FormItem name='name' style={{ fontWeight: 600 }} label='Repository Name'>
          <Input placeholder='Enter repository name' style={{ height: 48 }} />
        </FormItem>
        <FormItem name='url' style={{ fontWeight: 600 }} label='Repository URL'>
          <Input placeholder='Enter repository url' style={{ height: 48 }} />
        </FormItem>
        <FormItem name='token' style={{ fontWeight: 600 }} label='Repository Token'>
          <Input placeholder='Enter repository token' style={{ height: 48 }} />
        </FormItem>
        <FormItem name='description' style={{ fontWeight: 600 }} label='Repository Description'>
          <Input placeholder='Enter repository description' style={{ height: 48 }} />
        </FormItem>
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
