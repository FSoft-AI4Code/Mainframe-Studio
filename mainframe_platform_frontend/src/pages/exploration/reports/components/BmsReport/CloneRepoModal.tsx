import React, { useState } from "react";
import { Modal, Tabs, Input, Typography as TypographyAntd, Button } from "antd";
import { CopyOutlined } from "@ant-design/icons";

import { Typography } from "@components";

const { TabPane } = Tabs;
const { Text, Link } = TypographyAntd;

type Props = {
  open: boolean;
  onClose: () => void;
};

const CloneRepoModal: React.FC<Props> = ({ open, onClose }) => {
  const [tab, setTab] = useState<"https" | "ssh">("https");

  const urls = {
    https: "https://github.com/example/react-todo-app",
    ssh: "git@github.com:example/react-todo-app.git"
  };

  const command = `git clone ${urls[tab]}`;

  const handleCopy = () => {
    navigator.clipboard.writeText(command);
  };

  return (
    <Modal
      open={open}
      onCancel={onClose}
      footer={null}
      closable
      title={<Typography level='title-18b'>Clone Repository</Typography>}
      width={500}
    >
      <Text type='secondary'>Clone repository to your local machine.</Text>

      <Tabs
        activeKey={tab}
        onChange={key => setTab(key as "https" | "ssh")}
        style={{ marginTop: 16 }}
      >
        <TabPane tab='HTTPS' key='https' />
        <TabPane tab='SSH' key='ssh' />
      </Tabs>

      <Input
        readOnly
        value={command}
        size='large'
        addonAfter={<Button icon={<CopyOutlined />} onClick={handleCopy} type='text' />}
        style={{ marginTop: 8 }}
      />

      <Text type='secondary' style={{ display: "block", marginTop: 8 }}>
        Use Git or checkout with SVN using the web URL.
      </Text>

      <div
        style={{
          background: "#f5f5f5",
          padding: 12,
          borderRadius: 6,
          marginTop: 16
        }}
      >
        <Text strong>New to Git?</Text>{" "}
        <Link color='#1890FF' href='https://git-scm.com/doc' target='_blank'>
          Visit the Git documentation
        </Link>{" "}
        to learn how to set up Git.
      </div>
    </Modal>
  );
};

export default CloneRepoModal;
