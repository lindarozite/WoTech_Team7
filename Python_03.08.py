#version1
#Calculate the total number of Pokémon
total_pokemons = len(type1_pokemons)

#Calculate the number of Pokémon with 'Type 1' == 'Water'
water_pokemons = type1_pokemons[type1_pokemons['Type 1'] == 'Water']
num_water_pokemons = len(water_pokemons)

#Calculate the percentage
percentage_water_pokemons = (num_water_pokemons / total_pokemons) * 100

#Print the result
print("The percentage of Pokémon with 'Type 1' == 'Water' is:", round(percentage_water_pokemons, 2), "%")
max_speed = pokemon_df['Speed'].max()
print(f"The maximum 'Speed' value is: {max_speed}")


min_speed = pokemon_df['Speed'].min()
print(f"The minimum 'Speed' value is: {min_speed}")

#Calculate the difference between the maximum and minimum 'Speed' values
speed_difference = max_speed - min_speed
print(f"The difference between the maximum and minimum 'Speed' values is: {speed_difference}")


#Version2
#1.water percentage:
water_pokemon_percent= (pokemon_df['Type 1'] == 'Water').mean() * 100
print(f"Percentage of Water-type Pokémon: {water_pokemon_percent:.1f}%")

#Answer is 14%

#2.min/max speed:
max_speed = pokemon_df['Speed'].max()
min_speed = pokemon_df['Speed'].min()
speed_difference = max_speed - min_speed

print(f'Maximum Speed: {max_speed}')
print(f'Minimum Speed: {min_speed}')
print(f'Speed Difference (Max - Min): {speed_difference}')

#Answers are 180-5=175

#3.Speed > 80:
high_speed_pokemon = pokemon_df[pokemon_df['Speed'] >= 80]
print(f'Number of Pokémon with Speed >= 80: {len(high_speed_pokemon)}')

high_speed_pokemon['Speed'].hist(bins=5, edgecolor='black')
plt.title('Distribution of Pokémon Speeds (Speed >= 80)')
plt.xlabel('Speed')
plt.ylabel('Number of Pokémon')
plt.show()

#Answer is 296 and I don't like the histogram on this but I couldn't figure out a prettier way to show it

#4.The longest name:
pokemon_df['Name Length'] = pokemon_df['Name'].apply(lambda x: len(x.replace(' ', '')))
longest_name_pokemon = pokemon_df[pokemon_df['Name Length'] == pokemon_df['Name Length'].max()]
print(f'Pokémon with the longest name: {longest_name_pokemon["Name"].values[0]}')

#Answer is: KangaskhanMega Kangaskhan
