from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\Study\python\tools\chromedriver.exe")

driver.get('https://www.baidu.com/')

# 1. 获取所有cookie
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)
print("-"*30)

# 2. 根据key来获取cookie
# cookie = driver.get_cookie("delPer")
# print(cookie)
#
cookie = driver.get_cookie("BIDUPSID")
print(cookie)


# 3. 添加cookie
driver.add_cookie({"name":"username","value":"123"})

cookies = driver.get_cookies()
print(cookies)

# 4. 根据key删除某个cookie
# driver.add_cookie({"name":"password","value":"111111"})
# cookie1 = driver.get_cookie("password")
# print(cookie1)
# driver.delete_cookie("password")
# print("="*30)
# cookie2 = driver.get_cookie("password")
# print(cookie2)

# 5. 删除所有cookie
# cookies = driver.get_cookies()
# print(cookies)
# driver.delete_all_cookies()
# print("="*30)
# print(driver.get_cookies())







