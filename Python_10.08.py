#Version1
import pandas as pd #analysis
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv('/content/Pokemon.csv')

#1.Grass DataFrame
grass_df = pokemon_df[pokemon_df['Type 1'] == 'Grass']
grass_df.hist()
plt.show()
#Water DataFrame
water_df = pokemon_df[pokemon_df['Type 1'] == 'Water']
water_df.hist()
plt.show()

#correlation matrix
correlation_matrix = numeric_columns_1.corr()
correlation_matrix

import seaborn as sns
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True) 
plt.title('Correlation Matrix')

#correlation matrix_1
correlation_matrix_1 = numeric_columns.corr()
correlation_matrix_1

import seaborn as sns
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix_1, annot=True) 
plt.title('Correlation Matrix_1')
#2 Grass and Water regression plot
#grass
sns.regplot(x='Attack', y='Defense', data=grass_df, color='green', ci=99, marker='x', line_kws={'color':'red'})
plt.title('Attack vs Defense')
#water
sns.regplot(x='Attack', y='Defense', data=water_df, color='blue', ci=99, marker='o', line_kws={'color':'red'})
plt.title('Attack vs Defense')

#3Calculate the Pearson correlation for each DataFrame (variables: Attack and Defense)
sns.regplot(
    data=grass_df, x='Attack', y="Defense",
    ci=99, marker="x", color="green", line_kws=dict(color="g"), label='Grass',)
sns.regplot(
    data=water_df, x='Attack', y="Defense",
    ci=99, marker="o", color="blue", line_kws=dict(color="b"), label='Water',)
plt.legend()
plt.title('Grass and Water Type1 Pokemon, Attack/Defense')
plt.xlabel('Attack')
plt.ylabel('Defense')

correlation_1 = grass_df['Attack'].corr(grass_df['Defense'])
print('Pearson correlation coefficient: ', correlation_1)
correlation_2 = water_df['Attack'].corr(water_df['Defense'])
print('Pearson correlation coefficient: ', correlation_2)

#version2
import pandas as pd
import matplotlib.pyplot as plt
pokemon_df = pd.read_csv('/content/Pokemon.csv')
import seaborn as sns

grass_df = pokemon_df[pokemon_df['Type 1'] == 'Grass']
water_df = pokemon_df[pokemon_df['Type 1'] == 'Water']

sns.regplot(x='Attack', y='Defense', data=grass_df, label='Grass')
sns.regplot(x='Attack', y='Defense', data=water_df, label='Water')
plt.legend()

plt.title('Attack vs Defense for Grass and Water Type Pokemon')
plt.xlabel('Attack')
plt.ylabel('Defense')

correlation1 = grass_df['Attack'].corr(grass_df['Defense'])
print('Pearson correlation coefficient: {:.2f}'.format(correlation1))

correlation2 = water_df['Attack'].corr(water_df['Defense'])
print('Pearson correlation coefficient: {:.2f}'.format(correlation2))
