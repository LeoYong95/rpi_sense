#!/usr/local/bin/python
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
#Auth: LeoYong
#Reference: Sentdex youtube channel
#Description: Sensor Class
#FIXME: add Timer function or data limit
#       add generate CSV file function

#----------Imports
import time
import RPi.GPIO as GPIO
import csv

#-----Global
LDR=23
GPIO.setmode(GPIO.BCM) 
SenseDat=[]


class Sensor(object):
        
        def __init__(self, Pin):
                self.Pin=Pin

        #---------------------Read sensor reading
        def Read_Analog(self):
                reading=0
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



