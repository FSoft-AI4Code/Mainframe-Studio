import styled from "@emotion/styled";

import { Flex } from "@components";
import { allColors } from "@style";

export const EntriesWrapper = styled.div<{ showMore: boolean; scrollHeight: number }>`
  display: grid;
  // grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
  // grid-template-rows: repeat(auto-fill, 30px);
  grid-template-columns: repeat(auto-fit, minmax(90px, min-content));
  gap: 12px 8px;
  height: ${({ showMore }) => (showMore ? "auto" : 80)}px;
  overflow: hidden;
  transition: all 0.2s 0.2s;
  padding: 0 24px 16px;
`;

export const FileWrapper = styled(Flex)<{ type: "bms" | "jcl" }>`
  padding: 3px 15px;
  height: 30px;
  background: ${({ type }) => (type === "bms" ? allColors.brand1 : allColors.brand5)};
  border-radius: 100px;
  cursor: pointer;

  &:hover {
    background: ${({ type }) => (type === "bms" ? allColors.hBrand1 : allColors.hBrand5)};
  }
`;
