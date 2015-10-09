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
#FIXME: Configure Plot here
#    
import matplotlib.pyplot as plt
from drawnow import *

plt.ion()

def Plot_Dat(data):
        plt.plot(data)


#while True:
#        drawnow(Plot_Dat)


