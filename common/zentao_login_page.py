from poium import Page, PageElement, PageElements


class Login(Page):
    """
    舞泡登录元素封装
    """
    # 前往登录页面
    close_consult_pop = PageElement(xpath='/html/body/div[6]/div/p[2]/img', describe='关闭咨询弹窗')
    go_login = PageElement(xpath='/html/body/div[5]/footer/div/a[4]/p', describe='前往登录页')

    def m5pao_go_login(self):
        self.go_login.click()

    # 登录页元素封装
    login_username_loc = PageElement(id_='username', describe='用户名')
    login_password_loc = PageElement(id_='password', describe='密码')
    login_code_loc = PageElement(id_='vcode', describe='图片验证码')
    login_btn_loc = PageElement(xpath='//*[@id="fm1"]/div/div/input[4]', describe='登录按钮')
    login_go_register_loc = PageElement(xpath='//*[@id="fm1"]/div/div/div[5]/a[1]', describe='前往注册')
    login_go_forget_password_loc = PageElement(xpath='//*[@id="fm1"]/div/div/div[5]/a[2]', describe='忘记密码')

    # assert
    login_msg_hint = PageElement(id_='msg', describe='错误提示')
