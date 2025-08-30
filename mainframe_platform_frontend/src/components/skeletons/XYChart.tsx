import React from "react";
import ContentLoader, { IContentLoaderProps } from "react-content-loader";

const XYChart = (props: React.JSX.IntrinsicAttributes & IContentLoaderProps) => {
  return (
    <ContentLoader
      viewBox='0 0 400 300'
      height='100%'
      width='100%'
      preserveAspectRatio='xMinYMin meet'
      {...props}
    >
      <rect x='40' y='20' rx='4' ry='4' width='2' height='250' />
      <rect x='40' y='270' rx='4' ry='4' width='340' height='2' />
      {[
        { x: 60, height: 120 },
        { x: 100, height: 80 },
        { x: 140, height: 150 },
        { x: 180, height: 100 },
        { x: 220, height: 180 },
        { x: 260, height: 130 },
        { x: 300, height: 90 },
        { x: 340, height: 170 }
      ].map(({ x, height }, index) => (
        <rect key={index} x={x} y={270 - height} rx='4' ry='4' width='20' height={height} />
      ))}
    </ContentLoader>
  );
};

XYChart.metadata = {
  name: "XYChart",
  description: "XYChart Skeleton",
  filename: "XYChart"
};

export default XYChart;
