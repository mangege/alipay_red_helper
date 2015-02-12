# coding: utf-8
# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

w = 720
h = 1280

raw_input("按 Enter后再按 Ctrl+D 后开始乱点")
print('go')

while True:
    for wi in xrange(100, w, w/6):
        for hi in xrange(100, h, h/11):
            device.touch(wi, hi, MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot
#result = device.takeSnapshot()
# Writes the screenshot to a file
#result.writeToFile('/tmp/shot1.png','png')
