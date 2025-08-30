import styled from "@emotion/styled";
import { Image, Switch } from "antd";
import { useTranslation } from "react-i18next";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

import { LogOutSvg, SettingsSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { ROUTERS, storage } from "@defines";
import { userActions, userSelector } from "@store";

const Wrapper = styled(Flex)`
  padding: 12px 24px;
  border-radius: 16px;
  background-color: ${({ theme }) => theme.colors.primary200};
  width: 100%;
  height: 70px;
`;

export const UserBadge = () => {
  const userData = useSelector(userSelector.selectData);
  const navigate = useNavigate();
  const { i18n } = useTranslation();

  const handleLogout = () => {
    localStorage.removeItem(storage.TOKEN);
    userActions.clean();
    navigate(ROUTERS.LOGIN);
  };

  if (!userData) return null;

  return (
    <Wrapper align='center' justify='space-between'>
      <Flex gap={12} justify='space-between' align='center'>
        <Image
          alt='user avatar'
          height={36}
          width={36}
          src={userData.avatar ?? "/static/images/dummy.jpeg"}
          style={{ borderRadius: "50%" }}
          preview={false}
        />
        <Flex gap={2} direction='column'>
          <Typography level='h6-body1m'>{userData.username}</Typography>
          <Typography level='h7-body2M'>{userData.email}</Typography>
        </Flex>
      </Flex>
      <Flex gap={12} justify='space-between' align='center'>
        <SettingsSvg onClick={() => {}} style={{ cursor: "pointer" }} />
        <LogOutSvg onClick={handleLogout} style={{ cursor: "pointer" }} />
        <Switch
          checkedChildren='ja'
          unCheckedChildren='en'
          defaultChecked={i18n.language === "ja"}
          onClick={check => i18n.changeLanguage(check ? "ja" : "en")}
        />
      </Flex>
    </Wrapper>
  );
};
