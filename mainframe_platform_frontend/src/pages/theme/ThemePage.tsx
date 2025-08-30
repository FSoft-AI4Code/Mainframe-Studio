import { Col, Row, Form } from "antd";

import {
  OtherSection,
  RegisterSection,
  ValidateSection,
  ModalSection,
  TableSection,
  TabsSection
} from "./components";

export const ThemePage: React.FC = () => {
  const [form] = Form.useForm();

  // eslint-disable-next-line
  const onFinish = (values: any) => {
    // eslint-disable-next-line
    console.log("Received values of form: ", values);
  };

  return (
    <div className='layout-sidebar'>
      <Form
        form={form}
        name='validate_other'
        labelCol={{ span: 24 }}
        wrapperCol={{ span: 24 }}
        onFinish={onFinish}
        initialValues={{
          "input-number": 3,
          "checkbox-group": ["A", "B"],
          rate: 3.5,
          residence: ["zhejiang", "hangzhou", "xihu"],
          prefix: "86"
        }}
        scrollToFirstError
      >
        <Row justify='center'>
          <Col span={8}>
            <RegisterSection />
            <ModalSection />
          </Col>
          <Col span={8}>
            <ValidateSection />
          </Col>
          <Col span={8}>
            <OtherSection />
          </Col>
          <Col span={24}>
            <TabsSection />
          </Col>
          <Col span={24}>
            <TableSection />
          </Col>
        </Row>
      </Form>
    </div>
  );
};
