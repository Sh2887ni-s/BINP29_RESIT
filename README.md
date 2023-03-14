The geographic population structure (GPS) is a good method to reflect the historical gene flow and the potential environmental change. 
Here, I developed the structure to calculate the distance between the population and the predicted population to try to find the migration information of those two populations and their relationship with them. The data and the code of the GPS in R come from prof. Eran Elhaik.
firstly, the files should be downloaded from Github: https://github.com/Sh2887ni-s/BINP29_RESIT.git, the file name is Shijie_Niu_resit.rar
There are two python files, named GPS.py and filter_and_distance_calculation.py, and three .csv files named geo.csv, gen.csv and data.csv in the .rar file, those five files are the resource and the python scrips. 
There also are two .txt files named output_python.txt and comparing.txt, those two files are the example output files.
Please follow these steps if you want to do it again.
Step1: type the code: python GPS.py geo.csv gen.csv data.csv output_python.txt
After running, the output_python.txt file is created, in this file, there are six columns
The columns are Population, Sample_no., Sample_id, Prediction, Latitude, and Longitude, from left to right
Step2: type the code: python filter_and_distance_calculation.py output_python.txt comparing.txt geo.csv
After running, the comparing.txt.txt file is created, in this file, there are three columns
The columns are Population, Prediction, and distance, from left to right
Step3: type the code: python filter__close_distance.py output_python.txt close_file.txt geo.csv
This is the code that test how close the prediction lat and lon with the actual ones
Step4: type the code: python Graph.py close_file.txt
This is the script that make a graph to show how many record in each distance ranges in Step3
