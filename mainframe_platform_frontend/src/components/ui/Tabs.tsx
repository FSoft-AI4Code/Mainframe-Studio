import React, { useState } from "react";
import { Segmented, Tabs as AntdTabs } from "antd";
import type { TabsProps as AntdTabsProps } from "antd";

import { Flex } from "./Flex";
interface TabsProps extends AntdTabsProps {
  items: Array<{ label: string; key: string; icon: React.ReactNode }>;
}

const Tabs: React.FC<TabsProps> = ({ items, onChange, activeKey }) => {
  const [activeTab, setActiveTab] = useState<string | undefined>(activeKey);
  return (
    <AntdTabs
      activeKey={activeKey}
      onChange={onChange}
      items={items}
      renderTabBar={() => (
        <Flex direction='column'>
          <Segmented
            options={
              items?.map(item => ({
                label: item.label,
                value: item.key,
                icon: item.icon
              })) || []
            }
            value={activeTab || activeKey}
            onChange={value => {
              // eslint-disable-next-line no-console
              console.log("value", value);
              onChange?.(value as string);
              setActiveTab(value as string);
            }}
            block
          />
        </Flex>
      )}
    />
  );
};

export { Tabs };
