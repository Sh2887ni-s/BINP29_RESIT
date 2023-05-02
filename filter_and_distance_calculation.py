#!/bin/usr/env python3
"""
Title: Geographic population structure
Date: 2022-03-21
Author: Shijie Niu
Discription:
    This program will output the record that the population and predict is different and calculate the distance based on lat and lon.
List of functions:
    1. haversine: calculate the distance based on lat and lon
List of 'non-standard' modules:
    No non-standard modules in this program.
Procedure:
    1. Read the lines in the file.
    2. choose the record that population and prediction is different
    3. calculate the distance based on the lon and lat between the population and prediction
Usage: python filter_and_distance_calculation.py output_python.txt comparing.txt geo.csv
"""
from math import radians , cos, sin, asin, sqrt #import the math calculate method
def haversine(lat1,lat2,lon1,lon2):#define a 
    lon1,lat1,lon2,lat2 = map(radians, [lon1,lat1,lon2,lat2])#change the lon and lat to the radians
    #calculate the distance
    dlon=lon2-lon1
    dlat=lat2-lat1
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*asin(sqrt(a))
    r=6371
    return c*r
import sys
import os
Input_file=sys.argv[1]
Output_file=sys.argv[2]
geo_file=sys[3]
#%%
if os.path.isfile(Input_file) == False: # if the path of file is not contain in the folder
    print('Please check the file names') #print 'Please check the file names'
    sys.exit() #stop the script
elif os.path.isfile(geo_file) == False: # if the path of file is not contain in the folder
    print('Please check the file names') #print 'Please check the file names'
    sys.exit() #stop the script
#%%
f1=open(Input_file,'r')#open file
f2=open(Output_file,'w')#open file
f2.write('Population'+'\t'+'Prediction'+'\t'+'Distance'+'\n')#write theheader in outputfile 
f3=open(geo_file,'r')#open file
file=f3.readlines()#read files
list1=['0','1','2','3','4','5','6','7','8','9']#list for delete the number in population file
pred_popu=''#creat a string
#loop for prepare the population name and predict name and predict lon and lat
for line in f1:
    line1=line.split('\t')
    if line1[0]!='Population':
        pred_popu=line1[3].replace('_', '') #delete _ from name
        popu=line1[0]
        line1[0]=line1[0].replace('_', '') #delete _ from name
        line1[4]=line1[4].replace('[', '') #delete [ from lat
        lat1=float(line1[4].replace(']', ''))  #delete ] from lat and collect the predict lat
        line1[5]=line1[5].replace('[', '') #delete [ from lon
        line1[5]=line1[5].replace(']', '') #delete ] from lon 
        lon1=float(line1[5].replace('\n', '')) #remove the '\n' in each line and collect the predict lon
        for i in list1:
            if i in pred_popu:
                pred_popu=pred_popu.replace(i,'') #delete number from name
                #line3[0]=line3[0].replace(i, '')
                #check whether the propution name and predict name is equal
                if line1[0]!=pred_popu and line1[0]!=pred_popu.replace('s', '')and line1[0]!=pred_popu.replace('es', ''): # if the predicted name is notthe same with the pupolation name 
                    #loop for the popution name and lon and lat in GEO.csv
                    for line2 in file: #read the data in the file
                        line3=line2.split(',') #cut the information by ,
                        if line3[0]!='POPULATION':
                            line3[0]=line3[0].replace('_', '') #delete _ from name
                            lat2=float(line3[1]) #collect the predict lat
                            lon2=float(line3[2]) #collect the predict lon
                        for i in list1:
                            if i in line3[0]:
                                line3[0]=line3[0].replace(i, '')
                                #calculate the distance
                                if line1[0] == line3[0]:
                                    distance=haversine(lat1,lat2,lon1,lon2) #use the function calculate the distance
                    #print(popu+'\t'+line1[3]+'\t'+str(distance))
                    #write the population name, predicted name and distance in f2
                    f2.write(popu+'\t'+line1[3]+'\t'+str(distance)+'\n') #file write
f1.close()#close file
f2.close()#close file
f3.close()#close file
                                    
                                    
                                    
                               