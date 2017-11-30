# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:00:50 2017

@author: 林亦盛
"""

import csv
import os
import sys
num=0
pathProg = 'C:\\Users\\林亦盛\\Downloads\\UtilizationDataLog'
os.chdir(pathProg)
if os.getcwd() != pathProg:
    print ("EEROR: the file path incorrect.")
    sys.exit()

def average(s):
    return sum(s)/ len(s)
    
file = open(pathProg + '\\memA.csv', 'r')
csvCursor = csv.reader(file)

Data=[]
trans=[]
for row in csvCursor:
    Data.append(row)
####################################
def search_max (length,R,data):
    count=[]
    ff=[]
    for j in range(length):
        if j%R==0 and j<length-R:
            for i in range (j,j+R):
                count.append(data[i][1])
            ff.append(max(count))                                  ######  max or min
            count=[]
    return ff        
#####################################
def stdev(five):
    tt=[]
    ff=[]
    gg=[]
    
    for i in range(len(five)):
        tt.append(float(five[i]))
        avg=average(tt)                             ########be careful
    for i in range(len(tt)):        
        ff.append((tt[i]-avg)**2)
    std=(average(ff))**0.5     
    for i in range(len(tt)):
        if tt[i]>=avg+2*std:
            gg.append(2)
        elif tt[i]>=avg+std:
            gg.append(1)
        elif tt[i]>=avg-std:
            gg.append(0)
        elif tt[i]>=avg-2*std:
            gg.append(-1)
        else:
            gg.append(-2)
    return gg            
      
######################################    
    
file.close()
c=[1,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]


trans=search_max(len(Data),300,Data)
print(trans)
trans=stdev(trans)
print(trans)

file1 = open(pathProg + '\\mem_A_maxnew.csv', 'w',newline='')     ### max or min
csvCursor1 = csv.writer(file1)
#file1.write("%f"%(2.344))
for i in range(len(trans)):
    csvHeader = [trans[i]]
    csvCursor1.writerow(csvHeader)



file1.close()