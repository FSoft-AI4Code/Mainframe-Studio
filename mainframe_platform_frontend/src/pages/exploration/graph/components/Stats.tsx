import styled from "@emotion/styled";
import { ReactNode } from "react";

import { ApplicationInSvg, ChainInSvg, DatabaseInSvg, ExcludeInSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { colors } from "@style";

const StatWrapper = styled(Flex)<{ color: string }>`
  border-radius: 8px;
  padding: 7px 24px;
  border: 2px solid ${({ color }) => color};
  background-color: ${({ color }) => color}4D;
`;

type StatProps = {
  content?: ReactNode;
  icon?: ReactNode;
  color?: string;
};

function CommonStat({ content, color, icon }: StatProps) {
  return (
    <StatWrapper color={color ?? colors.black} center gap={10}>
      {icon}
      <Typography level='h7-body2M'>{content}</Typography>
    </StatWrapper>
  );
}

export function ApplicationStat({ content = "Application" }: Pick<StatProps, "content">) {
  const color = colors.purple;

  return (
    <CommonStat
      content={content}
      color={color}
      icon={<ApplicationInSvg style={{ width: 16, height: 16 }} />}
    />
  );
}

export function DatabaseStat({ content = "Database" }: Pick<StatProps, "content">) {
  const color = colors.orange;

  return (
    <CommonStat
      content={content}
      color={color}
      icon={<DatabaseInSvg style={{ width: 16, height: 16 }} />}
    />
  );
}

export function CopyStat({ content = "Copybook" }: Pick<StatProps, "content">) {
  const color = colors.pink;

  return (
    <CommonStat
      content={content}
      color={color}
      icon={<ChainInSvg style={{ width: 16, height: 16 }} />}
    />
  );
}

export function ExcludeStat({ content }: Pick<StatProps, "content">) {
  const color = colors.red;

  return (
    <CommonStat
      content={content}
      color={color}
      icon={<ExcludeInSvg style={{ width: 16, height: 16 }} />}
    />
  );
}
