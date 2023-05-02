# BINP29_RESIT
The geographic population structure (GPS) is a good method to reflect the historical gene flow and the potential environmental change. 
Here, I developed the structure to calculate the distance between the population and the predicted population to try to find the migration information of those two populations and their relationship with them. The data and the code of the GPS in R come from Prof. Eran Elhaik.
In this folder, there are six Python files, GPS.py: the main script of the GPS algorithm, filter_and_distance_calculation.py : the script to calculate the distance of the migration of population (if they migrated) by latitude and longitude, filter_close_distance.py: the script that calculates how close between the prediction of the location and the real location by latitude and longitude and the Graph.py, fig3.py and fig4.py : the script to make the graphs which are used in the report. And three .csv files named geo.csv, gen.csv and data.csv
In the GPS.py, geo.csv, gen.csv and data.csv are input files output_python.txt is the output file. In this output file, there are 6 columns, they are Population, Sample number, Sample id, Prediction population, and prediction latitude and longitude.
In the filter_and_distance_calculation.py, output_python.txt and geo.csv are input files and comparing.txt are output files. There are three columns in this output file, they are Population, Prediction population, and distance between those two populations, from left to right
In the filter__close_distance.py, output_python.txt and geo.csv are input files, close_file.txt is the output file, there are 7 columns in this output file, the first 6 columns is the same with the output_python.txt, and the last one ‘distinction’ records the distance of the prediction location and the real location of each population.
firstly, the files should be downloaded from Github: https://github.com/Sh2887ni-s/BINP29_RESIT.git
Please follow these steps if you want to do it again.
Step1: type the code: python GPS.py geo.csv gen.csv data.csv output_python.txt
After running, the output_python.txt file is created
Step2: type the code: python filter_and_distance_calculation.py output_python.txt comparing.txt geo.csv
After running, the comparing.txt.txt file is created, in this file, there are three columns
The columns are Population, Prediction, and Distance, from left to right
Step3: type the code: python filter__close_distance.py output_python.txt close_file.txt geo.csv
This is the code that tests how close the prediction latitude and longitude with the actual ones
Step4: type the code: python Graph.py close_file.txt
This is the script that makes a graph to show how many records in each distance range in Step3
Step5: type the code: python fig3.py output_python.txt
This is the script that makes a graph to show how many records in Vietnamese and Japanese are predict in Chinese
Step6: type the code: python fig4.py comparing.txt
This is the script that makes a graph to show how many records in each distance range in Step2

