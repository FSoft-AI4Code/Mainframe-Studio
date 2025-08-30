import styled from "@emotion/styled";
import { Button } from "antd";
import { PropsWithChildren } from "react";
import { useDispatch } from "react-redux";

import { appActions } from "@store";
import { MenuSvg } from "@assets/svg";

export const WrapChartTools = styled.div`
  position: fixed;
  right: 30px;
  bottom: 20px;

  & > *:not(:last-child) {
    margin-right: 5px;
  }

  & > * {
    opacity: 0.7;
  }
`;
export const WrapChartToolsInside = styled.div<{ isFullScreen?: boolean }>`
  position: absolute;
  right: ${({ isFullScreen }) => (isFullScreen ? "20px" : "155px")};
  bottom: 60px;

  & > *:not(:last-child) {
    margin-right: 5px;
  }

  & > * {
    opacity: 0.7;
  }
`;

export const WrapChartLegend = styled.div`
  position: absolute;
  right: 0px;
  top: 0px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1001;
`;

export const ContainerChartSearch = styled.div`
  position: absolute;
  left: 50px;
  top: 40px;
  display: flex;
  align-items: center;
  transition: 1s cubic-bezier(0.075, 0.82, 0.165, 1);

  & > *:not(:last-child) {
    margin-right: 10px;
  }

  .ant-btn {
    border-color: ${({ theme }) => theme.colors.primary100};
    background-color: transparent;

    svg {
      fill: ${({ theme }) => theme.colors.primary100};
    }
  }

  .ant-select {
    display: flex;
    align-items: center;
    height: 38px !important;
    width: 300px !important;

    .ant-select-selector {
      border-radius: 999px;
      border-color: ${({ theme }) => theme.colors.primary100};
      background-color: transparent;
    }

    input,
    .ant-select-selection-item {
      color: ${({ theme }) => theme.colors.primary100} !important;
    }
    .ant-select-selection-placeholder {
      color: ${({ theme }) => theme.colors.primary100}aa !important;
    }

    .ant-select-selector {
      padding-left: 38px;
    }
    .ant-select-selection-search {
      padding-left: 28px;
    }

    .ant-select-arrow,
    .ant-select-clear {
      top: 65%;
      transform: translateY(-50%);
    }

    .ant-select-arrow {
      left: 12px;

      svg {
        width: 20px;
        height: 20px;
      }
    }

    svg path {
      fill: ${({ theme }) => theme.colors.primary100};
    }
  }
`;

const WrapButton = styled.div`
  transition: 1s cubic-bezier(0.075, 0.82, 0.165, 1);
`;

const MenuIcon = styled(MenuSvg)`
  height: 15px !important;
  width: 15px !important;
`;

export const WrapChartSearch: React.FC<PropsWithChildren> = ({ children, ...props }) => {
  const dispatch = useDispatch();

  const onClickButton = () => dispatch(appActions.setTopBarShow(true));

  return (
    <ContainerChartSearch {...props} className='container-chart-search'>
      <WrapButton className='wrap-button'>
        <Button icon={<MenuIcon />} onClick={onClickButton} />
      </WrapButton>
      {children}
    </ContainerChartSearch>
  );
};
