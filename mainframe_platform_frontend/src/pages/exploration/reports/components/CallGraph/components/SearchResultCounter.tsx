import { theme } from "antd";
import { memo, useMemo } from "react";

interface SearchResultCounterProps {
  count: number;
}

const SearchResultCounter = memo(({ count }: SearchResultCounterProps) => {
  const { token } = theme.useToken();

  const backgroundColor = useMemo(
    () => (count > 0 ? token.colorInfo : token.colorError),
    [count, token.colorInfo, token.colorError]
  );

  const matchText = useMemo(() => `${count} match${count !== 1 ? "es" : ""}`, [count]);

  return (
    <div
      style={{
        position: "absolute",
        bottom: -20,
        right: 0,
        backgroundColor,
        color: "#fff",
        fontSize: 12,
        padding: "0 8px",
        borderRadius: 10,
        lineHeight: "20px",
        zIndex: 2,
        boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
        transition: "background-color 0.3s ease"
      }}
    >
      {matchText}
    </div>
  );
});

export default SearchResultCounter;
