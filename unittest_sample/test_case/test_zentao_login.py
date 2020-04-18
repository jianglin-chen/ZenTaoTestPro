import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestZenTao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.base_url = "http://127.0.0.1/pro/user-login-L3Byby8=.html"

    def login_selenium(self, name='admin', password='alin19941226061X.'):
        """
        禅道登录
        """
        self.driver.get(self.base_url)
        self.driver.find_element(By.XPATH, "//input[@id='account']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        # 记住密码
        # self.driver.find_element(By.XPATH, "//input[@id='keepLoginon']").click()
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()

    def go_to_bug_selenium(self):
        """
        前往alin学习系统BUG界面
        """
        self.driver.find_element(By.XPATH, "//a[contains(text(),'测试')]").click()
        self.driver.find_element(By.XPATH, "(//a[contains(text(),'Bug')])[2]").click()
        self.driver.find_element(By.XPATH, "//button[@id='currentItem']").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Alin学习系统')]").click()



    def zentao_quit_selenium(self):
        """
        禅道退出
        """
        test = self.driver.find_element(By.XPATH, "//ul[@id='userNav']/li/a/span[2]")
        self.driver.execute_script("arguments[0].click();", test)
        test2 = self.driver.find_element(By.XPATH, "//a[contains(text(),'退出')]")
        self.driver.execute_script("arguments[0].click();", test2)


    def test_a_1_submit_bug_selenium(self):
        """
        提交BUG
        """
        self.login_selenium()
        self.go_to_bug_selenium()
        self.driver.find_element(By.XPATH, "//div[@id='mainMenu']/div[3]/a[4]/i").click()
        # 选择所属模块
        self.driver.find_element(By.XPATH, "//div[@id='module_chosen']/a/span").click()
        self.driver.find_element(By.XPATH, "//div[@id='module_chosen']/div/ul/li[2]").click()
        # 选择影响版本
        sleep(2)
        self.driver.find_element(By.XPATH, "//div[@id='openedBuild_chosen']/ul").click()
        self.driver.find_element(By.XPATH, "//div[@id='openedBuild_chosen']/div/ul/li").click()
        # 输入标题
        sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='title']").send_keys("登录错误")
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()

    def test_b_2_test_designate_selenium(self):
        """
        BUG指派
        """
        self.login_selenium(name='testB', password='baison8888.')
        self.go_to_bug_selenium()

        # # 确认操作
        choice_element = self.driver.find_element(By.XPATH, "//input[@id='bugIDList4']")
        self.driver.execute_script("arguments[0].click();", choice_element)
        sleep(2)
        verify_element = self.driver.find_element(By.XPATH, "(//button[@type='button'])[11]")
        self.driver.execute_script("arguments[0].click();", verify_element)
        verify_element2 = self.driver.find_element(By.XPATH, "(//a[contains(text(),'确认')])[2]")
        self.driver.execute_script("arguments[0].click();", verify_element2)

        # 指派操作
        sleep(2)
        self.driver.find_element(By.XPATH, "//table[@id='bugList']/tbody/tr/td[9]/a/span").click()
        designate_frame = self.driver.find_element(By.XPATH, "//*[@id='iframe-triggerModal']")
        self.driver.switch_to.frame(designate_frame)
        self.driver.find_element(By.XPATH, "//div[@id='assignedTo_chosen']").click()
        self.driver.find_element(By.XPATH, "//div[@id='assignedTo_chosen']/div/ul/li[3]").click()
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        self.driver.switch_to.default_content()
        # 退出登录
        self.zentao_quit_selenium()

    def test_c_3_figure_selenium(self):
        """
        C解决问题
        """
        self.login_selenium(name='testC', password='baison8888.')
        self.go_to_bug_selenium()
        # 选择问题
        choice_element = self.driver.find_element(By.XPATH, "//input[@id='bugIDList4']")
        self.driver.execute_script("arguments[0].click();", choice_element)
        sleep(2)
        verify_element = self.driver.find_element(By.XPATH, "(//button[@type='button'])[11]")
        self.driver.execute_script("arguments[0].click();", verify_element)
        # 选择解决问题
        sleep(2)
        above = self.driver.find_element(By.ID, "resolveItem")
        ActionChains(self.driver).move_to_element(above).perform()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'不予解决')]").click()
        # 退出登录
        self.zentao_quit_selenium()

    def test_a_4_close_selenium(self):
        """
        A关闭问题
        """
        self.login_selenium()
        self.go_to_bug_selenium()
        # 选择问题
        choice_element = self.driver.find_element(By.XPATH, "//input[@id='bugIDList4']")
        self.driver.execute_script("arguments[0].click();", choice_element)
        sleep(10)
        verify_element = self.driver.find_element(By.XPATH, "(//button[@type='button'])[10]")
        self.driver.execute_script("arguments[0].click();", verify_element)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'关闭')]")
        self.zentao_quit_selenium()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestZenTao("test_a_1_submit_bug_selenium"))
    suite.addTest(TestZenTao("test_b_2_test_designate_selenium"))
    suite.addTest(TestZenTao("test_c_3_figure_selenium"))
    suite.addTest(TestZenTao("test_a_4_close_selenium"))
    unittest.TextTestRunner().run(suite)


