import GetTemp, Tweet
import time, datetime

interval = 10   # in minute(s)

get = GetTemp.GetTemp("/dev/tty.usbmodem14401", 115200)
tweet = Tweet.Tweet()

prevmin = 0
nextmin = 0


def makeContent():
    values = get.getFromArduino()
    temp = values["temp"]
    humidity = values["humidity"]
    thi = int(get.calcTHI(temp, humidity))
    feeling = get.thiFeeling(thi)
    now = datetime.datetime.now()
    strftime = now.strftime("%Y年%m月%d日 %H:%M")

    content = strftime + "\n現在の室温: " + str(temp) + "°C\n現在の湿度: " + str(humidity) + "%\n不快指数: " + str(thi) + " (" + feeling + ")"
    return content

def tweetIt(content):
    tweet.post(content)

def main():
    print("Welcome!")

    prevmin = datetime.datetime.now().minute
    nextmin = (prevmin + interval) % 60

    content = makeContent()
    print("10秒後に最初のツイートをします")
    time.sleep(10)

    #tweetIt(content)
    print("\n" + content + "\n")

    print("これから約" + str(interval) + "分ごとに自動ツイートします\nCtrl+C で終了できます")
    try:
        while True:
            if datetime.datetime.now().minute != nextmin:
                time.sleep(20)
                continue
            print("ツイート準備中")
            prevmin = datetime.datetime.now().minute
            nextmin = (prevmin + interval) % 60
            content = makeContent()
            print("10秒後にツイートします")
            time.sleep(10)
            print("\n" + content + "\n")
            #tweetIt(content)
            print(str(interval) + "分後にまた自動ツイートします\nCtrl+C で終了できます")
    except KeyboardInterrupt:
        print("終了します")
        exit(0)

if __name__ == "__main__":
    main()
