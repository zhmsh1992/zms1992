import json
from setting import REDISDB

# 存储
def set_chat(to_user,from_user):
    my_world = REDISDB.get(to_user)
    if not my_world:
        setchat = {from_user:1}
        setchat_json = json.dumps(setchat)
    else:
        my_world_dict = json.loads(my_world)
        if my_world_dict.get(from_user):
            my_world_dict[from_user] +=1
        else:
            my_world_dict[from_user] = 1
        setchat_json = json.dumps(my_world_dict)
    REDISDB.set(to_user,setchat_json)

def get_chat_all(to_user):
    chat = REDISDB.get(to_user)
    if not chat:
        return {"count":0}
    else:
        chat_dict = json.loads(chat)
        chat_dict["count"] = sum(chat_dict.values())
        return chat_dict

def get_chat(to_user,from_user):
    chat = REDISDB.get(to_user)
    count = 0
    if not chat:
        return 0
    else:
        chat_dict = json.loads(chat)
        if chat_dict.get(from_user):
            count =chat_dict.get(from_user)
        chat_dict[from_user] = 0
        REDISDB.set(to_user,json.dumps(chat_dict))
        return count