import { useEffect, useRef, useState } from "react";
import { Input } from "antd";

import { SendInSvg } from "@assets/svg";
import { Flex } from "@components";

export function InputMessage({
  sendMessage,
  disabled
}: {
  sendMessage: (text: string) => void;
  disabled?: boolean;
}) {
  const [value, setValue] = useState<string>("");
  const inputRef = useRef(null);

  const handleSend = () => {
    if (!value) return;
    sendMessage(value);
    setValue("");
  };
  const handleKeyPress = (e: any) => {
    if (e.keyCode !== 13) return;
    e.preventDefault();
    handleSend();
  };

  useEffect(() => {
    if (inputRef.current) {
      (inputRef.current as unknown as HTMLInputElement).focus();
    }
  }, [disabled]);

  return (
    <Flex gap={8} align='flex-end' style={{ padding: "10px 20px 20px" }}>
      <Input
        ref={inputRef}
        value={value}
        onChange={e => setValue(e.target.value)}
        onKeyDown={handleKeyPress}
        style={{ borderRadius: "8px" }}
        size='large'
        placeholder='Type a question'
        disabled={disabled}
        // autoSize={true}
        suffix={
          <Flex style={{ width: 40, height: 34 }} center onClick={handleSend}>
            <SendInSvg />
          </Flex>
        }
      />
    </Flex>
  );
}
