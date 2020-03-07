from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
import csv
import time

class TrainSpider(object):
    # 登录url
    login_url = "https://kyfw.12306.cn/otn/resources/login.html"
    # 个人中心url
    my_url = "https://kyfw.12306.cn/otn/view/index.html"
    # 搜索余票的url
    left_ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"

    def __init__(self,from_station,to_station,train_date,trains,passengers):
        """
        :param from_station: 出发地站点名称
        :param to_station: 目的地站点名称
        :param train_date: 出发日期
        :param trains: 需要为一个字典，可以为多个车次。示例如：{"G123":["M","O"]}
        :param passengers: 乘客姓名
        """
        self.driver = webdriver.Chrome(executable_path="D:\ProgramApp\chromedriver\chromedriver73.exe")
        self.from_station = from_station
        self.to_station = to_station
        self.trains = trains
        self.train_date = train_date
        self.passengers = passengers
        # 当前选中的车次和席位
        self.current_number = None
        self.current_seat_type = None
        # 初始化车站代码
        self.station_codes = {}
        self.init_station_code()

    def init_station_code(self):
        with open("stations.csv",'r',encoding='utf-8') as fp:
            reader = csv.DictReader(fp)
            for line in reader:
                name = line['name']
                code = line['code']
                self.station_codes[name] = code

    def login(self):
        self.driver.get(self.login_url)
        WebDriverWait(self.driver,100).until(
            EC.url_to_be(self.my_url)
        )
        print("登录成功！")

    def search_left_ticket(self):
        """
        查找余票信息
        :return: None
        """
        self.driver.get(self.left_ticket_url)
        from_code = self.station_codes[self.from_station]
        to_code = self.station_codes[self.to_station]
        # 找到输入框元素
        from_station_input = self.driver.find_element_by_id("fromStation")
        to_station_input = self.driver.find_element_by_id("toStation")
        train_date_input = self.driver.find_element_by_id("train_date")
        self.driver.execute_script("arguments[0].value='%s'"%from_code,from_station_input)
        self.driver.execute_script("arguments[0].value='%s'"%to_code,to_station_input)
        self.driver.execute_script("arguments[0].value='%s'"%self.train_date,train_date_input)
        queryBtn = self.driver.find_element_by_id("query_ticket")
        # 死循环不断的点击查询
        while True:
            # 点击查询
            queryBtn.click()
            # 等待查询的车次出现了
            WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located((By.XPATH, "//tbody[@id='queryLeftTable']/tr"))
            )
            # 是否查找到
            is_searched = False
            train_trs = self.driver.find_elements_by_xpath("//tbody[@id='queryLeftTable']/tr[not(@style)]")
            # 查看所有的列车
            for train_tr in train_trs:
                # 获取一列车的信息
                infos = train_tr.text.replace("\n", " ").split(" ")
                orderable = infos[-1]
                # 如果不能预订，就直接看下一趟列车
                if orderable != '预订':
                    continue
                # 获取到预订按钮
                order_btn = train_tr.find_element_by_xpath(".//a[@class='btn72']")
                number = infos[0]
                if number in self.trains:
                    for seat_type in self.trains[number]:
                        # 一等座
                        if seat_type == "M":
                            count = infos[8]
                            if count.isdigit() or count == '有':
                                is_searched = True
                                break
                        # 二等座
                        elif seat_type == "O":
                            count = infos[9]
                            if count.isdigit() or count == '有':
                                is_searched = True
                                break
                if is_searched:
                    self.current_number = number
                    order_btn.click()
                    return

    def confirm_passenger(self):
        """
        确认乘客和席位信息
        :return: None
        """
        # 等待页面跳转到确认乘客信息页面
        WebDriverWait(self.driver,1000).until(
            EC.url_contains("https://kyfw.12306.cn/otn/confirmPassenger/initDc")
        )

        # 等待乘客信息元素被加载进来
        WebDriverWait(self.driver,1000).until(
            EC.presence_of_element_located((By.XPATH,"//ul[@id='normal_passenger_id']/li"))
        )

        # 等待席位元素被加载进来
        WebDriverWait(self.driver,1000).until(
            EC.presence_of_element_located((By.XPATH,"//select[@id='seatType_1']/option"))
        )

        # 提取所有的乘客的label标签
        passenger_labels = self.driver.find_elements_by_xpath("//ul[@id='normal_passenger_id']/li/label")

        # 把需要购买票的用户勾选上
        for passenger_label in passenger_labels:
            if passenger_label.text in self.passengers:
                passenger_label.click()

        # 选择席位
        seat_select = Select(self.driver.find_element_by_id("seatType_1"))
        for seat_type in self.trains[self.current_number]:
            try:
                seat_select.select_by_value(seat_type)
                self.current_seat_type = seat_type
            except NoSuchElementException:
                continue
            else:
                break

        # 等待提交订单按钮可用，然后点击
        WebDriverWait(self.driver,1000).until(
            EC.element_to_be_clickable((By.ID,"submitOrder_id"))
        )
        submit_order_btn = self.driver.find_element_by_id("submitOrder_id")
        submit_order_btn.click()

        # 等待核对订单的模态对话框弹出来
        WebDriverWait(self.driver,1000).until(
            EC.presence_of_element_located((By.CLASS_NAME,"dhtmlx_window_active"))
        )
        WebDriverWait(self.driver,1000).until(
            EC.element_to_be_clickable((By.ID,"qr_submit_id"))
        )
        confirm_submit_btn = self.driver.find_element_by_id("qr_submit_id")
        try:
            while confirm_submit_btn:
                confirm_submit_btn.click()
                confirm_submit_btn = self.driver.find_element_by_id("qr_submit_id")
        except ElementNotVisibleException:
            pass
        print("恭喜！成功抢到【%s】次列车【%s】席位，请在30分钟内完成付款！"%(self.current_number,self.current_seat_type))

        time.sleep(100)

    def run(self):
        # 1. 登录
        self.login()
        # 2. 跳转到搜索余票的页面
        self.search_left_ticket()
        # 3. 确定购票乘客和席位信息
        self.confirm_passenger()


def main():
    # 9：商务座，M：一等座，O：二等座，3：硬卧，4：软卧，1：硬座
    spider = TrainSpider("北京","长沙","2019-05-07",{"G529":["O","M"]},["黄德和"])
    spider.run()


if __name__ == '__main__':
    main()

