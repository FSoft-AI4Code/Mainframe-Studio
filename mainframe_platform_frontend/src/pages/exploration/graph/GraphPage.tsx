import * as d3 from "d3";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useDispatch } from "react-redux";
import { useResizeDetector } from "react-resize-detector";
import { useParams } from "react-router-dom";

import { repositoryApi } from "@api";
import { OverflowLoading } from "@components";
import { useChartTooltip, useGraph, useSelectMenuSearch } from "@hooks";
import { repositoryActions } from "@store";
import { colors } from "@style";
import { LinkGraphType, NetworkingDataType, NodeGraphType } from "@types";
import { getFillColor } from "@utils";

import { DialogChart, DialogLink } from "./components";
import { GraphTool } from "./components/GraphTool";
import { Graph as GraphSvg, GraphWrapper, Wrapper } from "./styles";

const boxHeight = 25;

const Graph: React.FC<{ chartData: NetworkingDataType }> = ({ chartData }) => {
  const { render, onHoverInNode, onHoverOutNode } = useChartTooltip();
  const searchProps = useSelectMenuSearch(chartData, data => {
    return data.nodes.map(o => ({
      value: o.id,
      label: o.name
    }));
  });

  const refDebounceClick = useRef<NodeJS.Timeout>();
  const ref = useRef<any>();
  const { width: widthWrap, ref: refWrap } = useResizeDetector();
  const [dimensions, setDimensions] = useState({
    width: widthWrap || document.getElementById("root")?.clientWidth || 900,
    height: document.getElementById("root")?.clientHeight || 600
  });
  const [filter, setFilter] = useState<string>("");
  const [selectedNodes, setSelectedNodes] = useState<string[]>([]);
  const [clickedNodeId, setClickedNodeId] = useState<string>();
  const [isDeadCode, setIsDeadCode] = useState<boolean>();
  const [linkSelected, selectLink] = useState<LinkGraphType | undefined>();
  const refActive = useRef<any>(d3.select(null));
  const [groups, setGroups] = useState<string[]>([]);

  const { legend } = useGraph();

  const clearDebounceClick = () => {
    if (refDebounceClick.current) {
      clearTimeout(refDebounceClick.current);
      refDebounceClick.current = undefined;
    }
  };

  const zoomed = useCallback((e: any) => {
    const svg = d3.select(ref.current);
    const g = svg.selectChildren("g");
    g.attr("transform", e.transform);
  }, []);

  const zoom = useMemo(() => d3.zoom().scaleExtent([0.5, 8]).on("zoom", zoomed), []);

  const reset = useCallback(() => {
    setFilter("");
    // setSelectedNodes([])
    refActive.current = d3.select(null);

    const svg = d3.select(ref.current);
    svg.transition().duration(750).call(zoom.transform, d3.zoomIdentity);
  }, []);

  const onClickZoomIn = () => {
    const svg = d3.select(ref.current);
    zoom.scaleBy(svg.transition().duration(750), 1.4);
  };

  // const onClickZoomOut = () => {
  //   const svg = d3.select(ref.current);
  //   zoom.scaleBy(svg.transition().duration(750), 0.6);
  // };

  const focusByNodeId = (id: string) => {
    const svg = d3.select(ref.current);
    const g = d3.select("g#node");
    const listNode = g.selectAll("g");
    const node = listNode.filter((data: any) => id === data.id).node() as any;

    const bbox = node.getBBox(),
      bounds = [
        [bbox.x, bbox.y],
        [bbox.x + bbox.width, bbox.y + bbox.height]
      ];

    const dx = bounds[1][0] - bounds[0][0],
      dy = bounds[1][1] - bounds[0][1],
      x = (bounds[0][0] + bounds[1][0]) / 2,
      y = (bounds[0][1] + bounds[1][1]) / 2,
      scale = Math.max(
        1,
        Math.min(2.5, 0.9 / Math.max(dx / dimensions.width, dy / dimensions.height))
      );
    const tx = -x;
    const ty = -y;

    svg
      .transition()
      .duration(750)
      .call(zoom.transform, d3.zoomIdentity.scale(scale).translate(tx, ty));
  };

  const onClickNode = (e: PointerEvent, d: NodeGraphType) => {
    e.preventDefault();
    e.stopPropagation();
    // uncomment if want to show nodes related when click
    // const linksRelated = chartData.links?.filter(i => i.target === d.id || i.source === d.id)
    // const nodesRelated = linksRelated?.map(i => {
    //   if (i.source === d.id) {
    //     return i.target
    //   }
    //   return i.source
    // })
    // setSelectedNodes([...nodesRelated, d.id])
    clearDebounceClick();
    refDebounceClick.current = setTimeout(() => {
      clearDebounceClick();
      // setSelectedNodes([d.id])
      setClickedNodeId(d.id);
    }, 200);
  };

  const onClickLine = (e: PointerEvent, d: LinkGraphType) => {
    e.preventDefault();
    e.stopPropagation();
    clearDebounceClick();

    refDebounceClick.current = setTimeout(() => {
      clearDebounceClick();
      selectLink(d);
    }, 200);
  };

  const onDoubleClickNode = (
    e: PointerEvent,
    d: NodeGraphType,
    self: d3.BaseType | SVGCircleElement
  ) => {
    e.preventDefault();
    e.stopPropagation();
    clearDebounceClick();

    if (refActive.current && refActive.current.node() === self) return reset();
    if (refActive.current) refActive.current.classed("active", false);
    refActive.current = d3.select(self).classed("active", true);

    focusByNodeId(d.id);
  };

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
    // .on('click', () => {
    //   setSelectedNodes([])
    // })

    const links = chartData.links.map(d => ({ ...d }));
    const nodes = chartData.nodes
      .map(d => ({ ...d }))
      // COBOL_TRASH: remove jcl and other element from graph
      .filter(
        ({ group }) =>
          group !== "OTHER" && group !== "JCL_FUJITSU" && group !== "JCL_IBM" && group !== "JCL"
      );

    const simulation = d3
      .forceSimulation(nodes as d3.SimulationNodeDatum[])
      .force(
        "link",
        d3
          .forceLink(links)
          .id(d => (d as NodeGraphType).id)
          .distance(100)
      )
      .force("charge", d3.forceManyBody().strength(-500))
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
    const refX = 30;
    const refY = 16.5;

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
      .attr("transform", "rotate(180, 6.5, 10)");

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
      .attr("stroke-width", 0)
      .attr("transform", "rotate(180, 6.5, 10)");

    // * Add elements
    const link = glink
      .selectAll("line")
      .data(links)
      .join("line")
      .attr("stroke-width", 2)
      .attr("cursor", "pointer")
      .attr("marker-start", "url(#arrow)")
      .on("click", onClickLine);

    // const node = gnode
    //   .selectAll('image')
    //   .data(nodes)
    //   .join('image')
    //   .attr('xlink:href', (d: any) => {
    //     const typeSelectype = chartData?.nodes?.find(i => i.id === d?.id)?.type
    //     if (typeSelectype === 'jcl') {
    //       return ''
    //     }
    //     return legend?.find(i => i.id === typeSelectype)?.iconLink || unknowImg
    //   })
    //   .attr('width', 7)
    //   .attr('height', 7)
    //   .attr('x', -3.5)
    //   .attr('y', -3.5)
    //   .attr('fill', d => groups.indexOf(d.group) || '0')
    //   .on('click', onClickNode)
    //   .on('dblclick', function (e, d) {
    //     onDoubleClickNode(e, d, this)
    //   })
    //   .on('mouseover', onHoverInNode)
    //   .on('mouseout', onHoverOutNode)

    const node = gnode
      .selectAll("g")
      .data(nodes)
      .join("g")
      .attr("class", "node")
      .attr("id", d => d.id)
      .attr("fill", "white")
      .attr("cursor", "pointer")
      .on("click", onClickNode)
      .on("dblclick", function (e, d) {
        onDoubleClickNode(e, d, this);
      })
      .on("mouseover", onHoverInNode)
      .on("mouseout", onHoverOutNode);

    node
      .append("rect")
      .attr("fill", d => {
        let color;

        switch (d.group) {
          case "JCL":
            color = colors.purple;
            break;
          case "JCL_IBM":
            color = colors.purple;
            break;
          case "JCL_FUJITSU":
            color = colors.purple;
            break;
          case "COPY":
            color = colors.pink;
            break;
          case "DB":
            color = colors.orange;
            break;
          case "SCREEN":
            color = colors.blue;
            break;
          case "OTHER":
            color = colors.red;
            break;
          default:
            color = colors.purple;
            break;
        }
        return color;
      })
      .attr("rx", 5);

    node
      .append("text")
      .attr("dx", boxHeight / 2)
      .attr("dy", 18)
      .attr("fill", "white")
      .text(d => d.name);

    gnode
      .selectAll("rect")
      .attr("width", (d: any) => {
        let currentEl;

        ref.current.childNodes[1].childNodes.forEach((el: any) => {
          if (el.id === d.id) currentEl = el;
        });
        return (
          ((
            (currentEl as unknown as Node).childNodes[1] as unknown as SVGTextElement
          )?.getComputedTextLength?.() ?? 20) + boxHeight
        );
      })
      .attr("height", boxHeight);
    // * Simulation
    // Set the position attributes of links and nodes each time the simulation ticks.
    simulation.on("tick", () => {
      if (!ref.current) return;
      link
        .attr("x1", d => {
          let currentEl;

          ref.current.childNodes[1].childNodes.forEach((el: any) => {
            if (el.id === (d.source as unknown as NodeGraphType).id) currentEl = el;
          });

          const boxLength =
            ((
              (currentEl as unknown as Node).childNodes[1] as unknown as SVGTextElement
            )?.getComputedTextLength?.() ?? 20) + boxHeight;
          return (d.source as unknown as Required<d3.SimulationNodeDatum>).x + boxLength / 2;
        })
        .attr(
          "y1",
          d => (d.source as unknown as Required<d3.SimulationNodeDatum>).y + boxHeight / 2
        )
        .attr("x2", d => {
          let currentEl;

          ref.current.childNodes[1].childNodes.forEach((el: any) => {
            if (el.id === (d.target as unknown as NodeGraphType).id) currentEl = el;
          });

          const boxLength =
            ((
              (currentEl as unknown as Node).childNodes[1] as unknown as SVGTextElement
            )?.getComputedTextLength?.() ?? 20) + boxHeight;
          return (d.target as unknown as Required<d3.SimulationNodeDatum>).x + boxLength / 2;
        })
        .attr(
          "y2",
          d => (d.target as unknown as Required<d3.SimulationNodeDatum>).y + boxHeight / 2
        );

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
  }, [ref]);

  // > Get group list
  useEffect(() => {
    const grs = Array.from(new Set(chartData.nodes.map(o => o.group)));
    setGroups(grs);
  }, [chartData]);

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
    const observeTarget = ref.current;
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

  // > Select
  useEffect(() => {
    // const color = d3.scaleOrdinal(d3.schemeCategory10)
    const node = d3.select("g#node");
    const listNode = node.selectAll("g");
    const link = d3.select("g#link");
    const lines = link.selectAll("line");

    // * Node
    const notSelectedCircles = listNode.filter((data: any) => !selectedNodes.includes(data.id));
    const selectedCircles = listNode.filter((data: any) => selectedNodes.includes(data.id));
    notSelectedCircles
      .attr("fill", (d: any) => getFillColor(groups.indexOf(d.group) || "0"))
      .attr("opacity", 0.1);
    selectedCircles
      .attr("fill", (d: any) => getFillColor(groups.indexOf(d.group) || "0"))
      .attr("opacity", 1);

    // * Link
    const notSelectedLines = lines.filter((data: any) => !selectedNodes.includes(data.source.id));
    const selectedLines = lines.filter((data: any) => selectedNodes.includes(data.source.id));
    notSelectedLines.attr("stroke", colors.grey11).attr("marker-start", "url(#inactive-arrow)");
    selectedLines
      .attr("stroke", (d: any) => getFillColor(groups.indexOf(d.group) || "0"))
      .attr("marker-start", "url(#arrow)");
  }, [selectedNodes]);

  useEffect(() => {
    const id = searchProps.value;
    let listNodes = chartData.nodes;
    if (isDeadCode) {
      listNodes = chartData?.nodes?.filter(i => i.is_deadcode) || [];
    }

    if (!id) {
      setSelectedNodes(listNodes.map(o => o.id as string));
      reset();
    } else {
      setSelectedNodes([id]);
      focusByNodeId(id);

      const g = d3.select("g#node");
      const listNode = g.selectAll("g");
      const node = listNode.filter((data: any) => id === data.id).node() as any;
      if (node) refActive.current = d3.select(node);
    }
  }, [searchProps.value, isDeadCode]);

  useEffect(() => {
    const selectOptions = searchProps.options;
    if (!selectOptions) return;
    if (selectOptions.length === chartData.nodes.length && searchProps.refValue.current)
      setSelectedNodes([searchProps.refValue.current]);
    else setSelectedNodes(selectOptions.map(o => o.value as string));
  }, [searchProps.options]);

  // > Filter
  useEffect(() => {
    setSelectedNodes(chartData.nodes.filter(o => o.group === filter).map(o => o.id));
  }, [filter]);

  const colorByType = useMemo(() => {
    if (linkSelected) {
      return legend?.find(i => i.id === "link")?.backgroundColor;
    }
    const nodeSelected = chartData?.nodes?.find(i => i.id === clickedNodeId);
    if (nodeSelected) {
      return legend?.find(i => i.id === nodeSelected?.group)?.backgroundColor || colors.red;
    }
    return undefined;
  }, [clickedNodeId, chartData?.nodes, linkSelected]);

  const onChangeDeadCode = (e?: boolean) => {
    setIsDeadCode(e);
  };

  return (
    <Wrapper gap={18} direction='column'>
      <GraphTool
        onChangeDeadCode={onChangeDeadCode}
        isDeadCode={isDeadCode}
        onClickZoomIn={onClickZoomIn}
        searchProps={searchProps}
        chartData={chartData}
      />
      <GraphWrapper ref={refWrap} id='graph-page'>
        <GraphSvg ref={ref}></GraphSvg>
        {render()}
        {clickedNodeId ? (
          <DialogChart
            selectedId={clickedNodeId}
            nodes={chartData?.nodes}
            colorByType={colorByType}
            close={() => setClickedNodeId(undefined)}
          />
        ) : null}
        <DialogLink
          linkSelected={linkSelected}
          colorByType={colorByType}
          nodes={chartData?.nodes}
          close={() => selectLink(undefined)}
        />
      </GraphWrapper>
    </Wrapper>
  );
};

export const GraphPage: React.FC = () => {
  const { repoId } = useParams();
  const dispatch = useDispatch();

  const [chartData, setChartData] = useState<NetworkingDataType | null>();

  useEffect(() => {
    const fetchChartData = async () => {
      if (!repoId) return;
      const res = await repositoryApi.getGraphChartDataRequest(repoId);

      if (!res?.data) throw new Error();
      setChartData(res.data);
      dispatch(repositoryActions.setCopyGraph(res.data));
    };

    fetchChartData();
  }, [repoId]);

  return chartData ? <Graph chartData={chartData} /> : <OverflowLoading />;
};
