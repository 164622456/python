from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
#     <div data-name="xyz" id="mydiv"></div>
#     <h1>这是爬虫课程</h1>
#  <a href="javascript:;" title="关闭" class="modal-close"><i class="icon icon-close"></i></a>
# </body>
# </html>


driver = webdriver.Chrome(executable_path=r"D:\Study\python\tools\chromedriver.exe")

driver.get(r"D:\Study\python\代码\05爬虫进阶\02动态网页爬虫\abc.html")


a = driver.find_element_by_class_name("modal-close")
a.click()

# div = driver.find_element_by_id("mydiv")
# print(div.get_property("id"))
# print(div.get_property("data-name"))
# print(div.get_attribute("id"))
# print(div.get_attribute("data-name"))

# driver.get("https://www.baidu.com/")
# driver.save_screenshot("baidu.png")
# btn = driver.find_element_by_id("su")
# print(type(btn))