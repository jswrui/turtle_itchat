# -*- coding: utf-8 -*-

import os
from time import sleep

def tap_screen(x, y):
	os.system('adb shell input tap {} {}'.format(x, y))

if __name__ == '__main__':
	for i in range(60):
		if (i > 0):
			tap_screen(2489, 1307) #再次挑战
			print("再次挑战")
			sleep(5)
		tap_screen(1465, 913) #点击闯关
		print("开始闯关")
		sleep(10)
		tap_screen(1795, 40)  #自动按钮打怪
		print("自动按钮点击")
		sleep(27)
		tap_screen(1795, 40)  #跳过
		sleep(2)
		tap_screen(1795, 40)  #第二次跳过
		sleep(5)
		tap_screen(500, 500)
		print("点击屏幕继续")
		sleep(5)
		tap_screen(1588, 975)
		sleep(1)