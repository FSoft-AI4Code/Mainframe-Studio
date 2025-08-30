import { Card } from "antd";
import { useParams } from "react-router-dom";

import { OverflowEmpty, Typography } from "@components";
import { allColors } from "@style";

import { ScrollableWrapper } from "../../data-asset/styles";

export default function EmptyReport() {
  const { type = "", name = "" } = useParams();

  return (
    <ScrollableWrapper direction='column'>
      <Card
        title={
          <Typography level='title-24b' color='primary10'>
            {type} Program Report: {name}
          </Typography>
        }
        style={{ background: allColors.neutral1, width: "100%", height: "100%" }}
        bodyStyle={{ height: "calc(100% - 56px)" }}
      >
        <OverflowEmpty />
      </Card>
    </ScrollableWrapper>
  );
}
