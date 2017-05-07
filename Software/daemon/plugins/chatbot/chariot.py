import time
import serial
import struct
import helper

##--------------Chariot Class---------------
class Chariot:
    def __init__(self, port):
        print "init"
        self.connect(port)

##--------------Communication---------------
## Connect over serial    
    def connect(self, port):
        try:
            self.ser = serial.Serial(
            port=port,
            baudrate=115200,
            #parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS
            )
        except serial.SerialException:
            print("The chariot is not listening!")

## Send command over serial connection
    def sendCommand(self, command):
        if type(command) is list:
            string = ''
            for char in command:
                string += chr(char)
            self.ser.write(string)
        else:
            print('Command needs to be of type <list>, but is actually of type <' + type(command).__name__ + '>.')


##--------------Open Interface Commands---------------
## Start listening for commands
    def start(self):
        print "start"
        print self.ser.isOpen()
        command = [128]
        self.sendCommand(command)

## Reset the robot - equivalent to removing and reinserting the battery
    def reset(self):
        command = [7]
        self.sendCommand(command)

## Stop listening for commands
    def stop(self):
        print "stop"
        command = [173,0,173]
        self.sendCommand(command)

##--------------Mode Commands---------------   
## Safe mode
    def safeMode(self):
        command = [131]
        self.sendCommand(command)

## Full mode
    def fullMode(self):
        command = [132]
        self.sendCommand(command)

## Passive mode
    def passiveMode(self):
        command = [128]
        self.sendCommand(command)

##--------------Cleaning Commands---------------       
## Clean
    def clean(self):
        command = [135]
        self.sendCommand(command)
        
## Max - runs clean cycle until battery is dead...
    def maxClean(self):
        command = [136]
        self.sendCommand(command)

## Spot
    def spot(self):
        command = [134]
        self.sendCommand(command)

## Seek Dock
    def seekDock(self):
        command = [143]
        self.sendCommand(command)

## Power down Roomba
    def powerDown(self):
        command = [133]
        self.sendCommand(command)

## Schedule
## Day: Sunday->Saturday == 0->6
## Hour: 0-23
## Minute: 0-59
    def schedule(self,day,hour,minute):
        command = [168, day, hour, minute]
        self.sendCommand(command)

##--------------Actuator Commands---------------
## Drive
    def drive(self,velocity,radius):
        command = 'todo'
        self.sendCommand(command)

## Drive Direct - set velocity for each wheel independently
    def driveDirect(self,velocityRight,velocityLeft):
        command = 'todo'
        self.sendCommand(command)

## Drive PWM - set PWM for each wheel independently
    def drivePWM(self,pwmRight,pwmLeft):
        command = 'todo'
        self.sendCommand(command)

## Motors
    

##--------------Music Commands---------------
## Save Songs
    def saveSongs(self):
        #imperial march opening
        command = [140,1,9,52,32,52,32,52,32,48,16,55,8,52,32,48,16,55,8,52,64]
        self.sendCommand(command)
        #mario
        command = [140,2,12,64,8,64,8,10,8,64,8,10,8,60,8,64,8,10,8,67,8,10,8,10,16,55,8]
        self.sendCommand(command)

## Play Songs
    def playSong(self,number):
        if number == 1:
            command = [141, 1]
        else:
            command = [141, 2]
        self.sendCommand(command)
