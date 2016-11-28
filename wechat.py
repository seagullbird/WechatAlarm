#!/usr/bin/env python3
from itchat import client
import time


stopTxt = "stopTxt"
alarmTxt = "回复'" + stopTxt + "'即可停止闹钟～"
finalMsg = 'finalMsg'
toUserName = '<toUserName>'

__client = client()

statusStorageDir = 'itchat.pkl'
if not __client.load_login_status(statusStorageDir):
    __client.auto_login(enableCmdQR=False)
    __client.dump_login_status(statusStorageDir)


def listenToReply():
    for i in range(6):
        time.sleep(0.5)
        if __client.storageClass.msgList:
            for msg in __client.storageClass.msgList:
                if msg['Text'] == stopTxt:
                    print(msg)
                    __client.send_msg(finalMsg, toUserName)
                    return True
    return False


def run():
    count = 0
    while not listenToReply():
        print(__client.send_msg(alarmTxt[count % len(alarmTxt)], toUserName))
        count += 1
    return count


if __name__ == '__main__':
    print('今天发了 %d 条才叫醒她' % run())
