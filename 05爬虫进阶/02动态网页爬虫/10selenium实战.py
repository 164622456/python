from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
import csv

# 为什么需要把driver放在外面？
# 因为如果放在里面，那么driver将会随着对象的销毁而被销毁
# 而我们的TrainSpider的对象是放在main函数中执行的，
# 只要main函数运行完成后，里面所有的变量都不会被销毁，
# 也就说spider也会被销毁，那么spider里面的driver也会被销毁。
driver = webdriver.Chrome(executable_path="D:\ProgramApp\chromedriver\chromedriver73.exe")


# 9：商务座，M：一等座，O：二等座，3：硬卧，4：软卧，1：硬座

class TrainSpider(object):
    login_url = "https://kyfw.12306.cn/otn/resources/login.html"
    personal_url = "https://kyfw.12306.cn/otn/view/index.html"
    left_ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
    confirm_passenger_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"

    def __init__(self,from_station,to_station,train_date,trains,passengers):
        """
        :param from_station: 起始站
        :param to_station: 目的站
        :param train_date: 出发日期
        :param trains: 需要购买的车次。{"G529":["M","O"],"G403":["M","O"]}
        :param passengers: 乘客的姓名，需要为一个列表
        """
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
        # 等待url是否变成个人中心的url，来判断是否登录成功
        WebDriverWait(driver,1000).until(
            EC.url_contains(self.personal_url)
        )
        print("登录成功！")

    def search_left_ticket(self):
        driver.get(self.left_ticket_url)
        # 起始站的代号设置
        from_station_input = driver.find_element_by_id("fromStation")
        from_station_code = self.station_codes[self.from_station]
        driver.execute_script("arguments[0].value='%s'"%from_station_code,from_station_input)
        # 终点站的代号设置
        to_station_input = driver.find_element_by_id("toStation")
        to_station_code = self.station_codes[self.to_station]
        driver.execute_script("arguments[0].value='%s'" % to_station_code, to_station_input)
        # 时间设置
        train_date_input = driver.find_element_by_id("train_date")
        driver.execute_script("arguments[0].value='%s'" % self.train_date, train_date_input)

        # 执行查询操作
        search_btn = driver.find_element_by_id("query_ticket")
        search_btn.click()

        # 解析车次信息
        WebDriverWait(driver,1000).until(
            EC.presence_of_element_located((By.XPATH,"//tbody[@id='queryLeftTable']/tr"))
        )
        train_trs = driver.find_elements_by_xpath("//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
        is_searched = False
        while True:
            for train_tr in train_trs:
                infos = train_tr.text.replace("\n", " ").split(" ")
                number = infos[0]
                if number in self.trains:
                    seat_types = self.trains[number]
                    for seat_type in seat_types:
                        if seat_type == "O":
                            # 二等座
                            count = infos[9]
                            if count.isdigit() or count == '有':
                                is_searched = True
                                break
                        elif seat_type == 'M':
                            # 一等座
                            count = infos[8]
                            if count.isdigit() or count == '有':
                                is_searched = True
                                break
                    if is_searched:
                        self.selected_number = number
                        order_btn = train_tr.find_element_by_xpath(".//a[@class='btn72']")
                        order_btn.click()
                        return

    def confirm_passengers(self):
        WebDriverWait(driver,1000).until(
            EC.url_contains(self.confirm_passenger_url)
        )

        # 先等待一下乘客标签显示出来了
        WebDriverWait(driver,1000).until(
            EC.presence_of_element_located((By.XPATH,"//ul[@id='normal_passenger_id']/li/label"))
        )

        # 确认需要购买车票的乘客
        passenger_labels = driver.find_elements_by_xpath("//ul[@id='normal_passenger_id']/li/label")
        for passenger_label in passenger_labels:
            name = passenger_label.text
            if name in self.passengers:
                passenger_label.click()

        # 确认需要购买的席位信息
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

        # 等待提交订单按钮可以被点击
        WebDriverWait(driver,1000).until(
            EC.element_to_be_clickable((By.ID,"submitOrder_id"))
        )
        submit_btn = driver.find_element_by_id("submitOrder_id")
        submit_btn.click()

        # 判断模态对话框出现并且确认按钮可以点击了
        WebDriverWait(driver,1000).until(
            EC.presence_of_element_located((By.CLASS_NAME,"dhtmlx_window_active"))
        )
        WebDriverWait(driver,1000).until(
            EC.element_to_be_clickable((By.ID,"qr_submit_id"))
        )
        submit_btn = driver.find_element_by_id("qr_submit_id")
        while submit_btn:
            try:
                submit_btn.click()
                submit_btn = driver.find_element_by_id("qr_submit_id")
            except ElementNotVisibleException:
                break
        print("恭喜！%s车次%s抢票成功！"%(self.selected_number,self.selected_seat))



    def run(self):
        # 1. 登录
        self.login()
        # 2. 车次余票查询
        self.search_left_ticket()
        # 3. 确认乘客和车次信息
        self.confirm_passengers()


def main():
    from_station = input("请输入出发地：")
    to_station = input("请输入目的地：")
    spider = TrainSpider(from_station,to_station,"2019-05-07",{"G529":["O","M"],"G111":["M"]},['黄德和'])
    spider.run()


if __name__ == '__main__':
    main()

