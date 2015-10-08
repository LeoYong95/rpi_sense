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
#Description:Plot a graph based on data given
#!/usr/local/bin/python
#FIXME: 
#    
from pylab import plotfile, show,gca
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *

data = list()
plt.ion()

def read_datafile(filename):
        data= np.loadtxt(filename,delimiter=',')
        return data

        
def Plot_Dat():
        plt.plot(data)


while True:
        data=read_datafile('data/Light.csv')
        drawnow(Plot_Dat)


