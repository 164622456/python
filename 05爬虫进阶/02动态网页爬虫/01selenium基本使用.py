
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"D:\Study\python\tools\chromedriver.exe")

driver.get("https://www.baidu.com")

time.sleep(4)

driver.quit()

# 测试