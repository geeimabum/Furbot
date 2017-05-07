import chariot
import time
import struct

chariot = chariot.Chariot('/dev/ttyUSB0')
chariot.start()
chariot.fullMode()
##chariot.reset()
##time.sleep(2)
##chariot.readResponse(300)
##x = 10
##
##while (x > 0):
##    resp = chariot.getBumpsAndWheelDrops()
##    print resp
##    time.sleep(.2)
##    x -= 1

chariot.getAllData()
##chariot.drive(-100,0)
##time.sleep(1)
##chariot.getAllData()
chariot.stop()
##chariot.reset()
chariot.ser.close()
##chariot.drive(-100,0)
##time.sleep(1)
##chariot.driveDirect(300,0)
##time.sleep(1)
##chariot.seekDock()
##time.sleep(1)
##chariot.stop()

##chariot.saveSongs()
##time.sleep(1)
##chariot.playSong(1)
##
##ohno = [173,0,0,0]
##on = [128]
####(128,0,0,0,0,0)
##off = [173,0,173]
####(173,0)
##full = [132]
##led = [139,15,0,255]
##drive = [137,255,56,0,244]
##
##
##
#####reset
####chariot.sendCommand(ohno)
####time.sleep(1)
####
#####turn on
####chariot.sendCommand(on)
##chariot.start()
##time.sleep(1)
##
#####full mode
##chariot.sendCommand(full)
##time.sleep(1)
##
#####custom
##chariot.sendCommand(led)
####chariot.sendCommand(drive)
##time.sleep(1)
##
#####off
####chariot.sendCommand(off)
####chariot.sendCommand(off)
####chariot.stop()
##chariot.stop()
