/* eslint-disable @typescript-eslint/no-explicit-any */
import { FileGroup } from "@types";

export type Node = {
  _id: string;
  label: FileGroup;
  name: string;
  status: "ALIVE" | "MISSING";
  group: string[];
  loc?: number | null;
  complexity?: number | null;
};

export type Edge = {
  _id: string;
  source: string;
  target: string;
  type: "HAS_INTERACT" | "HAS_COPYBOOK" | "STATIC_CALL" | "JOB_RUN" | "EXEC_PGM";
  group: string[];
  properties: {
    label: string;
    calls?: Array<{
      paragraph: string;
      identifier: string[];
      programName: string;
    }>;
    steps?: Array<any>;
  };
};

export type EntryPoint = {
  _id: string;
  name: string;
  label: FileGroup;
  group: string[];
  status: "ALIVE";
};

export type GraphData = {
  repository_id: string;
  nodes: Node[];
  edges: Edge[];
  entry_points: EntryPoint[];
};

export const fakeData: {
  repository_id: string;
  nodes: Node[];
  edges: Edge[];
  entry_points: EntryPoint[];
} = {
  repository_id: "6720a7324bb4f21d4ecd99ce",
  nodes: [
    {
      _id: "672b29c93e4eb3f0ec40c013",
      name: "COMBTRAN",
      label: "JCL_IBM",
      group: ["COMBTRAN"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c014",
      name: "SORT",
      label: "UTILITY",
      group: ["COMBTRAN", "CREASTMT", "PRTCATBL", "TRANREPT"],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c015",
      name: "IDCAMS",
      label: "UTILITY",
      group: [
        "ACCTFILE",
        "CARDFILE",
        "COMBTRAN",
        "CREASTMT",
        "CUSTFILE",
        "DALYREJS",
        "DEFCUST",
        "DEFGDGB",
        "DISCGRP",
        "DUSRSECJ",
        "REPROC",
        "REPTFILE",
        "TCATBALF",
        "TRANBKP",
        "TRANCATG",
        "TRANFILE",
        "TRANIDX",
        "TRANTYPE",
        "XREFFILE"
      ],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c016",
      name: "COUSR03",
      label: "COPY",
      group: ["COUSR03"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c017",
      name: "COBIL00C",
      label: "COBOL",
      group: ["COBIL00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c018",
      name: "COCOM01Y",
      label: "COPY",
      group: [
        "COADM01",
        "COBIL00",
        "COMEN01",
        "CORPT00",
        "COSGN00",
        "COTRN00",
        "COTRN01",
        "COTRN02",
        "COUSR00",
        "COUSR01",
        "COUSR02",
        "COUSR03"
      ],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c019",
      name: "COBIL00",
      label: "COPY",
      group: ["COBIL00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c01a",
      name: "COTTL01Y",
      label: "COPY",
      group: [
        "COADM01",
        "COBIL00",
        "COMEN01",
        "CORPT00",
        "COSGN00",
        "COTRN00",
        "COTRN01",
        "COTRN02",
        "COUSR00",
        "COUSR01",
        "COUSR02",
        "COUSR03"
      ],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c01b",
      name: "CSDAT01Y",
      label: "COPY",
      group: [
        "COADM01",
        "COBIL00",
        "COMEN01",
        "CORPT00",
        "COSGN00",
        "COTRN00",
        "COTRN01",
        "COTRN02",
        "COUSR00",
        "COUSR01",
        "COUSR02",
        "COUSR03"
      ],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c01c",
      name: "CSMSG01Y",
      label: "COPY",
      group: [
        "COADM01",
        "COBIL00",
        "COMEN01",
        "CORPT00",
        "COSGN00",
        "COTRN00",
        "COTRN01",
        "COTRN02",
        "COUSR00",
        "COUSR01",
        "COUSR02",
        "COUSR03"
      ],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c01d",
      name: "CVACT01Y",
      label: "COPY",
      group: ["COBIL00", "COTRN02", "CREASTMT", "INTCALC", "POSTTRAN", "READACCT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c01e",
      name: "CVACT03Y",
      label: "COPY",
      group: ["COBIL00", "COTRN02", "CREASTMT", "INTCALC", "POSTTRAN", "READXREF", "TRANREPT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c01f",
      name: "CVTRA05Y",
      label: "COPY",
      group: [
        "COBIL00",
        "CORPT00",
        "COTRN00",
        "COTRN01",
        "COTRN02",
        "INTCALC",
        "POSTTRAN",
        "TRANREPT"
      ],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c020",
      name: "DFHAID",
      label: "UTILITY",
      group: [
        "COADM01",
        "COBIL00",
        "COMEN01",
        "CORPT00",
        "COSGN00",
        "COTRN00",
        "COTRN01",
        "COTRN02",
        "COUSR00",
        "COUSR01",
        "COUSR02",
        "COUSR03"
      ],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c021",
      name: "DFHBMSCA",
      label: "UTILITY",
      group: [
        "COADM01",
        "COBIL00",
        "COMEN01",
        "CORPT00",
        "COSGN00",
        "COTRN00",
        "COTRN01",
        "COTRN02",
        "COUSR00",
        "COUSR01",
        "COUSR02",
        "COUSR03"
      ],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c022",
      name: "COBIL00",
      label: "BMS",
      group: ["COBIL00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c023",
      name: "POSTTRAN",
      label: "JCL_IBM",
      group: ["POSTTRAN"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c024",
      name: "CBTRN02C",
      label: "COBOL",
      group: ["POSTTRAN"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c025",
      name: "COUSR01C",
      label: "COBOL",
      group: ["COUSR01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c026",
      name: "COUSR01",
      label: "COPY",
      group: ["COUSR01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c027",
      name: "CSUSR01Y",
      label: "COPY",
      group: ["COADM01", "COMEN01", "COSGN00", "COUSR00", "COUSR01", "COUSR02", "COUSR03"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c028",
      name: "COUSR01",
      label: "BMS",
      group: ["COUSR01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c029",
      name: "COTRN01",
      label: "BMS",
      group: ["COTRN01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c02a",
      name: "CVCRD01Y",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c02b",
      name: "CSLKPCDY",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c02c",
      name: "CMPBMS",
      label: "JCL_IBM",
      group: ["CMPBMS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c02d",
      name: "SDSF",
      label: "COBOL",
      group: [
        "CARDFILE",
        "CLOSEFIL",
        "CMP1BMS",
        "CMP1CICS",
        "CMPBMS",
        "CMPCICS",
        "CUSTFILE",
        "OPENFIL",
        "TRANFILE"
      ],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c02e",
      name: "CREASTMT",
      label: "JCL_IBM",
      group: ["CREASTMT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c02f",
      name: "IEFBR14",
      label: "UTILITY",
      group: ["CREASTMT", "DUSRSECJ", "PRTCATBL"],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c030",
      name: "CBSTM03A",
      label: "COBOL",
      group: ["CREASTMT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c031",
      name: "DEFGDGB",
      label: "JCL_IBM",
      group: ["DEFGDGB"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c032",
      name: "COMEN02Y",
      label: "COPY",
      group: ["COMEN01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c033",
      name: "COUSR02",
      label: "COPY",
      group: ["COUSR02"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c034",
      name: "CBACT02C",
      label: "COBOL",
      group: ["READCARD"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c035",
      name: "CEE3ABD",
      label: "COBOL",
      group: [
        "CREASTMT",
        "INTCALC",
        "POSTTRAN",
        "READACCT",
        "READCARD",
        "READCUST",
        "READXREF",
        "TRANREPT"
      ],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c036",
      name: "CVACT02Y",
      label: "COPY",
      group: ["READCARD"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c037",
      name: "TRANREPT",
      label: "JCL_IBM",
      group: ["TRANREPT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c038",
      name: "CBTRN03C",
      label: "COBOL",
      group: ["TRANREPT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c039",
      name: "COTRN00",
      label: "BMS",
      group: ["COTRN00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c03a",
      name: "CVTRA03Y",
      label: "COPY",
      group: ["TRANREPT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c03b",
      name: "CVTRA04Y",
      label: "COPY",
      group: ["TRANREPT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c03c",
      name: "CVTRA07Y",
      label: "COPY",
      group: ["TRANREPT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c03d",
      name: "TCATBALF",
      label: "JCL_IBM",
      group: ["TCATBALF"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c03e",
      name: "CUSTFILE",
      label: "JCL_IBM",
      group: ["CUSTFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c03f",
      name: "CORPT00C",
      label: "COBOL",
      group: ["CORPT00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c040",
      name: "CORPT00",
      label: "COPY",
      group: ["CORPT00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c041",
      name: "CORPT00",
      label: "BMS",
      group: ["CORPT00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c042",
      name: "OPENFIL",
      label: "JCL_IBM",
      group: ["OPENFIL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c043",
      name: "COTRN00",
      label: "COPY",
      group: ["COTRN00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c044",
      name: "COCRDLI",
      label: "BMS",
      group: ["COCRDLI"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c045",
      name: "TRANIDX",
      label: "JCL_IBM",
      group: ["TRANIDX"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c046",
      name: "CVTRA06Y",
      label: "COPY",
      group: ["POSTTRAN"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c047",
      name: "CVTRA01Y",
      label: "COPY",
      group: ["INTCALC", "POSTTRAN"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c048",
      name: "REPROC",
      label: "JCL_IBM",
      group: ["REPROC"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c049",
      name: "CBADMCDJ",
      label: "JCL_IBM",
      group: ["CBADMCDJ"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04a",
      name: "DFHCSDUP",
      label: "UTILITY",
      group: ["CBADMCDJ", "CMP1CSD", "CMPCSD"],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04b",
      name: "COUSR02",
      label: "BMS",
      group: ["COUSR02"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04c",
      name: "CBACT01C",
      label: "COBOL",
      group: ["READACCT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04d",
      name: "COSGN00B",
      label: "BMS",
      group: ["COSGN00B"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04e",
      name: "DALYREJS",
      label: "JCL_IBM",
      group: ["DALYREJS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04f",
      name: "CMP1CSD",
      label: "JCL_IBM",
      group: ["CMP1CSD"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c050",
      name: "ACCTFILE",
      label: "JCL_IBM",
      group: ["ACCTFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c051",
      name: "CSUTLDTC",
      label: "COBOL",
      group: ["COTRN02"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c052",
      name: "CEEDAYS",
      label: "COBOL",
      group: ["COTRN02"],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c053",
      name: "CVCUS01Y",
      label: "COPY",
      group: ["READCUST"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c054",
      name: "BUILDBMS",
      label: "JCL_IBM",
      group: ["BUILDBMS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c055",
      name: "COACTUP",
      label: "BMS",
      group: ["COACTUP"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c056",
      name: "COMEN01",
      label: "COPY",
      group: ["COMEN01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c057",
      name: "COACTUPC",
      label: "COBOL",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c058",
      name: "CSUTLDWY",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c059",
      name: "COACTUP",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c05a",
      name: "CSMSG02Y",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c05b",
      name: "CSSETATY",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c05c",
      name: "CSSTRPFY",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c05d",
      name: "CSUTLDPY",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c05e",
      name: "COTRN02C",
      label: "COBOL",
      group: ["COTRN02"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c05f",
      name: "COTRN02",
      label: "COPY",
      group: ["COTRN02"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c060",
      name: "COTRN02",
      label: "BMS",
      group: ["COTRN02"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c061",
      name: "CBSTM03B",
      label: "COBOL",
      group: ["CREASTMT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c062",
      name: "CSDDEL",
      label: "CSD",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c063",
      name: "REPTFILE",
      label: "JCL_IBM",
      group: ["REPTFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c064",
      name: "DEFCUST",
      label: "JCL_IBM",
      group: ["DEFCUST"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c065",
      name: "COUSR00",
      label: "COPY",
      group: ["COUSR00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c066",
      name: "COUSR03C",
      label: "COBOL",
      group: ["COUSR03"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c067",
      name: "COUSR03",
      label: "BMS",
      group: ["COUSR03"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c068",
      name: "COTRN01C",
      label: "COBOL",
      group: ["COTRN01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c069",
      name: "COTRN01",
      label: "COPY",
      group: ["COTRN01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c06a",
      name: "CBCUS01C",
      label: "COBOL",
      group: ["READCUST"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c06b",
      name: "CMPCICS",
      label: "JCL_IBM",
      group: ["CMPCICS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c06c",
      name: "CMP1CICS",
      label: "JCL_IBM",
      group: ["CMP1CICS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c06d",
      name: "COACTVW",
      label: "PLI",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c06e",
      name: "COADM01C",
      label: "COBOL",
      group: ["COADM01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c06f",
      name: "COADM02Y",
      label: "COPY",
      group: ["COADM01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c070",
      name: "COADM01",
      label: "COPY",
      group: ["COADM01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c071",
      name: "COADM01",
      label: "BMS",
      group: ["COADM01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c072",
      name: "COSGN00",
      label: "BMS",
      group: ["COSGN00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c073",
      name: "COCRDSLC",
      label: "COBOL",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c074",
      name: "COCRDSL",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c075",
      name: "CUSTREC",
      label: "COPY",
      group: ["CREASTMT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c076",
      name: "CBTRN01C",
      label: "COBOL",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c077",
      name: "BUILDBAT",
      label: "JCL_IBM",
      group: ["BUILDBAT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c078",
      name: "COCRDSL",
      label: "BMS",
      group: ["COCRDSL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c079",
      name: "COMEN01C",
      label: "COBOL",
      group: ["COMEN01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c07a",
      name: "COMEN01",
      label: "BMS",
      group: ["COMEN01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c07b",
      name: "COCRDUPC",
      label: "COBOL",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c07c",
      name: "COCRDUP",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c07d",
      name: "CICSCOB1",
      label: "JCL_IBM",
      group: ["CICSCOB1"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c07e",
      name: "COUSR02C",
      label: "COBOL",
      group: ["COUSR02"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c07f",
      name: "CVTRA02Y",
      label: "COPY",
      group: ["INTCALC"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c080",
      name: "INTCALC",
      label: "JCL_IBM",
      group: ["INTCALC"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c081",
      name: "CBACT04C",
      label: "COBOL",
      group: ["INTCALC"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c082",
      name: "READCARD",
      label: "JCL_IBM",
      group: ["READCARD"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c083",
      name: "TRANTYPE",
      label: "JCL_IBM",
      group: ["TRANTYPE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c084",
      name: "COTRN00C",
      label: "COBOL",
      group: ["COTRN00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c085",
      name: "DISCGRP",
      label: "JCL_IBM",
      group: ["DISCGRP"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c086",
      name: "COCRDUP",
      label: "BMS",
      group: ["COCRDUP"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c087",
      name: "CARDFILE",
      label: "JCL_IBM",
      group: ["CARDFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c088",
      name: "READXREF",
      label: "JCL_IBM",
      group: ["READXREF"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c089",
      name: "CBACT03C",
      label: "COBOL",
      group: ["READXREF"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08a",
      name: "TRANCATG",
      label: "JCL_IBM",
      group: ["TRANCATG"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08b",
      name: "CLOSEFIL",
      label: "JCL_IBM",
      group: ["CLOSEFIL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08c",
      name: "TRANBKP",
      label: "JCL_IBM",
      group: ["TRANBKP"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08d",
      name: "BUILDONL",
      label: "JCL_IBM",
      group: ["BUILDONL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08e",
      name: "DUSRSECJ",
      label: "JCL_IBM",
      group: ["DUSRSECJ"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08f",
      name: "IEBGENER",
      label: "UTILITY",
      group: ["DUSRSECJ"],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c090",
      name: "UNUSED1Y",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c091",
      name: "COUSR00C",
      label: "COBOL",
      group: ["COUSR00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c092",
      name: "COUSR00",
      label: "BMS",
      group: ["COUSR00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c093",
      name: "COSGN00",
      label: "COPY",
      group: ["COSGN00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c094",
      name: "LINHNV0",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c095",
      name: "PRTCATBL",
      label: "JCL_IBM",
      group: ["PRTCATBL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c096",
      name: "READCUST",
      label: "JCL_IBM",
      group: ["READCUST"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c097",
      name: "COCRDLIC",
      label: "COBOL",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c098",
      name: "COCRDLI",
      label: "COPY",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c099",
      name: "XREFFILE",
      label: "JCL_IBM",
      group: ["XREFFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c09a",
      name: "COSTM01",
      label: "COPY",
      group: ["CREASTMT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c09b",
      name: "READACCT",
      label: "JCL_IBM",
      group: ["READACCT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c09c",
      name: "COSGN00C",
      label: "COBOL",
      group: ["COSGN00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c09d",
      name: "COACTVWC",
      label: "COBOL",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c09e",
      name: "COACTVW",
      label: "COPY",
      group: [],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c09f",
      name: "CMPSUB",
      label: "JCL_IBM",
      group: ["CMPSUB"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a0",
      name: "TRANFILE",
      label: "JCL_IBM",
      group: ["TRANFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a1",
      name: "COACTVW",
      label: "BMS",
      group: ["COACTVW"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a2",
      name: "CMPBATCH",
      label: "JCL_IBM",
      group: ["CMPBATCH"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a3",
      name: "CMP1BMS",
      label: "JCL_IBM",
      group: ["CMP1BMS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a4",
      name: "IGYWCL",
      label: "JCL_IBM",
      group: ["IGYWCL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a5",
      name: "RACFUN",
      label: "JCL_IBM",
      group: ["RACFUN"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a6",
      name: "IRRDBU00",
      label: "UTILITY",
      group: ["RACFUN"],
      status: "MISSING"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a7",
      name: "CMPCSD",
      label: "JCL_IBM",
      group: ["CMPCSD"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a8",
      name: "CSDDEF",
      label: "CSD",
      group: [],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a9",
      name: "CMPBATC1",
      label: "JCL_IBM",
      group: ["CMPBATC1"],
      status: "ALIVE"
    }
  ],
  edges: [
    {
      _id: "672b29c93e4eb3f0ec40c0aa",
      source: "672b29c93e4eb3f0ec40c013",
      target: "672b29c93e4eb3f0ec40c014",
      type: "EXEC_PGM",
      group: ["COMBTRAN"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05R",
            code: {
              content:
                "//STEP05R  EXEC PGM=SORT\r\n//SORTIN   DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(0)\r\n//         DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.SYSTRAN(0)\r\n//SYMNAMES DD *\r\nTRAN-ID,1,16,CH\r\n//SYSIN    DD *\r\n SORT FIELDS=(TRAN-ID,A)\r\n//SYSOUT   DD SYSOUT=*\r\n//SORTOUT  DD DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(*.SORTIN),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED(+1)\r\n",
              start_line: 22,
              end_line: 37
            },
            statements: [
              {
                ddname: "SORTIN",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(0)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(0)",
                    variable_name: "SORTIN",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(0)",
                    program_id: "SORT"
                  }
                ],
                logic: null
              },
              {
                ddname: "",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.SYSTRAN(0)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.SYSTRAN(0)",
                    variable_name: "UNKNOWN",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.SYSTRAN(0)",
                    program_id: "SORT"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYMNAMES",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "TRAN-ID,1,16,CH\r\n"
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " SORT FIELDS=(TRAN-ID,A)\r\n"
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SORTOUT",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "(*.SORTIN)",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED(+1)",
                    variable_name: "SORTOUT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED(+1)",
                    program_id: "SORT"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ab",
      source: "672b29c93e4eb3f0ec40c013",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["COMBTRAN"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//TRANSACT DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED(+1)\r\n//TRANVSAM DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(TRANSACT) OUTFILE(TRANVSAM)\r\n",
              start_line: 41,
              end_line: 48
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TRANSACT",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED(+1)",
                    variable_name: "TRANSACT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED(+1)",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "TRANVSAM",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS",
                    variable_name: "TRANVSAM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(TRANSACT) OUTFILE(TRANVSAM)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ac",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ad",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c019",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ae",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0af",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b0",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b1",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c01d",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b2",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b3",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c01f",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b4",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b5",
      source: "672b29c93e4eb3f0ec40c017",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COBIL00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b6",
      source: "672b29c93e4eb3f0ec40c022",
      target: "672b29c93e4eb3f0ec40c017",
      type: "HAS_INTERACT",
      group: ["COBIL00"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b7",
      source: "672b29c93e4eb3f0ec40c023",
      target: "672b29c93e4eb3f0ec40c024",
      type: "EXEC_PGM",
      group: ["POSTTRAN"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=CBTRN02C\r\n//STEPLIB  DD DISP=SHR,\r\n//            DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB\r\n//SYSPRINT DD SYSOUT=*\r\n//SYSOUT   DD SYSOUT=*\r\n//TRANFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS\r\n//DALYTRAN DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.DALYTRAN.PS\r\n//XREFFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS\r\n//DALYREJS DD DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(RECFM=F,LRECL=430,BLKSIZE=0),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.DALYREJS(+1)\r\n//ACCTFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS\r\n//TCATBALF DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS\r\n",
              start_line: 23,
              end_line: 42
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.LOADLIB"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    program_id: "CBTRN02C"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TRANFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS",
                    variable_name: "TRANFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS",
                    program_id: "CBTRN02C"
                  }
                ],
                logic: null
              },
              {
                ddname: "DALYTRAN",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.DALYTRAN.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.DALYTRAN.PS",
                    variable_name: "DALYTRAN",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.DALYTRAN.PS",
                    program_id: "CBTRN02C"
                  }
                ],
                logic: null
              },
              {
                ddname: "XREFFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    variable_name: "XREFFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    program_id: "CBTRN02C"
                  }
                ],
                logic: null
              },
              {
                ddname: "DALYREJS",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "F",
                  RECFM: "F",
                  LRECL: "F",
                  BLKSIZE: "F",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.DALYREJS(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.DALYREJS(+1)",
                    variable_name: "DALYREJS",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.DALYREJS(+1)",
                    program_id: "CBTRN02C"
                  }
                ],
                logic: null
              },
              {
                ddname: "ACCTFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
                    variable_name: "ACCTFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
                    program_id: "CBTRN02C"
                  }
                ],
                logic: null
              },
              {
                ddname: "TCATBALF",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS",
                    variable_name: "TCATBALF",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS",
                    program_id: "CBTRN02C"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b8",
      source: "672b29c93e4eb3f0ec40c024",
      target: "672b29c93e4eb3f0ec40c035",
      type: "STATIC_CALL",
      group: ["POSTTRAN"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "9999-ABEND-PROGRAM",
            identifier: [],
            programName: "'CEE3ABD'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0b9",
      source: "672b29c93e4eb3f0ec40c024",
      target: "672b29c93e4eb3f0ec40c046",
      type: "HAS_COPYBOOK",
      group: ["POSTTRAN"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ba",
      source: "672b29c93e4eb3f0ec40c024",
      target: "672b29c93e4eb3f0ec40c01f",
      type: "HAS_COPYBOOK",
      group: ["POSTTRAN"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0bb",
      source: "672b29c93e4eb3f0ec40c024",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: ["POSTTRAN"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0bc",
      source: "672b29c93e4eb3f0ec40c024",
      target: "672b29c93e4eb3f0ec40c01d",
      type: "HAS_COPYBOOK",
      group: ["POSTTRAN"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0bd",
      source: "672b29c93e4eb3f0ec40c024",
      target: "672b29c93e4eb3f0ec40c047",
      type: "HAS_COPYBOOK",
      group: ["POSTTRAN"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0be",
      source: "672b29c93e4eb3f0ec40c025",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COUSR01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0bf",
      source: "672b29c93e4eb3f0ec40c025",
      target: "672b29c93e4eb3f0ec40c026",
      type: "HAS_COPYBOOK",
      group: ["COUSR01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c0",
      source: "672b29c93e4eb3f0ec40c025",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COUSR01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c1",
      source: "672b29c93e4eb3f0ec40c025",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COUSR01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c2",
      source: "672b29c93e4eb3f0ec40c025",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COUSR01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c3",
      source: "672b29c93e4eb3f0ec40c025",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: ["COUSR01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c4",
      source: "672b29c93e4eb3f0ec40c025",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COUSR01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c5",
      source: "672b29c93e4eb3f0ec40c025",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COUSR01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c6",
      source: "672b29c93e4eb3f0ec40c028",
      target: "672b29c93e4eb3f0ec40c025",
      type: "HAS_INTERACT",
      group: ["COUSR01"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c7",
      source: "672b29c93e4eb3f0ec40c029",
      target: "672b29c93e4eb3f0ec40c068",
      type: "HAS_INTERACT",
      group: ["COTRN01"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c8",
      source: "672b29c93e4eb3f0ec40c02c",
      target: "672b29c93e4eb3f0ec40c02d",
      type: "EXEC_PGM",
      group: ["CMPBMS"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "SDSF1",
            code: {
              content:
                "//SDSF1 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COACTUP) NEWCOPY'\r\n",
              start_line: 6,
              end_line: 10
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COACTUP) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSF2",
            code: {
              content:
                "//SDSF2 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COACTVW) NEWCOPY'\r\n",
              start_line: 13,
              end_line: 17
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COACTVW) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSF3",
            code: {
              content:
                "//SDSF3 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COADM01) NEWCOPY'\r\n",
              start_line: 20,
              end_line: 24
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COADM01) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSF4",
            code: {
              content:
                "//SDSF4 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COBIL00) NEWCOPY'\r\n",
              start_line: 27,
              end_line: 31
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COBIL00) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSF5",
            code: {
              content:
                "//SDSF5 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COCRDLI) NEWCOPY'\r\n",
              start_line: 34,
              end_line: 38
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COCRDLI) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSF6",
            code: {
              content:
                "//SDSF6 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COCRDSL) NEWCOPY'\r\n",
              start_line: 41,
              end_line: 45
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COCRDSL) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSF7",
            code: {
              content:
                "//SDSF7 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COCRDUP) NEWCOPY'\r\n",
              start_line: 48,
              end_line: 52
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COCRDUP) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSF8",
            code: {
              content:
                "//SDSF8 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COMEN01) NEWCOPY'\r\n",
              start_line: 55,
              end_line: 59
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COMEN01) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSF9",
            code: {
              content:
                "//SDSF9 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(CORPT00) NEWCOPY'\r\n",
              start_line: 62,
              end_line: 66
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(CORPT00) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSFA",
            code: {
              content:
                "//SDSFA EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COSGN00) NEWCOPY'\r\n",
              start_line: 69,
              end_line: 73
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COSGN00) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSFB",
            code: {
              content:
                "//SDSFB EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COTRN00) NEWCOPY'\r\n",
              start_line: 76,
              end_line: 80
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COTRN00) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSFC",
            code: {
              content:
                "//SDSFC EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COTRN01) NEWCOPY'\r\n",
              start_line: 83,
              end_line: 87
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COTRN01) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSFD",
            code: {
              content:
                "//SDSFD EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COUSR01) NEWCOPY'\r\n",
              start_line: 104,
              end_line: 108
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COUSR01) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSFE",
            code: {
              content:
                "//SDSFE EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CEMT SET PROG(COUSR02) NEWCOPY'\r\n",
              start_line: 111,
              end_line: 115
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CEMT SET PROG(COUSR02) NEWCOPY'\r\n"
              }
            ]
          },
          {
            step_name: "SDSFF",
            code: {
              content:
                "//SDSFF EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSA,'CCEMT SET PROG(COUSR03) NEWCOPY'\r\n",
              start_line: 118,
              end_line: 122
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSA,'CCEMT SET PROG(COUSR03) NEWCOPY'\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0c9",
      source: "672b29c93e4eb3f0ec40c02e",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["CREASTMT"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "DELDEF01",
            code: {
              content:
                "//DELDEF01 EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n  DELETE    FPTLT01.DEMO.CARDDEMO.TRXFL.SEQ\r\n  DELETE    FPTLT01.DEMO.CARDDEMO.TRXFL.VSAM.KSDS                     -\r\n            CLUSTER\r\n  SET       MAXCC = 0\r\n  DEFINE    CLUSTER  (NAME(FPTLT01.DEMO.CARDDEMO.TRXFL.VSAM.KSDS)     -\r\n                      KEYS(32 0)                                -\r\n                      VOLUMES(TSU023)                           -\r\n                      RECORDSIZE(350 350)                       -\r\n                      SHAREOPTIONS(2 3)                         -\r\n                      ERASE                                     -\r\n                      INDEXED                                   -\r\n                      CYL(1 5))                                 -\r\n            DATA      (NAME(FPTLT01.DEMO.CARDDEMO.TRXFL.DATA)         -\r\n                      CISZ(4096))                               -\r\n            INDEX     (NAME(FPTLT01.DEMO.CARDDEMO.TRXFL.INDEX))\r\n",
              start_line: 22,
              end_line: 39
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "  DELETE    FPTLT01.DEMO.CARDDEMO.TRXFL.SEQ\r\n  DELETE    FPTLT01.DEMO.CARDDEMO.TRXFL.VSAM.KSDS                     -\r\n            CLUSTER\r\n  SET       MAXCC = 0\r\n  DEFINE    CLUSTER  (NAME(FPTLT01.DEMO.CARDDEMO.TRXFL.VSAM.KSDS)     -\r\n                      KEYS(32 0)                                -\r\n                      VOLUMES(TSU023)                           -\r\n                      RECORDSIZE(350 350)                       -\r\n                      SHAREOPTIONS(2 3)                         -\r\n                      ERASE                                     -\r\n                      INDEXED                                   -\r\n                      CYL(1 5))                                 -\r\n            DATA      (NAME(FPTLT01.DEMO.CARDDEMO.TRXFL.DATA)         -\r\n                      CISZ(4096))                               -\r\n            INDEX     (NAME(FPTLT01.DEMO.CARDDEMO.TRXFL.INDEX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP020",
            code: {
              content:
                "//STEP020  EXEC PGM=IDCAMS,COND=(0,NE)\r\n//SYSPRINT DD  SYSOUT=*\r\n//INFILE   DD  DISP=SHR,DSN=FPTLT01.DEMO.CARDDEMO.TRXFL.SEQ\r\n//OUTFILE  DD  DISP=SHR,DSN=FPTLT01.DEMO.CARDDEMO.TRXFL.VSAM.KSDS\r\n//SYSIN    DD  *\r\n  REPRO INFILE(INFILE) OUTFILE(OUTFILE)\r\n",
              start_line: 56,
              end_line: 61
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "INFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "SHR"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SHR",
                    variable_name: "INFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRXFL.SEQ",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "OUTFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "SHR"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SHR",
                    variable_name: "OUTFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRXFL.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "  REPRO INFILE(INFILE) OUTFILE(OUTFILE)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ca",
      source: "672b29c93e4eb3f0ec40c02e",
      target: "672b29c93e4eb3f0ec40c014",
      type: "EXEC_PGM",
      group: ["CREASTMT"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP010",
            code: {
              content:
                "//STEP010  EXEC PGM=SORT\r\n//SORTIN   DD  DISP=SHR,DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSOUT   DD  SYSOUT=*\r\n//SORTOUT  DD  DSN=FPTLT01.DEMO.CARDDEMO.TRXFL.SEQ,\r\n//             DISP=(NEW,CATLG,DELETE),UNIT=SYSDA,\r\n//             DCB=(LRECL=350,BLKSIZE=3500,RECFM=FB),\r\n//             SPACE=(CYL,(1,1),RLSE)\r\n//SYSIN    DD *\r\n  SORT FIELDS=(263,16,CH,A,1,16,CH,A)\r\n  OUTREC FIELDS=(1:263,16,17:1,262,279:279,50)\r\n",
              start_line: 44,
              end_line: 54
            },
            statements: [
              {
                ddname: "SORTIN",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "SHR"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SHR",
                    variable_name: "SORTIN",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS",
                    program_id: "SORT"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SORTOUT",
                parameters_map: {
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRXFL.SEQ",
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "(NEW,CATLG,DELETE)",
                  DCB: "350",
                  LRECL: "350",
                  BLKSIZE: "350",
                  RECFM: "350",
                  SPACE: "(CYL,(1,1),RLSE)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRXFL.SEQ",
                    variable_name: "SORTOUT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRXFL.SEQ",
                    program_id: "SORT"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "  SORT FIELDS=(263,16,CH,A,1,16,CH,A)\r\n  OUTREC FIELDS=(1:263,16,17:1,262,279:279,50)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0cb",
      source: "672b29c93e4eb3f0ec40c02e",
      target: "672b29c93e4eb3f0ec40c02f",
      type: "EXEC_PGM",
      group: ["CREASTMT"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP030",
            code: {
              content:
                "//STEP030  EXEC PGM=IEFBR14,COND=(0,NE)\r\n//HTMLFILE DD DISP=(MOD,DELETE,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(LRECL=80,BLKSIZE=3200,RECFM=FB),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.STATEMNT.HTML\r\n//STMTFILE DD DISP=(MOD,DELETE,DELETE),\r\n//         DCB=(LRECL=80,BLKSIZE=8000,RECFM=FB),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.STATEMNT.PS\r\n",
              start_line: 66,
              end_line: 75
            },
            statements: [
              {
                ddname: "HTMLFILE",
                parameters_map: {
                  DISP: "(MOD,DELETE,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "80",
                  LRECL: "80",
                  BLKSIZE: "80",
                  RECFM: "80",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.STATEMNT.HTML"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.STATEMNT.HTML",
                    variable_name: "HTMLFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.STATEMNT.HTML",
                    program_id: "IEFBR14"
                  }
                ],
                logic: null
              },
              {
                ddname: "STMTFILE",
                parameters_map: {
                  DISP: "(MOD,DELETE,DELETE)",
                  DCB: "80",
                  LRECL: "80",
                  BLKSIZE: "80",
                  RECFM: "80",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.STATEMNT.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.STATEMNT.PS",
                    variable_name: "STMTFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.STATEMNT.PS",
                    program_id: "IEFBR14"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0cc",
      source: "672b29c93e4eb3f0ec40c02e",
      target: "672b29c93e4eb3f0ec40c030",
      type: "EXEC_PGM",
      group: ["CREASTMT"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP040",
            code: {
              content:
                "//STEP040  EXEC PGM=CBSTM03A,COND=(0,NE)\r\n//STEPLIB  DD  DISP=SHR,DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSOUT   DD  SYSOUT=*\r\n//TRNXFILE DD  DISP=SHR,DSN=FPTLT01.DEMO.CARDDEMO.TRXFL.VSAM.KSDS\r\n//XREFFILE DD  DISP=SHR,DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS\r\n//ACCTFILE DD  DISP=SHR,DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS\r\n//CUSTFILE DD  DISP=SHR,DSN=FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS\r\n//STMTFILE DD DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(LRECL=80,BLKSIZE=8000,RECFM=FB),\r\n//         SPACE=(CYL,(1,1),RLSE), 00,RECFM=FB), ATA.VSAM.KSDS\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.STATEMNT.PS\r\n//HTMLFILE DD  DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(LRECL=100,BLKSIZE=800,RECFM=FB),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.STATEMNT.HTML\r\n",
              start_line: 79,
              end_line: 96
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "SHR"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SHR",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    program_id: "CBSTM03A"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TRNXFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "SHR"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SHR",
                    variable_name: "TRNXFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRXFL.VSAM.KSDS",
                    program_id: "CBSTM03A"
                  }
                ],
                logic: null
              },
              {
                ddname: "XREFFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "SHR"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SHR",
                    variable_name: "XREFFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    program_id: "CBSTM03A"
                  }
                ],
                logic: null
              },
              {
                ddname: "ACCTFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "SHR"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SHR",
                    variable_name: "ACCTFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
                    program_id: "CBSTM03A"
                  }
                ],
                logic: null
              },
              {
                ddname: "CUSTFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "SHR"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SHR",
                    variable_name: "CUSTFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS",
                    program_id: "CBSTM03A"
                  }
                ],
                logic: null
              },
              {
                ddname: "STMTFILE",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "80",
                  LRECL: "80",
                  BLKSIZE: "80",
                  RECFM: "(CYL,(1,1),RLSE)",
                  SPACE: "(CYL,(1,1),RLSE)",
                  UNNAMED_1: "(CYL,(1,1),RLSE)",
                  UNNAMED_2: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.STATEMNT.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.STATEMNT.PS",
                    variable_name: "STMTFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.STATEMNT.PS",
                    program_id: "CBSTM03A"
                  }
                ],
                logic: null
              },
              {
                ddname: "HTMLFILE",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "100",
                  LRECL: "100",
                  BLKSIZE: "100",
                  RECFM: "100",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.STATEMNT.HTML"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.STATEMNT.HTML",
                    variable_name: "HTMLFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.STATEMNT.HTML",
                    program_id: "CBSTM03A"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0cd",
      source: "672b29c93e4eb3f0ec40c030",
      target: "672b29c93e4eb3f0ec40c061",
      type: "STATIC_CALL",
      group: ["CREASTMT"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "1000-XREFFILE-GET-NEXT",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "2000-CUSTFILE-GET",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "3000-ACCTFILE-GET",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "8100-TRNXFILE-OPEN",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "8100-TRNXFILE-OPEN",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "8200-XREFFILE-OPEN",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "8300-CUSTFILE-OPEN",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "8400-ACCTFILE-OPEN",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "8500-READTRNX-READ",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "9100-TRNXFILE-CLOSE",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "9200-XREFFILE-CLOSE",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "9300-CUSTFILE-CLOSE",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          },
          {
            paragraph: "9400-ACCTFILE-CLOSE",
            identifier: ["WS-M03B-AREA"],
            programName: "'CBSTM03B'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ce",
      source: "672b29c93e4eb3f0ec40c030",
      target: "672b29c93e4eb3f0ec40c035",
      type: "STATIC_CALL",
      group: ["CREASTMT"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "9999-ABEND-PROGRAM",
            identifier: [],
            programName: "'CEE3ABD'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0cf",
      source: "672b29c93e4eb3f0ec40c030",
      target: "672b29c93e4eb3f0ec40c09a",
      type: "HAS_COPYBOOK",
      group: ["CREASTMT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d0",
      source: "672b29c93e4eb3f0ec40c030",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: ["CREASTMT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d1",
      source: "672b29c93e4eb3f0ec40c030",
      target: "672b29c93e4eb3f0ec40c075",
      type: "HAS_COPYBOOK",
      group: ["CREASTMT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d2",
      source: "672b29c93e4eb3f0ec40c030",
      target: "672b29c93e4eb3f0ec40c01d",
      type: "HAS_COPYBOOK",
      group: ["CREASTMT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d3",
      source: "672b29c93e4eb3f0ec40c031",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["DEFGDGB"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANREPT) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TCATBALF.BKUP) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.SYSTRAN) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n",
              start_line: 21,
              end_line: 59
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANREPT) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TCATBALF.BKUP) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.SYSTRAN) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.COMBINED) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n   IF LASTCC=12 THEN SET MAXCC=0\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d4",
      source: "672b29c93e4eb3f0ec40c034",
      target: "672b29c93e4eb3f0ec40c035",
      type: "STATIC_CALL",
      group: ["READCARD"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "9999-ABEND-PROGRAM",
            identifier: [],
            programName: "'CEE3ABD'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d5",
      source: "672b29c93e4eb3f0ec40c034",
      target: "672b29c93e4eb3f0ec40c036",
      type: "HAS_COPYBOOK",
      group: ["READCARD"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d6",
      source: "672b29c93e4eb3f0ec40c037",
      target: "672b29c93e4eb3f0ec40c014",
      type: "EXEC_PGM",
      group: ["TRANREPT"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05R",
            code: {
              content:
                "//STEP05R  EXEC PGM=SORT\r\n//SORTIN   DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(+1)\r\n//SYMNAMES DD *\r\nTRAN-CARD-NUM,263,16,ZD\r\nTRAN-PROC-DT,305,10,CH\r\nPARM-START-DATE,C'2022-01-01'                                      //Date\r\nPARM-END-DATE,C'2022-07-06'                                        //Date\r\n//SYSIN    DD *\r\n SORT FIELDS=(TRAN-CARD-NUM,A)\r\n INCLUDE COND=(TRAN-PROC-DT,GE,PARM-START-DATE,AND,\r\n         TRAN-PROC-DT,LE,PARM-END-DATE)\r\n//SYSOUT   DD SYSOUT=*\r\n//SORTOUT  DD DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(*.SORTIN),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)\r\n",
              start_line: 37,
              end_line: 55
            },
            statements: [
              {
                ddname: "SORTIN",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(+1)",
                    variable_name: "SORTIN",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(+1)",
                    program_id: "SORT"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYMNAMES",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "TRAN-CARD-NUM,263,16,ZD\r\nTRAN-PROC-DT,305,10,CH\r\nPARM-START-DATE,C'2022-01-01'                                      //Date\r\nPARM-END-DATE,C'2022-07-06'                                        //Date\r\n"
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " SORT FIELDS=(TRAN-CARD-NUM,A)\r\n INCLUDE COND=(TRAN-PROC-DT,GE,PARM-START-DATE,AND,\r\n         TRAN-PROC-DT,LE,PARM-END-DATE)\r\n"
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SORTOUT",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "(*.SORTIN)",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)",
                    variable_name: "SORTOUT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)",
                    program_id: "SORT"
                  }
                ],
                logic: null
              }
            ]
          },
          {
            step_name: "STEP05R",
            code: {
              content:
                "//STEP05R  EXEC PGM=SORT\r\n//SORTIN   DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(+1)\r\n//SYMNAMES DD *\r\nTRAN-CARD-NUM,263,16,ZD\r\nTRAN-PROC-DT,305,10,CH\r\nPARM-START-DATE,C'2022-01-01'                                      //Date\r\nPARM-END-DATE,C'2022-07-06'                                        //Date\r\n//SYSIN    DD *\r\n SORT FIELDS=(TRAN-CARD-NUM,A)\r\n INCLUDE COND=(TRAN-PROC-DT,GE,PARM-START-DATE,AND,\r\n         TRAN-PROC-DT,LE,PARM-END-DATE)\r\n//SYSOUT   DD SYSOUT=*\r\n//SORTOUT  DD DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(*.SORTIN),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)\r\n",
              start_line: 35,
              end_line: 53
            },
            statements: [
              {
                ddname: "SORTIN",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(+1)",
                    variable_name: "SORTIN",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.BKUP(+1)",
                    program_id: "SORT"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYMNAMES",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "TRAN-CARD-NUM,263,16,ZD\r\nTRAN-PROC-DT,305,10,CH\r\nPARM-START-DATE,C'2022-01-01'                                      //Date\r\nPARM-END-DATE,C'2022-07-06'                                        //Date\r\n"
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " SORT FIELDS=(TRAN-CARD-NUM,A)\r\n INCLUDE COND=(TRAN-PROC-DT,GE,PARM-START-DATE,AND,\r\n         TRAN-PROC-DT,LE,PARM-END-DATE)\r\n"
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SORTOUT",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "(*.SORTIN)",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)",
                    variable_name: "SORTOUT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)",
                    program_id: "SORT"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d7",
      source: "672b29c93e4eb3f0ec40c037",
      target: "672b29c93e4eb3f0ec40c038",
      type: "EXEC_PGM",
      group: ["TRANREPT"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP10R",
            code: {
              content:
                "//STEP10R EXEC PGM=CBTRN03C\r\n//STEPLIB  DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB\r\n//SYSOUT   DD SYSOUT=*\r\n//SYSPRINT DD SYSOUT=*\r\n//TRANFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)\r\n//CARDXREF DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS\r\n//TRANTYPE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS\r\n//TRANCATG DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS\r\n//DATEPARM DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.DATEPARM\r\n//TRANREPT DD DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(LRECL=133,RECFM=FB,BLKSIZE=0),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANREPT(+1)\r\n//\r\n",
              start_line: 59,
              end_line: 81
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.LOADLIB"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TRANFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)",
                    variable_name: "TRANFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "CARDXREF",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    variable_name: "CARDXREF",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "TRANTYPE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS",
                    variable_name: "TRANTYPE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "TRANCATG",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS",
                    variable_name: "TRANCATG",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "DATEPARM",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.DATEPARM"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.DATEPARM",
                    variable_name: "DATEPARM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.DATEPARM",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "TRANREPT",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "133",
                  LRECL: "133",
                  RECFM: "133",
                  BLKSIZE: "133",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANREPT(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANREPT(+1)",
                    variable_name: "TRANREPT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANREPT(+1)",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              }
            ]
          },
          {
            step_name: "STEP10R",
            code: {
              content:
                "//STEP10R EXEC PGM=CBTRN03C\r\n//STEPLIB  DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB\r\n//SYSOUT   DD SYSOUT=*\r\n//SYSPRINT DD SYSOUT=*\r\n//TRANFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)\r\n//CARDXREF DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS\r\n//TRANTYPE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS\r\n//TRANCATG DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS\r\n//DATEPARM DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.DATEPARM\r\n//TRANREPT DD DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(LRECL=133,RECFM=FB,BLKSIZE=0),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANREPT(+1)\r\n// PEND\r\n",
              start_line: 57,
              end_line: 79
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.LOADLIB"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TRANFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)",
                    variable_name: "TRANFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.DALY(+1)",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "CARDXREF",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    variable_name: "CARDXREF",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "TRANTYPE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS",
                    variable_name: "TRANTYPE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "TRANCATG",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS",
                    variable_name: "TRANCATG",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "DATEPARM",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.DATEPARM"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.DATEPARM",
                    variable_name: "DATEPARM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.DATEPARM",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "TRANREPT",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "133",
                  LRECL: "133",
                  RECFM: "133",
                  BLKSIZE: "133",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANREPT(+1)",
                  UNNAMED_1: "PEND"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANREPT(+1)",
                    variable_name: "TRANREPT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANREPT(+1)",
                    program_id: "CBTRN03C"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d8",
      source: "672b29c93e4eb3f0ec40c038",
      target: "672b29c93e4eb3f0ec40c035",
      type: "STATIC_CALL",
      group: ["TRANREPT"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "9999-ABEND-PROGRAM",
            identifier: [],
            programName: "'CEE3ABD'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0d9",
      source: "672b29c93e4eb3f0ec40c038",
      target: "672b29c93e4eb3f0ec40c01f",
      type: "HAS_COPYBOOK",
      group: ["TRANREPT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0da",
      source: "672b29c93e4eb3f0ec40c038",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: ["TRANREPT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0db",
      source: "672b29c93e4eb3f0ec40c038",
      target: "672b29c93e4eb3f0ec40c03a",
      type: "HAS_COPYBOOK",
      group: ["TRANREPT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0dc",
      source: "672b29c93e4eb3f0ec40c038",
      target: "672b29c93e4eb3f0ec40c03b",
      type: "HAS_COPYBOOK",
      group: ["TRANREPT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0dd",
      source: "672b29c93e4eb3f0ec40c038",
      target: "672b29c93e4eb3f0ec40c03c",
      type: "HAS_COPYBOOK",
      group: ["TRANREPT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0de",
      source: "672b29c93e4eb3f0ec40c039",
      target: "672b29c93e4eb3f0ec40c084",
      type: "HAS_INTERACT",
      group: ["COTRN00"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0df",
      source: "672b29c93e4eb3f0ec40c03d",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["TCATBALF"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS -\r\n          CLUSTER\r\n   SET    MAXCC = 0\r\n",
              start_line: 22,
              end_line: 27
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS -\r\n          CLUSTER\r\n   SET    MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(17 0) -\r\n          RECORDSIZE(50 50) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS.IDX) -\r\n          )\r\n",
              start_line: 33,
              end_line: 49
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(17 0) -\r\n          RECORDSIZE(50 50) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS.IDX) -\r\n          )\r\n"
              }
            ]
          },
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//TCATBAL DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.PS\r\n//TCATBALV DD DISP=OLD,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(TCATBAL) OUTFILE(TCATBALV)\r\n",
              start_line: 54,
              end_line: 61
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TCATBAL",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TCATBALF.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TCATBALF.PS",
                    variable_name: "TCATBAL",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.PS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "TCATBALV",
                parameters_map: {
                  DISP: "OLD",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS",
                    variable_name: "TCATBALV",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(TCATBAL) OUTFILE(TCATBALV)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e0",
      source: "672b29c93e4eb3f0ec40c03e",
      target: "672b29c93e4eb3f0ec40c02d",
      type: "EXEC_PGM",
      group: ["CUSTFILE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "CLCIFIL",
            code: {
              content:
                "//CLCIFIL EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /F CICSA,'CEMT SET FIL(CUSTDAT ) CLO'\r\n",
              start_line: 22,
              end_line: 26
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /F CICSA,'CEMT SET FIL(CUSTDAT ) CLO'\r\n"
              }
            ]
          },
          {
            step_name: "OPCIFIL",
            code: {
              content:
                "//OPCIFIL EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /F CICSA,'CEMT SET FIL(CUSTDAT ) OPE'\r\n",
              start_line: 76,
              end_line: 80
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /F CICSA,'CEMT SET FIL(CUSTDAT ) OPE'\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e1",
      source: "672b29c93e4eb3f0ec40c03e",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["CUSTFILE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n",
              start_line: 32,
              end_line: 37
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(9 0) -\r\n          RECORDSIZE(500 500) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS.IDX) -\r\n          )\r\n",
              start_line: 43,
              end_line: 59
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(9 0) -\r\n          RECORDSIZE(500 500) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS.IDX) -\r\n          )\r\n"
              }
            ]
          },
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//CUSTDATA DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CUSTDATA.PS\r\n//CUSTVSAM DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(CUSTDATA) OUTFILE(CUSTVSAM)\r\n",
              start_line: 64,
              end_line: 71
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CUSTDATA",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CUSTDATA.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CUSTDATA.PS",
                    variable_name: "CUSTDATA",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CUSTDATA.PS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "CUSTVSAM",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS",
                    variable_name: "CUSTVSAM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(CUSTDATA) OUTFILE(CUSTVSAM)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e2",
      source: "672b29c93e4eb3f0ec40c03f",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["CORPT00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e3",
      source: "672b29c93e4eb3f0ec40c03f",
      target: "672b29c93e4eb3f0ec40c040",
      type: "HAS_COPYBOOK",
      group: ["CORPT00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e4",
      source: "672b29c93e4eb3f0ec40c03f",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["CORPT00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e5",
      source: "672b29c93e4eb3f0ec40c03f",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["CORPT00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e6",
      source: "672b29c93e4eb3f0ec40c03f",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["CORPT00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e7",
      source: "672b29c93e4eb3f0ec40c03f",
      target: "672b29c93e4eb3f0ec40c01f",
      type: "HAS_COPYBOOK",
      group: ["CORPT00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e8",
      source: "672b29c93e4eb3f0ec40c03f",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["CORPT00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0e9",
      source: "672b29c93e4eb3f0ec40c03f",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["CORPT00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ea",
      source: "672b29c93e4eb3f0ec40c041",
      target: "672b29c93e4eb3f0ec40c03f",
      type: "HAS_INTERACT",
      group: ["CORPT00"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0eb",
      source: "672b29c93e4eb3f0ec40c042",
      target: "672b29c93e4eb3f0ec40c02d",
      type: "EXEC_PGM",
      group: ["OPENFIL"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "OPCIFIL",
            code: {
              content:
                "//OPCIFIL EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /F CICSA,'CEMT SET FIL(TRANSACT ) OPE'\r\n /F CICSA,'CEMT SET FIL(CCXREF ) OPE'\r\n /F CICSA,'CEMT SET FIL(ACCTDAT ) OPE'\r\n /F CICSA,'CEMT SET FIL(CXACAIX ) OPE'\r\n /F CICSA,'CEMT SET FIL(USRSEC ) OPE'\r\n",
              start_line: 22,
              end_line: 30
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /F CICSA,'CEMT SET FIL(TRANSACT ) OPE'\r\n /F CICSA,'CEMT SET FIL(CCXREF ) OPE'\r\n /F CICSA,'CEMT SET FIL(ACCTDAT ) OPE'\r\n /F CICSA,'CEMT SET FIL(CXACAIX ) OPE'\r\n /F CICSA,'CEMT SET FIL(USRSEC ) OPE'\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ec",
      source: "672b29c93e4eb3f0ec40c045",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["TRANIDX"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP20",
            code: {
              content:
                "//STEP20  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n   DEFINE ALTERNATEINDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX)-\r\n   RELATE(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS)                    -\r\n   KEYS(26 304)                                                  -\r\n   NONUNIQUEKEY                                                  -\r\n   UPGRADE                                                       -\r\n   RECORDSIZE(350,350)                                           -\r\n   VOLUMES(AWSHJ1)                                               -\r\n   CYLINDERS(5,1))                                               -\r\n   DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.DATA))           -\r\n   INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.INDEX))\r\n",
              start_line: 22,
              end_line: 34
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE ALTERNATEINDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX)-\r\n   RELATE(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS)                    -\r\n   KEYS(26 304)                                                  -\r\n   NONUNIQUEKEY                                                  -\r\n   UPGRADE                                                       -\r\n   RECORDSIZE(350,350)                                           -\r\n   VOLUMES(AWSHJ1)                                               -\r\n   CYLINDERS(5,1))                                               -\r\n   DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.DATA))           -\r\n   INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.INDEX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP25",
            code: {
              content:
                "//STEP25  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n  DEFINE PATH                                           -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.PATH)        -\r\n    PATHENTRY(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX))\r\n",
              start_line: 39,
              end_line: 44
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "  DEFINE PATH                                           -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.PATH)        -\r\n    PATHENTRY(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP30",
            code: {
              content:
                "//STEP30  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n   BLDINDEX                                                      -\r\n   INDATASET(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS)                 -\r\n   OUTDATASET(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX)\r\n",
              start_line: 49,
              end_line: 54
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   BLDINDEX                                                      -\r\n   INDATASET(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS)                 -\r\n   OUTDATASET(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ed",
      source: "672b29c93e4eb3f0ec40c048",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["REPROC"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "PRC001",
            code: {
              content:
                "//PRC001 EXEC PGM=IDCAMS\r\n//SYSPRINT DD SYSOUT=*\r\n//FILEIN  DD DISP=SHR,\r\n//        DSN=NULLFILE\r\n//FILEOUT DD DISP=SHR,\r\n//        DSN=NULLFILE\r\n//SYSIN   DD DISP=SHR,\r\n//        DSN=&CNTLLIB(REPROCT)\r\n// PEND\r\n",
              start_line: 21,
              end_line: 29
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "FILEIN",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "NULLFILE"
                },
                dataset_map_list: [
                  {
                    dataset_name: "NULLFILE",
                    variable_name: "FILEIN",
                    dd_statement: "DSN=NULLFILE",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "FILEOUT",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "NULLFILE"
                },
                dataset_map_list: [
                  {
                    dataset_name: "NULLFILE",
                    variable_name: "FILEOUT",
                    dd_statement: "DSN=NULLFILE",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "&CNTLLIB(REPROCT)",
                  UNNAMED_1: "PEND"
                },
                dataset_map_list: [
                  {
                    dataset_name: "&CNTLLIB(REPROCT)",
                    variable_name: "SYSIN",
                    dd_statement: "DSN=&CNTLLIB(REPROCT)",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ee",
      source: "672b29c93e4eb3f0ec40c049",
      target: "672b29c93e4eb3f0ec40c04a",
      type: "EXEC_PGM",
      group: ["CBADMCDJ"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP1",
            code: {
              content:
                "//STEP1   EXEC PGM=DFHCSDUP,REGION=0M,\r\n//          PARM='CSD(READWRITE),PAGESIZE(60),NOCOMPAT'\r\n//STEPLIB  DD  DSN=OEM.CICSTS.V05R06M0.CICS.SDFHLOAD,DISP=SHR\r\n//DFHCSD   DD  UNIT=SYSDA,DISP=SHR,DSN=OEM.CICSTS.DFHCSD\r\n//OUTDD    DD  SYSOUT=*\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *,SYMBOLS=JCLONLY\r\n**** NOTE: INSTALL GROUP(CARDDEMO) - CEDA IN G(CARDDEMO)                *\r\n*     IF YOU ARE RERUNNING THIS, UNCOMMENT THE DELETE COMMAND. *\r\n*\r\n* START CARDDEMO RESOURCES:\r\n*\r\n* DELETE GROUP(CARDDEMO)\r\n\r\n  DEFINE LIBRARY(COM2DOLL) GROUP(CARDDEMO)\r\n                DSNAME01(&HLQ..LOADLIB)\r\n\r\n* DEFINE TDQUEUE(CSSD) GROUP(CARDDEMO) TYPE(INTRA)\r\n* DEFINE TDQUEUE(IRDC) GROUP(CARDDEMO) TYPE(INTRA)\r\n\r\n  DEFINE MAPSET(COSGN00M)   GROUP(CARDDEMO)\r\n         DESCRIPTION(LOGIN SCREEN)\r\n\r\n  DEFINE MAPSET(COSGN00M)   GROUP(CARDDEMO)\r\n         DESCRIPTION(LOGIN SCREEN)\r\n\r\n  DEFINE MAPSET(COACT00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(ACCOUNT MENU)\r\n  DEFINE MAPSET(COACTVWS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(VIEW ACCOUNT)\r\n  DEFINE MAPSET(COACTUPS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(UPDATE ACCOUNT)\r\n  DEFINE MAPSET(COACTDES)   GROUP(CARDDEMO)\r\n         DESCRIPTION(DEACTIVATE ACCOUNT)\r\n\r\n  DEFINE MAPSET(COACT00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(CARD MENU)\r\n  DEFINE MAPSET(COACTVWS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(VIEW CARD)\r\n  DEFINE MAPSET(COACTUPS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(UPDATE CARD)\r\n  DEFINE MAPSET(COACTDES)   GROUP(CARDDEMO)\r\n         DESCRIPTION(DEACTIVATE CARD)\r\n\r\n  DEFINE MAPSET(COTRN00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(TRANSACTION)\r\n  DEFINE MAPSET(COTRNVWS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(TRANSACTION REPORT)\r\n  DEFINE MAPSET(COTRNVDS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(TRANSACTION DETAILS)\r\n  DEFINE MAPSET(COTRNATS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(ADD TRANSACTIONS)\r\n\r\n  DEFINE MAPSET(COBIL00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(BILL PAY SETUP)\r\n\r\n  DEFINE MAPSET(COADM00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(ADMIN MENU)\r\n\r\n  DEFINE MAPSET(COTSTP1S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(PGM1 TEST)\r\n  DEFINE MAPSET(COTSTP2S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(PGM2 TEST)\r\n  DEFINE MAPSET(COTSTP3S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(PGM3 TEST)\r\n  DEFINE MAPSET(COTSTP4S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(PGM4 TEST)\r\n\r\n  DEFINE PROGRAM(COSGN00C) GROUP(CARDDEMO) DA(ANY) TRANSID(CC00)\r\n         DESCRIPTION(LOGIN)\r\n\r\n  DEFINE PROGRAM(COACT00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(ACCOUNT MAIN MENU)\r\n  DEFINE PROGRAM(COACTVWC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(VIEW ACCOUNT)\r\n  DEFINE PROGRAM(COACTUPC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(UPDATE ACCOUNT)\r\n  DEFINE PROGRAM(COACTDEC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(DEACTIVATE ACCOUNT)\r\n\r\n  DEFINE PROGRAM(COACT00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(CARD MENU)\r\n  DEFINE PROGRAM(COACTVWC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(VIEW CARD)\r\n  DEFINE PROGRAM(COACTUPC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(UPDATE CARD)\r\n  DEFINE PROGRAM(COACTDEC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(DEACTIVATE CARD)\r\n  DEFINE PROGRAM(COTRN00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(TRANSACTION)\r\n  DEFINE PROGRAM(COTRNVWC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(TRANSACTION REPORT)\r\n  DEFINE PROGRAM(COTRNVDC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(TRANSACTION DETAILS)\r\n  DEFINE PROGRAM(COTRNATC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(ADD TRANSACTIONS)\r\n\r\n  DEFINE PROGRAM(COBIL00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(BILL PAY)\r\n\r\n  DEFINE PROGRAM(COADM00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(ADMIN MENU)\r\n         TRANSID(CCAD)\r\n\r\n  DEFINE PROGRAM(COTSTP1C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(PGM1 TEST)\r\n         TRANSID(CCT1)\r\n  DEFINE PROGRAM(COTSTP2C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(PGM2 TEST)\r\n         TRANSID(CCT2)\r\n  DEFINE PROGRAM(COTSTP3C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(PGM1 TEST)\r\n         TRANSID(CCT3)\r\n  DEFINE PROGRAM(COTSTP4C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(PGM4 TEST)\r\n         TRANSID(CCT4)\r\n\r\n  DEFINE TRANSACTION(CCDM) GROUP(CARDDEMO)\r\n                PROGRAM(COADM00C) TASKDATAL(ANY)\r\n\r\n  DEFINE TRANSACTION(CCT1) GROUP(CARDDEMO)\r\n                PROGRAM(COTSTP1C) TASKDATAL(ANY)\r\n  DEFINE TRANSACTION(CCT2) GROUP(CARDDEMO)\r\n                PROGRAM(COTSTP2C) TASKDATAL(ANY)\r\n  DEFINE TRANSACTION(CCT3) GROUP(CARDDEMO)\r\n                PROGRAM(COTSTP3C) TASKDATAL(ANY)\r\n  DEFINE TRANSACTION(CCT4) GROUP(CARDDEMO)\r\n                PROGRAM(COTSTP4C) TASKDATAL(ANY)\r\n\r\n  LIST   GROUP(CARDDEMO)\r\n*\r\n* END CARDDEMO RESOURCES\r\n*\r\n//\r\n",
              start_line: 27,
              end_line: 164
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DSN: "OEM.CICSTS.V05R06M0.CICS.SDFHLOAD",
                  DISP: "OEM.CICSTS.V05R06M0.CICS.SDFHLOAD"
                },
                dataset_map_list: [
                  {
                    dataset_name: "OEM.CICSTS.V05R06M0.CICS.SDFHLOAD",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=OEM.CICSTS.V05R06M0.CICS.SDFHLOAD",
                    program_id: "DFHCSDUP"
                  }
                ],
                logic: null
              },
              {
                ddname: "DFHCSD",
                parameters_map: {
                  UNIT: "SYSDA",
                  DISP: "SYSDA",
                  DSN: "SYSDA"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SYSDA",
                    variable_name: "DFHCSD",
                    dd_statement: "DSN=OEM.CICSTS.DFHCSD",
                    program_id: "DFHCSDUP"
                  }
                ],
                logic: null
              },
              {
                ddname: "OUTDD",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*",
                  SYMBOLS: "JCLONLY"
                },
                dataset_map_list: [],
                logic:
                  "*/********************************************************************/\r\n*/*  CARDDEMO CICS DEFINITIONS                                       */\r\n*/********************************************************************/\r\n* NOTE: INSTALL GROUP(CARDDEMO) - CEDA IN G(CARDDEMO)                *\r\n*     IF YOU ARE RERUNNING THIS, UNCOMMENT THE DELETE COMMAND. *\r\n*\r\n* START CARDDEMO RESOURCES:\r\n*\r\n* DELETE GROUP(CARDDEMO)\r\n\r\n  DEFINE LIBRARY(COM2DOLL) GROUP(CARDDEMO)\r\n                DSNAME01(&HLQ..LOADLIB)\r\n\r\n* DEFINE TDQUEUE(CSSD) GROUP(CARDDEMO) TYPE(INTRA)\r\n* DEFINE TDQUEUE(IRDC) GROUP(CARDDEMO) TYPE(INTRA)\r\n\r\n  DEFINE MAPSET(COSGN00M)   GROUP(CARDDEMO)\r\n         DESCRIPTION(LOGIN SCREEN)\r\n\r\n  DEFINE MAPSET(COSGN00M)   GROUP(CARDDEMO)\r\n         DESCRIPTION(LOGIN SCREEN)\r\n\r\n  DEFINE MAPSET(COACT00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(ACCOUNT MENU)\r\n  DEFINE MAPSET(COACTVWS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(VIEW ACCOUNT)\r\n  DEFINE MAPSET(COACTUPS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(UPDATE ACCOUNT)\r\n  DEFINE MAPSET(COACTDES)   GROUP(CARDDEMO)\r\n         DESCRIPTION(DEACTIVATE ACCOUNT)\r\n\r\n  DEFINE MAPSET(COACT00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(CARD MENU)\r\n  DEFINE MAPSET(COACTVWS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(VIEW CARD)\r\n  DEFINE MAPSET(COACTUPS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(UPDATE CARD)\r\n  DEFINE MAPSET(COACTDES)   GROUP(CARDDEMO)\r\n         DESCRIPTION(DEACTIVATE CARD)\r\n\r\n  DEFINE MAPSET(COTRN00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(TRANSACTION)\r\n  DEFINE MAPSET(COTRNVWS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(TRANSACTION REPORT)\r\n  DEFINE MAPSET(COTRNVDS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(TRANSACTION DETAILS)\r\n  DEFINE MAPSET(COTRNATS)   GROUP(CARDDEMO)\r\n         DESCRIPTION(ADD TRANSACTIONS)\r\n\r\n  DEFINE MAPSET(COBIL00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(BILL PAY SETUP)\r\n\r\n  DEFINE MAPSET(COADM00S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(ADMIN MENU)\r\n\r\n  DEFINE MAPSET(COTSTP1S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(PGM1 TEST)\r\n  DEFINE MAPSET(COTSTP2S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(PGM2 TEST)\r\n  DEFINE MAPSET(COTSTP3S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(PGM3 TEST)\r\n  DEFINE MAPSET(COTSTP4S)   GROUP(CARDDEMO)\r\n         DESCRIPTION(PGM4 TEST)\r\n\r\n  DEFINE PROGRAM(COSGN00C) GROUP(CARDDEMO) DA(ANY) TRANSID(CC00)\r\n         DESCRIPTION(LOGIN)\r\n\r\n  DEFINE PROGRAM(COACT00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(ACCOUNT MAIN MENU)\r\n  DEFINE PROGRAM(COACTVWC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(VIEW ACCOUNT)\r\n  DEFINE PROGRAM(COACTUPC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(UPDATE ACCOUNT)\r\n  DEFINE PROGRAM(COACTDEC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(DEACTIVATE ACCOUNT)\r\n\r\n  DEFINE PROGRAM(COACT00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(CARD MENU)\r\n  DEFINE PROGRAM(COACTVWC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(VIEW CARD)\r\n  DEFINE PROGRAM(COACTUPC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(UPDATE CARD)\r\n  DEFINE PROGRAM(COACTDEC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(DEACTIVATE CARD)\r\n  DEFINE PROGRAM(COTRN00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(TRANSACTION)\r\n  DEFINE PROGRAM(COTRNVWC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(TRANSACTION REPORT)\r\n  DEFINE PROGRAM(COTRNVDC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(TRANSACTION DETAILS)\r\n  DEFINE PROGRAM(COTRNATC) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(ADD TRANSACTIONS)\r\n\r\n  DEFINE PROGRAM(COBIL00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(BILL PAY)\r\n\r\n  DEFINE PROGRAM(COADM00C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(ADMIN MENU)\r\n         TRANSID(CCAD)\r\n\r\n  DEFINE PROGRAM(COTSTP1C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(PGM1 TEST)\r\n         TRANSID(CCT1)\r\n  DEFINE PROGRAM(COTSTP2C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(PGM2 TEST)\r\n         TRANSID(CCT2)\r\n  DEFINE PROGRAM(COTSTP3C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(PGM1 TEST)\r\n         TRANSID(CCT3)\r\n  DEFINE PROGRAM(COTSTP4C) GROUP(CARDDEMO) DA(ANY)\r\n         DESCRIPTION(PGM4 TEST)\r\n         TRANSID(CCT4)\r\n\r\n  DEFINE TRANSACTION(CCDM) GROUP(CARDDEMO)\r\n                PROGRAM(COADM00C) TASKDATAL(ANY)\r\n\r\n  DEFINE TRANSACTION(CCT1) GROUP(CARDDEMO)\r\n                PROGRAM(COTSTP1C) TASKDATAL(ANY)\r\n  DEFINE TRANSACTION(CCT2) GROUP(CARDDEMO)\r\n                PROGRAM(COTSTP2C) TASKDATAL(ANY)\r\n  DEFINE TRANSACTION(CCT3) GROUP(CARDDEMO)\r\n                PROGRAM(COTSTP3C) TASKDATAL(ANY)\r\n  DEFINE TRANSACTION(CCT4) GROUP(CARDDEMO)\r\n                PROGRAM(COTSTP4C) TASKDATAL(ANY)\r\n\r\n  LIST   GROUP(CARDDEMO)\r\n*\r\n* END CARDDEMO RESOURCES\r\n*\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ef",
      source: "672b29c93e4eb3f0ec40c04b",
      target: "672b29c93e4eb3f0ec40c07e",
      type: "HAS_INTERACT",
      group: ["COUSR02"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f0",
      source: "672b29c93e4eb3f0ec40c04c",
      target: "672b29c93e4eb3f0ec40c035",
      type: "STATIC_CALL",
      group: ["READACCT"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "9999-ABEND-PROGRAM",
            identifier: [],
            programName: "'CEE3ABD'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f1",
      source: "672b29c93e4eb3f0ec40c04c",
      target: "672b29c93e4eb3f0ec40c01d",
      type: "HAS_COPYBOOK",
      group: ["READACCT"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f2",
      source: "672b29c93e4eb3f0ec40c04e",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["DALYREJS"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.DALYREJS) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n",
              start_line: 21,
              end_line: 28
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.DALYREJS) -\r\n    LIMIT(5) -\r\n    SCRATCH -\r\n   )\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f3",
      source: "672b29c93e4eb3f0ec40c04f",
      target: "672b29c93e4eb3f0ec40c04a",
      type: "EXEC_PGM",
      group: ["CMP1CSD"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "CSDDEF",
            code: {
              content:
                "//CSDDEF EXEC PGM=DFHCSDUP,REGION=0M\r\n//STEPLIB  DD DSN=DFH410.SDFHLOAD,DISP=SHR\r\n//DFHCSD   DD DSN=DFH410.CICS.DFHCSD,DISP=SHR\r\n//SYSPRINT DD   SYSOUT=*\r\n//CBDOUT   DD   SYSOUT=*\r\n//AMSDUMP  DD   SYSOUT=*\r\n//SYSIN    DD *,DLM='ZZ'\r\n DELETE FILE(ACCTDAT) GROUP(CARDDEMO)\r\nZZ\r\n",
              start_line: 4,
              end_line: 12
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DSN: "DFH410.SDFHLOAD",
                  DISP: "DFH410.SDFHLOAD"
                },
                dataset_map_list: [
                  {
                    dataset_name: "DFH410.SDFHLOAD",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=DFH410.SDFHLOAD",
                    program_id: "DFHCSDUP"
                  }
                ],
                logic: null
              },
              {
                ddname: "DFHCSD",
                parameters_map: {
                  DSN: "DFH410.CICS.DFHCSD",
                  DISP: "DFH410.CICS.DFHCSD"
                },
                dataset_map_list: [
                  {
                    dataset_name: "DFH410.CICS.DFHCSD",
                    variable_name: "DFHCSD",
                    dd_statement: "DSN=DFH410.CICS.DFHCSD",
                    program_id: "DFHCSDUP"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CBDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "AMSDUMP",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*",
                  DLM: "'ZZ'"
                },
                dataset_map_list: [],
                logic: " DELETE FILE(ACCTDAT) GROUP(CARDDEMO)\r\nZZ\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f4",
      source: "672b29c93e4eb3f0ec40c050",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["ACCTFILE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n",
              start_line: 22,
              end_line: 27
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS)     -\r\n          CYLINDERS(1 5)                                              -\r\n          VOLUMES(USER04)                                             -\r\n          KEYS(11 0)                                                  -\r\n          RECORDSIZE(300 300)                                         -\r\n          SHAREOPTIONS(2 3)                                           -\r\n          ERASE                                                       -\r\n          INDEXED                                                     -\r\n          )                                                           -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS.DAT))   -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS.IDX))\r\n",
              start_line: 33,
              end_line: 46
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS)     -\r\n          CYLINDERS(1 5)                                              -\r\n          VOLUMES(USER04)                                             -\r\n          KEYS(11 0)                                                  -\r\n          RECORDSIZE(300 300)                                         -\r\n          SHAREOPTIONS(2 3)                                           -\r\n          ERASE                                                       -\r\n          INDEXED                                                     -\r\n          )                                                           -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS.DAT))   -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS.IDX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//ACCTDATA DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.PS\r\n//ACCTVSAM DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(ACCTDATA) OUTFILE(ACCTVSAM)\r\n",
              start_line: 51,
              end_line: 58
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ACCTDATA",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.PS",
                    variable_name: "ACCTDATA",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.PS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "ACCTVSAM",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
                    variable_name: "ACCTVSAM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(ACCTDATA) OUTFILE(ACCTVSAM)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f5",
      source: "672b29c93e4eb3f0ec40c051",
      target: "672b29c93e4eb3f0ec40c052",
      type: "STATIC_CALL",
      group: ["COTRN02"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "A000-MAIN",
            identifier: ["WS-DATE-TO-TEST", "WS-DATE-FORMAT", "OUTPUT-LILLIAN", "FEEDBACK-CODE"],
            // eslint-disable-next-line prettier/prettier
            programName: "\"CEEDAYS\""
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f6",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c058",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f7",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c02a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f8",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c02b",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0f9",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0fa",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0fb",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0fc",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c059",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0fd",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0fe",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c0ff",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c05a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c100",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c101",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c01d",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c102",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c103",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c053",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c104",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c105",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c05b",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c106",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c05c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c107",
      source: "672b29c93e4eb3f0ec40c057",
      target: "672b29c93e4eb3f0ec40c05d",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c108",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c051",
      type: "STATIC_CALL",
      group: ["COTRN02"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "VALIDATE-INPUT-DATA-FIELDS",
            identifier: ["CSUTLDTC-DATE", "CSUTLDTC-DATE-FORMAT", "CSUTLDTC-RESULT"],
            programName: "'CSUTLDTC'"
          },
          {
            paragraph: "VALIDATE-INPUT-DATA-FIELDS",
            identifier: ["CSUTLDTC-DATE", "CSUTLDTC-DATE-FORMAT", "CSUTLDTC-RESULT"],
            programName: "'CSUTLDTC'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c109",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c10a",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c05f",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c10b",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c10c",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c10d",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c10e",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c01f",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c10f",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c01d",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c110",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c111",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c112",
      source: "672b29c93e4eb3f0ec40c05e",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COTRN02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c113",
      source: "672b29c93e4eb3f0ec40c060",
      target: "672b29c93e4eb3f0ec40c05e",
      type: "HAS_INTERACT",
      group: ["COTRN02"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c114",
      source: "672b29c93e4eb3f0ec40c063",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["REPTFILE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANREPT) -\r\n    LIMIT(10) -\r\n   )\r\n",
              start_line: 22,
              end_line: 28
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE GENERATIONDATAGROUP -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANREPT) -\r\n    LIMIT(10) -\r\n   )\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c115",
      source: "672b29c93e4eb3f0ec40c064",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["DEFCUST"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(AWS.CUSTDATA.CLUSTER) -\r\n          CYLINDERS(1 5) -\r\n          KEYS(10 0) -\r\n          RECORDSIZE(500 500) -\r\n          SHAREOPTIONS(1 4) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(AWS.CUSTDATA.CLUSTER.DATA) -\r\n          ) -\r\n          INDEX (NAME(AWS.CUSTDATA.CLUSTER.INDEX) -\r\n          )\r\n",
              start_line: 32,
              end_line: 46
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(AWS.CUSTDATA.CLUSTER) -\r\n          CYLINDERS(1 5) -\r\n          KEYS(10 0) -\r\n          RECORDSIZE(500 500) -\r\n          SHAREOPTIONS(1 4) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(AWS.CUSTDATA.CLUSTER.DATA) -\r\n          ) -\r\n          INDEX (NAME(AWS.CUSTDATA.CLUSTER.INDEX) -\r\n          )\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c116",
      source: "672b29c93e4eb3f0ec40c066",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COUSR03"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c117",
      source: "672b29c93e4eb3f0ec40c066",
      target: "672b29c93e4eb3f0ec40c016",
      type: "HAS_COPYBOOK",
      group: ["COUSR03"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c118",
      source: "672b29c93e4eb3f0ec40c066",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COUSR03"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c119",
      source: "672b29c93e4eb3f0ec40c066",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COUSR03"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c11a",
      source: "672b29c93e4eb3f0ec40c066",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COUSR03"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c11b",
      source: "672b29c93e4eb3f0ec40c066",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: ["COUSR03"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c11c",
      source: "672b29c93e4eb3f0ec40c066",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COUSR03"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c11d",
      source: "672b29c93e4eb3f0ec40c066",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COUSR03"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c11e",
      source: "672b29c93e4eb3f0ec40c067",
      target: "672b29c93e4eb3f0ec40c066",
      type: "HAS_INTERACT",
      group: ["COUSR03"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c11f",
      source: "672b29c93e4eb3f0ec40c068",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COTRN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c120",
      source: "672b29c93e4eb3f0ec40c068",
      target: "672b29c93e4eb3f0ec40c069",
      type: "HAS_COPYBOOK",
      group: ["COTRN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c121",
      source: "672b29c93e4eb3f0ec40c068",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COTRN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c122",
      source: "672b29c93e4eb3f0ec40c068",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COTRN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c123",
      source: "672b29c93e4eb3f0ec40c068",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COTRN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c124",
      source: "672b29c93e4eb3f0ec40c068",
      target: "672b29c93e4eb3f0ec40c01f",
      type: "HAS_COPYBOOK",
      group: ["COTRN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c125",
      source: "672b29c93e4eb3f0ec40c068",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COTRN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c126",
      source: "672b29c93e4eb3f0ec40c068",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COTRN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c127",
      source: "672b29c93e4eb3f0ec40c06a",
      target: "672b29c93e4eb3f0ec40c035",
      type: "STATIC_CALL",
      group: ["READCUST"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "Z-ABEND-PROGRAM",
            identifier: [],
            programName: "'CEE3ABD'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c128",
      source: "672b29c93e4eb3f0ec40c06a",
      target: "672b29c93e4eb3f0ec40c053",
      type: "HAS_COPYBOOK",
      group: ["READCUST"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c129",
      source: "672b29c93e4eb3f0ec40c06b",
      target: "672b29c93e4eb3f0ec40c02d",
      type: "EXEC_PGM",
      group: ["CMPCICS"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "NEWCOPY1",
            code: {
              content:
                "//NEWCOPY1 EXEC PGM=SDSF,COND=(4,LT)                                    00120002\r\n//ISFOUT DD SYSOUT=*                                                    00130002\r\n//CMDOUT DD SYSOUT=*                                                    00140002\r\n//ISFIN  DD *                                                           00150002\r\n /MODIFY CICSA,'CEMT SET PROG(COACTVWC) NEWCOPY'                        00160006\r\n                                                                        00171003\r\n",
              start_line: 10,
              end_line: 16
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COACTVWC) NEWCOPY'                        00160006\r\n                                                                        00171003\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPY2",
            code: {
              content:
                "//NEWCOPY2 EXEC PGM=SDSF,COND=(4,LT)                                    00240003\r\n//ISFOUT DD SYSOUT=*                                                    00250003\r\n//CMDOUT DD SYSOUT=*                                                    00260003\r\n//ISFIN  DD *                                                           00270003\r\n /MODIFY CICSA,'CEMT SET PROG(COCRDLIC) NEWCOPY'                        00280006\r\n                                                                        00291003\r\n",
              start_line: 23,
              end_line: 29
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COCRDLIC) NEWCOPY'                        00280006\r\n                                                                        00291003\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPY3",
            code: {
              content:
                "//NEWCOPY3 EXEC PGM=SDSF,COND=(4,LT)                                    00360003\r\n//ISFOUT DD SYSOUT=*                                                    00370003\r\n//CMDOUT DD SYSOUT=*                                                    00380003\r\n//ISFIN  DD *                                                           00390003\r\n /MODIFY CICSA,'CEMT SET PROG(COCRDSLC) NEWCOPY'                        00400006\r\n                                                                        00411003\r\n",
              start_line: 36,
              end_line: 42
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COCRDSLC) NEWCOPY'                        00400006\r\n                                                                        00411003\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPY4",
            code: {
              content:
                "//NEWCOPY4 EXEC PGM=SDSF,COND=(4,LT)                                    00480003\r\n//ISFOUT DD SYSOUT=*                                                    00490003\r\n//CMDOUT DD SYSOUT=*                                                    00500003\r\n//ISFIN  DD *                                                           00510003\r\n /MODIFY CICSA,'CEMT SET PROG(COCRDUPC) NEWCOPY'                        00520006\r\n                                                                        00531003\r\n",
              start_line: 49,
              end_line: 55
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COCRDUPC) NEWCOPY'                        00520006\r\n                                                                        00531003\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPY5",
            code: {
              content:
                "//NEWCOPY5 EXEC PGM=SDSF,COND=(4,LT)                                    00600003\r\n//ISFOUT DD SYSOUT=*                                                    00610003\r\n//CMDOUT DD SYSOUT=*                                                    00620003\r\n//ISFIN  DD *                                                           00630003\r\n /MODIFY CICSA,'CEMT SET PROG(COUSR03C) NEWCOPY'                        00640006\r\n                                                                        00651003\r\n",
              start_line: 62,
              end_line: 68
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COUSR03C) NEWCOPY'                        00640006\r\n                                                                        00651003\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPY6",
            code: {
              content:
                "//NEWCOPY6 EXEC PGM=SDSF,COND=(4,LT)                                    00720003\r\n//ISFOUT DD SYSOUT=*                                                    00730003\r\n//CMDOUT DD SYSOUT=*                                                    00740003\r\n//ISFIN  DD *                                                           00750003\r\n /MODIFY CICSA,'CEMT SET PROG(COUSR02C) NEWCOPY'                        00760006\r\n                                                                        00760203\r\n",
              start_line: 75,
              end_line: 81
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COUSR02C) NEWCOPY'                        00760006\r\n                                                                        00760203\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPY7",
            code: {
              content:
                "//NEWCOPY7 EXEC PGM=SDSF,COND=(4,LT)                                    00767003\r\n//ISFOUT DD SYSOUT=*                                                    00768003\r\n//CMDOUT DD SYSOUT=*                                                    00769003\r\n//ISFIN  DD *                                                           00769103\r\n /MODIFY CICSA,'CEMT SET PROG(COADM01C) NEWCOPY'                        00769206\r\n                                                                        00769403\r\n",
              start_line: 88,
              end_line: 94
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COADM01C) NEWCOPY'                        00769206\r\n                                                                        00769403\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPY8",
            code: {
              content:
                "//NEWCOPY8 EXEC PGM=SDSF,COND=(4,LT)                                    00770203\r\n//ISFOUT DD SYSOUT=*                                                    00770303\r\n//CMDOUT DD SYSOUT=*                                                    00771003\r\n//ISFIN  DD *                                                           00772003\r\n /MODIFY CICSA,'CEMT SET PROG(COBIL00C) NEWCOPY'                        00773006\r\n                                                                        00773203\r\n",
              start_line: 101,
              end_line: 107
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COBIL00C) NEWCOPY'                        00773006\r\n                                                                        00773203\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPY9",
            code: {
              content:
                "//NEWCOPY9 EXEC PGM=SDSF,COND=(4,LT)                                    00779103\r\n//ISFOUT DD SYSOUT=*                                                    00779203\r\n//CMDOUT DD SYSOUT=*                                                    00779303\r\n//ISFIN  DD *                                                           00779403\r\n /MODIFY CICSA,'CEMT SET PROG(COMEN01C) NEWCOPY'                        00779506\r\n                                                                        00779803\r\n",
              start_line: 114,
              end_line: 120
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COMEN01C) NEWCOPY'                        00779506\r\n                                                                        00779803\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPYA",
            code: {
              content:
                "//NEWCOPYA EXEC PGM=SDSF,COND=(4,LT)                                    00782003\r\n//ISFOUT DD SYSOUT=*                                                    00783003\r\n//CMDOUT DD SYSOUT=*                                                    00784003\r\n//ISFIN  DD *                                                           00785003\r\n                                                                        00785203\r\n /MODIFY CICSA,'CEMT SET PROG(CORPT00C) NEWCOPY'                        00786006\r\n",
              start_line: 127,
              end_line: 133
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "                                                                        00785203\r\n /MODIFY CICSA,'CEMT SET PROG(CORPT00C) NEWCOPY'                        00786006\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPYB",
            code: {
              content:
                "//NEWCOPYB EXEC PGM=SDSF,COND=(4,LT)                                    00789403\r\n//ISFOUT DD SYSOUT=*                                                    00789503\r\n//CMDOUT DD SYSOUT=*                                                    00789603\r\n//ISFIN  DD *                                                           00789703\r\n /MODIFY CICSA,'CEMT SET PROG(COSGN00C) NEWCOPY'                        00789806\r\n                                                                        00790003\r\n",
              start_line: 140,
              end_line: 146
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COSGN00C) NEWCOPY'                        00789806\r\n                                                                        00790003\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPYC",
            code: {
              content:
                "//NEWCOPYC EXEC PGM=SDSF,COND=(4,LT)                                    00795003\r\n//ISFOUT DD SYSOUT=*                                                    00796003\r\n//CMDOUT DD SYSOUT=*                                                    00797003\r\n//ISFIN  DD *                                                           00798003\r\n /MODIFY CICSA,'CEMT SET PROG(COTRN00C) NEWCOPY'                        00799006\r\n                                                                        00799203\r\n",
              start_line: 153,
              end_line: 159
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COTRN00C) NEWCOPY'                        00799006\r\n                                                                        00799203\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPYD",
            code: {
              content:
                "//NEWCOPYD EXEC PGM=SDSF,COND=(4,LT)                                    00799903\r\n//ISFOUT DD SYSOUT=*                                                    00800003\r\n//CMDOUT DD SYSOUT=*                                                    00800103\r\n//ISFIN  DD *                                                           00800203\r\n /MODIFY CICSA,'CEMT SET PROG(COTRN01C) NEWCOPY'                        00801006\r\n                                                                        00801203\r\n",
              start_line: 166,
              end_line: 172
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COTRN01C) NEWCOPY'                        00801006\r\n                                                                        00801203\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPYE",
            code: {
              content:
                "//NEWCOPYE EXEC PGM=SDSF,COND=(4,LT)                                    00808003\r\n//ISFOUT DD SYSOUT=*                                                    00809003\r\n//CMDOUT DD SYSOUT=*                                                    00809103\r\n//ISFIN  DD *                                                           00809203\r\n /MODIFY CICSA,'CEMT SET PROG(COTRN02C) NEWCOPY'                        00809306\r\n                                                                        00809503\r\n",
              start_line: 179,
              end_line: 185
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COTRN02C) NEWCOPY'                        00809306\r\n                                                                        00809503\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPYF",
            code: {
              content:
                "//NEWCOPYF EXEC PGM=SDSF,COND=(4,LT)                                    00810203\r\n//ISFOUT DD SYSOUT=*                                                    00811003\r\n//CMDOUT DD SYSOUT=*                                                    00812003\r\n//ISFIN  DD *                                                           00813003\r\n /MODIFY CICSA,'CEMT SET PROG(COUSR00C) NEWCOPY'                        00814006\r\n                                                                        00814203\r\n",
              start_line: 192,
              end_line: 198
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COUSR00C) NEWCOPY'                        00814006\r\n                                                                        00814203\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPYG",
            code: {
              content:
                "//NEWCOPYG EXEC PGM=SDSF,COND=(4,LT)                                    00819203\r\n//ISFOUT DD SYSOUT=*                                                    00819303\r\n//CMDOUT DD SYSOUT=*                                                    00819403\r\n//ISFIN  DD *                                                           00819503\r\n /MODIFY CICSA,'CEMT SET PROG(COUSR01C) NEWCOPY'                        00819606\r\n                                                                        00830003\r\n",
              start_line: 205,
              end_line: 211
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COUSR01C) NEWCOPY'                        00819606\r\n                                                                        00830003\r\n"
              }
            ]
          },
          {
            step_name: "NEWCOPYH",
            code: {
              content:
                "//NEWCOPYH EXEC PGM=SDSF,COND=(4,LT)                                    00900003\r\n//ISFOUT DD SYSOUT=*                                                    00910003\r\n//CMDOUT DD SYSOUT=*                                                    00920003\r\n//ISFIN  DD *                                                           00930003\r\n /MODIFY CICSA,'CEMT SET PROG(COACTUPC) NEWCOPY'                        00940006\r\n",
              start_line: 218,
              end_line: 222
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSA,'CEMT SET PROG(COACTUPC) NEWCOPY'                        00940006\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c12a",
      source: "672b29c93e4eb3f0ec40c06c",
      target: "672b29c93e4eb3f0ec40c02d",
      type: "EXEC_PGM",
      group: ["CMP1CICS"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "NEWCOPYB",
            code: {
              content:
                "//NEWCOPYB EXEC PGM=SDSF,COND=(4,LT)                                    00789501\r\n//ISFOUT DD SYSOUT=*                                                    00789601\r\n//CMDOUT DD SYSOUT=*                                                    00789701\r\n//ISFIN  DD *                                                           00789801\r\n /MODIFY CICSAWSA,'CEMT SET PROG(COSGN00C) NEWCOPY'                     00789901\r\n",
              start_line: 11,
              end_line: 15
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /MODIFY CICSAWSA,'CEMT SET PROG(COSGN00C) NEWCOPY'                     00789901\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c12b",
      source: "672b29c93e4eb3f0ec40c06e",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COADM01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c12c",
      source: "672b29c93e4eb3f0ec40c06e",
      target: "672b29c93e4eb3f0ec40c06f",
      type: "HAS_COPYBOOK",
      group: ["COADM01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c12d",
      source: "672b29c93e4eb3f0ec40c06e",
      target: "672b29c93e4eb3f0ec40c070",
      type: "HAS_COPYBOOK",
      group: ["COADM01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c12e",
      source: "672b29c93e4eb3f0ec40c06e",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COADM01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c12f",
      source: "672b29c93e4eb3f0ec40c06e",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COADM01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c130",
      source: "672b29c93e4eb3f0ec40c06e",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COADM01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c131",
      source: "672b29c93e4eb3f0ec40c06e",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: ["COADM01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c132",
      source: "672b29c93e4eb3f0ec40c06e",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COADM01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c133",
      source: "672b29c93e4eb3f0ec40c06e",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COADM01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c134",
      source: "672b29c93e4eb3f0ec40c071",
      target: "672b29c93e4eb3f0ec40c06e",
      type: "HAS_INTERACT",
      group: ["COADM01"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c135",
      source: "672b29c93e4eb3f0ec40c072",
      target: "672b29c93e4eb3f0ec40c09c",
      type: "HAS_INTERACT",
      group: ["COSGN00"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c136",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c02a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c137",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c138",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c139",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c13a",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c13b",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c074",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c13c",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c13d",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c13e",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c05a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c13f",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c140",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c036",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c141",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c053",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c142",
      source: "672b29c93e4eb3f0ec40c073",
      target: "672b29c93e4eb3f0ec40c05c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c143",
      source: "672b29c93e4eb3f0ec40c076",
      target: "672b29c93e4eb3f0ec40c035",
      type: "STATIC_CALL",
      group: [],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "Z-ABEND-PROGRAM",
            identifier: [],
            programName: "'CEE3ABD'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c144",
      source: "672b29c93e4eb3f0ec40c076",
      target: "672b29c93e4eb3f0ec40c046",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c145",
      source: "672b29c93e4eb3f0ec40c076",
      target: "672b29c93e4eb3f0ec40c053",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c146",
      source: "672b29c93e4eb3f0ec40c076",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c147",
      source: "672b29c93e4eb3f0ec40c076",
      target: "672b29c93e4eb3f0ec40c036",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c148",
      source: "672b29c93e4eb3f0ec40c076",
      target: "672b29c93e4eb3f0ec40c01d",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c149",
      source: "672b29c93e4eb3f0ec40c076",
      target: "672b29c93e4eb3f0ec40c01f",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c14a",
      source: "672b29c93e4eb3f0ec40c079",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COMEN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c14b",
      source: "672b29c93e4eb3f0ec40c079",
      target: "672b29c93e4eb3f0ec40c032",
      type: "HAS_COPYBOOK",
      group: ["COMEN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c14c",
      source: "672b29c93e4eb3f0ec40c079",
      target: "672b29c93e4eb3f0ec40c056",
      type: "HAS_COPYBOOK",
      group: ["COMEN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c14d",
      source: "672b29c93e4eb3f0ec40c079",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COMEN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c14e",
      source: "672b29c93e4eb3f0ec40c079",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COMEN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c14f",
      source: "672b29c93e4eb3f0ec40c079",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COMEN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c150",
      source: "672b29c93e4eb3f0ec40c079",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: ["COMEN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c151",
      source: "672b29c93e4eb3f0ec40c079",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COMEN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c152",
      source: "672b29c93e4eb3f0ec40c079",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COMEN01"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c153",
      source: "672b29c93e4eb3f0ec40c07a",
      target: "672b29c93e4eb3f0ec40c079",
      type: "HAS_INTERACT",
      group: ["COMEN01"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c154",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c02a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c155",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c156",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c157",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c158",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c159",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c07c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c15a",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c15b",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c15c",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c05a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c15d",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c15e",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c036",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c15f",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c053",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c160",
      source: "672b29c93e4eb3f0ec40c07b",
      target: "672b29c93e4eb3f0ec40c05c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c161",
      source: "672b29c93e4eb3f0ec40c07e",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COUSR02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c162",
      source: "672b29c93e4eb3f0ec40c07e",
      target: "672b29c93e4eb3f0ec40c033",
      type: "HAS_COPYBOOK",
      group: ["COUSR02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c163",
      source: "672b29c93e4eb3f0ec40c07e",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COUSR02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c164",
      source: "672b29c93e4eb3f0ec40c07e",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COUSR02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c165",
      source: "672b29c93e4eb3f0ec40c07e",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COUSR02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c166",
      source: "672b29c93e4eb3f0ec40c07e",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: ["COUSR02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c167",
      source: "672b29c93e4eb3f0ec40c07e",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COUSR02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c168",
      source: "672b29c93e4eb3f0ec40c07e",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COUSR02"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c169",
      source: "672b29c93e4eb3f0ec40c080",
      target: "672b29c93e4eb3f0ec40c081",
      type: "EXEC_PGM",
      group: ["INTCALC"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=CBACT04C,PARM='2022071800'\r\n//STEPLIB  DD DISP=SHR,\r\n//            DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB\r\n//SYSPRINT DD SYSOUT=*\r\n//SYSOUT   DD SYSOUT=*\r\n//TCATBALF DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS\r\n//XREFFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS\r\n//XREFFIL1 DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.PATH\r\n//ACCTFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS\r\n//DISCGRP  DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS\r\n//TRANSACT DD DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(RECFM=F,LRECL=350,BLKSIZE=0),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.SYSTRAN(+1)\r\n",
              start_line: 3,
              end_line: 22
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.LOADLIB"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    program_id: "CBACT04C"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TCATBALF",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS",
                    variable_name: "TCATBALF",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.VSAM.KSDS",
                    program_id: "CBACT04C"
                  }
                ],
                logic: null
              },
              {
                ddname: "XREFFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    variable_name: "XREFFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    program_id: "CBACT04C"
                  }
                ],
                logic: null
              },
              {
                ddname: "XREFFIL1",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.PATH"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.PATH",
                    variable_name: "XREFFIL1",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.PATH",
                    program_id: "CBACT04C"
                  }
                ],
                logic: null
              },
              {
                ddname: "ACCTFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
                    variable_name: "ACCTFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
                    program_id: "CBACT04C"
                  }
                ],
                logic: null
              },
              {
                ddname: "DISCGRP",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS",
                    variable_name: "DISCGRP",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS",
                    program_id: "CBACT04C"
                  }
                ],
                logic: null
              },
              {
                ddname: "TRANSACT",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "F",
                  RECFM: "F",
                  LRECL: "F",
                  BLKSIZE: "F",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.SYSTRAN(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.SYSTRAN(+1)",
                    variable_name: "TRANSACT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.SYSTRAN(+1)",
                    program_id: "CBACT04C"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c16a",
      source: "672b29c93e4eb3f0ec40c081",
      target: "672b29c93e4eb3f0ec40c035",
      type: "STATIC_CALL",
      group: ["INTCALC"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "9999-ABEND-PROGRAM",
            identifier: [],
            programName: "'CEE3ABD'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c16b",
      source: "672b29c93e4eb3f0ec40c081",
      target: "672b29c93e4eb3f0ec40c047",
      type: "HAS_COPYBOOK",
      group: ["INTCALC"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c16c",
      source: "672b29c93e4eb3f0ec40c081",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: ["INTCALC"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c16d",
      source: "672b29c93e4eb3f0ec40c081",
      target: "672b29c93e4eb3f0ec40c07f",
      type: "HAS_COPYBOOK",
      group: ["INTCALC"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c16e",
      source: "672b29c93e4eb3f0ec40c081",
      target: "672b29c93e4eb3f0ec40c01d",
      type: "HAS_COPYBOOK",
      group: ["INTCALC"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c16f",
      source: "672b29c93e4eb3f0ec40c081",
      target: "672b29c93e4eb3f0ec40c01f",
      type: "HAS_COPYBOOK",
      group: ["INTCALC"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c170",
      source: "672b29c93e4eb3f0ec40c082",
      target: "672b29c93e4eb3f0ec40c034",
      type: "EXEC_PGM",
      group: ["READCARD"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=CBACT02C\r\n//STEPLIB  DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB\r\n//CARDFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS\r\n//SYSOUT   DD SYSOUT=*\r\n//SYSPRINT DD SYSOUT=*\r\n",
              start_line: 22,
              end_line: 28
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.LOADLIB"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    program_id: "CBACT02C"
                  }
                ],
                logic: null
              },
              {
                ddname: "CARDFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS",
                    variable_name: "CARDFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS",
                    program_id: "CBACT02C"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c171",
      source: "672b29c93e4eb3f0ec40c083",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["TRANTYPE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS -\r\n          CLUSTER\r\n   SET    MAXCC = 0\r\n",
              start_line: 22,
              end_line: 27
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS -\r\n          CLUSTER\r\n   SET    MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(2 0) -\r\n          RECORDSIZE(60 60) -\r\n          SHAREOPTIONS(1 4) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS.IDX) -\r\n          )\r\n",
              start_line: 33,
              end_line: 49
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(2 0) -\r\n          RECORDSIZE(60 60) -\r\n          SHAREOPTIONS(1 4) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS.IDX) -\r\n          )\r\n"
              }
            ]
          },
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//TRANTYPE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANTYPE.PS\r\n//TTYPVSAM DD DISP=OLD,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(TRANTYPE) OUTFILE(TTYPVSAM)\r\n",
              start_line: 54,
              end_line: 61
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TRANTYPE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANTYPE.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANTYPE.PS",
                    variable_name: "TRANTYPE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANTYPE.PS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "TTYPVSAM",
                parameters_map: {
                  DISP: "OLD",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS",
                    variable_name: "TTYPVSAM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANTYPE.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(TRANTYPE) OUTFILE(TTYPVSAM)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c172",
      source: "672b29c93e4eb3f0ec40c084",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COTRN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c173",
      source: "672b29c93e4eb3f0ec40c084",
      target: "672b29c93e4eb3f0ec40c043",
      type: "HAS_COPYBOOK",
      group: ["COTRN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c174",
      source: "672b29c93e4eb3f0ec40c084",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COTRN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c175",
      source: "672b29c93e4eb3f0ec40c084",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COTRN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c176",
      source: "672b29c93e4eb3f0ec40c084",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COTRN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c177",
      source: "672b29c93e4eb3f0ec40c084",
      target: "672b29c93e4eb3f0ec40c01f",
      type: "HAS_COPYBOOK",
      group: ["COTRN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c178",
      source: "672b29c93e4eb3f0ec40c084",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COTRN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c179",
      source: "672b29c93e4eb3f0ec40c084",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COTRN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c17a",
      source: "672b29c93e4eb3f0ec40c085",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["DISCGRP"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS -\r\n          CLUSTER\r\n   SET    MAXCC = 0\r\n",
              start_line: 22,
              end_line: 27
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS -\r\n          CLUSTER\r\n   SET    MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(50 50) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS.IDX) -\r\n          )\r\n",
              start_line: 33,
              end_line: 49
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(50 50) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS.IDX) -\r\n          )\r\n"
              }
            ]
          },
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//DISCGRP DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.DISCGRP.PS\r\n//DISCVSAM DD DISP=OLD,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(DISCGRP) OUTFILE(DISCVSAM)\r\n",
              start_line: 54,
              end_line: 61
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "DISCGRP",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.DISCGRP.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.DISCGRP.PS",
                    variable_name: "DISCGRP",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.DISCGRP.PS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "DISCVSAM",
                parameters_map: {
                  DISP: "OLD",
                  DSN: "FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS",
                    variable_name: "DISCVSAM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.DISCGRP.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(DISCGRP) OUTFILE(DISCVSAM)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c17b",
      source: "672b29c93e4eb3f0ec40c087",
      target: "672b29c93e4eb3f0ec40c02d",
      type: "EXEC_PGM",
      group: ["CARDFILE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "CLCIFIL",
            code: {
              content:
                "//CLCIFIL EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /F CICSA,'CEMT SET FIL(CARDDAT ) CLO'\r\n /F CICSA,'CEMT SET FIL(CARDAIX ) CLO'\r\n",
              start_line: 22,
              end_line: 27
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /F CICSA,'CEMT SET FIL(CARDDAT ) CLO'\r\n /F CICSA,'CEMT SET FIL(CARDAIX ) CLO'\r\n"
              }
            ]
          },
          {
            step_name: "OPCIFIL",
            code: {
              content:
                "//OPCIFIL EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /F CICSA,'CEMT SET FIL(CARDDAT ) OPE'\r\n /F CICSA,'CEMT SET FIL(CARDAIX ) OPE'\r\n//\r\n",
              start_line: 118,
              end_line: 125
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /F CICSA,'CEMT SET FIL(CARDDAT ) OPE'\r\n /F CICSA,'CEMT SET FIL(CARDAIX ) OPE'\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c17c",
      source: "672b29c93e4eb3f0ec40c087",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["CARDFILE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n   DELETE FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX -\r\n          ALTERNATEINDEX\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n",
              start_line: 33,
              end_line: 41
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n   DELETE FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX -\r\n          ALTERNATEINDEX\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(150 150) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS.IDX) -\r\n          )\r\n",
              start_line: 47,
              end_line: 63
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(150 150) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS.IDX) -\r\n          )\r\n"
              }
            ]
          },
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//CARDDATA DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDDATA.PS\r\n//CARDVSAM DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(CARDDATA) OUTFILE(CARDVSAM)\r\n",
              start_line: 68,
              end_line: 75
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CARDDATA",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDDATA.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDDATA.PS",
                    variable_name: "CARDDATA",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDDATA.PS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "CARDVSAM",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS",
                    variable_name: "CARDVSAM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(CARDDATA) OUTFILE(CARDVSAM)\r\n"
              }
            ]
          },
          {
            step_name: "STEP40",
            code: {
              content:
                "//STEP40  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n   DEFINE ALTERNATEINDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX)-\r\n   RELATE(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS)                    -\r\n   KEYS(11 16)                                                   -\r\n   NONUNIQUEKEY                                                  -\r\n   UPGRADE                                                       -\r\n   RECORDSIZE(150,150)                                           -\r\n   VOLUMES(USER04)                                               -\r\n   CYLINDERS(5,1))                                               -\r\n   DATA (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX.DAT))           -\r\n   INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX.IDX))\r\n",
              start_line: 80,
              end_line: 92
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE ALTERNATEINDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX)-\r\n   RELATE(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS)                    -\r\n   KEYS(11 16)                                                   -\r\n   NONUNIQUEKEY                                                  -\r\n   UPGRADE                                                       -\r\n   RECORDSIZE(150,150)                                           -\r\n   VOLUMES(USER04)                                               -\r\n   CYLINDERS(5,1))                                               -\r\n   DATA (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX.DAT))           -\r\n   INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX.IDX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP50",
            code: {
              content:
                "//STEP50  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n  DEFINE PATH                                           -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX.PATH)        -\r\n    PATHENTRY(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX))\r\n",
              start_line: 97,
              end_line: 102
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "  DEFINE PATH                                           -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX.PATH)        -\r\n    PATHENTRY(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP60",
            code: {
              content:
                "//STEP60  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n   BLDINDEX                                                      -\r\n   INDATASET(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS)                 -\r\n   OUTDATASET(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX)\r\n",
              start_line: 107,
              end_line: 112
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   BLDINDEX                                                      -\r\n   INDATASET(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.KSDS)                 -\r\n   OUTDATASET(FPTLT01.DEMO.CARDDEMO.CARDDATA.VSAM.AIX)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c17d",
      source: "672b29c93e4eb3f0ec40c088",
      target: "672b29c93e4eb3f0ec40c089",
      type: "EXEC_PGM",
      group: ["READXREF"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=CBACT03C\r\n//STEPLIB  DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB\r\n//XREFFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS\r\n//SYSOUT   DD SYSOUT=*\r\n//SYSPRINT DD SYSOUT=*\r\n",
              start_line: 22,
              end_line: 28
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.LOADLIB"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    program_id: "CBACT03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "XREFFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    variable_name: "XREFFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    program_id: "CBACT03C"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c17e",
      source: "672b29c93e4eb3f0ec40c089",
      target: "672b29c93e4eb3f0ec40c035",
      type: "STATIC_CALL",
      group: ["READXREF"],
      properties: {
        label: "STATIC_CALL",
        calls: [
          {
            paragraph: "9999-ABEND-PROGRAM",
            identifier: [],
            programName: "'CEE3ABD'"
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c17f",
      source: "672b29c93e4eb3f0ec40c089",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: ["READXREF"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c180",
      source: "672b29c93e4eb3f0ec40c08a",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["TRANCATG"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS -\r\n          CLUSTER\r\n   SET    MAXCC = 0\r\n",
              start_line: 22,
              end_line: 27
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS -\r\n          CLUSTER\r\n   SET    MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(6 0) -\r\n          RECORDSIZE(60 60) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS.IDX) -\r\n          )\r\n",
              start_line: 33,
              end_line: 49
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(6 0) -\r\n          RECORDSIZE(60 60) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS.IDX) -\r\n          )\r\n"
              }
            ]
          },
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//TRANCATG DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANCATG.PS\r\n//TCATVSAM DD DISP=OLD,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(TRANCATG) OUTFILE(TCATVSAM)\r\n",
              start_line: 54,
              end_line: 61
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TRANCATG",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANCATG.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANCATG.PS",
                    variable_name: "TRANCATG",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANCATG.PS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "TCATVSAM",
                parameters_map: {
                  DISP: "OLD",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS",
                    variable_name: "TCATVSAM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANCATG.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(TRANCATG) OUTFILE(TCATVSAM)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c181",
      source: "672b29c93e4eb3f0ec40c08b",
      target: "672b29c93e4eb3f0ec40c02d",
      type: "EXEC_PGM",
      group: ["CLOSEFIL"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "CLCIFIL",
            code: {
              content:
                "//CLCIFIL EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /F CICSA,'CEMT SET FIL(TRANSACT ) CLO'\r\n /F CICSA,'CEMT SET FIL(CCXREF ) CLO'\r\n /F CICSA,'CEMT SET FIL(ACCTDAT ) CLO'\r\n /F CICSA,'CEMT SET FIL(CXACAIX ) CLO'\r\n /F CICSA,'CEMT SET FIL(USRSEC ) CLO'\r\n",
              start_line: 22,
              end_line: 30
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /F CICSA,'CEMT SET FIL(TRANSACT ) CLO'\r\n /F CICSA,'CEMT SET FIL(CCXREF ) CLO'\r\n /F CICSA,'CEMT SET FIL(ACCTDAT ) CLO'\r\n /F CICSA,'CEMT SET FIL(CXACAIX ) CLO'\r\n /F CICSA,'CEMT SET FIL(USRSEC ) CLO'\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c182",
      source: "672b29c93e4eb3f0ec40c08c",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["TRANBKP"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n   DELETE FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX -\r\n          ALTERNATEINDEX\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n",
              start_line: 37,
              end_line: 45
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n   DELETE FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX -\r\n          ALTERNATEINDEX\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS,COND=(4,LT)\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(AWSHJ1 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(350 350) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS.DATA) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS.INDEX) -\r\n          )\r\n",
              start_line: 51,
              end_line: 67
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(AWSHJ1 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(350 350) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS.DATA) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS.INDEX) -\r\n          )\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c183",
      source: "672b29c93e4eb3f0ec40c08e",
      target: "672b29c93e4eb3f0ec40c02f",
      type: "EXEC_PGM",
      group: ["DUSRSECJ"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "PREDEL",
            code: {
              content:
                "//PREDEL  EXEC PGM=IEFBR14\r\n//DD01     DD DSN=FPTLT01.DEMO.CARDDEMO.USRSEC.PS,\r\n//            DISP=(MOD,DELETE,DELETE),\r\n//            SPACE=(TRK,1)\r\n",
              start_line: 23,
              end_line: 27
            },
            statements: [
              {
                ddname: "DD01",
                parameters_map: {
                  DSN: "FPTLT01.DEMO.CARDDEMO.USRSEC.PS",
                  DISP: "(MOD,DELETE,DELETE)",
                  SPACE: "(TRK,1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.USRSEC.PS",
                    variable_name: "DD01",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.USRSEC.PS",
                    program_id: "IEFBR14"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c184",
      source: "672b29c93e4eb3f0ec40c08e",
      target: "672b29c93e4eb3f0ec40c08f",
      type: "EXEC_PGM",
      group: ["DUSRSECJ"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP01",
            code: {
              content:
                "//STEP01  EXEC PGM=IEBGENER\r\n//SYSUT1   DD *\r\nADMIN001MARGARET            GOLD                PASSWORDA\r\nADMIN002RUSSELL             RUSSELL             PASSWORDA\r\nADMIN003RAYMOND             WHITMORE            PASSWORDA\r\nADMIN004EMMANUEL            CASGRAIN            PASSWORDA\r\nADMIN005GRANVILLE           LACHAPELLE          PASSWORDA\r\nUSER0001LAWRENCE            THOMAS              PASSWORDU\r\nUSER0002AJITH               KUMAR               PASSWORDU\r\nUSER0003LAURITZ             ALME                PASSWORDU\r\nUSER0004AVERARDO            MAZZI               PASSWORDU\r\nUSER0005LEE                 TING                PASSWORDU\r\n//SYSUT2   DD DSN=FPTLT01.DEMO.CARDDEMO.USRSEC.PS,\r\n//            DISP=(NEW,CATLG,DELETE),\r\n//            DCB=(LRECL=80,RECFM=FB,DSORG=PS,BLKSIZE=0),\r\n//            UNIT=SYSDA,SPACE=(TRK,(10,5),RLSE)\r\n//SYSPRINT DD SYSOUT=*\r\n//SYSIN    DD DUMMY\r\n",
              start_line: 33,
              end_line: 53
            },
            statements: [
              {
                ddname: "SYSUT1",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "ADMIN001MARGARET            GOLD                PASSWORDA\r\nADMIN002RUSSELL             RUSSELL             PASSWORDA\r\nADMIN003RAYMOND             WHITMORE            PASSWORDA\r\nADMIN004EMMANUEL            CASGRAIN            PASSWORDA\r\nADMIN005GRANVILLE           LACHAPELLE          PASSWORDA\r\nUSER0001LAWRENCE            THOMAS              PASSWORDU\r\nUSER0002AJITH               KUMAR               PASSWORDU\r\nUSER0003LAURITZ             ALME                PASSWORDU\r\nUSER0004AVERARDO            MAZZI               PASSWORDU\r\nUSER0005LEE                 TING                PASSWORDU\r\n"
              },
              {
                ddname: "SYSUT2",
                parameters_map: {
                  DSN: "FPTLT01.DEMO.CARDDEMO.USRSEC.PS",
                  DISP: "(NEW,CATLG,DELETE)",
                  DCB: "80",
                  LRECL: "80",
                  RECFM: "80",
                  DSORG: "80",
                  BLKSIZE: "80",
                  UNIT: "SYSDA",
                  SPACE: "SYSDA"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.USRSEC.PS",
                    variable_name: "SYSUT2",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.USRSEC.PS",
                    program_id: "IEBGENER"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "DUMMY"
                },
                dataset_map_list: [],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c185",
      source: "672b29c93e4eb3f0ec40c08e",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["DUSRSECJ"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP02",
            code: {
              content:
                "//STEP02  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n DELETE                  FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS\r\n SET       MAXCC = 0\r\n DEFINE    CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS)    -\r\n                    KEYS(8,0)                                 -\r\n                    RECORDSIZE(80,80)                         -\r\n                    REUSE                                     -\r\n                    INDEXED                                   -\r\n                    VOLUMES(USER04)                           -\r\n                    TRACKS(45,15)                             -\r\n                    FREESPACE(10,15)                          -\r\n                    CISZ(8192))                               -\r\n           DATA    (NAME(FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS.DAT)) -\r\n           INDEX   (NAME(FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS.IDX))\r\n",
              start_line: 59,
              end_line: 75
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " DELETE                  FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS\r\n SET       MAXCC = 0\r\n DEFINE    CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS)    -\r\n                    KEYS(8,0)                                 -\r\n                    RECORDSIZE(80,80)                         -\r\n                    REUSE                                     -\r\n                    INDEXED                                   -\r\n                    VOLUMES(USER04)                           -\r\n                    TRACKS(45,15)                             -\r\n                    FREESPACE(10,15)                          -\r\n                    CISZ(8192))                               -\r\n           DATA    (NAME(FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS.DAT)) -\r\n           INDEX   (NAME(FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS.IDX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP03",
            code: {
              content:
                "//STEP03  EXEC PGM=IDCAMS\r\n//IN       DD  DSN=FPTLT01.DEMO.CARDDEMO.USRSEC.PS,DISP=SHR\r\n//OUT      DD  DSN=FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS,DISP=SHR\r\n//SYSOUT   DD  SYSOUT=*\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n  REPRO INFILE(IN) OUTFILE(OUT)\r\n//\r\n",
              start_line: 82,
              end_line: 91
            },
            statements: [
              {
                ddname: "IN",
                parameters_map: {
                  DSN: "FPTLT01.DEMO.CARDDEMO.USRSEC.PS",
                  DISP: "FPTLT01.DEMO.CARDDEMO.USRSEC.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.USRSEC.PS",
                    variable_name: "IN",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.USRSEC.PS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "OUT",
                parameters_map: {
                  DSN: "FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS",
                  DISP: "FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS",
                    variable_name: "OUT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.USRSEC.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "  REPRO INFILE(IN) OUTFILE(OUT)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c186",
      source: "672b29c93e4eb3f0ec40c091",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COUSR00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c187",
      source: "672b29c93e4eb3f0ec40c091",
      target: "672b29c93e4eb3f0ec40c065",
      type: "HAS_COPYBOOK",
      group: ["COUSR00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c188",
      source: "672b29c93e4eb3f0ec40c091",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COUSR00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c189",
      source: "672b29c93e4eb3f0ec40c091",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COUSR00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c18a",
      source: "672b29c93e4eb3f0ec40c091",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COUSR00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c18b",
      source: "672b29c93e4eb3f0ec40c091",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: ["COUSR00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c18c",
      source: "672b29c93e4eb3f0ec40c091",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COUSR00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c18d",
      source: "672b29c93e4eb3f0ec40c091",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COUSR00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c18e",
      source: "672b29c93e4eb3f0ec40c092",
      target: "672b29c93e4eb3f0ec40c091",
      type: "HAS_INTERACT",
      group: ["COUSR00"],
      properties: {
        label: "HAS_INTERACT"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c18f",
      source: "672b29c93e4eb3f0ec40c095",
      target: "672b29c93e4eb3f0ec40c02f",
      type: "EXEC_PGM",
      group: ["PRTCATBL"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "DELDEF",
            code: {
              content:
                "//DELDEF   EXEC PGM=IEFBR14\r\n//THEFILE  DD DISP=(MOD,DELETE),\r\n//         UNIT=SYSDA,\r\n//         SPACE=(TRK,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.REPT\r\n",
              start_line: 21,
              end_line: 25
            },
            statements: [
              {
                ddname: "THEFILE",
                parameters_map: {
                  DISP: "(MOD,DELETE)",
                  UNIT: "SYSDA",
                  SPACE: "(TRK,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TCATBALF.REPT"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TCATBALF.REPT",
                    variable_name: "THEFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.REPT",
                    program_id: "IEFBR14"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c190",
      source: "672b29c93e4eb3f0ec40c095",
      target: "672b29c93e4eb3f0ec40c014",
      type: "EXEC_PGM",
      group: ["PRTCATBL"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP10R",
            code: {
              content:
                "//STEP10R  EXEC PGM=SORT\r\n//SORTIN   DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.BKUP(+1)\r\n//SYMNAMES DD *\r\nTRANCAT-ACCT-ID,1,11,ZD\r\nTRANCAT-TYPE-CD,12,2,CH\r\nTRANCAT-CD,14,4,ZD\r\nTRAN-CAT-BAL,18,11,ZD\r\n//SYSIN    DD *\r\n SORT FIELDS=(TRANCAT-ACCT-ID,A,TRANCAT-TYPE-CD,A,TRANCAT-CD,A)\r\n OUTREC FIELDS=(TRANCAT-ACCT-ID,X,\r\n     TRANCAT-TYPE-CD,X,\r\n     TRANCAT-CD,X,\r\n     TRAN-CAT-BAL,EDIT=(TTTTTTTTT.TT),9X)\r\n//SYSOUT   DD SYSOUT=*\r\n//SORTOUT  DD DISP=(NEW,CATLG,DELETE),\r\n//         UNIT=SYSDA,\r\n//         DCB=(LRECL=40,RECFM=FB,BLKSIZE=0),\r\n//         SPACE=(CYL,(1,1),RLSE),\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.REPT\r\n",
              start_line: 43,
              end_line: 63
            },
            statements: [
              {
                ddname: "SORTIN",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TCATBALF.BKUP(+1)"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TCATBALF.BKUP(+1)",
                    variable_name: "SORTIN",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.BKUP(+1)",
                    program_id: "SORT"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYMNAMES",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "TRANCAT-ACCT-ID,1,11,ZD\r\nTRANCAT-TYPE-CD,12,2,CH\r\nTRANCAT-CD,14,4,ZD\r\nTRAN-CAT-BAL,18,11,ZD\r\n"
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " SORT FIELDS=(TRANCAT-ACCT-ID,A,TRANCAT-TYPE-CD,A,TRANCAT-CD,A)\r\n OUTREC FIELDS=(TRANCAT-ACCT-ID,X,\r\n     TRANCAT-TYPE-CD,X,\r\n     TRANCAT-CD,X,\r\n     TRAN-CAT-BAL,EDIT=(TTTTTTTTT.TT),9X)\r\n"
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SORTOUT",
                parameters_map: {
                  DISP: "(NEW,CATLG,DELETE)",
                  UNIT: "SYSDA",
                  DCB: "40",
                  LRECL: "40",
                  RECFM: "40",
                  BLKSIZE: "40",
                  SPACE: "(CYL,(1,1),RLSE)",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TCATBALF.REPT"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TCATBALF.REPT",
                    variable_name: "SORTOUT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TCATBALF.REPT",
                    program_id: "SORT"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c191",
      source: "672b29c93e4eb3f0ec40c096",
      target: "672b29c93e4eb3f0ec40c06a",
      type: "EXEC_PGM",
      group: ["READCUST"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=CBCUS01C\r\n//STEPLIB  DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB\r\n//CUSTFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS\r\n//SYSOUT   DD SYSOUT=*\r\n//SYSPRINT DD SYSOUT=*\r\n",
              start_line: 6,
              end_line: 12
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.LOADLIB"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    program_id: "CBCUS01C"
                  }
                ],
                logic: null
              },
              {
                ddname: "CUSTFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS",
                    variable_name: "CUSTFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CUSTDATA.VSAM.KSDS",
                    program_id: "CBCUS01C"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c192",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c02a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c193",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c194",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c195",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c196",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c197",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c098",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c198",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c199",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c19a",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c19b",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c036",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c19c",
      source: "672b29c93e4eb3f0ec40c097",
      target: "672b29c93e4eb3f0ec40c05c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c19d",
      source: "672b29c93e4eb3f0ec40c099",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["XREFFILE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n   DELETE  FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX  -\r\n          ALTERNATEINDEX\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n",
              start_line: 22,
              end_line: 30
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n   DELETE  FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX  -\r\n          ALTERNATEINDEX\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(50 50) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS.IDX) -\r\n          )\r\n",
              start_line: 36,
              end_line: 52
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(50 50) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS.IDX) -\r\n          )\r\n"
              }
            ]
          },
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//XREFDATA DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.PS\r\n//XREFVSAM DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(XREFDATA) OUTFILE(XREFVSAM)\r\n",
              start_line: 57,
              end_line: 64
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "XREFDATA",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDXREF.PS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDXREF.PS",
                    variable_name: "XREFDATA",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.PS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "XREFVSAM",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    variable_name: "XREFVSAM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(XREFDATA) OUTFILE(XREFVSAM)\r\n"
              }
            ]
          },
          {
            step_name: "STEP20",
            code: {
              content:
                "//STEP20  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n   DEFINE ALTERNATEINDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX)-\r\n   RELATE(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS)                    -\r\n   KEYS(11,25)                                                   -\r\n   NONUNIQUEKEY                                                  -\r\n   UPGRADE                                                       -\r\n   RECORDSIZE(50,50)                                             -\r\n   FREESPACE(10,20)                                              -\r\n   VOLUMES(USER04)                                               -\r\n   CYLINDERS(5,1))                                               -\r\n   DATA (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.DAT))           -\r\n   INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.IDX))\r\n",
              start_line: 69,
              end_line: 82
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE ALTERNATEINDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX)-\r\n   RELATE(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS)                    -\r\n   KEYS(11,25)                                                   -\r\n   NONUNIQUEKEY                                                  -\r\n   UPGRADE                                                       -\r\n   RECORDSIZE(50,50)                                             -\r\n   FREESPACE(10,20)                                              -\r\n   VOLUMES(USER04)                                               -\r\n   CYLINDERS(5,1))                                               -\r\n   DATA (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.DAT))           -\r\n   INDEX (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.IDX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP25",
            code: {
              content:
                "//STEP25  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n  DEFINE PATH                                           -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.PATH)        -\r\n    PATHENTRY(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX))\r\n",
              start_line: 87,
              end_line: 92
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "  DEFINE PATH                                           -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX.PATH)        -\r\n    PATHENTRY(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP30",
            code: {
              content:
                "//STEP30  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n   BLDINDEX                                                      -\r\n   INDATASET(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS)                 -\r\n   OUTDATASET(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX)\r\n",
              start_line: 97,
              end_line: 102
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   BLDINDEX                                                      -\r\n   INDATASET(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.KSDS)                 -\r\n   OUTDATASET(FPTLT01.DEMO.CARDDEMO.CARDXREF.VSAM.AIX)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c19e",
      source: "672b29c93e4eb3f0ec40c09b",
      target: "672b29c93e4eb3f0ec40c04c",
      type: "EXEC_PGM",
      group: ["READACCT"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=CBACT01C\r\n//STEPLIB  DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB\r\n//ACCTFILE DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS\r\n//SYSOUT   DD SYSOUT=*\r\n//SYSPRINT DD SYSOUT=*\r\n",
              start_line: 22,
              end_line: 28
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.LOADLIB"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.LOADLIB",
                    program_id: "CBACT01C"
                  }
                ],
                logic: null
              },
              {
                ddname: "ACCTFILE",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
                    variable_name: "ACCTFILE",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
                    program_id: "CBACT01C"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c19f",
      source: "672b29c93e4eb3f0ec40c09c",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: ["COSGN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a0",
      source: "672b29c93e4eb3f0ec40c09c",
      target: "672b29c93e4eb3f0ec40c093",
      type: "HAS_COPYBOOK",
      group: ["COSGN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a1",
      source: "672b29c93e4eb3f0ec40c09c",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: ["COSGN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a2",
      source: "672b29c93e4eb3f0ec40c09c",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: ["COSGN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a3",
      source: "672b29c93e4eb3f0ec40c09c",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: ["COSGN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a4",
      source: "672b29c93e4eb3f0ec40c09c",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: ["COSGN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a5",
      source: "672b29c93e4eb3f0ec40c09c",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: ["COSGN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a6",
      source: "672b29c93e4eb3f0ec40c09c",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: ["COSGN00"],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a7",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c02a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a8",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c018",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1a9",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c021",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1aa",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c020",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1ab",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c01a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1ac",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c09e",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1ad",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c01b",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1ae",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c01c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1af",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c05a",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b0",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c027",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b1",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c01d",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b2",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c036",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b3",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c01e",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b4",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c053",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b5",
      source: "672b29c93e4eb3f0ec40c09d",
      target: "672b29c93e4eb3f0ec40c05c",
      type: "HAS_COPYBOOK",
      group: [],
      properties: {
        label: "HAS_COPYBOOK"
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b6",
      source: "672b29c93e4eb3f0ec40c0a0",
      target: "672b29c93e4eb3f0ec40c02d",
      type: "EXEC_PGM",
      group: ["TRANFILE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "CLCIFIL",
            code: {
              content:
                "//CLCIFIL EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /F CICSA,'CEMT SET FIL(TRANSACT ) CLO'\r\n /F CICSA,'CEMT SET FIL(CXACAIX ) CLO'\r\n",
              start_line: 22,
              end_line: 27
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /F CICSA,'CEMT SET FIL(TRANSACT ) CLO'\r\n /F CICSA,'CEMT SET FIL(CXACAIX ) CLO'\r\n"
              }
            ]
          },
          {
            step_name: "OPCIFIL",
            code: {
              content:
                "//OPCIFIL EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /F CICSA,'CEMT SET FIL(TRANSACT ) OPE'\r\n /F CICSA,'CEMT SET FIL(CXACAIX ) OPE'\r\n",
              start_line: 116,
              end_line: 121
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  " /F CICSA,'CEMT SET FIL(TRANSACT ) OPE'\r\n /F CICSA,'CEMT SET FIL(CXACAIX ) OPE'\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b7",
      source: "672b29c93e4eb3f0ec40c0a0",
      target: "672b29c93e4eb3f0ec40c015",
      type: "EXEC_PGM",
      group: ["TRANFILE"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "STEP05",
            code: {
              content:
                "//STEP05 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DELETE FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n   DELETE FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX -\r\n          ALTERNATEINDEX\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n",
              start_line: 32,
              end_line: 40
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DELETE FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n   DELETE FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX -\r\n          ALTERNATEINDEX\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n"
              }
            ]
          },
          {
            step_name: "STEP10",
            code: {
              content:
                "//STEP10 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//SYSIN    DD   *\r\n   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(350 350) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS.IDX) -\r\n          )\r\n",
              start_line: 46,
              end_line: 62
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS) -\r\n          CYLINDERS(1 5) -\r\n          VOLUMES(USER04 -\r\n          ) -\r\n          KEYS(16 0) -\r\n          RECORDSIZE(350 350) -\r\n          SHAREOPTIONS(2 3) -\r\n          ERASE -\r\n          INDEXED -\r\n          ) -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS.DAT) -\r\n          ) -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS.IDX) -\r\n          )\r\n"
              }
            ]
          },
          {
            step_name: "STEP15",
            code: {
              content:
                "//STEP15 EXEC PGM=IDCAMS\r\n//SYSPRINT DD   SYSOUT=*\r\n//TRANSACT DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.DALYTRAN.PS.INIT\r\n//TRANVSAM DD DISP=SHR,\r\n//         DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS\r\n//SYSIN    DD   *\r\n   REPRO INFILE(TRANSACT) OUTFILE(TRANVSAM)\r\n",
              start_line: 67,
              end_line: 74
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "TRANSACT",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.DALYTRAN.PS.INIT"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.DALYTRAN.PS.INIT",
                    variable_name: "TRANSACT",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.DALYTRAN.PS.INIT",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "TRANVSAM",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS",
                    variable_name: "TRANVSAM",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS",
                    program_id: "IDCAMS"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: "   REPRO INFILE(TRANSACT) OUTFILE(TRANVSAM)\r\n"
              }
            ]
          },
          {
            step_name: "STEP20",
            code: {
              content:
                "//STEP20  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n   DEFINE ALTERNATEINDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX)-\r\n   RELATE(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS)                    -\r\n   KEYS(26 304)                                                  -\r\n   NONUNIQUEKEY                                                  -\r\n   UPGRADE                                                       -\r\n   RECORDSIZE(350,350)                                           -\r\n   VOLUMES(USER04)                                               -\r\n   CYLINDERS(5,1))                                               -\r\n   DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.DAT))           -\r\n   INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.IDX))\r\n",
              start_line: 79,
              end_line: 91
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   DEFINE ALTERNATEINDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX)-\r\n   RELATE(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS)                    -\r\n   KEYS(26 304)                                                  -\r\n   NONUNIQUEKEY                                                  -\r\n   UPGRADE                                                       -\r\n   RECORDSIZE(350,350)                                           -\r\n   VOLUMES(USER04)                                               -\r\n   CYLINDERS(5,1))                                               -\r\n   DATA (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.DAT))           -\r\n   INDEX (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.IDX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP25",
            code: {
              content:
                "//STEP25  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n  DEFINE PATH                                           -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.PATH)        -\r\n    PATHENTRY(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX))\r\n",
              start_line: 96,
              end_line: 101
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "  DEFINE PATH                                           -\r\n   (NAME(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX.PATH)        -\r\n    PATHENTRY(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX))\r\n"
              }
            ]
          },
          {
            step_name: "STEP30",
            code: {
              content:
                "//STEP30  EXEC PGM=IDCAMS\r\n//SYSPRINT DD  SYSOUT=*\r\n//SYSIN    DD  *\r\n   BLDINDEX                                                      -\r\n   INDATASET(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS)                 -\r\n   OUTDATASET(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX)\r\n",
              start_line: 106,
              end_line: 111
            },
            statements: [
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic:
                  "   BLDINDEX                                                      -\r\n   INDATASET(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.KSDS)                 -\r\n   OUTDATASET(FPTLT01.DEMO.CARDDEMO.TRANSACT.VSAM.AIX)\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b8",
      source: "672b29c93e4eb3f0ec40c0a3",
      target: "672b29c93e4eb3f0ec40c02d",
      type: "EXEC_PGM",
      group: ["CMP1BMS"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "SDSF1",
            code: {
              content:
                "//SDSF1 EXEC PGM=SDSF\r\n//ISFOUT DD SYSOUT=*\r\n//CMDOUT DD SYSOUT=*\r\n//ISFIN  DD *\r\n /MODIFY CICSCICS,'CEMT SET PROG(COSGN00) NEWCOPY'\r\n",
              start_line: 6,
              end_line: 10
            },
            statements: [
              {
                ddname: "ISFOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CMDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "ISFIN",
                parameters_map: {
                  UNNAMED_1: "*"
                },
                dataset_map_list: [],
                logic: " /MODIFY CICSCICS,'CEMT SET PROG(COSGN00) NEWCOPY'\r\n"
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1b9",
      source: "672b29c93e4eb3f0ec40c0a5",
      target: "672b29c93e4eb3f0ec40c0a6",
      type: "EXEC_PGM",
      group: ["RACFUN"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "UNLOAD",
            code: {
              content:
                "//UNLOAD  EXEC PGM=IRRDBU00,PARM='NOLOCKINPUT'                          00050001\r\n//INDD1    DD DSN=SYS1.BACKUP.RACF,DISP=SHR                             00060001\r\n//OUTDD    DD DSN=FPTLT01.RACF.UNLOAD,DISP=(,CATLG),                    00070001\r\n//         UNIT=SYSDA,SPACE=(CYL,(50,50)),                              00080001\r\n//         RECFM=VB,LRECL=4096                                          00090001\r\n//SYSPRINT DD SYSOUT=*                                                  00100001\r\n",
              start_line: 5,
              end_line: 10
            },
            statements: [
              {
                ddname: "INDD1",
                parameters_map: {
                  DSN: "SYS1.BACKUP.RACF",
                  DISP: "SYS1.BACKUP.RACF"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SYS1.BACKUP.RACF",
                    variable_name: "INDD1",
                    dd_statement: "DSN=SYS1.BACKUP.RACF",
                    program_id: "IRRDBU00"
                  }
                ],
                logic: null
              },
              {
                ddname: "OUTDD",
                parameters_map: {
                  DSN: "FPTLT01.RACF.UNLOAD",
                  DISP: "FPTLT01.RACF.UNLOAD",
                  UNIT: "SYSDA",
                  SPACE: "SYSDA",
                  RECFM: "VB",
                  LRECL: "VB"
                },
                dataset_map_list: [
                  {
                    dataset_name: "FPTLT01.RACF.UNLOAD",
                    variable_name: "OUTDD",
                    dd_statement: "DSN=FPTLT01.RACF.UNLOAD",
                    program_id: "IRRDBU00"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              }
            ]
          }
        ]
      }
    },
    {
      _id: "672b29c93e4eb3f0ec40c1ba",
      source: "672b29c93e4eb3f0ec40c0a7",
      target: "672b29c93e4eb3f0ec40c04a",
      type: "EXEC_PGM",
      group: ["CMPCSD"],
      properties: {
        label: "EXEC_PGM",
        steps: [
          {
            step_name: "CSDDEF",
            code: {
              content:
                "//CSDDEF      EXEC PGM=DFHCSDUP,REGION=0M\r\n//STEPLIB  DD DSN=DFH410.SDFHLOAD,DISP=SHR\r\n//DFHCSD   DD DSN=DFH410.CICS.DFHCSD,DISP=SHR\r\n//SYSPRINT DD   SYSOUT=*\r\n//CBDOUT   DD   SYSOUT=*\r\n//AMSDUMP  DD   SYSOUT=*\r\n//SYSIN    DD DISP=SHR,DSN=FPTLT01.DEMO.CARDDEMO.CSD(CSDDEL)\r\n",
              start_line: 4,
              end_line: 10
            },
            statements: [
              {
                ddname: "STEPLIB",
                parameters_map: {
                  DSN: "DFH410.SDFHLOAD",
                  DISP: "DFH410.SDFHLOAD"
                },
                dataset_map_list: [
                  {
                    dataset_name: "DFH410.SDFHLOAD",
                    variable_name: "STEPLIB",
                    dd_statement: "DSN=DFH410.SDFHLOAD",
                    program_id: "DFHCSDUP"
                  }
                ],
                logic: null
              },
              {
                ddname: "DFHCSD",
                parameters_map: {
                  DSN: "DFH410.CICS.DFHCSD",
                  DISP: "DFH410.CICS.DFHCSD"
                },
                dataset_map_list: [
                  {
                    dataset_name: "DFH410.CICS.DFHCSD",
                    variable_name: "DFHCSD",
                    dd_statement: "DSN=DFH410.CICS.DFHCSD",
                    program_id: "DFHCSDUP"
                  }
                ],
                logic: null
              },
              {
                ddname: "SYSPRINT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "CBDOUT",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "AMSDUMP",
                parameters_map: {
                  SYSOUT: "*"
                },
                dataset_map_list: [],
                logic: null
              },
              {
                ddname: "SYSIN",
                parameters_map: {
                  DISP: "SHR",
                  DSN: "SHR"
                },
                dataset_map_list: [
                  {
                    dataset_name: "SHR",
                    variable_name: "SYSIN",
                    dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.CSD(CSDDEL)",
                    program_id: "DFHCSDUP"
                  }
                ],
                logic: null
              }
            ]
          }
        ]
      }
    }
  ],
  entry_points: [
    {
      _id: "672b29c93e4eb3f0ec40c013",
      name: "COMBTRAN",
      label: "JCL_IBM",
      group: ["COMBTRAN"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c022",
      name: "COBIL00",
      label: "BMS",
      group: ["COBIL00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c023",
      name: "POSTTRAN",
      label: "JCL_IBM",
      group: ["POSTTRAN"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c028",
      name: "COUSR01",
      label: "BMS",
      group: ["COUSR01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c029",
      name: "COTRN01",
      label: "BMS",
      group: ["COTRN01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c02c",
      name: "CMPBMS",
      label: "JCL_IBM",
      group: ["CMPBMS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c02e",
      name: "CREASTMT",
      label: "JCL_IBM",
      group: ["CREASTMT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c031",
      name: "DEFGDGB",
      label: "JCL_IBM",
      group: ["DEFGDGB"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c037",
      name: "TRANREPT",
      label: "JCL_IBM",
      group: ["TRANREPT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c039",
      name: "COTRN00",
      label: "BMS",
      group: ["COTRN00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c03d",
      name: "TCATBALF",
      label: "JCL_IBM",
      group: ["TCATBALF"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c03e",
      name: "CUSTFILE",
      label: "JCL_IBM",
      group: ["CUSTFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c041",
      name: "CORPT00",
      label: "BMS",
      group: ["CORPT00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c042",
      name: "OPENFIL",
      label: "JCL_IBM",
      group: ["OPENFIL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c044",
      name: "COCRDLI",
      label: "BMS",
      group: ["COCRDLI"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c045",
      name: "TRANIDX",
      label: "JCL_IBM",
      group: ["TRANIDX"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c048",
      name: "REPROC",
      label: "JCL_IBM",
      group: ["REPROC"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c049",
      name: "CBADMCDJ",
      label: "JCL_IBM",
      group: ["CBADMCDJ"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04b",
      name: "COUSR02",
      label: "BMS",
      group: ["COUSR02"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04d",
      name: "COSGN00B",
      label: "BMS",
      group: ["COSGN00B"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04e",
      name: "DALYREJS",
      label: "JCL_IBM",
      group: ["DALYREJS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c04f",
      name: "CMP1CSD",
      label: "JCL_IBM",
      group: ["CMP1CSD"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c050",
      name: "ACCTFILE",
      label: "JCL_IBM",
      group: ["ACCTFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c054",
      name: "BUILDBMS",
      label: "JCL_IBM",
      group: ["BUILDBMS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c055",
      name: "COACTUP",
      label: "BMS",
      group: ["COACTUP"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c060",
      name: "COTRN02",
      label: "BMS",
      group: ["COTRN02"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c063",
      name: "REPTFILE",
      label: "JCL_IBM",
      group: ["REPTFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c064",
      name: "DEFCUST",
      label: "JCL_IBM",
      group: ["DEFCUST"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c067",
      name: "COUSR03",
      label: "BMS",
      group: ["COUSR03"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c06b",
      name: "CMPCICS",
      label: "JCL_IBM",
      group: ["CMPCICS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c06c",
      name: "CMP1CICS",
      label: "JCL_IBM",
      group: ["CMP1CICS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c071",
      name: "COADM01",
      label: "BMS",
      group: ["COADM01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c072",
      name: "COSGN00",
      label: "BMS",
      group: ["COSGN00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c077",
      name: "BUILDBAT",
      label: "JCL_IBM",
      group: ["BUILDBAT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c078",
      name: "COCRDSL",
      label: "BMS",
      group: ["COCRDSL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c07a",
      name: "COMEN01",
      label: "BMS",
      group: ["COMEN01"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c07d",
      name: "CICSCOB1",
      label: "JCL_IBM",
      group: ["CICSCOB1"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c080",
      name: "INTCALC",
      label: "JCL_IBM",
      group: ["INTCALC"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c082",
      name: "READCARD",
      label: "JCL_IBM",
      group: ["READCARD"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c083",
      name: "TRANTYPE",
      label: "JCL_IBM",
      group: ["TRANTYPE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c085",
      name: "DISCGRP",
      label: "JCL_IBM",
      group: ["DISCGRP"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c086",
      name: "COCRDUP",
      label: "BMS",
      group: ["COCRDUP"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c087",
      name: "CARDFILE",
      label: "JCL_IBM",
      group: ["CARDFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c088",
      name: "READXREF",
      label: "JCL_IBM",
      group: ["READXREF"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08a",
      name: "TRANCATG",
      label: "JCL_IBM",
      group: ["TRANCATG"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08b",
      name: "CLOSEFIL",
      label: "JCL_IBM",
      group: ["CLOSEFIL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08c",
      name: "TRANBKP",
      label: "JCL_IBM",
      group: ["TRANBKP"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08d",
      name: "BUILDONL",
      label: "JCL_IBM",
      group: ["BUILDONL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c08e",
      name: "DUSRSECJ",
      label: "JCL_IBM",
      group: ["DUSRSECJ"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c092",
      name: "COUSR00",
      label: "BMS",
      group: ["COUSR00"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c095",
      name: "PRTCATBL",
      label: "JCL_IBM",
      group: ["PRTCATBL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c096",
      name: "READCUST",
      label: "JCL_IBM",
      group: ["READCUST"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c099",
      name: "XREFFILE",
      label: "JCL_IBM",
      group: ["XREFFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c09b",
      name: "READACCT",
      label: "JCL_IBM",
      group: ["READACCT"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c09f",
      name: "CMPSUB",
      label: "JCL_IBM",
      group: ["CMPSUB"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a0",
      name: "TRANFILE",
      label: "JCL_IBM",
      group: ["TRANFILE"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a1",
      name: "COACTVW",
      label: "BMS",
      group: ["COACTVW"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a2",
      name: "CMPBATCH",
      label: "JCL_IBM",
      group: ["CMPBATCH"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a3",
      name: "CMP1BMS",
      label: "JCL_IBM",
      group: ["CMP1BMS"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a4",
      name: "IGYWCL",
      label: "JCL_IBM",
      group: ["IGYWCL"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a5",
      name: "RACFUN",
      label: "JCL_IBM",
      group: ["RACFUN"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a7",
      name: "CMPCSD",
      label: "JCL_IBM",
      group: ["CMPCSD"],
      status: "ALIVE"
    },
    {
      _id: "672b29c93e4eb3f0ec40c0a9",
      name: "CMPBATC1",
      label: "JCL_IBM",
      group: ["CMPBATC1"],
      status: "ALIVE"
    }
  ]
};
