#import ping
#import weather
import time
import slack as s
import chariot as c
import scratch

# Custom function calls that fall outside of main bot response AI
def response(response, var1):
##  slack = slack.Slack()
##  chariot = chariot.Chariot('/dev/ttyUSB0')
##  chariot.start()
##  chariot.fullMode()
##  chariot.saveSongs()
##  time.sleep(1)

  print response

  if response == 'status sp':
    return response
##    return ping.test(0)

  elif response == 'talk':
    print "external slack call"
    slack = s.Slack()
    time.sleep(1)
    slack.sendMsg("no", 0)
    response = "blank"
    return response

  elif response == 'sing 1':
    print "sing"
    chariot = c.Chariot('/dev/ttyUSB0')
    chariot.start()
    time.sleep(1)
    chariot.fullMode()
    time.sleep(1)
    chariot.saveSongs()
    time.sleep(1)
    chariot.playSong(1)
    time.sleep(1)
    chariot.stop()

  elif response == 'sing 2':
    print "sing"
    chariot = c.Chariot('/dev/ttyUSB0')
    chariot.start()
    time.sleep(1)
    chariot.fullMode()
    time.sleep(1)
    chariot.saveSongs()
    time.sleep(1)
    chariot.playSong(2)
    time.sleep(1)
    chariot.stop()

  elif 'scratch' in response:
    scratch.sing()
    response = "done"
    return response
##  elif 'weather' in response:
##    if 'forecast' in response:
##      return weather.forecast(response)
##    else:
##      return weather.check(response)
  elif 'sleep' in response:
    return sleep()

  #check for user tag to include user in response
  else:
    if '%user' in response:
      response = response.replace('%user', var1)
    else:
      response = response
    return response
    
def sleep():
  time = time.time() + 300
  return "I'll be back at " + time
