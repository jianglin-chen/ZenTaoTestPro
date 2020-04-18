import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MenuLinkCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.base_url = "http://127.0.0.1/pro/user-login-L3Byby8=.html"
        self.driver.get(self.base_url)

    def test_my_link(self):
        """
        验证我的地盘链接跳转正确
        """
        self.driver.find_element(By.XPATH, "//input[@id='account']").send_keys('admin')
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('alin19941226061X.')
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        self.driver.find_element(By.XPATH, "//li[@data-id='my']").click()
        self.assertTrue(EC.title_is("我的地盘 - 禅道"))

    def test_product_link(self):
        """
        验证产品主页链接跳转正确
        """
        self.driver.find_element(By.XPATH, "//input[@id='account']").send_keys('admin')
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('alin19941226061X.')
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        self.driver.find_element(By.XPATH, "//li[@data-id='product']").click()
        self.assertTrue(EC.title_is("产品主页 - 禅道"))


    def test_test_link(self):
        """
        验证测试主页链接跳转正确
        """
        self.driver.find_element(By.XPATH, "//input[@id='account']").send_keys('admin')
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys('alin19941226061X.')
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'测试')]").click()
        self.assertTrue(EC.title_is("测试主页 - 禅道"))

    def tearDown(self):
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()