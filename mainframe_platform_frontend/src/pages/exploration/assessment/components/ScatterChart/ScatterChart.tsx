/* eslint-disable @typescript-eslint/no-explicit-any */
import { ReloadOutlined, SearchOutlined, ZoomInOutlined, ZoomOutOutlined } from "@ant-design/icons";
import { Button, Select } from "antd";
import * as d3 from "d3";
import { zoomIdentity } from "d3";
import { t } from "i18next";
import { PropsWithChildren, useCallback, useEffect, useRef, useState } from "react";

import { ContainerChartSearch, WrapChartToolsInside } from "@components";
import { useFullScreen, useSelectMenuSearch } from "@hooks";
import { colors } from "@style";
import { ClusterDataType } from "@types";
import { getFillColor } from "@utils";

import { AxisBottom, AxisLeft, DialogChart } from "./components";
import { Wrapper } from "./styles";

type Props = {
  clusterData: ClusterDataType;
};

type SelectedData = Record<keyof ClusterDataType | "key", any>;

export const ScatterChart: React.FC<Props> = ({ clusterData }) => {
  const fullScreenHook = useFullScreen("scatter-chart");
  const searchProps = useSelectMenuSearch(clusterData, data => {
    return Object.keys(data.name).map(k => ({
      value: k,
      label: data.name[k]
    }));
  });
  const refZoom = useRef<d3.ZoomBehavior<Element, unknown>>();
  const [currentYZoomState, setCurrentYZoomState] = useState(zoomIdentity);
  const [currentXZoomState, setCurrentXZoomState] = useState(zoomIdentity);
  // const [legendData, setLegendData] = useState<string[]>([])
  const [selectedData, setSelectedData] = useState<string[]>([]);
  const [clickedData, setClickedData] = useState<SelectedData>();
  const [k, setK] = useState(1);
  const [x, setX] = useState(0);
  const [y, setY] = useState(0);
  const [width, setWidth] = useState(document.getElementById("root")?.clientWidth || 1000);
  const [height, setHeight] = useState(document.getElementById("root")?.clientHeight || 1000);

  const refSvg: any = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    // recaculate with case delay fullscreen change
    setTimeout(() => {
      setWidth(document.getElementById("root")?.clientWidth || 1000);
      setHeight(document.getElementById("root")?.clientHeight || 1000);
    }, 50);
  }, [fullScreenHook.isFullScreen]);

  function getValue(data: ClusterDataType["x1"] | ClusterDataType["x2"]) {
    return Object.values(data).map(d => d);
  }

  const getMinValue = (data: ClusterDataType["x1"] | ClusterDataType["x2"]) => {
    const min = Math.min(...getValue(data));
    return min;
  };

  const getMaxValue = (data: ClusterDataType["x1"] | ClusterDataType["x2"]) => {
    const max = Math.max(...getValue(data));
    return max;
  };

  const reset = useCallback(() => {
    // setFilter('')
    // refActive.current = d3.select(null)

    const svg = d3.select(refSvg.current);
    if (refZoom.current)
      svg.transition().duration(750).call(refZoom.current.transform, d3.zoomIdentity);
  }, []);

  const onClickZoomIn = () => {
    const svg = d3.select(refSvg.current);
    if (refZoom.current) refZoom.current.scaleBy(svg.transition().duration(750), 1.2);
  };

  const onClickZoomOut = () => {
    const svg = d3.select(refSvg.current);
    if (refZoom.current) refZoom.current.scaleBy(svg.transition().duration(750), 0.8);
  };

  const [xMin, xMax, yMin, yMax] = [
    getMinValue(clusterData.x1 || {}),
    getMaxValue(clusterData.x1 || {}),
    getMinValue(clusterData.x2 || {}),
    getMaxValue(clusterData.x2 || {})
  ];

  const xScale = d3.scaleLinear().domain([xMin, xMax]).range([0, width]);
  const yScale = d3.scaleLinear().domain([yMin, yMax]).range([height, 0]);

  const ZoomableSVG: React.FC<PropsWithChildren> = ({ children }) => {
    if (currentXZoomState) {
      const newXScale = currentXZoomState.rescaleX(xScale);
      xScale.domain(newXScale.domain()).range(newXScale.range());
    }

    if (currentYZoomState) {
      const newYScale = currentYZoomState.rescaleY(yScale);
      yScale.domain(newYScale.domain()).range(newYScale.range());
    }

    useEffect(() => {
      const zoom = d3
        .zoom()
        .scaleExtent([0.5, 20])
        .extent([
          [0, 0],
          [width, height]
        ])
        .on("zoom", event => {
          let { k: prevK, x: prevX, y: prevY } = zoomIdentity;
          const { k: newK, x: newX, y: newY } = event.transform;
          setK(newK);
          setX(newX);
          setY(newY);
          setCurrentXZoomState(
            currentXZoomState.translate((newX - prevX) / prevK, 0).scale(newK / prevK)
          );
          setCurrentYZoomState(
            currentYZoomState.translate(0, (newY - prevY) / prevK).scale(newK / prevK)
          );
          prevK = event.transform.k;
          prevX = event.transform.x;
          prevY = event.transform.y;
        });

      d3.select(refSvg.current).call(zoom);
      refZoom.current = zoom;
    }, [currentXZoomState, currentYZoomState, xScale, yScale]);

    return (
      <svg ref={refSvg} width={width} height={height}>
        <AxisLeft yScale={yScale} pixelsPerTick={40} width={width} />
        <g transform={`translate(${x},${y})scale(${k})`}>{children}</g>
        <g transform={`translate(0, ${height - 50})`} style={{ width: width }}>
          <AxisBottom xScale={xScale} pixelsPerTick={40} height={height} />
        </g>
      </svg>
    );
  };

  const ChartContent: React.FC<{ data: ClusterDataType }> = ({ data }) => {
    return (
      <>
        {Object.keys(data?.x1 || {}).map((key, index) => {
          const [cx, cy] = [xScale(clusterData.x1[key]), yScale(clusterData.x2[key])];
          return (
            <circle
              key={index}
              style={{ zIndex: 1000 }}
              r={13}
              cx={cx}
              cy={cy}
              opacity={1}
              fill={getFillColor(clusterData.cluster[key])}
              stroke={getFillColor(clusterData.cluster[key])}
              fillOpacity={!selectedData || selectedData.includes(key) ? 1 : 0.1}
              strokeWidth={!selectedData || selectedData.includes(key) ? 1 : 0}
              onClick={() => {
                d3.select("#count").style("display", "none");

                setClickedData({
                  key,
                  cluster: clusterData.cluster[key],
                  path: clusterData.path[key],
                  x1: clusterData.x1[key],
                  x2: clusterData.x2[key],
                  name: clusterData.name[key],
                  start_line: clusterData.start_line[key]
                });
              }}
              onMouseOver={function (e) {
                const tooltip = d3.select("#tooltip").style("position", "relative");
                tooltip
                  .select("#count")
                  .html(
                    `<div class="wrapper">
                      <div class="title">SECTION: ${clusterData.name[key]}</div>
                      <div class="path">PATH: ${clusterData.path[key]}</div>
                    </div>`
                  )
                  .style("position", "fixed")
                  .style("top", e.clientY + 20 + "px")
                  .style("left", e.clientX - 40 + "px")
                  .style("display", "block");
              }}
              onMouseOut={function () {
                d3.select("#count").style("display", "none");
              }}
            />
          );
        })}
      </>
    );
  };

  // useEffect(() => {
  //   setLegendData(Array.from(new Set(Object.values(clusterData.cluster))).map(o => String(o)))
  // }, [clusterData])

  useEffect(() => {
    const key = searchProps.value;
    if (!key) setSelectedData(Object.keys(clusterData.name));
    else {
      setSelectedData([key]);
    }
  }, [searchProps.value]);

  useEffect(() => {
    const selectOptions = searchProps.options;
    if (!selectOptions) return;
    const clusterKeys = Object.keys(clusterData.name);

    if (selectOptions.length === clusterKeys.length && searchProps.refValue.current)
      setSelectedData([searchProps.refValue.current]);
    else setSelectedData(selectOptions.map(o => o.value as string));
  }, [searchProps.options]);

  return (
    <Wrapper style={{ width: width, height: height }} id='scatter-chart'>
      <ContainerChartSearch className='container-chart-search'>
        <Select
          {...searchProps}
          suffixIcon={<SearchOutlined />}
          placeholder={t("component.input.search_blob")}
          allowClear
        />
      </ContainerChartSearch>
      {/* <WrapChartLegend>
        <Legend data={legendData} />
      </WrapChartLegend> */}
      <div id='tooltip' style={{ color: colors.colorWhite00 }}>
        <div id='count'></div>
      </div>
      <ZoomableSVG>
        <ChartContent data={clusterData} />
      </ZoomableSVG>
      <WrapChartToolsInside isFullScreen={fullScreenHook.isFullScreen}>
        <Button onClick={onClickZoomIn} icon={<ZoomInOutlined />} />
        <Button onClick={onClickZoomOut} icon={<ZoomOutOutlined />} />
        <Button onClick={reset} icon={<ReloadOutlined />} />
        <Button onClick={fullScreenHook.onClickFullScreen} icon={fullScreenHook.renderIcon()} />
      </WrapChartToolsInside>
      <DialogChart
        selectedId={clickedData?.path}
        close={() => {
          setClickedData(undefined);
          // searchProps.setValue(undefined)
        }}
      />
    </Wrapper>
  );
};
