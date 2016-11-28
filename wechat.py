#!/usr/bin/env python3
from itchat import client
import time


stopTxt = "我爱你老公"
alarmTxt = "宝贝，快起床吧，爱你么么，"
alarmTxt += "回‘" + stopTxt + "’解锁闹铃[Shy]"
alarmTxt = alarmTxt.split('，')
finalMsg = '我也爱你宝宝'
toUserName = '<herUserName>'

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
