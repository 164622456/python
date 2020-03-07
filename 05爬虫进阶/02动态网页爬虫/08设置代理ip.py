from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://110.52.235.176:9999")
driver = webdriver.Chrome(executable_path=r"D:\Study\python\tools\chromedriver.exe", chrome_options=options)

driver.get("http://httpbin.org/ip")
