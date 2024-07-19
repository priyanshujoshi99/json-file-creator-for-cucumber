# -*- coding: utf-8 -*-
"""json file creator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iYElJWripm_YdUlW48PP655tNwvmQT7G
"""

import os
import pandas as pd

os.getcwd()

data = open(os.getcwd() + '/input.txt')

con = data.readlines()
con

iden = 'Scenario:' # Use this regex to find scenario name

file_names = []
for l in con:
    # print(l)
    if (l.find(iden) != -1):
        sd = l.split(iden)[1]
        sd = sd.strip()
        print(sd)
        file_names.append(sd)

file_names

os.mkdir('file_created')
for i in file_names:
    file = open('file_created/' + i + '.json', "w")
    file.write("")



merged_df = {}


# merged_df.at[i,'from'] = stores_list[]

