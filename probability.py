import pandas as pd

evaluate = pd.read_excel("evaluate.xlsx")

#おいしい
extract_1 = evaluate.query('評価 == 1')
length_1 = len(extract_1.index)

list_1 = (extract_1.sum(axis=0) / length_1) * 100

#まずい
extract_0 = evaluate.query('評価 == 0')
length_0 = len(extract_0.index)

list_0 = (extract_0.sum(axis=0) / length_0) * 100

print(list_1 - list_0)
