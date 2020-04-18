import os
from selenium import webdriver

def set_driver():
    current = os.path.dirname(__file__)
    chrome_driver_path = os.path.join(current, '../webdrver/chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("http://127.0.0.1/pro/user-login-L3Byby8=.html")