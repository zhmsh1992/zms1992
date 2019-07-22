import time
XMLY_URL = "https://www.ximalaya.com/revision/play/album?albumId=%s&pageNum=%s&sort=-1&pageSize=30"
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}

#数据库配置
import pymongo
conn = pymongo.MongoClient('127.0.0.1',27017)
MONGODB = conn['VistaToy']

from redis import Redis
REDISDB = Redis("127.0.0.1",6379,db=8)

#目录配置
MUSIC_PATH = "Music"
COVER_PATH ="Cover"
QRCODE_PATH = "QRcode"
CHAT_PATH = "Chats"

#App通讯协议
RET ={
    "CODE":0,
    "MSG":'',
    "DATA":{}
}

#联图二维码
LT_URL = "http://qr.topscan.com/api.php?text=%s"

#百度AI配置
from aip import AipSpeech
from aip import AipNlp

APP_ID = '15838158'
API_KEY = '4hMGPfu6fxPVUA6aCEUv4Eiu'
SECRET_KEY = 'suZ8RDXZ1G0qpcTaQzRd8ZI396sFH8ID'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
NLP = AipNlp(APP_ID, API_KEY, SECRET_KEY)

VOICE = {
        'vol': 5,
        'per': 4,
        'spd': 4,
        'pit': 7,
    }



# 图灵机器人
TULING_URL = "http://openapi.tuling123.com/openapi/api/v2"
TULING_DATA = {
        "perception": {
            "inputText": {
                "text": ""
            }
        },
        "userInfo": {
            "apiKey": "3e430be2120c4097886b422943e94592",
            "userId": ""
        }
    }