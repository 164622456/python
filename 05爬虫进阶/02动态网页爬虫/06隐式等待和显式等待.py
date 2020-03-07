from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"D:\Study\python\tools\chromedriver.exe")

# 1. 隐式等待：
# driver.get("https://www.baidu.com/")
# driver.implicitly_wait(10)
# driver.find_element_by_id("afsdasdf")

# 2. 显式等待：
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc")

WebDriverWait(driver,100).until(
    EC.text_to_be_present_in_element_value((By.ID,"fromStationText"),"长沙")
)

WebDriverWait(driver,100).until(
    EC.text_to_be_present_in_element_value((By.ID,"toStationText"),"北京")
)

btn = driver.find_element_by_id("query_ticket")
btn.click()