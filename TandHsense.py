
#!/usr/bin/python
import time
import sleep
import sys
sys.path.append("/root/Adafruit_Python_DHT")
import RPi.GPIO as GPIO
import os
import Adafruit_DHT
import urllib


#Setup DHT pins
RCpin = 24  #LightSensor
DHTpin = 23  #Humidity

#Setup our API and delay
myAPI = "F0PV3WXX7OJH5FVT"
myDelay = 30 #how many seconds between posting data to Thingspeak

GPIO.setmode(GPIO.BCM)
GPIO.setup(RCpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Functions
def getSensorData():
    RHW, TW = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
    
    #Convert from Celius to Farenheit
    TWF = 9/5*TW+32
   
    # return dict
    return (str(RHW), str(TW),str(TWF))

def RCtime(RCpin):
    LT = 0
    
    if (GPIO.input(RCpin) == True):
        LT += 1
    return (str(LT))


#Thingspeak
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
def RCtime(RCpin):
    LT = 0
    
    if (GPIO.input(RCpin) == True):
        LT += 1
    return (str(LT))

    while True:
            try:
                RHW, TW, TWF = getSensorData()
                LT = RCtime(RCpin)
                f = urllib2.urlopen(baseURL + 
                                "&field1=%s&field2=%s&field3=%s" % (TW, TWF, RHW)+
                                "&field4=%s" % (LT))
            print(f.read())
            print(TW + " " + TWF+ " " + RHW + " " + LT)
            f.close()
            

            sleep(int(myDelay))


#Main function
c = 0   #Keeps polling in infinite loop
while (c < 1):
    #5 mintute polling
    time1 = time.strftime("%I:%M:%S:- %m/%d/%Y")
    time1 = str(time1)
    timelog = str(time.strftime("%m%d%Y.txt"))
    
    
#open sensor files (plug-&-play-driver created)
    filea = open("/sys/bus/w1/devices/28-800000280af5/w1_slave")
    fileb = open("/sys/bus/w1/devices/28-800000280ea3/w1_slave")
    filec = open("/sys/bus/w1/devices/28-800000281298/w1_slave")

#Read in temp data
    tempa = filea.read()
    filea.close()
    tempb = fileb.read()
    fileb.close()
    tempc = filec.read()
    filec.close()

#Format data
    secondlinea = tempa.split("\n")[1]
    secondlineb = tempb.split("\n")[1]
    secondlinec = tempc.split("\n")[1]

    temperaturedataa = secondlinea.split(" ")[9]
    temperaturedatab = secondlineb.split(" ")[9]
    temperaturedatac = secondlinec.split(" ")[9]

    temperaturea = float(temperaturedataa[2:])
    temperatureb = float(temperaturedatab[2:])
    temperaturec = float(temperaturedatac[2:])

    temperaturea = temperaturea/1000
    temperatureaf = round(temperaturea * 1.8 + 32, 2)
    temperatureb = temperatureb/1000
    temperaturebf = round(temperatureb * 1.8 + 32, 2)
    temperaturec = temperaturec/1000
    temperaturecf = round(temperaturec * 1.8 + 32, 2)

    print (time1)
    print (temperaturecf , " F")   #InsideNear = C
    print (temperatureaf , " F")   #InsideFar  = A
    print (temperaturebf , " F")   #Outside    = B

#Convert to string
    temperaturecf = str(temperaturecf)
    temperatureaf = str(temperatureaf)
    temperaturebf = str(temperaturebf)

#Write to file
    fileOut = open("/var/www/html/check.txt", "w")
    fileOut.write(temperaturecf)
    fileOut.write("\n")
    fileOut.write(temperatureaf)
    fileOut.write("\n")
    fileOut.write(temperaturebf)
    fileOut.write("\n")
    fileOut.close()

#Write to log
    log = open( timelog,"a")
    log.write(time1)
    log.write("\n")
    log.write(temperaturecf)
    log.write("\n")
    log.write(temperatureaf)
    log.write("\n")
    log.write(temperaturebf)
    log.write("\n")
    log.close()
    time.sleep(598)
    



