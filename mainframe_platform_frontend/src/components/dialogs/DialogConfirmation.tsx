import { useTranslation } from "react-i18next";
import { Modal, ModalProps } from "antd";

type Props = {
  title?: string;
  description: string;
  close: () => void;
  ok?: () => Promise<void> | void;
} & ModalProps;

export const DialogConfirmation: React.FC<Props> = ({ title, ...props }) => {
  const { t } = useTranslation();

  const submit = () => {
    if (props.ok) props.ok();
    else props.close();
  };

  return (
    <Modal
      {...props}
      title={title || t("notice")}
      onCancel={e => {
        props.close();
        if (props.onCancel) props.onCancel(e);
      }}
      onOk={e => {
        submit();
        if (props.onOk) props.onOk(e);
      }}
    >
      <p>{t(props.description)}</p>
    </Modal>
  );
};
