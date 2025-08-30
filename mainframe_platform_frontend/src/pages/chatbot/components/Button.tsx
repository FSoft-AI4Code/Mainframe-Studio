import { useCallback } from "react";

import { repositoryApi } from "@api";
import { ArrowRightSvg, CirclePlusSvg } from "@assets/svg";
import { Button } from "@components";
import { useController, useRepository } from "@hooks";
import { useMessages } from "@pages/workspace/WorkspacePage";
import { useTriggerAssessment } from "@services";

export const AssessBtn = () => {
  const { setMessages } = useMessages();
  const { repository } = useRepository();
  const { mutate: triggerAssessment, isPending } = useTriggerAssessment();

  const handleTriggerAssessment = () => {
    if (!repository?.id) return;
    setMessages(prev => [
      {
        content: "Starting assessment of the repository...",
        role: "assistant"
      },
      ...prev
    ]);
    triggerAssessment(repository?.id, {
      onSuccess() {
        setMessages(prev => [
          {
            content:
              "Assessment has been initiated. The system will analyze your code and provide detailed insights. Would you like to start reverse engineering to get an overview of the whole source code?",
            role: "assistant"
          },
          ...prev
        ]);
      },
      onError() {
        setMessages(prev => [
          {
            content: "Failed to start assessment. Please try again.",
            role: "assistant"
          },
          ...prev
        ]);
      }
    });
  };

  // const triggerAssess = useCallback(() => {
  //   controller(
  //     async () => {
  //       if (!repositoryProject) return;
  //       setMessages(prev => [
  //         {
  //           content: "Starting assessment of the repository...",
  //           role: "assistant"
  //         },
  //         ...prev
  //       ]);
  //       await repositoryApi.triggerAssessment(repositoryProject.id);

  //       setMessages(prev => [
  //         {
  //           content:
  //             "Assessment has been initiated. The system will analyze your code and provide detailed insights. Would you like to start reverse engineering to get an overview of the whole source code?",
  //           role: "assistant"
  //         },
  //         ...prev
  //       ]);
  //     },
  //     {
  //       onError: () => {
  //         setMessages(prev => [
  //           {
  //             content: "Failed to start assessment. Please try again.",
  //             role: "assistant"
  //           },
  //           ...prev
  //         ]);
  //       }
  //     }
  //   );
  // }, [repositoryProject]);

  return (
    <Button
      iconPrefix={<ArrowRightSvg width={14} height={14} />}
      type='primary'
      style={{ borderRadius: 4, width: "min-content" }}
      loading={isPending}
      onClick={handleTriggerAssessment}
    >
      Perform Assessment
    </Button>
  );
};

export const ReverseBtn = () => {
  const { controller } = useController();
  const { setMessages } = useMessages();
  const { repository } = useRepository();
  const triggerReverse = useCallback(() => {
    controller(
      async () => {
        if (!repository) return;
        setMessages(prev => [
          {
            content: "Starting reverse engineering process...",
            role: "assistant"
          },
          ...prev
        ]);
        await repositoryApi.parseRepositoryData(repository.id);

        setMessages(prev => [
          {
            content:
              "Reverse engineering process has been initiated. The system will analyze your code structure and generate detailed documentation.",
            role: "assistant"
          },
          ...prev
        ]);
      },
      {
        onError: () => {
          setMessages(prev => [
            {
              content: "Failed to start reverse engineering. Please try again.",
              role: "assistant"
            },
            ...prev
          ]);
        }
      }
    );
  }, []);

  return (
    <Button
      iconPrefix={<CirclePlusSvg width={14} height={14} />}
      type='primary'
      style={{ borderRadius: 4, width: "min-content" }}
      onClick={triggerReverse}
    >
      Reverse Engineering
    </Button>
  );
};
