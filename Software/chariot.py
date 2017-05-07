import time
import serial
import struct
import helper
import json

##--------------Chariot Class---------------
class Chariot:
    def __init__(self, port='/dev/ttyUSB0'):
        self.connect(port)
        self.helper = helper.Helper()

##--------------Communication---------------
## Connect over serial    
    def connect(self, port):
        try:
            self.ser = serial.Serial(
            port=port,
            baudrate=115200,
            #parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
            )
        except (serial.SerialException, serial.SerialTimeoutException):
            print('The chariot is not listening!')

## Send command over serial connection
    def sendCommand(self, command):
        if type(command) is list:
            string = ''
            for char in command:
                string += chr(char)
            self.ser.write(string)
        else:
            print('Command needs to be of type <list>, but is actually of type <' + type(command).__name__ + '>.')

## Read response over serial connection
    def readResponse(self, length):
        try:
            response = self.ser.read(length)
            print response
            return response
        except (serial.SerialException, serial.SerialTimeoutException):
            print('Roomba read exception')

##--------------Open Interface Commands---------------
## Start listening for commands
    def start(self):
        command = [128]
        self.sendCommand(command)
        time.sleep(0.2)

## Reset the robot - equivalent to removing and reinserting the battery
    def reset(self):
        command = [7]
        self.sendCommand(command)
        time.sleep(0.2)

## Stop listening for commands
    def stop(self):
        command = [173,0,173]
        self.sendCommand(command)
        time.sleep(0.2)

##--------------Mode Commands---------------   
## Safe mode
    def safeMode(self):
        command = [131]
        self.sendCommand(command)
        time.sleep(0.2)

## Full mode
    def fullMode(self):
        command = [132]
        self.sendCommand(command)
        time.sleep(0.2)

## Passive mode
    def passiveMode(self):
        command = [128]
        self.sendCommand(command)
        time.sleep(0.2)

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
        velBytes = self.helper.intToBytes(velocity)
        radBytes = self.helper.intToBytes(radius)
        command = [137]
        command.extend(velBytes)
        command.extend(radBytes)
        self.sendCommand(command)

## Drive Direct - set velocity for each wheel independently
    def driveDirect(self,velocityRight,velocityLeft):
        velRightBytes = self.helper.intToBytes(velocityRight)
        velLeftBytes = self.helper.intToBytes(velocityLeft)
        command = [145]
        command.extend(velRightBytes)
        command.extend(velLeftBytes)
        self.sendCommand(command)

## Drive PWM - set PWM for each wheel independently
    def drivePWM(self,pwmRight,pwmLeft):
        pwmRightBytes = self.helper.intToBytes(pwmRight)
        pwmLeftBytes = self.helper.intToBytes(pwmLeft)
        command = [146]
        command.extend(pwmRightBytes)
        command.extend(pwmLeftBytes)
        self.sendCommand(command)

## Motors
    def motors(self, sideBrush, vacuum, mainBrush, sideClock, mainClock):
        cmdByte = self.helper.bitsToByte(sideBrush, vacuum, mainBrush, sideClock, mainClock, 0, 0, 0)
        command = [138]
        command.append(cmdByte)
        self.sendCommand(command)

## PWM Motors
    def pwmMotors(self, mainBrushPWM, sideBrushPWM, vacuumPWM):
        command = [144, mainBrushPWM, sideBrushPWM, vacuumPWM]
        self.sendCommand(command)
## LEDs
    def leds(self, debris, spot, dock, checkRobot, powerColor, powerIntensity):
        cmdByte = self.helper.bitsToByte(debris, spot, dock, checkRobot, 0, 0, 0, 0)
        command = [139, cmdByte, powerColor, powerIntensity]
        self.sendCommand(command)

## Digit LEDs - ASCII
    def digitLeds(self, digit0, digit1, digit2, digit3):
        command = [164, digit3, digit2, digit1, digit0]
        self.sendCommand(command)

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
        command = [141, number]
        self.sendCommand(command)

##--------------Input Commands---------------
## Sensors
    def sensors(self, packetID, responseLength, encoding):
        command = [142, packetID]
        self.sendCommand(command)
##        response = str(self.readResponse(responseLength).decode(encoding).split())[5:-2]
        response = str(self.readResponse(responseLength).encode('Latin-1'))
        ##print response
        return response

## Query List


   

## Get all data
    def getAllData(self):
        with open('sensorData.json', 'w') as file:
            data = {'Bump&Wheels' : self.sensors(7,1,'utf-8'),
                    'Wall' : self.sensors(8,1,'utf-8'),
                    'CliffLeft' : self.sensors(9,1,'utf-8'),
                    'CliffFrontLeft' : self.sensors(10,1,'utf-8'),
                    'CliffFrontRight' : self.sensors(11,1,'utf-8'),
                    'CliffRight' : self.sensors(12,1,'utf-8'),
                    'VirtualWall' : self.sensors(13,1,'utf-8'),
                    'WheelOvercurrents' : self.sensors(14,1,'utf-8'),
                    'DirtDetect' : self.sensors(15,1,'utf-8'),
                    'UnusedByte' : self.sensors(16,1,'utf-8'),
                    'InfraredCharacterOmni' : self.sensors(17,1,'utf-8'),
                    'InfraredCharacterLeft' : self.sensors(52,1,'utf-8'),
                    'InfraredCharacterRight' : self.sensors(53,1,'utf-8'),
                    'Buttons' : self.sensors(18,1,'utf-8'),
                    'Distance' : self.sensors(19,2,'utf-16-be'),
                    'Angle' : self.sensors(20,2,'utf-16-be')


                    }
            
            json.dump(data, file)

        
        
## Bumps and Wheel Drops
    def getBumpsAndWheelDrops(self):
        response = self.sensors(7, 1)

        response = response.decode('utf-8').split()
        print "decode"
        print response
        response = str(response)
        print "str"
        print response
        response = response[5:-2]
        print "trunc"
        print response
        response = int(response)
        #num = int(response, 24)
                    
        ##print type(response)
        print "return"
        return response
    
