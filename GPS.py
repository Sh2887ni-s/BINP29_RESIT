#!/bin/usr/env python3
"""
Title: Geographic population structure
Date: 2022-03-21
Author: Shijie Niu
Discription:
    This program will output predict closest population based on the GPS.
List of functions:
    1. dist_calculate: calculate the distance matrics
    2. IsFloatnum: the function which could judge the float number
List of 'non-standard' modules:
    No non-standard modules in this program.
Procedure:
    1. check whether the input file names are correct
    2. check whether the input files have the float number in the correct position
    3. Read the lines in the file.
    4. Calculate the distance matrics of GEO.csv and GEN.csv
    5. Predict the model of those two matrics.
    6.calculate the predict lat and lon, and find the closed population
Usage: python GPS.py geo.csv gen.csv data.csv output_python.txt
"""

import numpy as np #import numpy
import numpy.linalg as la #import numpy.linalg
import math #import math
import sys
import os.path
#%%
def IsFloatnum(string):#The function that could check whether the string could be transfer to the float number 
        if '-' in string:# check whether contain the '-' in the string
            string=string.replace('-','') # if it contain in the string, remove it
        if 'E' in string: # check whether contain the '-' in the string
            string=string.replace('E','') # if it contain in the string, remove it
            #print(string)
        s=string.split('.')#devide the string into list by '.'
        if len(s)>2:#if the list more than 2 elements
            return False#return false
        else: #if the list less than or equal to 2 elements
            for si in s: # create a loop to load check the elements in the list
                if not si.isdigit(): #if this element is not a digit
                    return False #return false
            return True #else return true
#%%
def dist_calculate(X): #define a function to calculate distance matrics
    
    n,m=X.shape # n, m is row and cloumn in Xmatrics
    D=np.zeros([n,n]) #create a empty matrics with n rows and column
    #write a loop to file the distance matrics
    for i in range(n):
        for j in range(i+1,n):
            D[i,j] =la.norm(X[i,:]-X[j,:])
            D[j,i]=D[i,j]
    return D #return the matrics
#%%
GEO_file=sys.argv[1]
Gen_file=sys.argv[2]
DATA_file=sys.argv[3]
Output_file=sys.argv[4]
#%%
if os.path.isfile(GEO_file) == False:# if the path of file is not contain in the folder
    print('Please check the file names')#print 'Please check the file names'
    sys.exit() #stop the script
elif os.path.isfile(Gen_file) == False: # if the path of file is not contain in the folder
    print('Please check the file names') #print 'Please check the file names'
    sys.exit() #stop the script
elif os.path.isfile(DATA_file) == False:# if the path of file is not contain in the folder
    print('Please check the file names') #print 'Please check the file names'
    sys.exit() #stop the script
#%%
f1 = open(GEO_file,'r')#open file
f2 = open(Gen_file,'r')#open file
f3 = open(DATA_file,'r')#open file
f4 = open(Output_file,'w')#open file
GEO=f1.readlines()#readlines of file
GEN=f2.readlines()#readlines of file
data=f3.readlines()#readlines of file
#%%
i=1 #create a loop count variable start with 1
while i < len(GEO): # if i less than or equal to the lenth of the GEO
    #print(GEO[i])
    geo_lat=GEO[i].replace('\n', '').split(',')[1] #devide the each element into a list and replace the '\n' and pick up the second element
    geo_lon=GEO[i].replace('\n', '').split(',')[2] #devide the each element into a list and replace the '\n' and pick up the second element
   #print(geo_lat)
    #print(geo_lon)
    if IsFloatnum(geo_lat) == False or IsFloatnum(geo_lon) ==False: #if both of elements are return false which are returned by the function 'IsFloatnum'
        print('Please check the data in geo file') #print 'Please check the data in geo file'
        sys.exit() # #stop the script
    
    i+=1 # i=i+1

j=0#create a loop count variable start with 0

