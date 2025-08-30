import React, { useEffect, useRef, useState } from "react";
import { Button, Card, Progress, Alert, Typography as TypographyAntd, Space, Modal } from "antd";
import {
  CheckCircleOutlined,
  LoadingOutlined,
  CloseCircleOutlined,
  ClockCircleOutlined
} from "@ant-design/icons";
import { useParams } from "react-router-dom";

import { Typography } from "@components";
import { useSummarizationBmsMutation, useTriggerBmsMigration } from "@services";
import { handleErrorMessage } from "@utils";
import { Repository } from "@types";
import { v2CommonColors } from "@style";

const { success } = Modal;

const { Text, Paragraph } = TypographyAntd;

export type StepStatus = "pending" | "loading" | "success" | "error";

interface Step {
  id: string;
  title: string;
  description: string;
  status: StepStatus;
}

interface ProgressConvertBMSProps {
  status: Repository["status"];
  refetchReport: () => void;
  cancelRetryConvert: () => void;
  retryConvert: () => void;
}

const ProgressConvertBMS: React.FC<ProgressConvertBMSProps> = ({
  status,
  refetchReport,
  cancelRetryConvert,
  retryConvert
}) => {
  const [isProcessing, setIsProcessing] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);
  const { name = "", repoId = "" } = useParams();

  const { mutateAsync: summarizeAsync } = useSummarizationBmsMutation();
  const { mutateAsync: migrateAsync } = useTriggerBmsMigration();

  const statusRef = useRef(status);
  useEffect(() => {
    statusRef.current = status;
  }, [status]);

  const [steps, setSteps] = useState<Step[]>([
    {
      id: "summarize",
      title: "Summarize Data",
      description: "Summarizing repository content",
      status: "pending"
    },
    {
      id: "migrate",
      title: "Converting BMS",
      description: "Migrating to Java",
      status: "pending"
    }
  ]);

  const handleSuccessModal = () => {
    success({
      title: (
        <>
          <Typography
            style={{
              color: v2CommonColors.primary9
            }}
            level='body-16b'
          >
            Converted Successfully!
          </Typography>
          <Typography
            style={{
              color: v2CommonColors.primary10
            }}
            level='body-14r'
          >
            Code successfully converted to Java. You can now view the converted code.
          </Typography>
        </>
      ),
      closable: true,
      centered: true,
      onOk: cancelRetryConvert
    });
  };
  const updateStepStatus = (index: number, stepStatus: StepStatus) => {
    setSteps(prev => prev.map((step, i) => (i === index ? { ...step, status: stepStatus } : step)));
  };

  const waitUntilStatusMatch = async (
    expectedStatus: Repository["status"],
    retryLimit = 2,
    delayMs = 15000
  ) => {
    // eslint-disable-next-line no-console
    console.log(expectedStatus, "expectedStatus");
    // eslint-disable-next-line no-console
    console.log(statusRef.current, "statusRef.current");
    if (statusRef.current === expectedStatus) return true;
    while (true) {
      let retryCount = 0;
      let reportResult: any;

      while (retryCount <= retryLimit) {
        try {
          reportResult = await refetchReport();
          break;
        } catch (err) {
          retryCount++;
          if (retryCount > retryLimit) {
            throw new Error("refetchReport failed after maximum retries");
          }
        }
      }

      const currentStatus = reportResult?.data?.data?.entry_point?.status;
      // eslint-disable-next-line no-console
      console.log(currentStatus, "currentStatus", { reportResult });

      if (currentStatus === expectedStatus) {
        return true;
      }

      await new Promise(res => setTimeout(res, delayMs));
    }
  };

  const startSummarization = async () => {
    updateStepStatus(0, "loading");
    const summarizeRes = await summarizeAsync({ repository_id: repoId, file_name: name });
    if (!summarizeRes) throw new Error("Summarization failed");
    await waitUntilStatusMatch("summarized");
    updateStepStatus(0, "success");
  };

  const startMigration = async () => {
    if (status !== "summarized") return;
    retryConvert();
    updateStepStatus(1, "loading");
    const migrateRes = await migrateAsync({ repository_id: repoId, bms_file_name: name });
    if (!migrateRes) throw new Error("Migration failed");
    await waitUntilStatusMatch("migrated");
    handleSuccessModal();
    updateStepStatus(1, "success");
    setCurrentStep(2);
  };

  useEffect(() => {
    const run = async () => {
      if (status === "summarizing") {
        setIsProcessing(true);
        updateStepStatus(0, "loading");
        await waitUntilStatusMatch("summarized");
        updateStepStatus(0, "success");
        await startMigration();
      } else if (status === "summarized") {
        setIsProcessing(true);
        updateStepStatus(0, "success");
        await startMigration();
      } else if (status === "migrating") {
        setIsProcessing(true);
        updateStepStatus(1, "loading");
        await waitUntilStatusMatch("migrated");
        updateStepStatus(1, "success");
        setCurrentStep(2);
        setIsProcessing(false);
      }
    };

    run();
  }, [status]);

  const handleProcess = async () => {
    setIsProcessing(true);
    setCurrentStep(0);
    setSteps(prev => prev.map(s => ({ ...s, status: "pending" })));

    try {
      await startSummarization();
      setCurrentStep(1);
      await startMigration();
    } catch (error) {
      updateStepStatus(currentStep, "error");
      handleErrorMessage(error, { show: true });
    } finally {
      setIsProcessing(false);
    }
  };
  const getStatusIcon = (stepStatus: StepStatus) => {
    switch (stepStatus) {
      case "loading":
        return <LoadingOutlined style={{ color: "#1890ff" }} spin />;
      case "success":
        return <CheckCircleOutlined style={{ color: "#52c41a" }} />;
      case "error":
        return <CloseCircleOutlined style={{ color: "#ff4d4f" }} />;
      default:
        return <ClockCircleOutlined style={{ color: "#d9d9d9" }} />;
    }
  };

  const getProgressValue = () => {
    const completed = steps.filter(s => s.status === "success").length;
    return Math.round((completed / steps.length) * 100);
  };

  const getOverallStatus = (): StepStatus => {
    if (steps.every(s => s.status === "success")) return "success";
    if (steps.some(s => s.status === "error")) return "error";
    if (steps.some(s => s.status === "loading")) return "loading";
    return "pending";
  };

  const overallStatus = getOverallStatus();

  return (
    <div style={{ maxWidth: 600, margin: "0 auto", padding: 24 }}>
      <Card
        type='inner'
        title={
          <>
            <Typography level='body-16b'>Convert BMS to Java</Typography>
            <Paragraph style={{ marginBottom: 0 }}>
              Convert repository in two simple steps.
            </Paragraph>
          </>
        }
      >
        <div style={{ marginBottom: 16 }}>
          <div style={{ display: "flex", justifyContent: "space-between" }}>
            <Text type='secondary'>Progress</Text>
            <Text>{getProgressValue()}%</Text>
          </div>
          <Progress rootClassName='progress-bms' percent={getProgressValue()} showInfo={false} />
        </div>

        <Space direction='vertical' size='middle' style={{ width: "100%" }}>
          {steps.map(step => (
            <Alert
              key={step.id}
              message={
                <Space>
                  {getStatusIcon(step.status)}
                  <span>{step.title}</span>
                </Space>
              }
              description={
                <Text type={step.status === "error" ? "danger" : "secondary"}>
                  {step.description}
                  {step.status === "loading" ? "..." : ""}
                </Text>
              }
              type={
                step.status === "success"
                  ? "success"
                  : step.status === "error"
                  ? "error"
                  : step.status === "loading"
                  ? "info"
                  : "warning"
              }
            />
          ))}
        </Space>

        <div style={{ marginTop: 24 }}>
          <Button
            type='primary'
            block
            size='large'
            onClick={handleProcess}
            disabled={isProcessing}
            loading={isProcessing}
          >
            {isProcessing
              ? `Processing Step ${currentStep + 1} of 2...`
              : overallStatus === "success"
              ? "Process Complete!"
              : overallStatus === "error"
              ? "Retry Process"
              : "Start Process"}
          </Button>

          {overallStatus === "success" && (
            <Alert
              message='✅ All steps completed successfully!'
              type='success'
              style={{ marginTop: 16 }}
            />
          )}
          {overallStatus === "error" && (
            <Alert
              message='❌ Process failed. Please try again.'
              type='error'
              style={{ marginTop: 16 }}
            />
          )}
        </div>
      </Card>
    </div>
  );
};

export default ProgressConvertBMS;
