# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:50:00 2018

@author: OKAMOTO_LAB
"""

import pandas as pd
import csv

input = pd.read_excel("materials.xlsx")
list = input.sample(3)
x = list.index.values
output = x.tolist()

counter_list = [0] * len(input.index)

for i in output:
    counter_list[i] = 1

print(list)
print(counter_list)

with open('test.csv','a') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(counter_list)