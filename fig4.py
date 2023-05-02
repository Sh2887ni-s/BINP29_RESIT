# -*- coding: utf-8 -*-
"""
Title: graph made for the distance 
Date: 2023-04-28
Author: Shijie Niu
Discription:
    This program will output the graph of the percentage of each distance groups
List of functions:
    No function
List of 'non-standard' modules:
    No non-standard modules in this program.
Procedure:
    1. Read the lines in the file.
    2. choose the distance record 
    3. filter the record
    4. make the graph
Usage: python fig4.py comparing.txt
"""
import matplotlib.pyplot as plt #plt to make the graph
import sys #import sys
import os

close_file=sys.argv[1] 
#%%

if os.path.isfile(close_file) == False: # if the path of file is not contain in the folder
    print('Please check the file names') #print 'Please check the file names'
    sys.exit() #stop the script
#%%
f1=open(close_file,'r')#open file
'''
f1=open('comparing.txt','r')
'''
distance=[] #make a list to store the distance data
for line in f1: #a loop to read each line in file
    if line.startswith('Population')==False: #don't read the header line
        record_list=line.replace('\n', '').split('\t') #make a list for each line and remove the '\n'
    
        distance.append(record_list[2]) #store the distance data in the list
close=0 #creat a count variable for the close group
middle=0 #creat a count variable for the middle group
far=0 #creat a count variable for the far group
very_far=0 #creat a count variable for the very far group
for distance_in_each_record in distance: # a loop read each element in the distance list
    if float(distance_in_each_record)<=2000: # distance<=2000
        close+=1 #close count plus one
    elif float(distance_in_each_record)>2000 and float(distance_in_each_record)<=5000: # 2000<distance<=5000
        middle+=1 #middle count plus one
    elif float(distance_in_each_record)>5000 and float(distance_in_each_record)<=10000: # 5000<distance<=10000
        far+=1 #far count plus one
    else: #else
        very_far+=1 #very far count plus one
X=[close,very_far,middle,far] #make a list to store the four different counts
labels=['Close distance','Very far distance','Middle distance','Far distance'] #make a list to store the labels in the graph
plt.figure(figsize=(10,8),dpi=1000) #set the parameters of graph
plt.pie(X, labels=labels, autopct='%1.2f%%') #make pie graph
plt.savefig('fig4.png',bbox_inches='tight', pad_inches=0.1, dpi=1000) #save the pie graph
#print(close, middle,far,very_far)