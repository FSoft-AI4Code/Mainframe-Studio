import { Input, InputProps, message as messageApi } from "antd";
import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { useDispatch, useSelector } from "react-redux";

import { repositoryApi } from "@api";
import { Button, Flex, Typography } from "@components";
import { storage } from "@defines";
import {
  fileActions,
  migrationRepositoryActions,
  migrationRepositorySelector,
  repositoryActions
} from "@store";
import { checkURL } from "@utils";

import { CommonProps } from "./types";

const defaultValues = { url: "", token: "" };

type Props = CommonProps & { setShowSuccess: (v: boolean) => void };

export const InputContent: React.FC<Props> = ({ data, isOnEdit, setIsOnEdit, setShowSuccess }) => {
  const dispatch = useDispatch();
  const { t } = useTranslation();
  const [loading, setLoading] = useState(false);
  const [inputValues, setInputValues] = useState(defaultValues);
  const [helperInput, setHelperInput] = useState<string>();
  const migrationRepositoryData = useSelector(
    migrationRepositorySelector.selectMigrationRepositoryData
  );

  const fetchRepo = async (isUpdate?: boolean) => {
    try {
      setLoading(true);
      const res = await repositoryApi.postRepositoryRequest(inputValues);

      if (isUpdate && migrationRepositoryData?.url) {
        // clear migration
        dispatch(migrationRepositoryActions.clean());
        localStorage.removeItem(storage.MIGRATION_REPO);
      }
      dispatch(fileActions.clean());
      dispatch(repositoryActions.setRepositoryData(res.data));
      setShowSuccess(true);

      localStorage.setItem(storage.REPO, JSON.stringify(res.data));
    } catch (error) {
      messageApi.error(String(error));
    } finally {
      setLoading(false);
    }
  };

  const onClickCancel = () => setIsOnEdit(false);

  const onClickUpdate = async () => {
    await fetchRepo(true);
    setIsOnEdit(false);
  };

  const onClickFetch = () => fetchRepo();

  const onChangeUrl: InputProps["onChange"] = e => {
    const url = e.target.value;
    setInputValues(s => ({ ...s, url }));
    setHelperInput(checkURL(url) ? undefined : "Please enter a URL");
  };

  const onChangeToken: InputProps["onChange"] = e =>
    setInputValues(s => ({ ...s, token: e.target.value }));

  useEffect(() => {
    if (isOnEdit && data) setInputValues({ url: data.url, token: "" });
    else setInputValues(defaultValues);
  }, [isOnEdit]);

  return (
    <Flex direction='column' gap={24} style={{ width: 616 }}>
      <Flex direction='column' gap={16}>
        <Flex direction='column' gap={8}>
          <Typography level='h7-body2M' color='white'>
            {t("label.repo_url")}
          </Typography>
          <Input
            size='large'
            placeholder={t("label.repo_url")}
            allowClear
            value={inputValues.url}
            onChange={onChangeUrl}
            disabled={loading}
            status={helperInput ? "error" : undefined}
          />
          {helperInput && (
            <Typography level='h8-captions' color='danger'>
              {helperInput}
            </Typography>
          )}
        </Flex>
        <Flex direction='column' gap={8}>
          <Typography level='h7-body2M' color='white'>
            {t("label.token")}
          </Typography>
          <Input
            size='large'
            placeholder={t("label.token")}
            allowClear
            value={inputValues.token}
            onChange={onChangeToken}
            disabled={loading}
          />
        </Flex>
      </Flex>
      <Flex gap={24} justify='flex-end'>
        {isOnEdit ? (
          <>
            <Button onClick={onClickCancel} disabled={loading}>
              {t("button.cancel")}
            </Button>
            <Button
              type='primary'
              onClick={onClickUpdate}
              loading={loading}
              disabled={!inputValues.url || Boolean(helperInput)}
            >
              {t("button.update")}
            </Button>
          </>
        ) : (
          <Button
            type='primary'
            onClick={onClickFetch}
            loading={loading}
            disabled={!inputValues.url || Boolean(helperInput)}
            style={{ padding: "5px 16px" }}
          >
            {t("button.fetch")}
          </Button>
        )}
      </Flex>
    </Flex>
  );
};
