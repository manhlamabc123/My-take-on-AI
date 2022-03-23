import pandas as pd
import re

dataframe = pd.read_csv('pokemon_data.csv')
# dataframe = pd.read_excel('pokemon_data.xlsx')
# dataframe = pd.read_csv('pokemon_data.txt', delimiter='\t')

# Read Headers
## print(dataframe.columns)

# Read each Columns
## print(dataframe['Name'])
## print(dataframe.Name)

# Read Each Row
## print(dataframe.head(3))
## print(dataframe.iloc[0:4])

## for index, row in dataframe.iterrows():
##     print(index, row['Legendary'])

## print(dataframe.loc[dataframe["Type 1"] == "Fire"])

# Read a specific Location (R, C)
## print(dataframe.iloc[2,1])

# Describing Data
## print(dataframe.describe())

# Sorting Data
## print(dataframe.sort_values('Name', ascending = False))
## print(dataframe.sort_values(['Type 1', 'HP'], ascending=[1,0])) # First is True, Second is False

# Making changes to the Data
## dataframe['Total'] = dataframe['HP'] + dataframe['Attack'] + dataframe['Defense'] + dataframe['Sp. Atk'] + dataframe['Sp. Def'] + dataframe['Speed'] # Method 1
## dataframe['Total'] = dataframe.iloc[:, 4:10].sum(axis = 1) # Method 2
## print(dataframe.head(5))

## dataframe = dataframe.drop(columns=['Total'])
## print(dataframe.head(5))

## cols = list(dataframe.columns)
## dataframe = dataframe[cols[0:4] + [cols[-1]] + cols[4:12]]
## print(dataframe.head(5))

# Save
## dataframe.to_csv('modified.csv', index=False)
## dataframe.to_excel('modified.xlsx', index = False)
## dataframe.to_csv('modified.txt', index=False, sep='\t')

# Filtering Data
## print(dataframe.loc[(dataframe['Type 1'] == 'Grass') & (dataframe['Type 2'] == 'Poison')])
## new_dataframe = dataframe.loc[(dataframe['Type 1'] == 'Grass') | (dataframe['Type 2'] == 'Poison')]
## print(new_dataframe)

## new_dataframe = new_dataframe.reset_index(drop=True) #Method 1
## new_dataframe.reset_index(drop=True, inplace=True) #Method 2
## print(new_dataframe)

## print(dataframe.loc[dataframe['Type 1'].str.contains('Fire|Grass', regex = True)]) #Method 1
## print(dataframe.loc[dataframe['Type 1'].str.contains('fire|grass', flags=re.I, regex = True)]) #Method 2
## print(dataframe.loc[dataframe['Name'].str.contains('^pi[a:z]*', flags=re.I, regex = True)])

#Conditional Change
## dataframe.loc[dataframe['Type 1'] == 'Fire', 'Type 1'] = 'Flame'
## print(dataframe)
## dataframe.loc[dataframe['Type 1'] == 'Flame', 'Type 1'] = 'Fire'

## dataframe.loc[dataframe['HP'] > 70, ['Legendary', 'Generation']] = [True, '100']
## print(dataframe)

# Group by
## print(dataframe.groupby(['Type 1']).mean().sort_values('Sp. Def', ascending=False))

## dataframe['count'] = 1
## new_dataframe = dataframe.groupby(['Type 1', 'Type 2']).count()[['count']]

# Working with large amounts of data
new_dataframe = pd.DataFrame(columns=dataframe.columns)

for df in pd.read_csv('modified.csv', chunksize = 5): # 5 rows per time
    print("-----------------------")
    print(df)