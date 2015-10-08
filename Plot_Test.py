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
import matplotlib.cbook as cbook

fname = 'data/Light.csv'

def Plot_Dat():
        plotfile(fname)
        #show()


while True:
        Plot_Dat()


