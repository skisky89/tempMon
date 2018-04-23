#!/usr/bin/python
import time
import sys
#sys.path.append("/root/Adafruit_Python_DHT")
import RPi.GPIO as GPIO
import os
#import Adafruit_DHT
import urllib
c = 0
tempAC = str(72)

###Setup DHT pins
##RCpin = 24  #LightSensor
##DHTpin = 23  #Humidity

##GPIO.setmode(GPIO.BCM)
##GPIO.setup(RCpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

###Functions
##def getSensorData():
##    RHW, TW = Adafruit_DHT.read_retrypart(Adafruit_DHT.DHT11, DHTpin)
##    
##    #Convert from Celius to Farenheit
##    TWF = 9/5*TW+32
##   
##    # return dict
##    return (str(RHW), str(TW),str(TWF))
##
##def RCtime(RCpin):
##    LT = 0
##    
##    if (GPIO.input(RCpin) == True):
##        LT += 1
##    return (str(LT))   

#########################################################Functions
def timeStr():
    time1 = time.strftime("%m/%d/%Y %I:%M:%S")
    time1 = str(time1)
    timelog = str(time.strftime("%m%d%Y.txt"))
    time2 = time.strftime("%m/%d/%Y %I:%M:%S")
    time2= str(time2)
    print (time1)
    return (time1,time2,timelog )

#open sensor files (plug-&-play-driver created)
def rAndr():
    error = 0
    filea = open("/sys/bus/w1/devices/28-800000280af5/w1_slave")
    #fileb = open("/sys/bus/w1/devices/28-800000280ea3/w1_slave")
    filec = open("/sys/bus/w1/devices/28-800000281298/w1_slave")
    tempa = filea.read()
    filea.close()
    #tempb = fileb.read()
    #fileb.close()
    tempc = filec.read()

#Formatting
    secondlinea = tempa.split("\n")[1]
    #secondlineb = tempb.split("\n")[1]
    secondlinec = tempc.split("\n")[1]

    temperaturedataa = secondlinea.split(" ")[9]
    #temperaturedatab = secondlineb.split(" ")[9]
    temperaturedatac = secondlinec.split(" ")[9]

    temperaturea = float(temperaturedataa[2:])
    #temperatureb = float(temperaturedatab[2:])
    temperaturec = float(temperaturedatac[2:])
    if temperaturea == 85000:
        error = 1
    if temperaturec == 85000:
        error = 1
    temperaturea = temperaturea/1000
    temperatureaf = round(temperaturea * 1.8 + 32, 1)
    #temperatureb = temperatureb/1000
    #temperaturebf = round(temperatureb * 1.8 + 32, 1)
    temperaturec = temperaturec/1000
    temperaturecf = round(temperaturec * 1.8 + 32, 1)
    if error == 1:
        rAndr('Bad sensor read, the sensor data needs to be flushed or is not recieving enough power')
    temperaturecf = str(temperaturecf)
    temperatureaf = str(temperatureaf)
    #temperaturebf = str(temperaturebf)
    return (temperatureaf,temperaturecf)

def printit(temperatureaf, temperaturecf):
    print ('Inside: ', temperatureaf, "F" )  #InsideFar  = A
    print ("Outside: ", temperaturecf, "F")  #outside    = C
    print ("Set:" ,tempAC )
    #print (temperaturebf , " F")  #Inside     = B

def tofile(temperatureaf, temperaturecf):
    fileOut = open("/var/www/html/check.txt", "w")
    fileOut.write(temperatureaf)
    fileOut.write("\n")
    fileOut.write(temperaturecf)
    fileOut.write("\n")
    #fileOut.write(temperaturebf)
    #fileOut.write("\n")
    
    fileOut.write(tempAC)
    fileOut.close()
    
def tolog(datetime,temperatureaf, temperaturecf, timelog):
    log = open( timelog,"a")
    log.write("")
    log.write(time2)
    log.write(",")
    log.write(temperatureaf)
    log.write(",")
    log.write(temperaturecf)
    log.write(",")
    log.write(tempAC)
    #log.write(temperaturebf)
    log.write("\n")
    log.close()

############################################################Main function                

#Can't stop won't stop
    
while (c < 1):
#try:
    c = 0
    datetime, time2, timelog = timeStr()
    temperatureaf,temperaturecf = rAndr()
    printit(temperatureaf,temperaturecf)
    tofile(temperatureaf,temperaturecf)
    tolog(datetime,temperatureaf,temperaturecf, timelog)

    #10 mintute polling
    time.sleep(597)

#except:
#    print ("Safely terminating routine")
#    break
#
