/* eslint-disable unused-imports/no-unused-vars */
/* eslint-disable @typescript-eslint/no-unused-vars */
import { FC, useCallback, useEffect, useMemo, useRef, useState } from "react";
import * as d3 from "d3";
import { useResizeDetector } from "react-resize-detector";
import { useSelector } from "react-redux";

import { repositorySelector } from "@store";
import { NetworkingDataType } from "@types";
import { colors } from "@style";
import { useChartTooltip, useGraph } from "@hooks";
import unknowImg from "@assets/svg/unknow-icon.svg";
import { Legend, WrapChartLegend } from "@components";

import { GraphSvg } from "./styles";

type Props = {
  id?: string;
};

type NodeType = NetworkingDataType["nodes"][number];
type LinkType = NetworkingDataType["links"][number];

export const SmallGraph: FC<Props> = ({ id }) => {
  const ref = useRef<any>();
  const { width: widthWrap, ref: refWrap } = useResizeDetector();
  const chartData = useSelector(repositorySelector.selectRepositoryCopyGraph);
  const { legend } = useGraph();
  const { render, onHoverInNode, onHoverOutNode } = useChartTooltip();

  const [dimensions, setDimensions] = useState({
    width: 200,
    height: 70
  });
  const [groups, setGroups] = useState<string[]>([]);

  const zoomed = useCallback((e: any) => {
    const svg = d3.select(ref.current);
    const g = svg.selectAll("g");
    g.attr("transform", e.transform);
  }, []);

  const zoom = useMemo(() => d3.zoom().scaleExtent([0.5, 8]).on("zoom", zoomed), []);

  const onClickLine = (e: PointerEvent, d: LinkType) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const onClickNode = (e: PointerEvent, d: NodeType) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const onDoubleClickNode = (
    e: PointerEvent,
    d: NodeType,
    self: d3.BaseType | SVGCircleElement
  ) => {
    e.preventDefault();
    e.stopPropagation();
  };

  // > Get group list
  useEffect(() => {
    const grs = Array.from(new Set(chartData?.nodes?.map?.(o => o.group)));
    setGroups(grs);
  }, [chartData]);

  useEffect(() => {
    if (!ref.current) return;

    // * Init
    const svg = d3.select(ref.current);
    svg.selectChildren().remove();
    svg
      .attr("width", dimensions.width)
      .attr("height", dimensions.height)
      .attr("viewBox", [
        -dimensions.width / 2,
        -dimensions.height / 2,
        dimensions.width,
        dimensions.height
      ])
      .attr("style", "max-width: 100%; height: auto; background-color: #eeeeee");
    // .on('click', () => {
    //   setSelectedNodes([])
    // })

    const linkSet = new Set([id]);
    const links =
      chartData?.links
        ?.filter(link => link.source === id || link.target === id)
        .map?.(d => ({ ...d })) || [];

    links.forEach(link => {
      linkSet.add(link.source);
      linkSet.add(link.target);
    });
    const nodes =
      chartData?.nodes?.filter(node => linkSet.has(node.id)).map?.(d => ({ ...d })) || [];

    const simulation = d3
      .forceSimulation(nodes as d3.SimulationNodeDatum[])
      .force(
        "link",
        d3.forceLink(links).id(d => (d as NodeType).id)
      )
      .force("charge", d3.forceManyBody())
      .force("x", d3.forceX())
      .force("y", d3.forceY());

    // * Create G
    const glink = svg
      .append("g")
      .attr("id", "link")
      .attr("stroke", colors.grey11)
      .attr("stroke-opacity", 0.6);

    const gnode = svg.append("g").attr("id", "node");

    const markerBoxWidth = 13;
    const markerBoxHeight = 20;
    const refX = 9.3;
    const refY = 3.7;

    // Add arrows active
    svg
      .append("defs")
      .append("marker")
      .attr("id", "arrow")
      .attr("viewBox", [0, 0, markerBoxWidth, markerBoxHeight])
      .attr("refX", refX)
      .attr("refY", refY)
      .attr("markerWidth", markerBoxWidth)
      .attr("markerHeight", markerBoxHeight)
      .attr("orient", "auto-start-reverse")
      .append("path")
      .attr("fill", "#F6D053")
      .attr("d", "M2,2 L2,5 L5,3.7 L2,2")
      .attr("stroke-width", 0);

    // Add arrows in-active
    svg
      .append("defs")
      .append("marker")
      .attr("id", "inactive-arrow")
      .attr("viewBox", [0, 0, markerBoxWidth, markerBoxHeight])
      .attr("refX", refX)
      .attr("refY", refY)
      .attr("markerWidth", markerBoxWidth)
      .attr("markerHeight", markerBoxHeight)
      .attr("orient", "auto-start-reverse")
      .append("path")
      .attr("fill", colors.grey11)
      .attr("d", "M2,2 L2,5 L5,3.7 L2,2")
      .attr("stroke-width", 0);

    // * Add elements
    const link = glink
      .selectAll("line")
      .data(links)
      .join("line")
      .attr("stroke-width", 1)
      .attr("cursor", "pointer")
      .attr("marker-end", "url(#arrow)")
      .on("click", onClickLine);

    const node = gnode
      .selectAll("image")
      .data(nodes)
      .join("image")
      .attr("xlink:href", (d: any) => {
        const nodeType = chartData?.nodes?.find(i => i.id === d?.id)?.group;
        if (nodeType === "JCL_IBM" || nodeType === "JCL_FUJITSU" || nodeType === "JCL") {
          return "";
        }
        return legend?.find(i => i.id === nodeType)?.iconLink || unknowImg;
      })
      .attr("width", (d: any) => {
        const typeSelectype = chartData?.nodes?.find(i => i.id === d?.id)?.group;
        const selectLegend = legend?.find(l => l.id === typeSelectype);
        return selectLegend?.width || 7;
      })
      .attr("height", (d: any) => {
        const typeSelectype = chartData?.nodes?.find(i => i.id === d?.id)?.group;
        const selectLegend = legend?.find(l => l.id === typeSelectype);
        return selectLegend?.height || 7;
      })
      .attr("x", (d: any) => {
        const typeSelectype = chartData?.nodes?.find(i => i.id === d?.id)?.group;
        const selectLegend = legend?.find(l => l.id === typeSelectype);
        return selectLegend?.x || -3.5;
      })
      .attr("y", (d: any) => {
        const typeSelectype = chartData?.nodes?.find(i => i.id === d?.id)?.group;
        const selectLegend = legend?.find(l => l.id === typeSelectype);
        return selectLegend?.y || -3.5;
      })
      .attr("cursor", "pointer")
      .attr("fill", d => groups?.indexOf(d.group) || "0")
      .attr("opacity", d => (d.id === id ? "1" : "0.4"))
      .on("click", onClickNode)
      .on("dblclick", function (e, d) {
        onDoubleClickNode(e, d, this);
      })
      .on("mouseover", onHoverInNode)
      .on("mouseout", onHoverOutNode);

    // * Simulation
    // Set the position attributes of links and nodes each time the simulation ticks.
    simulation.on("tick", () => {
      link
        .attr("x1", d => (d.source as unknown as Required<d3.SimulationNodeDatum>).x)
        .attr("y1", d => (d.source as unknown as Required<d3.SimulationNodeDatum>).y)
        .attr("x2", d => (d.target as unknown as Required<d3.SimulationNodeDatum>).x)
        .attr("y2", d => (d.target as unknown as Required<d3.SimulationNodeDatum>).y);

      node
        .attr("transform", (d: any) => "translate(" + d.x + "," + d.y + ")")
        .attr("cx", d => (d as unknown as Required<d3.SimulationNodeDatum>).x)
        .attr("cy", d => (d as unknown as Required<d3.SimulationNodeDatum>).y);
    });

    // * Event
    // - Link
    link.call(
      d3
        .drag()
        .on("start", () => {})
        .on("drag", () => {})
        .on("end", () => {}) as d3.DragBehavior<any, any, any>
    );

    // - Node
    node.call(
      d3
        .drag()
        .on("start", event => {
          if (!event.active) simulation.alphaTarget(0.3).restart();
          event.subject.fx = event.subject.x;
          event.subject.fy = event.subject.y;
        })
        .on("drag", event => {
          event.subject.fx = event.x;
          event.subject.fy = event.y;
        })
        .on("end", event => {
          if (!event.active) simulation.alphaTarget(0);
          event.subject.fx = null;
          event.subject.fy = null;
        }) as d3.DragBehavior<any, any, any>
    );

    // - Zoom
    svg.call(zoom);
  }, [ref, id]);

  // > Zoom observe and resize
  useEffect(() => {
    if (!widthWrap) return;
    setDimensions(s => ({
      width: widthWrap,
      height: document.getElementById("small-graph")?.clientHeight || s.height
    }));
  }, [widthWrap, id]);

  useEffect(() => {
    const observeTarget = ref.current;
    const resizeObserver = new ResizeObserver(entries => {
      entries.forEach(entry => {
        setDimensions(entry.contentRect);
      });
    });
    resizeObserver.observe(observeTarget);
    return () => resizeObserver.disconnect();
  }, [ref]);

  useEffect(() => {
    const svg = d3.select(ref.current);
    svg.attr("width", dimensions.width).attr("height", dimensions.height);
  }, [dimensions]);

  return (
    <div style={{ width: "100%", height: 350 }}>
      <WrapChartLegend>
        <Legend data={legend?.filter(i => i.type !== "group")} size='small' />
      </WrapChartLegend>

      <div ref={refWrap} style={{ height: "100%" }} id='small-graph'>
        <GraphSvg ref={ref}></GraphSvg>
      </div>
    </div>
  );
};
