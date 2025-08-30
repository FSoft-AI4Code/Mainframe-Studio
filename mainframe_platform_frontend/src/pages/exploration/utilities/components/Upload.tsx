/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable unused-imports/no-unused-imports */
import { PlusCircleOutlined } from "@ant-design/icons";
import styled from "@emotion/styled";
import { Button, Form, Input, message } from "antd";
import { Dispatch, SetStateAction, useCallback, useRef } from "react";
import { useParams } from "react-router-dom";

import { CloseSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { useCreateUtility } from "@services";
import { CreateUtilityRequest } from "@types";
import { handleErrorMessage } from "@utils";

export const CommonButtonWrapper = styled(Flex)<{ disabled: boolean }>`
  background: ${({ theme, disabled }) =>
    disabled ? theme.allColors.neutral6 : theme.allColors.primary6};
  color: ${({ theme }) => theme.allColors.neutral1};
  cursor: ${({ disabled }) => (disabled ? "default" : "pointer")};
  ${({ disabled }) => (disabled ? "'pointer-event': 'none'" : null)}
  &:hover {
    background: ${({ theme }) => theme.allColors.primary5};
  },
`;

const StepWrapper = styled(Flex)`
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  // background: rgba(245, 245, 245, 1);
  // padding: 32px 32px 85px;
  border-radius: 16px;
`;

const DetailStepWrapper = styled(Flex)`
  z-index: 1000;
  width: 630px;
  border-radius: 16px;
  position: relative;
  padding: 24px;
  background: ${({ theme }) => theme.allColors.neutral1};
  color: ${({ theme }) => theme.allColors.primary10};
`;

export function WrapperForm({
  setAddNew,
  addNew,
  refetchRepository
}: Readonly<{
  setAddNew: Dispatch<SetStateAction<boolean>>;
  addNew: boolean;
  refetchRepository: () => void;
}>) {
  const wrapperRef = useRef(null);
  const [messageApi, contextHolder] = message.useMessage();

  const { mutate: createUltility, isPending } = useCreateUtility();

  const { repoId = "" } = useParams();

  // const handleClose = () => {
  //   setAddNew(false);
  // };
  // const handleUpload = useCallback((value: CreateUtilityRequest) => {
  //   if (!repoId) return;
  //   createUltility(
  //     {
  //       name: value.name,
  //       description: value.description,
  //       category: value.category,
  //       node_id: value.node_id,
  //       repository_id: repoId,
  //       comment: value.comment
  //     },
  //     {
  //       onSuccess() {
  //         handleClose();
  //         messageApi.open({
  //           type: "success",
  //           content: "Uploaded repository success!"
  //         });
  //         refetchRepository();
  //       },
  //       onError(error) {
  //         handleErrorMessage(error as never, { show: true });
  //       }
  //     }
  //   );
  // }, []);

  return (
    <>
      {addNew && (
        <Flex
          ref={wrapperRef}
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            zIndex: 1000,
            backdropFilter: "blur(8px)",
            background: "rgba(0, 0, 0, 0.5)"
          }}
          onClick={e => e.target === wrapperRef.current && setAddNew(false)}
          gap={48}
        >
          <StepWrapper direction='column' align='center' justify='center' gap={32}>
            <DetailStepWrapper gap={16} direction='column'>
              <Flex center>
                <Typography color='primary10' level='title-24b'>
                  Add New Utilities
                </Typography>
              </Flex>
              <Flex
                justify='flex-end'
                style={{ cursor: "pointer", position: "absolute", right: "24px" }}
                onClick={() => setAddNew(false)}
              >
                <CloseSvg />
              </Flex>

              {/* name: value.name,
        description: value.description,
        category: value.category,
        node_id: value.node_id,
        repository_id: repoId,
        comment: value.comment */}
              <Form
                // onFinish={handleUpload}
                style={{ gap: 8, display: "flex", flexDirection: "column" }}
                layout='vertical'
              >
                <Form.Item
                  rules={[{ required: true, message: "Please input utilities name!" }]}
                  name='name'
                  required
                  style={{ fontWeight: 600 }}
                  label='Name'
                >
                  <Input placeholder='Enter utilities name' style={{ height: 40 }} />
                </Form.Item>
                <Form.Item
                  rules={[{ required: true, message: "Please input node Id" }]}
                  name='node_id'
                  required
                  style={{ fontWeight: 600 }}
                  label='Node Id'
                >
                  <Input placeholder='Enter category' style={{ height: 40 }} />
                </Form.Item>
                <Form.Item
                  rules={[{ required: true, message: "Please input node Id!" }]}
                  name='category'
                  required
                  style={{ fontWeight: 600 }}
                  label='Category'
                >
                  <Input placeholder='Enter category' style={{ height: 40 }} />
                </Form.Item>
                <Form.Item name='description' style={{ fontWeight: 600 }} label='Description'>
                  <Input placeholder='Enter description' style={{ height: 40 }} />
                </Form.Item>
                <Form.Item name='comment' style={{ fontWeight: 600 }} label='Comment'>
                  <Input placeholder='Enter comment' style={{ height: 40 }} />
                </Form.Item>
                <Flex justify='flex-end'>
                  <Button
                    style={{
                      padding: "2px 16px",
                      borderRadius: "8px",
                      color: "white"
                    }}
                    icon={<PlusCircleOutlined />}
                    type='primary'
                    htmlType='submit'
                    loading={isPending}
                  >
                    Add new
                  </Button>
                </Flex>
              </Form>
            </DetailStepWrapper>
          </StepWrapper>
        </Flex>
      )}
      {contextHolder}
    </>
  );
}
