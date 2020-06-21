import json
from requests_oauthlib import OAuth1Session

class Tweet:
    # コンストラクタ #
    def __init__(self):
        #JSONファイルから接続に必要な情報を読み込む
        self.json_open = open("temp-reporter/twitter_config.json", "r")
        self.json_load = json.load(json_open)

        self.CK = self.json_load["CONSUMER_KEY"]
        self.CS = self.json_load["CONSUMER_SECRET"]
        self.AT = self.json_load["ACCESS_TOKEN"]
        self.ATS = self.json_load["ACCESS_TOKEN_SECRET"]

        #認証処理 
        self.twitter = OAuth1Session(CK, CS, AT, ATS)

        self.url = "https://api.twitter.com/1.1/statuses/update.json"
    
    def post(self, content):
        params = {"status": content}

        res = twitter.post(url, params=params)  #post送信

        if res.status_code == 200:  #正常に投稿できた場合
            print("Success: Tweet")
        else:   #正常に投稿できなかった場合
            print("FAILED!: %d" % res.status_code)