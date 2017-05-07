import random
import time

import phpbot
import users

crontable = []
outputs = []

sleeping = False
sleepstart = 0


#def process_reaction_added(data):
#  user = users.get(data)
    
#  #Always sends to reaction_added case
#  if 'U0TEA2Z97' in data['item_user']:
#    outputs.append([data['item']['channel'], "{}".format(phpbot.respond(data['type'], user)) ])


def process_message(data):
  # Sleep for a bit before replying; you'll seem more real this way
  time.sleep(random.randint(0,9) *.2)

  user = users.get(data)
  
  global sleeping
  global sleepstart
   
   
  #Respond if directly mentioned, is an @channel or if 'php' is in the message
  if sleeping == True:
    currentTime = (time.time() - sleepstart)
    #print currentTime
    if currentTime > 900:
      sleeping = False
      #print "done sleeping"
      if '<@U0TEA2Z97>' in data['text']:
        outputs.append([data['channel'], "{}".format(phpbot.respond(data['text'], user)) ])
      #elif '<!channel>' in data['text']:
      #  outputs.append([data['channel'], "{}".format(phpbot.respond(data['text'], user)) ])
      elif 'fur' in data['text']:
        outputs.append([data['channel'], "{}".format(phpbot.respond(data['text'], user)) ])
    else:
      nothing = 'nothing'
  elif 'quiet' in data['text']:
    #print "sleeping"
    sleeping = True
    sleepstart = time.time()
  #outputs.append([data['channel'], "{}".format(phpbot.respond(data['text'], user)) ])
  #print sleepstart
  # elif '<@U0TEA2Z97>' in data['text']:
  #   print "hello"
  #   outputs.append([data['channel'], "{}".format(phpbot.respond(data['text'], user)) ])
  #elif '<!channel>' in data['text']:
  #  outputs.append([data['channel'], "{}".format(phpbot.respond(data['text'], user)) ])
  elif 'fur' in data['text']:
    print "furby"
    dummy = phpbot.respond(data['text'], user)
  #  outputs.append([data['channel'], "{}".format(phpbot.respond(data['text'], user)) ])
  #elif ':8ball:' in data['text']:
  #  outputs.append([data['channel'], "{}".format(phpbot.respond(data['text'], user)) ])
  else:
    bs = 'bs'