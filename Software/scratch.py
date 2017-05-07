#import numpy
import helper
import slack

slack = slack.Slack()

helper = helper.Helper()

print helper.intToBytes(-200)

#sideBrush, Vacuum, mainBrush, sideClock, mainClock)
print helper.bitMotors(1,0,1,1,0)

slack.sendMsg("hi", 0)
slack.sendMsg("ANNOUNCEMENT", 1)

