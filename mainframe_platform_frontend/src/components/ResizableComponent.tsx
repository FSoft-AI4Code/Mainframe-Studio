import { Resizable } from "re-resizable";

type Props = {
  children: React.ReactElement;
  initialWidth: number;
  initialHeight: number;
  minWidth?: number;
  maxWidth?: number;
};

export const ResizableComponent: React.FC<Props> = ({
  children,
  initialWidth,
  initialHeight,
  minWidth,
  maxWidth
}) => {
  return (
    <Resizable
      defaultSize={{
        width: initialWidth,
        height: initialHeight
      }}
      minWidth={minWidth}
      maxWidth={maxWidth}
    >
      <div>{children}</div>
    </Resizable>
  );
};
