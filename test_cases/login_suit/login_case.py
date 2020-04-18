import unittest
import warnings
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestZenTaoLogin(unittest.TestCase):

    def setUp(self):
        # 临时屏蔽相关警告
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.base_url = "http://127.0.0.1/pro/user-login-L3Byby8=.html"
        self.driver.get(self.base_url)

    def test_login_success(self, name='admin', password='alin19941226061X.'):
        """
        禅道登录
        """
        self.driver.find_element(By.XPATH, "//input[@id='account']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        self.assertTrue(EC.title_is("我的地盘 - 禅道"))

    def test_login_username_error(self, name='admn', password='alin19941226061X.'):
        """
        账户名错误登录失败
        """
        self.driver.find_element(By.XPATH, "//input[@id='account']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.alert_is_present()))

    def test_login_password_error(self, name='admin', password='alin199'):
        """
        密码错误登录失败
        """
        self.driver.find_element(By.XPATH, "//input[@id='account']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.alert_is_present()))

    def tearDown(self):
        sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()