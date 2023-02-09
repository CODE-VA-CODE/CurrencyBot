import time


BlockdUserList = dict()
msgs = 6 # Messages in
_max = 60 # Seconds
ban = 600 # Seconds


def userIsBlockd(user_id):
    try:
        user = BlockdUserList[user_id]
        user["messages"] += 1
    except:
        BlockdUserList[user_id] = {"next_time": int(time.time()) + _max, "messages": 1, "banned": 0}
        user = BlockdUserList[user_id]
    if user["banned"] >= int(time.time()):
        return True
    else:
        if user["next_time"] >= int(time.time()):
            if user["messages"] >= msgs:
                BlockdUserList[user_id]["banned"] = time.time() + ban
                return True
        else:
            BlockdUserList[user_id]["messages"] = 1
            BlockdUserList[user_id]["next_time"] = int(time.time()) + _max
    return False
