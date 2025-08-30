import { Empty, Spin } from "antd";
import { useParams } from "react-router-dom";
import { useEffect } from "react";

import { Flex } from "@components";
import { useInferenceModernizationQuery } from "@services";
import { allColors } from "@style";
import { handleErrorMessage } from "@utils";

const TransformedWebInterface = () => {
  const { repoId = "", type: fileType = "", name = "" } = useParams();
  const { url, loading, error } = useInferenceModernizationQuery({
    repository_id: repoId,
    type: fileType,
    name: name
  });

  useEffect(() => {
    if (error) handleErrorMessage(error, { show: true });
  }, [error]);

  return (
    <Flex direction='column' style={{ width: "100%", height: "100%" }}>
      {loading && (
        <Flex justify='center' align='center' style={{ width: "100%", padding: "80px 0" }}>
          <Spin size='large' tip='Generating web interface...' />
        </Flex>
      )}

      {url && (
        <div
          style={{
            width: "100%",
            height: "calc(100vh - 320px)",
            border: `1px solid ${allColors.neutral4}`,
            borderRadius: "4px",
            overflow: "hidden"
          }}
        >
          <iframe
            src={url}
            style={{ width: "100%", height: "100%", border: "none" }}
            title='Modernized Web Interface'
            // onLoad={handleIframeLoad}
          />
        </div>
      )}

      {!url && !loading && (
        <Flex justify='center' align='center' style={{ width: "100%", padding: "80px 0" }}>
          <Empty description='No web interface available.' />
        </Flex>
      )}
    </Flex>
  );
};

export default TransformedWebInterface;
