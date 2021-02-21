# some initial things to import
import os
import csv

# numpy and curve_fit
import numpy as np
from scipy.optimize import curve_fit

# for plotting
import matplotlib as mpl
import matplotlib.pyplot as plt

################################
##### Loading Data         #####
################################

def load_data(folder):
    # list of lists of lateral distances
    distlistlist=[]

    # list of lists of counts
    countlistlist=[]

    # list of angles
    anglist=[]

    k=0
    for file in os.listdir(folder):
        if file.endswith(".dat"):

            # extract the angle from the file name
            namelist=file.split()
            degtext=namelist[4].split("_")
            degrees=float(degtext[0])+float(degtext[1])/10


            file=os.path.join(folder,file)
            with open(file, 'r') as f:
                reader = csv.reader(f, delimiter='\t')
                distlist=[]
                countlist=[]

                # grab the counts and distance from each row
                i=0
                for row in reader:
                    if i>0:
                        countlist.append(float(row[1]))
                        distlist.append(float(row[0]))
                    i=i+1

            # append the dist and count lists to the list of lists
            distlistlist.append(distlist)
            countlistlist.append(countlist)

            # append the angle to the list of angles
            anglist.append(np.abs(degrees))

            k=k+1
            
    # Computing the range, and step in lateral distance
    mind=float(min(distlist))
    maxd=float(max(distlist))
    if (np.size(distlist) > 1):
        dint=float(distlist[1]-distlist[0])
    else:
        dint = 0

    # sorting the angle and list of count lists by increasing angle
    anglist,countlistlist=zip(*sorted(zip(anglist,countlistlist)))
    
    # returns list of count lists, list of distance lists, angles, minimum and maximum distances, 
    #  and the distance step interval
    return countlistlist, distlistlist, anglist, mind, maxd, dint