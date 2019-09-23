import requests
import sys
import os
from datetime import datetime, timedelta, date
import time
from pytz import timezone


class TESTLINE:
    def __init__(self):
        self.token = 'ABCD....'

    def lineNotify(self, msg):
        headers = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = {'message': msg}
        r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
        return r.status_code

    def testMessage(self):
        message = input("請輸入欲發送訊息>")
        self.lineNotify(message)

    def queryCourse(self, goDate=None):
        if goDate == None:
            goDate = input("請輸入欲發送訊息的日期YYYY/MM/DD>")
        # 以下是你需寫的程式 ....
        message = (goDate)
        self.lineNotify(message)

    def run(self):
        while (True):
            now = datetime.now(timezone('Asia/Taipei'))
            nowTime = now.timetuple()
            # today = now.date().strftime('%Y/%m/%d')
            tomorrow = (now.date() + timedelta(1)).strftime('%Y/%m/%d')
            # 時間條件
            # if (nowTime.tm_hour==21 and nowTime.tm_min== 0) :
            self.queryCourse(tomorrow)
            time.sleep(60)


def main():
    testline = TESTLINE()
    while (True):
        k = input("請輸入數字 1(測試Line Notify),2(手動發送課程訊息),3 (auto run) 或 q>")
        if k == '1':
            testline.testMessage()
        elif k == '2':
            testline.queryCourse()
        elif k == '3':
            testline.run()
        elif k == 'q':
            sys.exit(0)


if __name__ == '__main__':
    if 'DYNO' in os.environ:
        testline = TESTLINE()
        testline.run()
    else:
        main()


