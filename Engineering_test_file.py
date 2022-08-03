import pandas as pd
import os
import zipfile

master_df= pd.DataFrame()
c_file_new=pd.DataFrame()
c_file=pd.DataFrame()

#Taking path input from user
take_path = input('Enter the path of Engineering Test Files.zip file ')    


combined_zipfile= (os.path.join(take_path, 'Engineering Test Files\Combined.csv'))
combined_final_file= (os.path.join(take_path, 'Engineering Test Files\Combined_finale_file.csv'))
col_list =['Source IP']

#Accessing zip folder and extracting the files to current directory
zf = zipfile.ZipFile(os.path.join(take_path, 'Engineering Test Files.zip'))
zf.extractall()

#Accessing files inside of zip extracted folder in a loop
for file in os.listdir(os.chdir(os.path.join(take_path, 'Engineering Test Files'))):
    if ((file != 'Combined.csv'  and file.endswith(".csv"))):
    
    #Reading files of folder and retriving unique data of specific column 'Source IP'
     master_df=pd.read_csv(file, usecols=col_list)
     master_df=pd.concat([master_df]).drop_duplicates().reset_index(drop=True)
    
     #Splitting file name
     o=file.split('/')
     env=(o[0])

     # remove last number and extension csv from csv file name string
     env=env.rstrip("1234567890.csv")
        
     # add file_source column
     master_df["Environment"]=env
     
     #Concated Source IP column and Env column
     c_file=pd.concat([master_df,c_file_new]).drop_duplicates().reset_index(drop=True)
     c_file_new=c_file.append(master_df)
     c_file_new=pd.concat([c_file_new]).drop_duplicates().reset_index(drop=True)

#print(c_file_new)

#stored proccesd data to a new file Combined_finale_file
c_file_new.to_csv(combined_final_file, index=False)

#Deleted existing Combined.csv file
os.remove(os.path.join(take_path, 'Engineering Test Files\Combined.csv'))

#renaming Combined_finale_file to Combined.csv
old_name= (combined_final_file)
new_name= (combined_zipfile)
os.rename(old_name, new_name)
            
