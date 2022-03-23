import pandas as pd

dataframe = pd.read_csv('pokemon_data.csv')
# dataframe = pd.read_excel('pokemon_data.xlsx')
# dataframe = pd.read_csv('pokemon_data.txt', delimiter='\t')

print(dataframe.head(3))