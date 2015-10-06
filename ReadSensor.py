#SENSE_PRO
#         ______  ______  ____     ______  ______ 
#        /  ___/ /  ___/ /    \   /  ___/ /  ___/ 
#       /  /__  /  /__  /  /\  \ /  /__  /  /__ 
#      /__   / /   __/ /  / /  //__   / /   __/
#     ___/  / /   /__ /  / /  /___/  / /   /__ 
#    /_____/ /______//__/ /__//_____/ /______/
#
#
#
#
#Auth:LeoYong
#Description:Read data from sensor
#!/usr/local/bin/python
#FIXME: add Timer function
#       compile in a vnc file

import time
import RPi.GPIO as GPIO
import csv
import matplotlib.pyplot as plt
import Plot_Test	
from drawnow import *

LDR=23
GPIO.setmode(GPIO.BCM)

class Sensor(object):
        #-----------------------construct class
        def __init__(self, Pin):
                ##Return a new Read_Data object
                self.Pin =Pin

        #---------------------Read sensor reading
        def Read_Analog(self):
                reading = 0
                #Discharge capacitor
                GPIO.setup(self.Pin, GPIO.OUT)
                GPIO.output(self.Pin, GPIO.LOW)
                time.sleep(0.1)

                GPIO.setup(self.Pin, GPIO.IN)
                #Start Count
                while(GPIO.input(self.Pin)==GPIO.LOW):
                        reading +=1

                return reading

        #------------------------Generate data CSV file 
        def CSV_Gen(self,data,f):
                dat = list()
                dat.append(data)
                wr = csv.writer(f)
                for i in range(len(dat)):

                        wr.writerow([dat[i]])

        #------------------Cuztomiz Plot.gplt
        def Set_Plot(self,sensor):
                Pltf1 = open("Plot_Test",'r').read()
                Pltf2 = open("Plot.gplt",'w')
                m = Pltf1.replace("@sensor",sensor)
                Pltf2.write(m)

        #------------------PLot Graph       
        def Plot_Dat(self):
                print "Plot data"
            
light = Sensor(LDR)
light.Set_Plot(str("Light"))#---HARD CODE

with open('data/Light.csv','wb') as DataFile:
        #----------Main Loop<this will not be an infinity loop FIXME>
        while True:
                data = light.Read_Analog() #Read fron the LDR
                print data
                light.CSV_Gen(data,DataFile)
                light.Plot_Dat()
