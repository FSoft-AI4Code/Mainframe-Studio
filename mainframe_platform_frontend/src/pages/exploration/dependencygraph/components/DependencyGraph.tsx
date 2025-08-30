import * as d3 from "d3";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useResizeDetector } from "react-resize-detector";

import unknowImg from "@assets/svg/unknow-icon.svg";
import { allColors } from "@style";
import { useSystemGraph } from "@hooks";
import { Node } from "@types";

import { Node as NodeGraph } from "../../entrypoints/fake/graph";

import { legendsGraph } from "./LegendDependencyGraph";
import { boxHeight, GraphSvg, GraphWrapper } from "./styles";

interface DependencyGraphProps {
  initialScale?: number;
}

type DNode = Required<d3.SimulationNodeDatum>;
export function DependencyGraph({ initialScale = 1 }: DependencyGraphProps) {
  const ref = useRef<SVGSVGElement>(null);
  const { width: widthWrap, ref: refWrap } = useResizeDetector();
  const [dimensions, setDimensions] = useState({
    width: widthWrap || document.getElementById("root")?.clientWidth || 900,
    height: document.getElementById("root")?.clientHeight || 600
  });
  const { nodes, links } = useSystemGraph();

  const zoomed = useCallback((e: { transform: number }) => {
    const svg = d3.select(ref.current);
    const g = svg.selectChildren("g");
    g.attr("transform", e.transform);
  }, []);

  const zoom = useMemo(() => d3.zoom().scaleExtent([0.5, 8]).on("zoom", zoomed), []);

  // > Config
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

    const simulation = d3
      .forceSimulation(nodes as d3.SimulationNodeDatum[])
      .force(
        "link",
        d3
          .forceLink(links)
          .id(d => (d as NodeGraph)._id)
          .distance(100)
      )
      .force("charge", d3.forceManyBody().strength(-500))
      .force("x", d3.forceX())
      .force("y", d3.forceY());

    // * Create G
    const glink = svg
      .append("g")
      .attr("id", "link")
      .attr("stroke", allColors.grey11)
      .attr("stroke-opacity", 0.6);

    const gnode = svg.append("g").attr("id", "node");

    const markerBoxWidth = 13;
    const markerBoxHeight = 20;
    const refX = 14;
    const refY = 7.5;

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
      .attr("stroke-width", 0)
      // trick to rotate marker by 180 degree
      .attr("transform", "scale(2, 2)");

    // * Add elements
    const link = glink
      .selectAll("line")
      .data(links)
      .join("line")
      .attr("stroke-width", 2)
      .attr("cursor", "pointer")
      .attr("marker-end", "url(#arrow)");

    const node = gnode
      .selectAll("g")
      .data(nodes)
      .join("g")
      .attr("class", "node")
      .attr("id", d => d._id)
      .attr("fill", "transparent")
      .attr("cursor", "pointer");
    // .on("mouseover", onHoverInNode)
    // .on("mouseout", onHoverOutNode);

    node
      .filter((d: Node) => d.status !== "DEAD")
      .append("image")
      .attr("xlink:href", (d: Node) => {
        const { label, status } = d || {};
        const isMissing = status === ("MISSING" as const);
        if (["JCL_FUJITSU", "JCL_IBM", "JCL"]?.includes(label))
          return !isMissing ? legendsGraph.JCL?.img : legendsGraph.JCL.missingImg;
        return !isMissing
          ? legendsGraph[label as keyof typeof legendsGraph]?.img || unknowImg
          : legendsGraph[label as keyof typeof legendsGraph]?.missingImg || unknowImg;
      })
      .attr("width", 20)
      .attr("height", 20)
      .attr("x", -10)
      .attr("y", -10);

    node
      .filter((d: Node) => d.status !== "DEAD")
      .append("text")
      .attr("dx", boxHeight / 2)
      .attr("dy", 18)
      .attr("fill", allColors.primary10)
      .text(d => d.name);

    // * Simulation
    // Set the position attributes of links and nodes each time the simulation ticks.
    simulation.on("tick", () => {
      if (!ref.current) return;
      link
        .attr("x1", d => (d.source as unknown as DNode).x)
        .attr("y1", d => (d.source as unknown as DNode).y)
        .attr("x2", d => (d.target as unknown as DNode).x)
        .attr("y2", d => (d.target as unknown as DNode).y);

      node
        .attr(
          "transform",
          d => "translate(" + (d as unknown as DNode).x + "," + (d as unknown as DNode).y + ")"
        )
        .attr("cx", d => (d as unknown as DNode).x)
        .attr("cy", d => (d as unknown as DNode).y);
    });

    // * Event
    // - Link
    link.call(
      d3
        .drag()
        .on("start", () => {})
        .on("drag", () => {})
        .on("end", () => {}) as never
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
        }) as never
    );

    // - Zoom
    svg.call(zoom as never);

    // - Set initial zoom scale
    svg.call(zoom.transform as never, d3.zoomIdentity.scale(initialScale));
  }, [ref, nodes, links]);

  // > Zoom observe and resize
  useEffect(() => {
    if (!widthWrap) return;
    const clientHeight = document.getElementById("root")?.clientHeight;

    setDimensions(s => ({
      width: widthWrap,
      height: clientHeight ? clientHeight - 190 : s.height
    }));
  }, [widthWrap]);

  useEffect(() => {
    const observeTarget = ref.current as Element;
    const resizeObserver = new ResizeObserver(entries => {
      entries.forEach(entry => {
        setDimensions(entry.contentRect);
      });
    });
    resizeObserver.observe(observeTarget);
    return () => resizeObserver.unobserve(observeTarget);
  }, [ref]);

  useEffect(() => {
    const svg = d3.select(ref.current);
    svg.attr("width", dimensions.width).attr("height", dimensions.height);
  }, [dimensions]);

  return (
    <GraphWrapper ref={refWrap} id='graph-page'>
      <GraphSvg ref={ref}></GraphSvg>
    </GraphWrapper>
  );
}
