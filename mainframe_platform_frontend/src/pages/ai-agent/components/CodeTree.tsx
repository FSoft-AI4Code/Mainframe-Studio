/* eslint-disable no-console */
import React from "react";
import { Tree, type TreeDataNode } from "antd";
import { GetProps } from "react-redux/es/types";

import { Flex, Typography } from "@components";

type DirectoryTreeProps = GetProps<typeof Tree.DirectoryTree>;
const { DirectoryTree } = Tree;

const treeData: TreeDataNode[] = [
  {
    key: "0",
    title: "DEMOLAB_SRC_FPTLT01",
    children: [
      {
        title: "DEMO.CARDDEMO.BMS",
        key: "0-0",
        children: [
          { isLeaf: true, title: "COACTUP", key: "0-0-0" },
          { isLeaf: true, title: "COACTVW", key: "0-0-1" },
          { isLeaf: true, title: "COADM01", key: "0-0-2" },
          { isLeaf: true, title: "COBIL00", key: "0-0-3" },
          { isLeaf: true, title: "COCRDLI", key: "0-0-4" },
          { isLeaf: true, title: "COCRDSL", key: "0-0-5" },
          { isLeaf: true, title: "COCRDUP", key: "0-0-6" },
          { isLeaf: true, title: "COMEN01", key: "0-0-7" },
          { isLeaf: true, title: "CORPT00", key: "0-0-8" },
          { isLeaf: true, title: "COSGN00", key: "0-0-9" },
          { isLeaf: true, title: "COSGN00B", key: "0-0-10" },
          { isLeaf: true, title: "COTRN00", key: "0-0-11" },
          { isLeaf: true, title: "COTRN01", key: "0-0-12" },
          { isLeaf: true, title: "COTRN02", key: "0-0-13" },
          { isLeaf: true, title: "COUSR00", key: "0-0-14" },
          { isLeaf: true, title: "COUSR01", key: "0-0-15" },
          { isLeaf: true, title: "COUSR02", key: "0-0-16" },
          { isLeaf: true, title: "COUSR03", key: "0-0-17" }
        ]
      },
      {
        title: "DEMO.CARDDEMO.CBL",
        key: "0-1",
        children: [
          { isLeaf: true, title: "CBACT01C", key: "0-1-0" },
          { isLeaf: true, title: "CBACT02C", key: "0-1-1" },
          { isLeaf: true, title: "CBACT03C", key: "0-1-2" },
          { isLeaf: true, title: "CBACT04C", key: "0-1-3" },
          { isLeaf: true, title: "CBCUS01C", key: "0-1-4" },
          { isLeaf: true, title: "CBSTM03A", key: "0-1-5" },
          { isLeaf: true, title: "CBSTM03B", key: "0-1-6" },
          { isLeaf: true, title: "CBTRN01C", key: "0-1-7" },
          { isLeaf: true, title: "CBTRN02C", key: "0-1-8" },
          { isLeaf: true, title: "CBTRN03C", key: "0-1-9" },
          { isLeaf: true, title: "COACTUPC", key: "0-1-10" },
          { isLeaf: true, title: "COACTVWC", key: "0-1-11" },
          { isLeaf: true, title: "COADM01C", key: "0-1-12" },
          { isLeaf: true, title: "COBIL00C", key: "0-1-13" },
          { isLeaf: true, title: "COCRDLIC", key: "0-1-14" },
          { isLeaf: true, title: "COCRDSLC", key: "0-1-15" },
          { isLeaf: true, title: "COCRDUPC", key: "0-1-16" },
          { isLeaf: true, title: "COMEN01C", key: "0-1-17" },
          { isLeaf: true, title: "CORPT00C", key: "0-1-18" },
          { isLeaf: true, title: "COSGN00C", key: "0-1-19" },
          { isLeaf: true, title: "COTRN00C", key: "0-1-20" },
          { isLeaf: true, title: "COTRN01C", key: "0-1-21" },
          { isLeaf: true, title: "COTRN02C", key: "0-1-22" },
          { isLeaf: true, title: "COUSR00C", key: "0-1-23" },
          { isLeaf: true, title: "COUSR01C", key: "0-1-24" },
          { isLeaf: true, title: "COUSR02C", key: "0-1-25" },
          { isLeaf: true, title: "COUSR03C", key: "0-1-26" },
          { isLeaf: true, title: "CSUTLDTC", key: "0-1-27" }
        ]
      },
      {
        title: "DEMO.CARDDEMO.CPY",
        key: "0-2",
        children: [
          { title: "COACTUP", isLeaf: true, key: "0-2-0" },
          { title: "COACTVW", isLeaf: true, key: "0-2-1" },
          { title: "COADM01", isLeaf: true, key: "0-2-2" },
          { title: "COADM02Y", isLeaf: true, key: "0-2-3" },
          { title: "COMEN01", isLeaf: true, key: "0-2-4" },
          { title: "COMEN02Y", isLeaf: true, key: "0-2-5" },
          { title: "CORPT00", isLeaf: true, key: "0-2-6" },
          { title: "COSGN00", isLeaf: true, key: "0-2-7" },
          { title: "COSTM01", isLeaf: true, key: "0-2-8" },
          { title: "COTRN00", isLeaf: true, key: "0-2-9" },
          { title: "COTRN01", isLeaf: true, key: "0-2-10" },
          { title: "COTRN02", isLeaf: true, key: "0-2-11" },
          { title: "COTTL01Y", isLeaf: true, key: "0-2-12" },
          { title: "COUSR00", isLeaf: true, key: "0-2-13" },
          { title: "COUSR01", isLeaf: true, key: "0-2-14" },
          { title: "COUSR02", isLeaf: true, key: "0-2-15" },
          { title: "COUSR03", isLeaf: true, key: "0-2-16" },
          { title: "CSDAT01Y", isLeaf: true, key: "0-2-17" },
          { title: "CSLKPCDY", isLeaf: true, key: "0-2-18" },
          { title: "CSMSG01Y", isLeaf: true, key: "0-2-19" },
          { title: "CSMSG02Y", isLeaf: true, key: "0-2-20" },
          { title: "CSSETATY", isLeaf: true, key: "0-2-21" },
          { title: "CSSTRPFY", isLeaf: true, key: "0-2-22" },
          { title: "CSUSR01Y", isLeaf: true, key: "0-2-23" },
          { title: "CSUTLDPY", isLeaf: true, key: "0-2-24" },
          { title: "CSUTLDWY", isLeaf: true, key: "0-2-25" },
          { title: "CUSTREC", isLeaf: true, key: "0-2-26" },
          { title: "CVACT01Y", isLeaf: true, key: "0-2-27" },
          { title: "CVACT02Y", isLeaf: true, key: "0-2-28" },
          { title: "CVACT03Y", isLeaf: true, key: "0-2-29" },
          { title: "CVCRD01Y", isLeaf: true, key: "0-2-30" },
          { title: "CVCUS01Y", isLeaf: true, key: "0-2-31" },
          { title: "CVTRA01Y", isLeaf: true, key: "0-2-32" },
          { title: "CVTRA02Y", isLeaf: true, key: "0-2-33" },
          { title: "CVTRA03Y", isLeaf: true, key: "0-2-34" },
          { title: "CVTRA04Y", isLeaf: true, key: "0-2-35" },
          { title: "CVTRA05Y", isLeaf: true, key: "0-2-36" },
          { title: "CVTRA06Y", isLeaf: true, key: "0-2-37" },
          { title: "CVTRA07Y", isLeaf: true, key: "0-2-38" },
          { title: "LINHNV0", isLeaf: true, key: "0-2-39" },
          { title: "UNUSED1Y", isLeaf: true, key: "0-2-40" }
        ]
      },
      {
        title: "DEMO.CARDDEMO.CSD",
        key: "0-3",
        children: [
          {
            isLeaf: true,
            key: "0-3-0",
            title: "CSDDEF"
          },
          { isLeaf: true, key: "0-3-1", title: "CSDDEL" }
        ]
      },
      {
        title: "DEMO.CARDDEMO.JCL",
        key: "0-4",
        children: [
          { title: "ACCTFILE", key: "0-4-0", isLeaf: true },
          { title: "CARDFILE", key: "0-4-1", isLeaf: true },
          { title: "CBADMCDJ", key: "0-4-2", isLeaf: true },
          { title: "CICSCOB1", key: "0-4-3", isLeaf: true },
          { title: "CLOSEFIL", key: "0-4-4", isLeaf: true },
          { title: "CMP1BMS", key: "0-4-5", isLeaf: true },
          { title: "CMP1CICS", key: "0-4-6", isLeaf: true },
          { title: "CMP1CSD", key: "0-4-7", isLeaf: true },
          { title: "CMPBATC1", key: "0-4-8", isLeaf: true },
          { title: "CMPBATCH", key: "0-4-9", isLeaf: true },
          { title: "CMPBMS", key: "0-4-10", isLeaf: true },
          { title: "CMPCICS", key: "0-4-11", isLeaf: true },
          { title: "CMPCSD", key: "0-4-12", isLeaf: true },
          { title: "CMPSUB", key: "0-4-13", isLeaf: true },
          { title: "COMBTRAN", key: "0-4-14", isLeaf: true },
          { title: "CREASTMT", key: "0-4-15", isLeaf: true },
          { title: "CUSTFILE", key: "0-4-16", isLeaf: true },
          { title: "DALYREJS", key: "0-4-17", isLeaf: true },
          { title: "DEFCUST", key: "0-4-18", isLeaf: true },
          { title: "DEFGDGB", key: "0-4-19", isLeaf: true },
          { title: "DISCGRP", key: "0-4-20", isLeaf: true },
          { title: "DUSRSECJ", key: "0-4-21", isLeaf: true },
          { title: "IGYWCL", key: "0-4-22", isLeaf: true },
          { title: "INTCALC", key: "0-4-23", isLeaf: true },
          { title: "OPENFIL", key: "0-4-24", isLeaf: true },
          { title: "POSTTRAN", key: "0-4-25", isLeaf: true },
          { title: "PRTCATBL", key: "0-4-26", isLeaf: true },
          { title: "RACFUN", key: "0-4-27", isLeaf: true },
          { title: "READACCT", key: "0-4-28", isLeaf: true },
          { title: "READCARD", key: "0-4-29", isLeaf: true },
          { title: "READCUST", key: "0-4-30", isLeaf: true },
          { title: "READXREF", key: "0-4-31", isLeaf: true },
          { title: "REPTFILE", key: "0-4-32", isLeaf: true },
          { title: "TCATBALF", key: "0-4-33", isLeaf: true },
          { title: "TRANBKP", key: "0-4-34", isLeaf: true },
          { title: "TRANCATG", key: "0-4-35", isLeaf: true },
          { title: "TRANIDX", key: "0-4-36", isLeaf: true },
          { title: "TRANREPT", key: "0-4-37", isLeaf: true },
          { title: "TRANTYPE", key: "0-4-38", isLeaf: true }
        ]
      },
      {
        title: "DEMO.CARDDEMO.PRC.UTIL",
        key: "0-5",
        children: [
          { key: "0-5-0", isLeaf: true, title: "BUILDBAT" },
          { key: "0-5-1", isLeaf: true, title: "BUILDBMS" },
          { key: "0-5-2", isLeaf: true, title: "BUILDONL" }
        ]
      },
      {
        title: "DEMO.CARDDEMO.PROC",
        key: "0-6",
        children: [
          { key: "0-6-0", isLeaf: true, title: "REPROC" },
          { key: "0-6-1", isLeaf: true, title: "TRANREPT" }
        ]
      },
      { key: "0-7", isLeaf: true, title: "DEMO.CARDDEMO.ACCDATA.PS" },
      { key: "0-8", isLeaf: true, title: "DEMO.CARDDEMO.ACCTDATA.PS" },
      { key: "0-9", isLeaf: true, title: "DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS.DAT" },
      { key: "0-10", isLeaf: true, title: "DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS.IDX" },
      { key: "0-11", isLeaf: true, title: "DEMO.CARDDEMO.CARDDATA.PS" },
      { key: "0-12", isLeaf: true, title: "DEMO.CARDDEMO.CARDDATA.VSAM.AIX.IDX" },
      { key: "0-13", isLeaf: true, title: "DEMO.CARDDEMO.CARDDATA.VSAM.KSDS" },
      { key: "0-14", isLeaf: true, title: "DEMO.CARDDEMO.CARDDATA.VSAM.KSDS.IDX" },
      { key: "0-15", isLeaf: true, title: "DEMO.CARDDEMO.CARDXREF.PS" },
      { key: "0-16", isLeaf: true, title: "DEMO.CARDDEMO.CARDXREF.VSAM.KSDS" },
      { key: "0-17", isLeaf: true, title: "DEMO.CARDDEMO.CARDXREF.VSAM.KSDS.IDX" },
      { key: "0-18", isLeaf: true, title: "DEMO.CARDDEMO.CUSTDATA.PS" },
      { key: "0-19", isLeaf: true, title: "DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS.DAT" },
      { key: "0-20", isLeaf: true, title: "DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS.IDX" },
      { key: "0-21", isLeaf: true, title: "DEMO.CARDDEMO.DALYTRAN.PS" },
      { key: "0-22", isLeaf: true, title: "DEMO.CARDDEMO.DALYTRAN.PS.INIT" },
      { key: "0-23", isLeaf: true, title: "DEMO.CARDDEMO.DISCGRP.PS" },
      { key: "0-24", isLeaf: true, title: "DEMO.CARDDEMO.DISCGRP.VSAM.KSDS.DAT" },
      { key: "0-25", isLeaf: true, title: "DEMO.CARDDEMO.SYSTRAN.G0001V00" },
      { key: "0-26", isLeaf: true, title: "DEMO.CARDDEMO.SYSTRAN.G0002V00" },
      { key: "0-27", isLeaf: true, title: "DEMO.CARDDEMO.TCATBALF.PS" },
      { key: "0-28", isLeaf: true, title: "DEMO.CARDDEMO.TCATBALF.VSAM.KSDS.DAT" },
      { key: "0-29", isLeaf: true, title: "DEMO.CARDDEMO.TCATBALF.VSAM.KSDS.IDX" },
      { key: "0-30", isLeaf: true, title: "DEMO.CARDDEMO.TRANCATG.PS" },
      { key: "0-31", isLeaf: true, title: "DEMO.CARDDEMO.TRANCATG.VSAM.KSDS.DAT" },
      { key: "0-32", isLeaf: true, title: "DEMO.CARDDEMO.TRANCATG.VSAM.KSDS.IDX" },
      { key: "0-33", isLeaf: true, title: "DEMO.CARDDEMO.TRANSACT.VSAM.KSDS" },
      { key: "0-34", isLeaf: true, title: "DEMO.CARDDEMO.TRANSACT.VSAM.KSDS.IDX" },
      { key: "0-35", isLeaf: true, title: "DEMO.CARDDEMO.TRANTYPE.PS" },
      { key: "0-36", isLeaf: true, title: "DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS.IDX" },
      { key: "0-37", isLeaf: true, title: "DEMO.CARDDEMO.USRSEC.PS" }
    ]
  }
];

const CodeTree: React.FC = () => {
  const onSelect: DirectoryTreeProps["onSelect"] = (keys, info) => {
    console.log("Trigger Select", keys, info);
  };

  const onExpand: DirectoryTreeProps["onExpand"] = (keys, info) => {
    console.log("Trigger Expand", keys, info);
  };

  return (
    <Flex direction='column' gap={16} style={{ width: "100%" }}>
      <Typography color='primary10' level='body-16b'>
        Code Tree
      </Typography>
      <DirectoryTree
        virtual
        multiple
        // draggable
        blockNode
        // defaultExpandAll
        style={{
          fontSize: 13
        }}
        onSelect={onSelect}
        onExpand={onExpand}
        treeData={treeData}
      />
    </Flex>
  );
};

export default CodeTree;
