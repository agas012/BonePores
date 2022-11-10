#%%Libs
import os
import gc
#Math
import numpy as np
import math

#Dataframe
import pandas as pd
from pathlib import Path

#input
cwd = Path.cwd()
dir_I =  Path(cwd, "In/")

#output folders
out_path_files = Path(cwd, "Out/")
out_path_files.mkdir(parents=True, exist_ok=True)


# list to store files
files_I = []
foldername = []
for root, dirs, files in os.walk(dir_I):
    for file in files:
        if file.endswith('.xlsx'):
            files_I.append(os.path.join(root,file))
            foldername.append(os.path.basename(os.path.normpath(root)))

dataframes = []
for file in files_I:
    dataframes.append(pd.read_excel(file))

outdf = pd.DataFrame(columns=['FileName','PorosityFraction','NumberPores'])
for i in range(len(dataframes)):
    dataframe = dataframes[i]
    recarea = (dataframe.X.max() - dataframe.X.min()) * (dataframe.Y.max() - dataframe.Y.min())
    porosityfraction = (dataframe.Area.sum()) / recarea
    numelements = dataframe.shape[0]
    nameim = foldername[i]
    new_row = {'FileName':nameim, 'PorosityFraction':porosityfraction, 'NumberPores':numelements}
    new_df = pd.DataFrame([new_row])
    outdf = pd.concat([outdf, new_df], axis=0, ignore_index=True)



