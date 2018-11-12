import pandas as pd
import random

input_material = pd.read_excel("materials.xlsx", sheet_name="materials")
input_sauce = pd.read_excel("materials.xlsx", sheet_name="sauces")

kind = random.randint(2,4)
sample = input_material.sample(n=kind)

print(sample)
or_data = sample.iloc[0,1:]
for i in range(len(sample.index) - 1):
    or_data = or_data | sample.iloc[i+1,1:]

print(or_data)

pentagon = input_sauce[['旨味','塩味','辛味','酸味','甘味']] & ~or_data
print(pentagon)
print(input_sauce[pentagon & ~or_data])

