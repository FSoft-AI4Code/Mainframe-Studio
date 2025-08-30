import { Badge, Progress } from "antd";

import { Title, WrapBadge, WrapperProcess } from "./style";

const mockDataBadges = [
  {
    color: "#FF3A29",
    name: "text"
  },
  {
    color: "#FFE5D3",
    name: "text"
  }
];

export const Maintainability: React.FC = () => {
  return (
    <div>
      <Title>Maintainability</Title>
      <WrapperProcess>
        <Progress
          type='circle'
          percent={75}
          width={142}
          strokeColor='#FF3A29'
          trailColor='#FFE5D3'
        />
      </WrapperProcess>
      <WrapBadge>
        {mockDataBadges?.map(badge => (
          <Badge key={badge.name} status='success' text={badge.name} color={badge.color} />
        ))}
      </WrapBadge>
    </div>
  );
};
