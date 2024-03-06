# coding=utf-8
'''
作者：林海峰
日期：2024年03月06日08:45
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

from selenium.webdriver.support.select import Select

#货币字典
currency_dict = {
    'GBP': '英镑',
    'HKD': '港币',
    'USD': '美元',
    'CHF': '瑞士法郎',
    'DEM': '德国马克',
    'FRF': '法国法郎',
    'SGD': '新加坡元',
    'SEK': '瑞典克朗',
    'DKK': '丹麦克朗',
    'NOK': '挪威克朗',
    'JPY': '日元',
    'CAD': '加拿大元',
    'AUD': '澳大利亚元',
    'EUR': '欧元',
    'MOP': '澳门元',
    'PHP': '菲律宾比索',
    'THB': '泰国铢',
    'NZD': '新西兰元',
    'KRW': '韩元',
    'RUB': '卢布',
    'MYR': '林吉特',
    'TWD': '新台币',
    'ESP': '西班牙比塞塔',
    'ITL': '意大利里拉',
    'NLG': '荷兰盾',
    'BEF': '比利时法郎',
    'FIM': '芬兰马克',
    'INR': '印度卢比',
    'IDR': '印尼卢比',
    'BRL': '巴西里亚尔',
    'AED': '阿联酋迪拉姆',
    'ZAR': '南非兰特',
    'SAR': '沙特里亚尔',
    'TRY': '土耳其里拉',
}

class YinHangTest():

    def __init__(self):
        self.url = 'https://www.boc.cn/sourcedb/whpj/'
        self.driver = webdriver.Chrome()

    #按日期和货币种类查找
    def search(self, data, currency_ch):
        #输入日期
        data_in = self.driver.find_element(By.XPATH, '//div[@class="search_bar"]/input[@name="nothing"]')
        data_in.send_keys(data)
        #选择货币
        currency_in = self.driver.find_element(By.XPATH, '//select[@id="pjname"]')
        s = Select(currency_in)
        s.select_by_value(currency_ch)
        #点击查找
        search_click = self.driver.find_element(By.XPATH, '//tbody//input[@class="search_btn"]')
        search_click.click()

    #存储数据
    def save_date(self):
        #找到所需数据
        out = self.driver.find_element(By.XPATH,'//div[@class="BOC_main publish"]/table/tbody/tr[2]/td[4]').text
        print(out)
        dates = self.driver.find_elements(By.XPATH,'//div[@class="BOC_main publish"]/table/tbody/tr')
        #写入记事本
        with open('result.txt', 'w', encoding='utf-8') as f:
            # 设置格式tplt，12代表间隔距离，使数据整洁好看
            tplt = "{:<15}{:<12}{:<12}{:<12}{:<12}{:<12}{:<15}"
            f.write(tplt.format('货币名称', '现汇买入价', '现钞买入价', '现汇卖出价', '现钞卖出价', '中行折算价', '发布时间'))
            f.write('\n')
            for i in dates[1:-1]:
                n = []
                n = i.text.split(' ')
                tplt = "{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}"
                f.write(tplt.format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7]))
                f.write('\n')

    def run(self, data, currency_ch):
        self.driver.get(self.url)
        self.search(data, currency_ch)
        self.save_date()

if __name__ == '__main__':
    #接收命令行输入
    data = sys.argv[1]
    currency = sys.argv[2]
    # 判断输入是否合法
    if not data.isdigit() or not currency.isalpha():
        print('输入不合法')
        exit()
    try:
        currency_ch = currency_dict[currency]
    except:
        print("货币英文代码查询不到")
        exit()

    browser = YinHangTest()
    browser.run(data, currency_ch)
