import requests
from bson import ObjectId
from uuid import uuid4
from setting import client, MONGODB, VOICE, CHAT_PATH,TULING_URL, TULING_DATA
from my_gensim import my_xsjzxs
import os

def get_file_content(filePath):
    os.system(f"ffmpeg -y -i {filePath}  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
    with open(f"{filePath}.pcm", 'rb') as fp:
        return fp.read()

def audio2text(filePath):
    res = client.asr(get_file_content(filePath), 'pcm', 16000, {
        'dev_pid': 1536,
    })
    print(res.get("result"))
    text = res.get("result")[0]
    print(text)

    return text


def text2audio(text):
    result = client.synthesis(text, 'zh', 1, VOICE)
    filename = f"{uuid4()}.mp3"
    file_path = os.path.join(CHAT_PATH,filename)
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        # print(result)
        with open(file_path, 'wb') as f:
            f.write(result)

    return filename


def to_tuling(text, uid):
    TULING_DATA["perception"]["inputText"]["text"] = text
    TULING_DATA["userInfo"]["userId"] = uid
    res = requests.post(TULING_URL, json=TULING_DATA)
    res_json = res.json()
    text = res_json.get("results")[0].get("values").get("text")
    print(text)
    return text

from pypinyin import lazy_pinyin,TONE2

def my_nlp_lowB(text,uid):
    if "黄文" in text:
        res="爸爸你好"
        filename=text2audio(res)
        return {"from_user": "ai", "chat": filename}
    # text = "我要给爸爸发消息"
    py_text = "".join(lazy_pinyin(text, style=TONE2))
    if "发消息" in text:
        toy_info=MONGODB.toys.find_one({"_id":ObjectId(uid)})
        for friend in toy_info.get("friend_list"):
            py_nick = "".join(lazy_pinyin(friend.get("friend_nick"), style=TONE2))
            py_remark = "".join(lazy_pinyin(friend.get("friend_remark"), style=TONE2))
            if py_nick in py_text or py_remark in py_text:
                filename = text2audio(f"可以给{friend.get('friend_remark')}发消息了")
                return {"from_user":friend.get("friend_id"),"chat":filename,"friend_type":friend.get('friend_type')}

    if "播放" in text or "我要听" in text or "唱一首" in text:
        content = my_xsjzxs(text)
        if content:
            return {"from_user": 'ai', "music": content.get("music")}

    res = to_tuling(text,uid)
    filename = text2audio(res)
    return {"from_user": "ai", "chat": filename}