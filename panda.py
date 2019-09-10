import pandas as pd
import re
import os.path
from os import path
import sys

def run(filename, parameterName):
    data = pd.read_csv(filename, low_memory=False, sep=',')
    if not parameterName in data.columns:
        data.insert(0, parameterName, '')

    for i, row in data.iterrows():
        
        regex = re.escape(parameterName) + r"\\(.+)"        
        
        searchObj = re.findall(regex, str(row['/parameters/parameter@textid[pol]']), re.M|re.I)

        if searchObj:
            data.at[i, parameterName] = ', '.join(searchObj)
        else:
            data.at[i, parameterName] = ''

    data.to_csv(filename, sep=',', index=False)

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        parameterName = sys.argv[2]
        if path.exists(filename):
            run(filename, parameterName)
        else:
            print('File doesn\'t exist')
    except:
        print('usecase: python3 filename "parameterName". ex: python3 scienne.csv "kolor obudowy"')