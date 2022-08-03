# Enginnering-Test-Risk-Analytics
In this project I have to write Python code that traverses through the files in the zipped folder (Engineering Test Files) and generates the combined.csv file also found in that folder such that if a new file called NA Preview.csv gets dropped in the same folder, the script will be able to process it and rows in the combined.csv file will be added with the environment value being set to NA Preview. 
Same applies if a new file called Asia Prod 4.csv gets dropped. It should add new rows to the combined.csv file with the environment being set to Asia Prod.
File path for files are taken by user.

Steps for building code:

1.File path is dynamic i.e as per user's input.

2.Extracted the zip folder and the files were read by as data frame using for loop excluding the Combined file as the final output will be updated in this file.

3.The Source IP column present in each file was extraced and appended in a new dataframe.

4.File names were split according to new column 'Environment' in a dataframe. 

5.The Source IP and Environment dataframe were concatenated as new dataframe and then converted to csv file.

6.The existing combined file was removed and the name of new csv file was renamed as Combined.csv.
