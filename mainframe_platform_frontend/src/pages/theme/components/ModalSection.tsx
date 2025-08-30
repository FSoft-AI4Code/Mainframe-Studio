import React, { useState } from "react";
import { Button, Card, Modal } from "antd";

export const ModalSection: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [open, setOpen] = useState(false);

  const showModal = () => {
    setOpen(true);
  };

  const handleOk = () => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      setOpen(false);
    }, 3000);
  };

  const handleCancel = () => {
    setOpen(false);
  };

  return (
    <Card>
      <Button type='primary' onClick={showModal}>
        Open Modal with customized footer
      </Button>
      <Modal
        open={open}
        title='Title'
        onOk={handleOk}
        onCancel={handleCancel}
        footer={[
          <Button key='back' onClick={handleCancel}>
            Return
          </Button>,
          <Button key='submit' type='primary' loading={loading} onClick={handleOk}>
            Submit
          </Button>,
          <Button
            key='link'
            href='https://google.com'
            type='primary'
            loading={loading}
            onClick={handleOk}
          >
            Search on Google
          </Button>
        ]}
      >
        <p>Some contents...</p>
        <p>Some contents...</p>
        <p>Some contents...</p>
        <p>Some contents...</p>
        <p>Some contents...</p>
      </Modal>
    </Card>
  );
};
