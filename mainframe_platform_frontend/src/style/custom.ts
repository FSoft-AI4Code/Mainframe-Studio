import { css } from "@emotion/react";

import { allColors, colors, v2Colors, v2CommonColors } from "./colors";

export const customStyle = css`
  /* stylelint-disable */
  .ant-input {
    background: ${allColors.neutral1};
    color: ${allColors.neutral7};
    border-radius: 8px;

    border: 1px solid rgba(191, 191, 191, 1);
  }

  // .ant-dropdown-menu,
  // .ant-select-dropdown,
  // .ant-table-filter-dropdown,
  // .ant-picker-panel-container {
  //   background-color: ${colors.grey} !important;
  //   border: solid 1px ${allColors.primary1};
  // }

  .ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-normal {
    display: inline-flex;
  }
  .ant-spin-nested-loading {
    width: 100%;
    overflow: auto;
    .ant-spin.ant-spin-spinning {
      max-height: 100%;
    }
  }
  .full_height.ant-spin-nested-loading {
    height: 100%;
    .ant-spin-container {
      height: 100%;
    }
  }

  // .ant-table-filter-dropdown {
  //   .ant-table-filter-dropdown-btns {
  //     border: none !important;
  //   }
  //   .ant-dropdown-menu-item-selected {
  //     background-color: ${allColors.primary1}50 !important;
  //   }
  // }

  // .ant-cascader-menus {
  //   .ant-cascader-menu {
  //     border-inline-end: none !important;
  //   }
  // }

  // .ant-picker-time-panel-cell-selected .ant-picker-time-panel-cell-inner,
  // .ant-cascader-menu-item-active,
  // .ant-select-item-option-selected {
  //   background-color: ${allColors.primary1}50 !important;
  // }

  // /* > Hover item menu */
  // .ant-select-dropdown .ant-select-item-option-active:not(.ant-select-item-option-disabled) {
  //   background-color: ${allColors.primary1}33 !important;
  // }

  // .ant-picker-panel {
  //   .ant-picker-header {
  //     border-bottom: none !important;
  //   }
  //   .ant-picker-footer {
  //     border-top: none !important;
  //   }
  //   .ant-picker-time-panel-column {
  //     border-inline-start: none !important;
  //   }
  // }

  .ant-tree-treenode-selected::before {
    width: calc(100% + 32px);
  }
  .ant-tree-node-content-wrapper.ant-tree-node-content-wrapper-normal.ant-tree-node-selected {
    background: #1890ff !important;
  }

  .ant-table-body {
    // border-right: 1px solid ${v2CommonColors.neutral5};
    &::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }

    /* Track */
    &::-webkit-scrollbar-track {
      background: transparent;
    }

    /* Handle */
    &::-webkit-scrollbar-thumb {
      background: ${allColors.primary3};
      border-radius: 4px;
    }

    /* Handle on hover */
    &::-webkit-scrollbar-thumb:hover {
      background: ${allColors.primary3};
    }
  }

  .ant-slider {
    .ant-slider-track {
      background-color: ${allColors.primary1} !important;
    }
  }

  .ant-modal-content {
    // background-color: ${colors.grey} !important;
    border: solid 1px ${allColors.primary1} !important;

    // .ant-modal-title {
    //   background-color: ${colors.grey} !important;
    // }
  }

  .ant-card.ant-card-bordered {
    border: solid 1px ${allColors.neutral4} !important;
  }

  .ant-layout {
    background: ${allColors.neutral1};
  }

  // :where(.css-dev-only-do-not-override-bc5zci).ant-layout-header {
  //   background: inherit !important;
  // }

  .ant-layout-sider,
  .ant-layout-sider-trigger {
    background: ${v2Colors.neutral1} !important;
  }

  .ant-tabs {
    .ant-tabs-tab {
      padding: 0 0 18px;
    }
    .ant-tabs-nav::before {
      display: none;
    }
  }

  .ant-form-item {
    margin: 0 !important;
  }

  .main-sidebar.ant-menu {
    &.ant-menu-light.ant-menu-root.ant-menu-vertical {
      border-inline-end: 5px solid white;
    }
    padding: 0 16px;
    .ant-menu-item {
      padding-top: 4px;
      padding-bottom: 4px;
    }
    .ant-menu-item.ant-menu-item-selected {
      &:hover {
        background-color: ${v2CommonColors.primary6};
      }
    }
    .ant-menu-item.ant-menu-item-selected,
    .ant-menu-item.ant-menu-item-active.ant-menu-item-selected,
    .ant-menu-item.ant-menu-item-selected.ant-menu-item-only-child {
      background-color: ${v2CommonColors.primary6};
      .ant-menu-title-content {
        color: ${v2CommonColors.neutral1};
      }
      .ant-menu-item-icon {
        stroke: ${v2CommonColors.neutral1};
      }
    }
    .ant-menu-item.ant-menu-item-selected.ant-menu-item-only-child {
      background-color: ${v2CommonColors.neutral4};
      .ant-menu-title-content {
        color: ${v2CommonColors.primary10};
      }
    }

    .ant-menu-submenu.ant-menu-submenu-vertical.ant-menu-submenu-selected {
      .ant-menu-item-icon {
        stroke: ${v2CommonColors.neutral1}!important;
      }
    }
    .ant-menu-submenu.ant-menu-submenu-vertical.ant-menu-submenu-selected div {
      background-color: ${v2CommonColors.primary6};
      .ant-menu-item-icon {
        stroke: ${v2CommonColors.neutral1}!important;
      }
    }
    .ant-menu-submenu.ant-menu-submenu-inline.ant-menu-submenu-selected div {
      background-color: ${v2CommonColors.primary6};
      .ant-menu-title-content,
      .ant-menu-submenu-arrow {
        color: ${v2CommonColors.neutral1};
      }
      .ant-menu-item-icon {
        stroke: ${v2CommonColors.neutral1};
      }
    }
    .ant-menu-item.ant-menu-item-only-child {
      padding-left: 42px !important;
    }
    .ant-menu-item,
    .ant-menu-submenu-title {
      padding-left: 14px !important;
      border-radius: 8px;
      .ant-menu-item-icon {
        position: relative;
      }
      &:hover {
        background-color: ${v2CommonColors.neutral4};
      }
      .ant-menu-item-active.ant-menu-item-selected {
        background-color: ${v2CommonColors.neutral6};
      }
    }
  }

  .ant-breadcrumb-link > a {
    color: ${allColors.primary1};
  }

  .ant-segmented {
    width: fit-content;
    // color: ${colors.white};
    // background: ${allColors.primary1}33;

    // .ant-segmented-group {
    //   gap: 24px;

    //   .ant-segmented-item {
    //     padding: 4px 12px;
    //   }
    //   .ant-segmented-item-label {
    //     font-size: 16px;
    //     line-height: 24px;
    //     font-weight: 600;
    //     min-height: 0px;
    //     padding: 0;
    //   }
    // }

    // .ant-segmented-thumb-motion-appear {
    //   background: ${allColors.primary1};
    // }

    // &,
    // .ant-segmented-thumb-motion-appear,
    // .ant-segmented-item {
    //   border-radius: 999px;
    // }

    // .ant-segmented-item-selected {
    //   background: ${allColors.primary1};
    //   .ant-segmented-item-label {
    //     color: ${colors.grey900};
    //   }
    // }
  }

  .ant-progress {
    // .ant-progress-outer {
    //   background-color: ${allColors.primary1}19;
    // }
    // &.ant-progress-default .ant-progress-bg {
    //   background-color: ${allColors.primary1} !important;
    // }
  }

  .ant-tooltip {
    max-width: max-content;
    .ant-tooltip-inner {
      // box-shadow: none;
      font-size: 14px;
    }
  }
  .ant-tooltip.entrypoint {
    .ant-tooltip-arrow {
      &:before,
      &:after {
        background: ${allColors.neutral1};
        border: 1px solid ${allColors.neutral6};
      }
    }
    .ant-tooltip-inner {
      padding: 0px;
      border-radius: 16px;
    }
  }
  .ant-tooltip.table {
    max-width: 250px;
    .ant-tooltip-inner {
      box-shadow: none;
      font-size: 14px;
      border-radius: 8px;
      padding: 6px 8px;
    }
  }
  .ant-tooltip.default {
    .ant-tooltip-inner {
      font-size: 14px;
      border-radius: 8px;
      background-color: ${allColors.neutral1};
      padding: 6px 8px;
    }
    .ant-tooltip-arrow {
      &:before,
      &:after {
        background: ${allColors.neutral1};
      }
    }
  }
  .ant-table {
    .ant-table-header {
      border-radius: 0 !important;
    }
    .ant-table-thead {
      .ant-table-cell {
        background: ${allColors.neutral2};
        border-radius: 0 !important;
        color: ${allColors.neutral10};

        font-family: SF Pro Text;
        font-size: 16px;
        font-weight: 510;
        line-height: 22px;
        text-align: left;

        svg {
          fill: ${colors.grey900};
        }

        &::before {
          display: none;
        }
      }
    }
    .ant-table-tbody .ant-table-cell {
      background: ${allColors.neutral1};
    }
    .ant-table-cell {
      border: solid 1px ${allColors.neutral5};

      font-family: SF Pro Text;
      font-size: 16px;
      font-weight: 400;
      line-height: 22px;
      text-align: left;
      color: ${allColors.primary10};
    }
    .ant-table-cell.ant-table-cell-row-hover {
      background: ${allColors.primary1} !important;
    }
    .ant-table-row .ant-table-cell:first-of-type {
      border-left: solid 1px ${allColors.neutral5} !important;
    }
  }

  // .ant-pagination .ant-pagination-item {
  //   background: ${allColors.neutral4};
  //   border: none;

  //   display: flex;
  //   justify-content: center;
  //   align-items: center;

  //   font-family: SF Pro Text;
  //   font-size: 14px;
  //   font-weight: 400;
  //   line-height: 20px;
  //   letter-spacing: 0.02em;
  //   text-align: left;
  //   color: ${allColors.primary10};
  // }

  // .ant-pagination .ant-pagination-item.ant-pagination-item-active {
  //   background-color: ${allColors.primary6};
  //   a {
  //     color: ${allColors.neutral1};
  //   }
  // }

  .ant-notification {
    .cobol-notification {
      /* border-radius: 16px; */
      border-radius: 999px;
      background-color: ${allColors.primary1};
      padding: 10px 12px;
      width: unset;

      &,
      .ant-notification-notice-description,
      .ant-notification-notice-message {
        color: ${colors.grey900};
      }

      .ant-notification-notice-description,
      .ant-notification-notice-message {
        margin: 0 !important;
        padding: 0 !important;
        max-width: 500px;
      }

      .ant-notification-notice-close {
        display: none;
      }
    }
  }

  // .chartTooltip {
  //   .ant-tooltip-inner {
  //     background-color: black;
  //     border: 1px solid ${allColors.primary1};
  //   }
  // }
  /* stylelint-enable */

  &::-webkit-scrollbar {
    width: 6px;
    height: 6px;
  }

  /* Track */
  &::-webkit-scrollbar-track {
    background: transparent;
  }

  /* Handle */
  &::-webkit-scrollbar-thumb {
    background: ${v2CommonColors.primary3};
    border-radius: 4px;
  }

  /* Handle on hover */
  &::-webkit-scrollbar-thumb:hover {
    background: ${v2CommonColors.primary3};
  }

  .ant-card-head-wrapper {
    flex-wrap: wrap;
  }
`;

// ant-dropdown-menu
