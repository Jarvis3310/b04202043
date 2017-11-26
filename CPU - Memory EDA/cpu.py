# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:38:46 2017

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
    
file = open(pathProg + '\\cpu_data.csv', 'r')
csvCursor = csv.reader(file)
MMM=157402

trans=[]
cpu=[]
count=[]
five=[]
ff=[]
tt=[]
for row in csvCursor:
    cpu.append(row)
    
print(cpu[0])
   
#print (cpu[0][0])
x=MMM
for j in range(x):
    if j%900==0 and j<x-900:
        for i in range (j,j+10):
             count.append(cpu[i][1])
        five.append(max(count))
        count=[]
    
''' 
for j in range(int(x/10)):
    if j%10==0 and j<x:
        for i in range (j,j+10):
             count.append(five[i])
        ff.append(max(count))
        count=[]
        
for j in range(int(x/100)):
    if j%10==0 and j<x:
        for i in range (j,j+10):
             count.append(five[i])
        tt.append(max(count))
        count=[]
'''        
#print(five)
'''
file1 = open(pathProg + '\\cpuuse_A_max.csv', 'w',newline='')
csvCursor1 = csv.writer(file1)
#file1.write("%f"%(2.344))
for i in range(int(x/900)):
    csvHeader = [five[i]]
    csvCursor1.writerow(csvHeader)



file1.close()
'''

    
for i in range(len(five)):
    tt.append(float(five[i]))
avg=average(tt)
for i in range(len(five)):
    ff.append((tt[i]-avg)**2)
std=(average(ff))**0.5    
print(five[0])
print(float(five[0]))
print(avg)
print(std)

for i in range(len(tt)):
    if tt[i]>=avg+2*std:
        trans.append(2)
    elif tt[i]>=avg+std:
        trans.append(1)
    elif tt[i]>=avg-std:
        trans.append(0)
    elif tt[i]>=avg-2*std:
        trans.append(-1)
    else:
        trans.append(-2)
print(trans)
        
        
#print (cpu[0][0])
x=len(tt)


file1 = open(pathProg + '\\cpughz_A_max100.csv', 'w',newline='')
csvCursor1 = csv.writer(file1)
#file1.write("%f"%(2.344))
for i in range(int(x)):
    csvHeader = [trans[i]]
    csvCursor1.writerow(csvHeader)



file1.close()
file.close()














