# -*- coding: utf-8 -*-
"""
Title: graph made for the percentage which predict population of the Chinese in the Vietnamese and Japanese 
Date: 2023-04-28
Author: Shijie Niu
Discription:
    This program will output the graph of the distance
List of functions:
    No function
List of 'non-standard' modules:
    No non-standard modules in this program.
Procedure:
    1. Read the lines in the file.
    2. choose the data in the Vietnames and Japanese 
    3. filter the predict populations and the same of the actual and predict population in the Vietnames and Japanese, and divide them into two different groups
    4. make the graph
Usage: python fig3.py output_python.txt
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
f1=open('output_python.txt','r')
'''
count_diff=0 #The create a count variable for predict population which is Chinese in Vietnamese and Japannese
count_same=0 #The create a count variable for predict population and actual population in Vietnamese and Japannese
count_total=0 #The create a count variable for all actual population in Vietnamese and Japannese
for line in f1: #a loop to read each line in file
    record_list=line.replace('\n', '').split('\t') #make a list for each line and remove the '\n'
    if record_list[0]=='Japan' or record_list[0] == 'Vietnamese': #if the actual population is Japanese and Vietnamese
        record_list[3]=record_list[3].rstrip('0123456789_') #remove the digit and '_' in predict population
        if record_list[0]==record_list[3]: #if actual population and predict population is same
            count_same+=1 #count variable plus one
        elif record_list[3]=='Chinese': #if the predict population is Chinese
            count_diff+=1 #count variable plus one
        count_total+=1 #total count variable plus one
X=[count_same,count_diff] #make a list to store the two different counts
labels=['Jap or Viet','Chinese'] #make a list to store the labels in the graph
plt.figure(figsize=(6,4),dpi=1000) #set the parameters of graph
plt.pie(X,labels=labels, autopct='%1.2f%%')  #make pie graph

plt.savefig('fig3.png', pad_inches=0.1, dpi=1000) #save the pie graph
#print(count_diff,count_same,count_total)
    