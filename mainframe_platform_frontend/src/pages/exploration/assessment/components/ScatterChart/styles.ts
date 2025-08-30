import styled from "@emotion/styled";

export const Wrapper = styled.div`
  position: relative;
  background-color: ${({ theme }) => theme.colors.neutral};
  background-image: linear-gradient(
      ${({ theme }) => theme.colors.primary100}33 0.5px,
      transparent 0.1em
    ),
    linear-gradient(90deg, ${({ theme }) => theme.colors.primary100}33 0.5px, transparent 0.1em);
  background-size: 3em 3em;

  g text {
    fill: ${({ theme }) => theme.colors.white};
  }

  #tooltip {
    position: fixed;
    left: 0;
    right: 0;
    width: 0;
    height: 0;

    .wrapper {
      background-color: ${({ theme }) => theme.colors.black};
      padding: 5px 10px;
      border-radius: 8px;
      border: 1px solid #f6d053;

      .title {
      }
      .path {
      }
    }
  }
`;
