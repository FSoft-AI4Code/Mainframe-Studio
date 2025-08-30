import { useRef, useState } from "react";
import { useTranslation } from "react-i18next";

import { DialogConfirmation } from "@components";

type Props =
  | {
      title?: string;
      message?: string;
    }
  | undefined;

export const useCheckRedirect = (props?: Props) => {
  const { t } = useTranslation();
  const [showModal, setShowModal] = useState(false);
  const refBlock = useRef<boolean>(false);
  const refRedirect = useRef<Promise<void>>(new Promise(res => res()));
  const refRedirectConfirm = useRef<() => unknown>();

  const block = () => {
    refBlock.current = true;
  };

  const approve = () => {
    if (refRedirectConfirm.current) {
      refRedirectConfirm.current();
      refRedirectConfirm.current = undefined;
    }
    refBlock.current = false;
  };

  const check = () => {
    if (refBlock.current) {
      refRedirect.current = new Promise(res => (refRedirectConfirm.current = res));
      setShowModal(true);
    }
    return refRedirect.current;
  };

  const onClickCancel = () => {
    refRedirect.current = new Promise(res => res());
    refRedirectConfirm.current = undefined;
    setShowModal(false);
  };

  const onClickOk = () => {
    approve();
    setShowModal(false);
  };

  const renderModal = () => (
    <DialogConfirmation
      open={showModal}
      close={onClickCancel}
      ok={onClickOk}
      okButtonProps={{ danger: true }}
      description={props?.message || t("message.unsaved_changes")}
      centered
    />
  );

  return {
    approve,
    block,
    check,
    renderModal
  };
};