while j < len(GEN): # if j less than or equal to the lenth of the GEN
    each_GEN_line_list=GEN[j].replace('\n', '').split(',') #devide the each element into a list and replace the '\n'
    
    k=1 #create a loop count variable start with 1
    while k < len( each_GEN_line_list): #read the all elements in the list
        
        if IsFloatnum(each_GEN_line_list[k]) == False:  #if the element is return false which are returned by the function 'IsFloatnum'
            print('please check the data in gen file') #print 'Please check the data in gen file'
            
            sys.exit() #stop the script
       
        k+=1 # k=k+1
    j+=1 #j=j+1

j=1#create a loop count variable start with 1
while j < len(data): # if j less than or equal to the lenth of the data
    
    each_data_line_list=data[j].replace('\n', '').split(',') #devide the each element into a list and replace the '\n'
    
   
    k=1 #create a loop count variable start with 1
    while k < len(each_data_line_list)-1: #read the all elements in the list
        if IsFloatnum(each_data_line_list[k]) == False: #if the element is return false which are returned by the function 'IsFloatnum'
            print('please check the data in data file') #print 'Please check the data in data file'
            
            sys.exit() #stop the script
        
        k+=1 # k=k+1
    j+=1 #j=j+1


#%%
i=1 #create a loop count variable start with 1
GEO_country_name=[] #create a list to store country name
GEO_matrix=np.zeros([len(GEO)-1,2]) #create a empty matrics with length of GEO -1 rows and 2 columns
#loop to store the country name in the list and the data in the matrics the sequences of list and matrics are same
while i < len(GEO):
    line=GEO[i]
    line1=line.replace('\n', '')
    line1=line1.split(',')
    GEO_country_name.append(line1[0])
    GEO_matrix[i-1,0]=float(line1[1])
    GEO_matrix[i-1,1]=float(line1[2])
    i+=1
#print(GEO_matrix)
GEO_distance_matrix=dist_calculate(GEO_matrix) #calculate the distance matrics by function

#%%
GEN_matrix=np.zeros([len(GEN),9])#create a empty matrics with length of GEN rows and 9 columns
j=0#create a loop count variable start with 0
GEN_country_name=[]#create a list to store country name
#loop to store the country name in the list and the data in the matrics the sequences of list and matrics are same
while j < len(GEN):
    line=GEN[j]
    line1=line.replace('\n', '')
    line1=line1.split(',')
    GEN_country_name.append(line1[0])
    k=1
    while k < len(line1):
        GEN_matrix[j,k-1]=float(line1[k])
        k+=1
    j+=1
#print(GEN_matrix)
GEN_distance_matrix=dist_calculate(GEN_matrix)#calculate the distance matrics by function
#print(GEN_distance_matrix)
#%%
TRAINLING_DATA=np.zeros([len(data)-1,9])#create a empty matrics with length of GEN rows and 9 columns
MATRIX_GROUPS=[]#creat a list to store the group name
sample_id=[]#creat a list to store sample id
j=1#create a loop count variable start with 1
#loop to store the group name and sample ID in the list and the data in the matrics the sequences of list and matrics are same
while j < len(data):
    line=data[j]
    line1=line.replace('\n', '')
    line1=line1.split(',')
    MATRIX_GROUPS.append(line1[10])
    sample_id.append(line1[0])
    k=1
    while k < len(line1)-1:
        TRAINLING_DATA[j-1,k-1]=line1[k]
        
        k+=1
    j+=1
#%%
L=len(GEO_distance_matrix)# line of GEO_distance_matrics
i=0 #create a loop count variable start with 0
j=0 #create a loop count variable start with 0
k=0 #create a loop count variable start with 0
x=[] #creat a list
y=[] #creat a list
#loop to remove extreme value and store the value to x axis and y axis
for i in range(0,L):
    for j in range(0,L):
        if GEO_distance_matrix[i,j] >= 70 or GEN_distance_matrix[i,j]>=0.8:
            GEO_distance_matrix[i,j] = 0
            GEN_distance_matrix[i,j] = 0 
        if i < j:
            x.append( GEN_distance_matrix[i,j])
            y.append(GEO_distance_matrix[i,j])
