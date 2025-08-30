import ContentLoader, { IContentLoaderProps } from "react-content-loader";
import { JSX } from "react/jsx-runtime";

const PageSkeleton = (props: JSX.IntrinsicAttributes & IContentLoaderProps) => (
  <ContentLoader
    width={"100%"}
    viewBox='0 0 450 450'
    backgroundColor='#f5f5f5'
    foregroundColor='#dbdbdb'
    {...props}
  >
    <rect x='0' y='60' rx='3' ry='3' width='140' height='50' />
    <rect x='0' y='120' rx='3' ry='3' width='140' height='50' />
    <rect x='0' y='180' rx='3' ry='3' width='140' height='50' />
    <rect x='0' y='15' rx='3' ry='3' width='50' height='15' />
    <rect x='60' y='15' rx='3' ry='3' width='50' height='15' />
    <rect x='115' y='15' rx='3' ry='3' width='50' height='15' />
    <rect x='170' y='15' rx='3' ry='3' width='50' height='15' />
    <rect x='225' y='15' rx='3' ry='3' width='50' height='15' />
    <rect x='285' y='15' rx='3' ry='3' width='50' height='15' />
    <rect x='340' y='15' rx='3' ry='3' width='50' height='15' />

    <rect x='0' y='35' rx='3' ry='3' width='100%' height='1' />

    <rect x='0' y='45' rx='3' ry='3' width='35' height='8' />
    <rect x='380' y='45' rx='3' ry='3' width='70' height='8' />
    <rect x='150' y='60' rx='3' ry='3' width='140' height='50' />
    <rect x='160' y='60' rx='3' ry='3' width='140' height='50' />
    <rect x='310' y='60' rx='3' ry='3' width='140' height='50' />
    <rect x='150' y='120' rx='3' ry='3' width='140' height='50' />
    <rect x='160' y='120' rx='3' ry='3' width='140' height='50' />
    <rect x='310' y='120' rx='3' ry='3' width='140' height='50' />
    <rect x='160' y='180' rx='3' ry='3' width='140' height='50' />
    <rect x='310' y='180' rx='3' ry='3' width='140' height='50' />
    <rect x='150' y='180' rx='3' ry='3' width='140' height='50' />
    <rect x='310' y='180' rx='3' ry='3' width='140' height='50' />
    <rect x='235' y='245' rx='3' ry='3' width='50%' height='100' />
    <rect x='0' y='245' rx='3' ry='3' width='50%' height='100' />
    {/* <rect x='235' y='320' rx='3' ry='3' width='50%' height='50' />
    <rect x='0' y='320' rx='3' ry='3' width='50%' height='50' /> */}
    <rect x='235' y='360' rx='3' ry='3' width='50%' height='75' />
    <rect x='0' y='360' rx='3' ry='3' width='50%' height='75' />

    {/* <rect x='5' y='150' rx='3' ry='3' width='130' height='15' />
                <rect x='5' y='170' rx='3' ry='3' width='70' height='10' />
                <rect x='10' y='190' rx='3' ry='3' width='115' height='15' />
                <rect x='10' y='210' rx='3' ry='3' width='35' height='8' />
                <rect x='50' y='210' rx='3' ry='3' width='35' height='8' />
                <rect x='90' y='210' rx='3' ry='3' width='35' height='8' /> */}
  </ContentLoader>
);

PageSkeleton.metadata = {
  name: "PageSkeleton",
  github: "PageSkeleton",
  filename: "PageSkeleton"
};

export default PageSkeleton;
