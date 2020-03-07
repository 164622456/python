import csv
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r"D:\Study\python\tools\chromedriver.exe")


class TrainSpider(object):
    login_url = "https://kyfw.12306.cn/otn/resources/login.html"
    personal_url = "https://kyfw.12306.cn/otn/view/index.html"
    left_ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
    confirm_passenger_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"

    def __init__(self,from_station,to_station,train_date,trains,passengers):
        self.from_station = from_station
        self.to_station = to_station
        self.train_date = train_date
        self.trains = trains
        self.passengers = passengers
        self.selected_number = None
        self.selected_seat = None
        # 初始化站点所对应的代号
        self.station_codes = {}
        self.init_station_code()

    def init_station_code(self):
        with open("stations.csv", 'r', encoding='utf-8') as fp:
            reader = csv.DictReader(fp)
            for line in reader:
                name = line["name"]
                code = line['code']
                self.station_codes[name] = code

    def login(self):
        driver.get(self.login_url)
        WebDriverWait(driver,1000).until(
            EC.url_contains(self.personal_url)
        )
        print("登录成功！")
        driver.implicitly_wait(10)
        a = driver.find_element_by_class_name("modal-close")
        if a != None:
            print(type(a))
            a.click()
        else:
            print("没有找到关闭按钮")

    def search_left_ticket(self):
        print("开始车次查询")
        driver.get(self.left_ticket_url)
        # 起始站的代号
        from_station_input = driver.find_element_by_id("fromStation")
        from_station_code = self.station_codes[self.from_station]
        driver.execute_script("arguments[0].value='%s'"%from_station_code,from_station_input)
        # 终点站的代号
        to_station_input = driver.find_element_by_id("toStation")
        to_station_code = self.station_codes[self.to_station]
        driver.execute_script("arguments[0].value='%s'" % to_station_code, to_station_input)
        # 设置时间
        train_date_input = driver.find_element_by_id("train_date")
        driver.execute_script("arguments[0].value='%s'" % self.train_date, train_date_input)
        # 执行查询操作
        search_btn = driver.find_element_by_id("query_ticket")
        search_btn.click()
        print("车次查询成功！")
        # 解析车次信息
        WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, "//tbody[@id='queryLeftTable']/tr"))
        )
        # 是否查找到
        is_searched = False
        train_trs = driver.find_elements_by_xpath("//tbody[@id='queryLeftTable']/tr[not(@style)]")
        # 查看所有的列车
        while True:
            for train_tr in train_trs:
                print(train_tr)
                # 获取列车的信息
                infos = train_tr.text.replace("\n", " ").split(" ")
                number = infos[0]  # 车次
                print(infos)
                print(number)
                if number in self.trains:
                    for seat_type in self.trains[number]:
                        # 2等座
                        if seat_type == "O":
                            count = infos[9]
                            if count.isdigit() or count == '有':
                                is_searched = True
                                break
                        # 1等座
                        elif seat_type == "M":
                            count = infos[8]
                            if count.isdigit() or count == '有':
                                is_searched = True
                                break
                    print(is_searched)
                    if is_searched:
                        self.selected_number = number
                        order_btn = train_tr.find_element_by_xpath(".//a[@class='btn72']")
                        order_btn.click()
                        return

    def confirm_passengers(self):
        WebDriverWait(driver, 1000).until(
            EC.url_contains(self.confirm_passenger_url)
        )
        # 先等待一下乘客标签显示出来了
        WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@id='normal_passenger_id']/li/label"))
        )
        # 等待席位元素被加载进来
        WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, "//select[@id='seatType_1']/option"))
        )

        # 确定要购买的乘客
        passenger_labels = driver.find_elements_by_xpath("//ul[@id='normal_passenger_id']/li/label")
        for passenger_label in passenger_labels:
            name = passenger_label.text
            print(name)
            if name in self.passengers:
                print(type(passenger_label))
                passenger_label.click()

        # 确定要购买的席位
        seat_select = Select(driver.find_element_by_id("seatType_1"))
        seat_types = self.trains[self.selected_number]
        for seat_type in seat_types:
            try:
                self.selected_seat = seat_type
                seat_select.select_by_value(seat_type)
            except NoSuchElementException:
                continue
            else:
                break
        # 等待提交按钮可以被点击
        WebDriverWait(driver, 1000).until(
            EC.element_to_be_clickable((By.ID, "submitOrder_id"))
        )
        submit_btn = driver.find_element_by_id("submitOrder_id")
        submit_btn.click()
        print("提交按钮已点击")
        # ---------------------------------------------------
        # 判断模态对话框出现并且确认按钮可以点击
        print("开始等待模态对话框")
        WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dhtmlx_window_active"))
        )
        print("开始等待模态对话框中的确定按钮")
        WebDriverWait(driver, 1000).until(
            EC.element_to_be_clickable((By.ID, "qr_submit_id"))
        )
        # ---------------------------------------------------
        confirm_submit_btn = driver.find_element_by_id("qr_submit_id")
        print(confirm_submit_btn)
        print("开始点击确定按钮")
        while confirm_submit_btn:
            try:
                print(confirm_submit_btn)
                confirm_submit_btn.click()
                confirm_submit_btn = driver.find_element_by_id("qr_submit_id")
            except ElementNotVisibleException:
                break
        print("恭喜！%s车次%s抢票成功！" % (self.selected_number, self.selected_seat))
        time.sleep(100)

    def run(self):
        # 1.登录
        self.login()
        print("-----------------车次余票查询-----------------")
        # 2.车次余票查询
        self.search_left_ticket()
        # 3.确认乘客和车次信息
        self.confirm_passengers()


def main():
    spider = TrainSpider("北京", "沈阳南", "2020-04-03", {"D3": ["O", "M"]}, ["杨春苗"])
    spider.run()


if __name__ == '__main__':
    main()
