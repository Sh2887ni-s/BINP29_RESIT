# -*- coding: utf-8 -*-
"""
Title: test how close is the predicted data
Date: 2023-03-10
Author: Shijie Niu
Discription:
    This program will output the distance that predict location and the actually location  based on lat and lon.
List of functions:
    1. haversine: calculate the distance based on lat and lon
List of 'non-standard' modules:
    No non-standard modules in this program.
Procedure:
    1. Read the lines in the file.
    2. calculate the distance based on the lon and lat between the population and prediction
Usage: python filter__close_distance.py output_python.txt close_file.txt geo.csv
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
f1=open(Input_file,'r')#open file
f2=open(Output_file,'w')#open file
f2.write('Population\tSample_no\tSample_id\tPrediction\tLat\tLon\tdistinction\n')#write theheader in outputfile 
f3=open(geo_file,'r')#open file

#%%
'''
f1=open('output_python.txt','r')#open file
f2=open('close_file.txt','w')#open file
f2.write('Population\tSample_no\tSample_id\tPrediction\tLat\tLon\tdistinction\n')#write theheader in outputfile 
f3=open('geo.csv','r') #open file
'''
number_list=['0','1','2','3','4','5','6','7','8','9']#list for delete the number in population file
file=f3.readlines() #read the data from geo.csv
for line in f1:#read file from output_python.txt
    if line.startswith('Population')==False:#don't read the header line
        line=line.replace('\n','')#remove the '\n' in each line
        infor_in_each_record=line.split('\t')#cut the information by tab
        temp_store=infor_in_each_record[3]#store the population name in the list
        
        if infor_in_each_record[3][-1] in number_list: #check wheter there is number name in the name
            
            temp_store=temp_store.strip(temp_store[-1])#delete number from name
            temp_store=temp_store.strip('_')#delete _ from name
        
        #print(infor_in_each_record)
        infor_in_each_record[4]=infor_in_each_record[4].strip('[') #delete [ from lat
        infor_in_each_record[4]=infor_in_each_record[4].strip(']') #delete ] from lat
        infor_in_each_record[5]=infor_in_each_record[5].strip('[') #delete [ from lon
        infor_in_each_record[5]=infor_in_each_record[5].strip(']')#delete ] from lon
        lat1=float(infor_in_each_record[4]) #collect the predict lat 
        lon1=float(infor_in_each_record[5])#collect predict lon
        for line1 in file: #read the data in the file
            
            if line1.startswith('POPULATION') == False: #don't read the header line
                line1=line1.strip('\n') #remove the '\n' in each line
                infor_popu=line1.split(',') #cut the information by ,
                
                if infor_in_each_record[3] == infor_popu[0]: # if the predicted name is the same with the name in the geo.csv
                    
                    lat2=float(infor_popu[1]) #store the lat
                    lon2=float(infor_popu[2]) #store the lon
                    #print(lon1,lon2,lat1,lat2)
                    distance=haversine(lat1,lat2,lon1,lon2) #use the function calculate the distance
                    
                    
                    close_record=line+'\t'+str(distance)+'\n'  #sore the information as a string
                    f2.write(close_record) #file write
            
f1.close() #file close
f2.close() #file close
f3.close() #file close
