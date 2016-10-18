#!/usr/bin/env python3
from itchat import client
import time


stopTxt = "老公我爱你"
alarmTxt = "回复'" + stopTxt + "'即可停止闹钟～"
finalMsg = '么么哒！'
toUserName = 'aj_18610508701'

__client = client()

__client.auto_login(enableCmdQR=True)


def listenToReply():
    for i in range(5):
        if __client.storageClass.msgList:
            msg = __client.storageClass.msgList.pop()
            if msg['Text'] == stopTxt:
                print(msg)
                __client.send_msg(finalMsg, toUserName)
                return True
    return False

if __name__ == '__main__':
    while not listenToReply():
        print(__client.send_msg(alarmTxt, toUserName))
        time.sleep(3)