#creat two arrays for x and y axis
x_train=np.array(x[:len(x)]).reshape(len(x),1)
y_train=np.array(y[:len(x)])
from sklearn import linear_model#import linear_model
#fit the model
linear_regressor=linear_model.LinearRegression()
linear_regressor.fit(x_train,y_train)
import matplotlib.pyplot as plt #import matplotlib.pyplot
y_train_pred=linear_regressor.predict(x_train) #calculate the predict Y value based on X
#print(y_train_pred)
#print(x_train)
#plot the data
plt.figure()
plt.scatter(x_train,y_train,color='green')
plt.plot(x_train,y_train_pred,color='black',linewidth=4)

#%%
groups=[]#creat a name list
i=0# creat a loop count variable
#store the unique groutname in groupname list
for group in MATRIX_GROUPS:
    if group not in groups:
        groups.append(group)
        
#print (groups)
#set the parameters
N_best=10 #set the initial parameter
N_best=min(N_best,len(GEO_matrix)) #
f4.write("Population\tSample_no\tSample_id\tPrediction\tLat\tLon\n")
count=0
temp=0
#loop for GPS algorithm (This part is encode by the raw stript which encode by R, most variables are same with that file)
while i < len(groups):
    group=groups[i]
    temp=count
    count+=MATRIX_GROUPS.count(group)
    for j in range(temp,count):
        
        if j == temp:
            Y=[]
            row_name=[]
            row_name.append(sample_id[j])
            Y=[TRAINLING_DATA[j,]]
        else:
            row_name.append(sample_id[j])
            Y=np.r_[Y,[TRAINLING_DATA[j,]]]
    K=MATRIX_GROUPS.count(group)
    for a in range(0,K):
    
        if a!=K-1:
            X=Y[a,0:9]
            minE=10000 #set the parameter
            minG=-1 #set the parameter
            E=[]
            second_minG=-1 #set the parameter
            for g  in range(0, len(GEO)-1):
                ethnic=GEO_country_name[g]
                gene=GEN_matrix[g,0:9]
                E.append(math.sqrt(sum(pow((gene-X),2))))
    #            print(gene)
            minE=[]
            minE=(sorted(E)[0:N_best])
            minG=[]
            j=0
            for g  in range(0,len(GEO)-1):
            
                for j in range(0,N_best):
                    if minE[j]== E[g]:
                        minG.append(g)
                        
        else:
            minE=10000 
            minG=-1 
            E=[]
            second_minG=-1
            for g  in range(0, len(GEO)-1):
                ethnic=GEO_country_name[g]
                gene=GEN_matrix[g,0:9]
                E.append(math.sqrt(sum(pow((gene-Y[K-1]),2))))
                #            print(gene)
            minE=[]
            minG=[]
            minE=(sorted(E)[0:N_best])
            for create_list in range(0,N_best):
                minG.append(-1)
            j=0
            for g  in range(0,len(GEO)-1):
            
                for j in range(0,N_best):
                    if minE[j]== E[g]:
                        minG[j]=g
        radius=[]
        best_ethnic=[]
        for mg in minG:
            radius.append(E[mg])
            best_ethnic.append(GEO_country_name[mg])
        E_test=np.array(minE)
        W=pow(E_test[0]/E_test,4)
        W=W/sum(W)
        delta_lat=[]
        delta_lon=[]
        radius_geo=(y_train_pred[3]-y_train_pred[0])/(x_train[3]-x_train[0])*radius[0]
        for pos in minG:
            delta_lat.append(GEO_matrix[pos,0]-GEO_matrix[minG[0],0])
            delta_lon.append(GEO_matrix[pos,1]-GEO_matrix[minG[0],1])
        new_lon=sum(W*delta_lon)
        new_lat=sum(W*delta_lat)
        lo1=new_lon*min(1,radius_geo/math.sqrt(pow(new_lon,2)+pow(new_lat,2)) )
        la1=new_lat*min(1,radius_geo/math.sqrt(pow(new_lon,2)+pow(new_lat,2)))
        f4.write(group+'\t'+str(a+1)+'\t'+row_name[a]+'\t'+best_ethnic[0]+'\t'+str(GEO_matrix[minG[0],0]+la1)+'\t'+str(GEO_matrix[minG[0],1]+lo1)+'\n') #file write
    i+=1 #round count
f1.close()#file close
f2.close()#file close
f3.close()#file close
f4.close()#file close

