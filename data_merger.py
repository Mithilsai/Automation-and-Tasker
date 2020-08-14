import os
import pandas as pd
path = ""# path of the csv file's folder
files = [file for file in os.listdir(path) if not file.startswith('.')] # Ignore hidden files

all_data = pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path+"/"+file)
    all_data = pd.concat([all_data, current_data])

all_data.to_csv("", index=False)#merged output file name exam.csv
