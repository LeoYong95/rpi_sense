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
from drawnow import *

LDR=23
GPIO.setmode(GPIO.BCM)
plt.ion()
SenseDat=[]
cnt=0

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

#---------------------------Plot Data
def Plot_Dat():
        plt.plot(SenseDat,'ro-')


light = Sensor(LDR)

with open('data/Light.csv','wb') as DataFile:
        #----------Main Loop<this will not be an infinity loop FIXME>

   while True:
        data = light.Read_Analog() #Read fron the LDR
        print data
        SenseDat.append(data)
        light.CSV_Gen(data,DataFile)
   #    drawnow(Plot_Dat)
   #    plt.pause(.000001)
   #    cnt=cnt+1
   #    if(cnt>25):
   #            SenseDat.pop(0)

