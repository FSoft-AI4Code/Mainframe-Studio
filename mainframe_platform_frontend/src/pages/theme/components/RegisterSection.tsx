import { useState } from "react";
import {
  Form,
  Input,
  InputNumber,
  Cascader,
  Select,
  Row,
  Col,
  Checkbox,
  Button,
  AutoComplete,
  Segmented
} from "antd";

import { Wrap } from "./styles";

const { Option } = Select;

const residences = [
  {
    value: "zhejiang",
    label: "Zhejiang",
    children: [
      {
        value: "hangzhou",
        label: "Hangzhou",
        children: [
          {
            value: "xihu",
            label: "West Lake"
          }
        ]
      }
    ]
  },
  {
    value: "jiangsu",
    label: "Jiangsu",
    children: [
      {
        value: "nanjing",
        label: "Nanjing",
        children: [
          {
            value: "zhonghuamen",
            label: "Zhong Hua Men"
          }
        ]
      }
    ]
  }
];

export const RegisterSection: React.FC = () => {
  const prefixSelector = (
    <Form.Item name='prefix' noStyle>
      <Select style={{ width: 70 }}>
        <Option value='86'>+86</Option>
        <Option value='87'>+87</Option>
      </Select>
    </Form.Item>
  );

  const [autoCompleteResult, setAutoCompleteResult] = useState<string[]>([]);

  const onWebsiteChange = (value: string) => {
    if (!value) {
      setAutoCompleteResult([]);
    } else {
      setAutoCompleteResult([".com", ".org", ".net"].map(domain => `${value}${domain}`));
    }
  };

  const websiteOptions = autoCompleteResult.map(website => ({
    label: website,
    value: website
  }));

  return (
    <Wrap>
      <Form.Item
        name='email'
        label='E-mail'
        rules={[
          {
            type: "email",
            message: "The input is not valid E-mail!"
          },
          {
            required: true,
            message: "Please enter your E-mail!"
          }
        ]}
      >
        <Input disabled />
      </Form.Item>

      <Form.Item
        name='password'
        label='Password'
        rules={[
          {
            required: true,
            message: "Please enter your password!"
          }
        ]}
        hasFeedback
      >
        <Input.Password />
      </Form.Item>

      <Form.Item
        name='confirm'
        label='Confirm Password'
        dependencies={["password"]}
        hasFeedback
        rules={[
          {
            required: true,
            message: "Please confirm your password!"
          },
          ({ getFieldValue }) => ({
            validator(_, value) {
              if (!value || getFieldValue("password") === value) {
                return Promise.resolve();
              }
              return Promise.reject(new Error("The two passwords that you entered do not match!"));
            }
          })
        ]}
      >
        <Input.Password placeholder='Confirm Password' size='large' />
      </Form.Item>

      <Form.Item
        name='nickname'
        label='Nickname'
        tooltip='What do you want others to call you?'
        rules={[{ required: true, message: "Please enter your nickname!", whitespace: true }]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        name='residence'
        label='Habitual Residence'
        rules={[
          { type: "array", required: true, message: "Please select your habitual residence!" }
        ]}
      >
        <Cascader options={residences} />
      </Form.Item>

      <Form.Item
        name='phone'
        label='Phone Number'
        rules={[{ required: true, message: "Please enter your phone number!" }]}
      >
        <Input addonBefore={prefixSelector} style={{ width: "100%" }} />
      </Form.Item>

      <Form.Item
        name='donation'
        label='Donation'
        rules={[{ required: true, message: "Please enter donation amount!" }]}
      >
        <InputNumber style={{ width: "100%" }} />
      </Form.Item>

      <Form.Item
        name='website'
        label='Website'
        rules={[{ required: true, message: "Please enter website!" }]}
      >
        <AutoComplete options={websiteOptions} onChange={onWebsiteChange} placeholder='website'>
          <Input />
        </AutoComplete>
      </Form.Item>

      <Form.Item
        name='gender'
        label='Gender'
        rules={[{ required: true, message: "Please select gender!" }]}
      >
        <Select placeholder='select your gender'>
          <Option value='male'>Male</Option>
          <Option value='female'>Female</Option>
          <Option value='other'>Other</Option>
        </Select>
      </Form.Item>

      <Form.Item label='Captcha' extra='We must make sure that your are a human.'>
        <Row gutter={8}>
          <Col span={12}>
            <Form.Item
              name='captcha'
              noStyle
              rules={[{ required: true, message: "Please enter the captcha you got!" }]}
            >
              <Input />
            </Form.Item>
          </Col>
          <Col span={12}>
            <Button>Get captcha</Button>
          </Col>
        </Row>
      </Form.Item>

      <Form.Item
        name='agreement'
        valuePropName='checked'
        rules={[
          {
            validator: (_, value) =>
              value ? Promise.resolve() : Promise.reject(new Error("Should accept agreement"))
          }
        ]}
      >
        <Checkbox>
          I have read the <a href=''>agreement</a>
        </Checkbox>
      </Form.Item>
      <Form.Item>
        <Button type='primary' htmlType='submit'>
          Register
        </Button>
        <Button type='primary' htmlType='submit' disabled>
          Register
        </Button>
      </Form.Item>
      <Segmented
        options={[
          "Daily",
          { label: "Weekly", value: "Weekly", disabled: true },
          "Monthly",
          { label: "Quarterly", value: "Quarterly" },
          "Yearly"
        ]}
      />
    </Wrap>
  );
};
