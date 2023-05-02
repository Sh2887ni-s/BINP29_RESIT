# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 20:09:30 2023

@author: NSJ
"""
import sys
import os.path
f1 = open('geo.csv','r')#open file
f2 = open('gen.csv','r')#open file
f3 = open('data.csv','r')#open file
GEO=f1.readlines()#readlines of file
GEN=f2.readlines()#readlines of file
data=f3.readlines()#readlines of file
def IsFloatnum(string):
        if '-' in string:
            string=string.replace('-','') 
        if 'E' in string:
            string=string.replace('E','')
            print(string)
        s=string.split('.')
        if len(s)>2:
            return False
        else:
            for si in s:
                if not si.isdigit():
                    return False
            return True
#%%
if os.path.isfile('geo.csv') == False:
    print('Please check the file names')
    sys.exit()
print(os.path.isfile('gee.csv'))
#%%
'''
i=1
while i < len(GEO):
    #print(GEO[i])
    geo_lat=GEO[i].replace('\n', '').split(',')[1]
    geo_lon=GEO[i].replace('\n', '').split(',')[2]
    print(geo_lat)
    print(geo_lon)
    if IsFloatnum(geo_lat) == False or IsFloatnum(geo_lon) ==False:
        print('Check the data')
        sys.exit()
    elif IsFloatnum(geo_lat) == True and IsFloatnum(geo_lon) == True:
        print('correct')
    i+=1

j=0#create a loop count variable start with 0

while j < len(GEN):
    each_GEN_line_list=GEN[j].replace('\n', '').split(',')
    
    k=1
    while k < len( each_GEN_line_list):
        
        if IsFloatnum(each_GEN_line_list[k]) == False: 
            print('Check the data')
            print(each_GEN_line_list[k])
            sys.exit()
        elif IsFloatnum(each_GEN_line_list[k]) == True: 
            print('correct')
        k+=1
    j+=1

j=1#create a loop count variable start with 1
while j < len(data):
    
    each_data_line_list=data[j].replace('\n', '').split(',')
    
   
    k=1
    while k < len(each_data_line_list)-1:
        if IsFloatnum(each_data_line_list[k]) == False: 
            print('Check the data')
            print(each_data_line_list[k])
            sys.exit()
        elif IsFloatnum(each_data_line_list[k]) == True: 
            print('correct')
            print(each_data_line_list[k])
        k+=1
    j+=1
'''
f1.close()#file close
f2.close()#file close
f3.close()#file close