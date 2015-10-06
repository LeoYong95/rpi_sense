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

import matplotlib.pyplot as plt

def Plot_Dat(data , name)
        plt.title( name + ' SENSOR')
        plt.ylim(0,1300)
        plt.grid(True)
        plt.ylabel(name)
        plt.plot(data,'ro-', label= name)
        
        
