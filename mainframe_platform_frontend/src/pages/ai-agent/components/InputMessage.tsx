import { ChangeEventHandler, KeyboardEventHandler, useEffect, useRef, useState } from "react";
import { Input, type InputRef } from "antd";

import { SendInSvg } from "@assets/svg";
import { Flex } from "@components";
import { allColors } from "@style";

export function InputMessage({
  sendMessage,
  disabled
}: {
  sendMessage: (text: string) => void;
  disabled?: boolean;
}) {
  const [value, setValue] = useState<string>("");
  const inputRef = useRef<InputRef>(null);

  const handleSend = () => {
    if (!value) return;
    sendMessage(value);
    setValue("");
  };
  const handleKeyPress: KeyboardEventHandler<HTMLInputElement> = e => {
    if (e.keyCode !== 13) return;
    e.preventDefault();
    handleSend();
  };
  const handleChangeValue: ChangeEventHandler<HTMLInputElement> = e => setValue(e.target.value);

  useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, [disabled]);

  return (
    <Flex gap={8} align='flex-end' style={{ padding: "10px 20px 20px" }}>
      <Input
        ref={inputRef}
        value={value}
        onChange={handleChangeValue}
        onKeyDown={handleKeyPress}
        style={{ borderRadius: "8px" }}
        size='large'
        placeholder='Type a question'
        disabled={disabled}
        suffix={
          <Flex style={{ width: 40, height: 34, cursor: "pointer" }} center onClick={handleSend}>
            <SendInSvg color={!!value ? allColors.primary6 : allColors.neutral6} />
          </Flex>
        }
      />
    </Flex>
  );
}
