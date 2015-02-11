# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

w = 854
h = 480

while True:
    for wi in xrange(10, w, w/5):
        for hi in xrange(10, h, w/10):
            device.touch(wi, hi, MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot
#result = device.takeSnapshot()
# Writes the screenshot to a file
#result.writeToFile('/tmp/shot1.png','png')
