import { Modal, Result } from "antd";
import React, { useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import { useNavigate } from "react-router-dom";

import { Typography } from "@components";

export const ModalSuccess: React.FC<{ repositoryId?: string }> = ({ repositoryId }) => {
  const refTimeout = useRef<NodeJS.Timeout>();
  const { t } = useTranslation();
  const navigate = useNavigate();
  const [step1, setStep1] = useState(false);
  const [step2, setStep2] = useState(false);

  const clearRefTimeout = () => {
    if (refTimeout.current) {
      clearTimeout(refTimeout.current);
      refTimeout.current = undefined;
    }
  };

  useEffect(() => {
    if (repositoryId && !step1) {
      clearRefTimeout();
      setTimeout(() => {
        clearRefTimeout();
        setStep1(true);
      }, 3000);
    }
  }, [repositoryId, step1]);

  useEffect(() => {
    if (step1 && !step2) {
      clearRefTimeout();
      setTimeout(() => {
        clearRefTimeout();
        setStep2(true);
      }, 2000);
    }
  }, [step1, step2]);

  useEffect(() => {
    if (!step1 || !step2) return;
    navigate(`/exploration/${repositoryId}/assets/inventory/`);
  }, [step1, step2]);

  return repositoryId ? (
    <Modal open centered footer closeIcon closable>
      <Result
        status='success'
        title={<Typography level='h3s'>{t("notification.git_success")}</Typography>}
        subTitle={
          <Typography level='h7-body2r'>
            {t(step1 ? "message.redirect" : "message.success_fetch")}
          </Typography>
        }
      />
    </Modal>
  ) : null;
};
