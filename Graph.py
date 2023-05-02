# -*- coding: utf-8 -*-
"""
Title: graph made for the distance 
Date: 2023-03-10
Author: Shijie Niu
Discription:
    This program will output the graph of the distance
List of functions:
    No function
List of 'non-standard' modules:
    No non-standard modules in this program.
Procedure:
    1. Read the lines in the file.
    2. choose the distance record 
    3. filter the record
    4. make the graph
Usage: python Graph.py close_file.txt
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
f1=open('close_file.txt','r')#open file
'''
distance=[] #creat a list to store distance data
distance_range=['0-25', '25-50','50-75','75-100','100-200','larger than 200']#creat a list to stroe the catalogs of the graph
for line in f1: #loop for collect the distance data from file
    if line.startswith('Population') ==False: #don't read the header line
        line=line.strip('\n') #remove the ''\n' in each line
        infor=line.split('\t') #cut the information by tab
        distance.append(float(infor[6])) #store the distance data in the list
plt.rcParams['font.sans-serif'] = ['Calibri'] #set the type of the word in graph
plt.rcParams['axes.unicode_minus'] = False 
distance.sort() #sort the list
#print(max(distance))
#print(min(distance))
very_close=[]#0-25
close=[]#25-50
midium=[]#50-75
far=[]#75-100
very_far=[]#100-200
others=[]#200+
for i in distance: #loop to collect the distance data by range
    if i >=0 and i<=25: # 0<=distance<=25
        very_close.append(i)
    elif i>25 and i<=50:  # 25<distance<=50
        close.append(i)
    elif i >50 and i<=75: # 50<distance<=75
        midium.append(i)
    elif i>75 and i<=100: # 75<distance<=100
        far.append(i)
    elif i>100 and i<=200: ## 100<distance<=200
        very_far.append(i)
    elif i>200: # 200<distance
        others.append(i)
distance_num=[len(very_close),len(close),len(midium),len(far),len(very_far),len(others)] #put the number of each distange range in the same list
fig=plt.figure(figsize=(6,4),dpi=1000) #set the figue size

plt.bar(distance_range, distance_num,color='rgb') # make the graph
for a,b in zip(distance_range, distance_num): #loop to make the text in the graph
    plt.text(a,b, b, ha='center', va='bottom', ) #set the text int the graph
plt.savefig('fig1.png', pad_inches=0.1, dpi=1000) #save the pie graph
f1.close() #file close