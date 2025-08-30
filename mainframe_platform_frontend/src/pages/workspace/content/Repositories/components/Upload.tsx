import { Dispatch, SetStateAction, useCallback, useRef } from "react";
import styled from "@emotion/styled";
import { Button, Form, Input, message, Select } from "antd";

import { Flex, Typography } from "@components";
import { CloseSvg } from "@assets/svg";
import { useCreateRepository } from "@services";
import { handleErrorMessage } from "@utils";
import { CreateReponsitoryInput, SystemTypeEnum } from "@types";
import { useRepository } from "@hooks";

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

const StyledSelect = styled(Select)`
  .ant-select-selection-item {
    font-size: 14px;
  }
  .ant-select-selection-placeholder {
    font-size: 14px;
    font-weight: 500;
  }
`;

export function WrapperForm({
  setAddNew,
  addNew,
  refetchRepository
}: {
  setAddNew: Dispatch<SetStateAction<boolean>>;
  addNew: boolean;
  refetchRepository: () => void;
}) {
  const wrapperRef = useRef(null);
  const [messageApi, contextHolder] = message.useMessage();
  const { mutate: createRepo, isPending } = useCreateRepository();
  const { projectId } = useRepository();

  const handleClose = () => {
    setAddNew(false);
  };
  const handleUpload = useCallback((value: CreateReponsitoryInput) => {
    if (!projectId) return;
    createRepo(
      {
        ...value,
        project_id: projectId
      },
      {
        onSuccess() {
          handleClose();
          messageApi.open({
            type: "success",
            content: "Uploaded repository success!"
          });
          refetchRepository();
        },
        onError(error) {
          handleErrorMessage(error as never, { show: true });
        }
      }
    );
  }, []);

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
            {/* <Flex
              justify='flex-end'
              style={{ width: "100%", cursor: "pointer", position: "relative" }}
              onClick={() => setAddNew(false)}
            >
              <CloseSvg />
            </Flex> */}
            <DetailStepWrapper gap={16} direction='column'>
              <Flex center>
                <Typography color='primary10' level='title-24b'>
                  Git Link
                </Typography>
              </Flex>
              <Flex
                justify='flex-end'
                style={{ cursor: "pointer", position: "absolute", right: "24px" }}
                onClick={() => setAddNew(false)}
              >
                <CloseSvg />
              </Flex>
              <Form
                onFinish={handleUpload}
                style={{ gap: 8, display: "flex", flexDirection: "column" }}
                layout='vertical'
              >
                <Form.Item
                  rules={[{ required: true, message: "Please input repository name!" }]}
                  name='name'
                  required
                  style={{ fontWeight: 600 }}
                  label='Name'
                >
                  <Input placeholder='Enter name' style={{ height: 40 }} />
                </Form.Item>
                <Form.Item
                  rules={[{ required: true, message: "Please input repository url!" }]}
                  name='url'
                  required
                  style={{ fontWeight: 600 }}
                  label='Repository URL'
                >
                  <Input placeholder='Enter url' style={{ height: 40 }} />
                </Form.Item>
                <Form.Item
                  rules={[{ required: true, message: "Please input repository token!" }]}
                  name='token'
                  required
                  style={{ fontWeight: 600 }}
                  label='Token'
                >
                  <Input placeholder='Enter token' style={{ height: 40 }} />
                </Form.Item>
                <Form.Item
                  rules={[{ required: true, message: "Please select System type!" }]}
                  name='system_type'
                  required
                  style={{ fontWeight: 600 }}
                  label='System type'
                >
                  <StyledSelect size='large' placeholder='Select system type'>
                    {Object.keys(SystemTypeEnum)
                      .filter(key => isNaN(Number(key)))
                      ?.map(type => (
                        <Select.Option key={type} value={type}>
                          {type}
                        </Select.Option>
                      ))}
                  </StyledSelect>
                </Form.Item>
                <Form.Item name='description' style={{ fontWeight: 600 }} label='Description'>
                  <Input placeholder='Enter description' style={{ height: 40 }} />
                </Form.Item>
                <Flex justify='flex-end'>
                  <Button
                    style={{
                      padding: "2px 8px",
                      borderRadius: "100px",
                      color: "white"
                    }}
                    type='primary'
                    htmlType='submit'
                    loading={isPending}
                  >
                    Upload
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
