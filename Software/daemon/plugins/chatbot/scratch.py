#import numpy
import chariot as c
import time



def sing():
    print "singing"
    chariot = c.Chariot('/dev/ttyUSB0')
    chariot.stop()
    time.sleep(1)
    chariot.start()
    time.sleep(1)
    chariot.fullMode()
    time.sleep(1)
    chariot.saveSongs()
    time.sleep(1)
    chariot.playSong(2)
    time.sleep(5)
    chariot.stop()

