import { Card, Col, type CardProps } from "antd";
import type { ColProps } from "antd/es/col";

interface CustomCardProps extends CardProps {
  colProps?: ColProps;
}

export function CustomCard({ colProps, children, bordered = false, ...props }: CustomCardProps) {
  return (
    <Col {...colProps}>
      <Card {...props} bordered={bordered}>
        {children}
      </Card>
    </Col>
  );
}
