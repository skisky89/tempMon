#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Temp Sensor reading
import time


c = 0
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
    print (temperaturecf , " F")   #InsideNear=C
    print (temperatureaf , " F")   #InsideFar =A
    print (temperaturebf , " F")   #Outside   =B

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
    time.sleep(600)
    



