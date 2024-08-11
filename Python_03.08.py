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

#version3

#1. How many Pokémons are with 'Type 1' == Water as a % of total?

Water_pokemons = pokemon_df[pokemon_df['Type 1'] == 'Water']
print(len(Water_pokemons))


total_water_pokemons = len(Water_pokemons)
print(total_water_pokemons)

all_pokemons = len(pokemon_df)
print(all_pokemons)


Water_pokemons_percentage = (total_water_pokemons / all_pokemons) * 100




print(f"Pokemons Type1 Water as a percentage of total: {Water_pokemons_percentage:.2f} % ")

#2. What is the maximum 'Speed' value? 
#What is the minimum 'Speed' value? 
#What is the difference between max and min 'Speed'?

min_speed_value = pokemon_df['Speed'].min()
max_speed_value = pokemon_df['Speed'].max()
difference_max_min = max_speed_value-min_speed_value
print(min_speed_value)
print(max_speed_value)
print(difference_max_min)


#3. Filter the DataFrame to include only the Pokémon with 'Speed' >= 80. 
#How many Pokémon meet this criterion? 
#Display this DataFrame using your preferred visualization method.


Filtered_Data_Frame = pokemon_df[pokemon_df['Speed'] >= 80]
print(len(Filtered_Data_Frame))
