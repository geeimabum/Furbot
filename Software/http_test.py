import urllib2
import json
import time

message = "<!here|humans>%20slack%20test"
#Slack API tester
#tok = "xoxp-3594134292-7713583937-24243203685-bdb3126d5a"
#phpbot tok
tok = "xoxb-27486101313-45eVdQkiZBxURIW4Kx8HWBEe"
chan = "dev"
GET = ""
icon = "http://dmc-inet.azurewebsites.net/uploads/furbot3.png"
#botname = "phpbot"
botname = "furbot"


#url = "https://slack.com/api/chat.postMessage?token=" + tok + "&channel=%23" + chan + "&text=" + message + "&username=" + botname + "&icon_url=" + icon + "&pretty=1"
#urllib2.urlopen(url)


#http://[HOST]:3872/cmd/[NAME]
#idle
req = urllib2.Request('http://localhost:3872/cmd/setidle')
req.add_header('Content-Type', 'application/json')

data = {"params":{"idle":"1"}}

response = urllib2.urlopen(req, json.dumps(data))
time.sleep(1)


#antenna
req = urllib2.Request('http://localhost:3872/cmd/antenna')
req.add_header('Content-Type', 'application/json')

data = {"params":{"red":"0","green":"255","blue":"0"}}

response = urllib2.urlopen(req, json.dumps(data))
time.sleep(1)


###lcd
req = urllib2.Request('http://localhost:3872/cmd/lcd')
req.add_header('Content-Type', 'application/json')

data = {"params":{"state":"1"}}

response = urllib2.urlopen(req, json.dumps(data))
time.sleep(1)
