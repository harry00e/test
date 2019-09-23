import requests
import datetime
import pandas as pd
import time
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 設定 request 之限制 重試 5 次 關閉 session
requests.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False


def get_data():
    # 假 User
    user_agent = UserAgent()
    # 產生日期列表
    date_list = [datetime.datetime.strftime(x, '%Y%m01') for x in
                 list(pd.date_range(start="19990101", end="20190901", freq="M"))]
    all_data = pd.DataFrame()
    for date in date_list:
        print(date)
        # 嘗試獲取資料
        try:
            res = requests.get("https://www.twse.com.tw/indicesReport/MI_5MINS_HIST?response=csv&date=" + date,
                               headers={'Connection': 'close',
                                        'User-Agent': user_agent.random})
            print("status_code:", res.status_code)
        except Exception as e:
            res = None
            print(date, e)
        if res:
            try:
                content = convert_to_df(res)
                # 連接新資料到 DataFrame
                all_data = pd.concat([all_data, content], ignore_index=True, sort=False)
                # 避免頻率過高
                time.sleep(random.uniform(3, 5.5))
            except Exception as e:
                print(date, e)
                print(res)
        else:
            print(date, "request error, response is none.")

    print(all_data)
    all_data.to_csv('twii_2.csv', index=False, header=True)


def convert_to_df(res):
    # 以換行符號切割每列並剔除第一列標題
    content = res.text.strip().split("\n")[1:]
    # 將多餘的符號去除
    content = [row.strip().replace(" ", "")[:-1] for row in content]
    content = [row.split("\",") for row in content]
    content = [[element.replace("\"", "").replace(",", "") for element in row] for row in content]
    # 轉換成 pandas DataFrame 格式並串接
    content = pd.DataFrame(content[1:], index=None, columns=content[0])
    return content


if __name__ == '__main__':
    get_data()