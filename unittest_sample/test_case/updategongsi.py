import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

    def go_organization_company(self):
        """
        前往组织公司
        """
        self.driver.find_element(By.XPATH, "//a[contains(text(),'组织')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'公司')]").click()

    def go_organization_department(self):
        """
        前往组织部门
        """
        self.driver.find_element(By.XPATH, "//a[contains(text(),'组织')]").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'部门')]").click()

    def go_organization_user(self):
        """
        前往组织用户
        """
        self.driver.find_element(By.XPATH, "//a[contains(text(),'组织')]").click()
        self.driver.find_element(By.XPATH, "(//a[contains(text(),'用户')])[2]").click()

    def test_update_company(self):
        """
        修改公司
        """
        self.login_selenium()
        self.go_organization_company()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'编辑')]").click()
        company_frame = self.driver.find_element(By.XPATH, "//*[@id='iframe-triggerModal']")
        self.driver.switch_to.frame(company_frame)
        self.driver.find_element(By.XPATH, "//input[@id='name']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='name']").send_keys('alin')
        self.driver.find_element(By.XPATH, "//input[@id='name']").send_keys(Keys.ENTER)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "")

    def test_add_department(self):
        """
        添加部门
        """
        self.login_selenium()
        self.go_organization_department()
        self.driver.find_element(By.XPATH, "//input[@id='depts[]']").send_keys("部门1")
        self.driver.find_element(By.XPATH, "(//input[@id='depts[]'])[2]").send_keys("部门2")
        self.driver.find_element(By.XPATH, "(//input[@id='depts[]'])[3]").send_keys("部门3")
        self.driver.find_element(By.XPATH, "(//input[@id='depts[]'])[4]").send_keys("部门4")
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()

    def test_add_department_user(self):
        self.login_selenium()
        self.go_organization_user()
        self.driver.find_element(By.XPATH, "//input[@id='userstestB']").click()
        self.driver.find_element(By.XPATH, "//input[@id='userstestC']").click()
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        self.driver.find_element(By.XPATH, "//div[@id='dept2_chosen']/a").click()
        self.driver.find_element(By.XPATH, "//div[@id='dept2_chosen']/div/ul/li[2]").click()
        self.driver.find_element(By.XPATH, "//input[@id='verifyPassword']").send_keys("alin19941226061X.")
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestZenTao("test_go_update_company"))
    suite.addTest(TestZenTao("test_add_department"))
    suite.addTest(TestZenTao("test_add_department_user"))
    unittest.TextTestRunner().run(suite)