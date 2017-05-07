import urllib2
import time

class Slack:
    def __init__(self):
        print "slack init"
        return None

    def sendMsg(self, msg, announce):
        print "send"
        tok = "xoxb-27486101313-45eVdQkiZBxURIW4Kx8HWBEe"
        chan = "dev"
        #chan = "denver"
        botname = "furbot"
        icon = "http://dmc-inet.azurewebsites.net/uploads/furbot3.png"
        message = ""

        if(announce != 0):
            message = "<!here|humans>%20" + msg
        else:
            message = msg
        
        message = message.replace(" ", "%20")
        
        url = "https://slack.com/api/chat.postMessage?token=" + tok + "&channel=%23" + chan + "&text=" + message + "&username=" + botname + "&icon_url=" + icon + "&pretty=1"
        urllib2.urlopen(url)
