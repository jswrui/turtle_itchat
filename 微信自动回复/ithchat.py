import itchat
import time

#自动回复
#封装好的装饰器，当接收到的消息是text，即文字信息
#注册消息响应事件，消息类型为text，即文本消息

@itchat.msg_register('Text')

def text_reply(msg):
	#当消息不是自己发出的时候
	if not msg['FromUserName'] == myUserName:
		#发送一条提示给文件助手
		itchat.send_msg(u"[%s]收到好友@%s的消息: %s\n" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])), msg['User']['NickName'], msg['Text']), 'filehelper')
		return "[自动回复]你好，我现在有事，稍后与你联系。\n已经收到您的信息： %s\n" %(msg['Text'])

if __name__ == '__main__':
	itchat.auto_login()

	#获取自己的UserName
	myUserName = itchat.get_friends(update=True)[0]["UserName"]
	itchat.run()


# itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])), msg['User']['NickName'], msg['Text']), 'filehelper')