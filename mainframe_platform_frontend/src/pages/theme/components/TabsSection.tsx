import React, { useState } from "react";
import type { RadioChangeEvent } from "antd";
import { Radio, Space, Tabs } from "antd";
import type { SizeType } from "antd/es/config-provider/SizeContext";

const TabsSection1: React.FC = () => {
  const [size, setSize] = useState<SizeType>("small");

  const onChange = (e: RadioChangeEvent) => {
    setSize(e.target.value);
  };

  return (
    <div>
      <Radio.Group value={size} onChange={onChange} style={{ marginBottom: 16 }}>
        <Radio.Button value='small'>Small</Radio.Button>
        <Radio.Button value='middle'>Middle</Radio.Button>
        <Radio.Button value='large'>Large</Radio.Button>
      </Radio.Group>
      <Tabs
        defaultActiveKey='1'
        size={size}
        style={{ marginBottom: 32 }}
        items={new Array(3).fill(null).map((_, i) => {
          const id = String(i + 1);
          return {
            label: `Tab ${id}`,
            key: id,
            children: `Content of tab ${id}`
          };
        })}
      />
      <Tabs
        defaultActiveKey='1'
        type='card'
        size={size}
        items={new Array(3).fill(null).map((_, i) => {
          const id = String(i + 1);
          return {
            label: `Card Tab ${id}`,
            key: id,
            children: `Content of card tab ${id}`
          };
        })}
      />
    </div>
  );
};

type TabPosition = "left" | "right" | "top" | "bottom";

const TabsSection2: React.FC = () => {
  const [tabPosition, setTabPosition] = useState<TabPosition>("left");

  const changeTabPosition = (e: RadioChangeEvent) => {
    setTabPosition(e.target.value);
  };

  return (
    <>
      <Space style={{ marginBottom: 24 }}>
        Tab position:
        <Radio.Group value={tabPosition} onChange={changeTabPosition}>
          <Radio.Button value='top'>top</Radio.Button>
          <Radio.Button value='bottom'>bottom</Radio.Button>
          <Radio.Button value='left'>left</Radio.Button>
          <Radio.Button value='right'>right</Radio.Button>
        </Radio.Group>
      </Space>
      <Tabs
        tabPosition={tabPosition}
        items={new Array(3).fill(null).map((_, i) => {
          const id = String(i + 1);
          return {
            label: `Tab ${id}`,
            key: id,
            children: `Content of Tab ${id}`
          };
        })}
      />
    </>
  );
};

export const TabsSection: React.FC = () => {
  return (
    <>
      <TabsSection1 />
      <TabsSection2 />
    </>
  );
};
