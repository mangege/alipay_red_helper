# coding: utf-8
# Imports the monkeyrunner modules used by this program
import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

w = 720
h = 1280

#raw_input("按 Enter后再按 Ctrl+D 后开始乱点")
print('go')

while True:
    # 抢
    for i in xrange(0, 9):
        device.touch(362, 692, MonkeyDevice.DOWN_AND_UP)
        time.sleep(0.5)

    # 领
    for i in xrange(0, 2):
        device.touch(384, 978, MonkeyDevice.DOWN_AND_UP)
        time.sleep(0.5)

    # 关
    for i in xrange(0, 2):
        device.touch(120, 332, MonkeyDevice.DOWN_AND_UP)
        time.sleep(0.5)

# Takes a screenshot
#result = device.takeSnapshot()
# Writes the screenshot to a file
#result.writeToFile('/tmp/shot1.png','png')
