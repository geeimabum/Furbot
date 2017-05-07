#import numpy
import helper
import slack

slack = slack.Slack()

helper = helper.Helper()

print helper.intToBytes(-200)

slack.sendMsg("hi", 0)
slack.sendMsg("ANNOUNCEMENT", 1)

