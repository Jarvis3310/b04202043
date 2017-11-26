# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:59:10 2017

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

cpu=[]
MMM=900000   
file = open(pathProg + '\\cpus.csv', 'r')
csvCursor = csv.reader(file)

for row in csvCursor:
    cpu.append(row)
    
x=len(cpu)    
print(cpu[0])

f = open("cpu_data.csv","w",newline='')
w = csv.writer(f)


for i in range(MMM):
    if cpu[i][0]=='a-957043145-UserCluster1-sysadmin':
        csvHeader = [cpu[i][1],cpu[i][3],cpu[i][4]]
        w.writerow(csvHeader)
'''    
for j in range(x):
    if j%900==0 and j<x-900:
        csvHeader = cpu[j]
        w.writerow(csvHeader)
'''        
f.close()


file.close    