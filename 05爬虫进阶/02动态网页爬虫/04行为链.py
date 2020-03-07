from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome(executable_path="D:\ProgramApp\chromedriver\chromedriver73.exe")
driver = webdriver.Chrome(executable_path=r"D:\Study\python\tools\chromedriver.exe")

# driver.get("https://www.zhihu.com/signin?next=%2F")

# actions = ActionChains(driver)
# usernameTag = driver.find_element_by_name("username")
# passwordTag = driver.find_element_by_name("password")
# submitBtn = driver.find_element_by_class_name("SignFlow-submitButton")
#
# actions.move_to_element(usernameTag)
# actions.send_keys_to_element(usernameTag,"18888888888")
# actions.move_to_element(passwordTag)
# actions.send_keys_to_element(passwordTag,"xxxxxx")
# actions.move_to_element(submitBtn)
# actions.click(submitBtn)
#
# actions.perform()


driver.get("https://www.dy2018.com/")

actions = ActionChains(driver)

# <input name="keyboard" type="text" value="" class="formhue">
keyboard = driver.find_element_by_name("keyboard")
actions.move_to_element(keyboard)
actions.send_keys_to_element(keyboard,"大上海")

# <input name="Submit" type="Submit" value="立即搜索">
submitBtn = driver.find_element_by_name("Submit")
actions.move_to_element(submitBtn)
actions.click(submitBtn)

actions.perform()