# Exercise A:

stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, 'Glasgow Queen St')
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4,"Polmont")
#4. Print out the index position of "Linlithgow"
print(stops.index("Linlithgow"))
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
#6. Delete "Cumbernauld" from the list by index
stops.pop(2)
#7. Print the number of stops there are in the list
print(len(stops))
#8. Sort the list alphabetically
stops.sort()
#9. Reverse the positions of the stops in the list
stops.sort(reverse = True)
#10 Print out all the stops using a for loop
print(stops)
for stop in stops:
    print(stop)


#Exercise B:

    users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jonathan_twitter_handle = users["Jonathan"]["twitter"]
print(jonathan_twitter_handle)
# 2. Get Erik's hometown
erik_hometown = users["Erik"]["home_town"]
print(erik_hometown)
# 3. Get the list of Erik's lottery numbers
erik_lottery_numbers = users["Erik"]["lottery_numbers"]
print(erik_lottery_numbers)
# 4. Get the species of Avril's pet Monty
avril_pet_species = users["Avril"]["pets"][0]["species"]
print(avril_pet_species)
# 5. Get the smallest of Erik's lottery numbers
erik_smallest_number = min(erik_lottery_numbers)
print(erik_smallest_number)
# 6. Return a list of Avril's lottery numbers that are even
avril_even_numbers = []
avril_lottery_numbers = users["Avril"]["lottery_numbers"]
for number in avril_lottery_numbers:
    if number % 2 == 0:
        avril_even_numbers.append(number)
print(avril_even_numbers)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
erik_lottery_numbers.append(7)
print(erik_lottery_numbers)
# 8. Change Erik's hometown to Edinburgh
erik_new_home = users["Erik"]["lottery_numbers"] = "Edinburgh"
print(erik_new_home)
# 9. Add a pet dog to Erik called "fluffy"
new_pet = {
    "name" : "fluffy",
    "species" : "dog"}
users["Erik"]["pets"].append(new_pet)
eriks_pets = users["Erik"]["pets"]
print(eriks_pets)
# 10. Add another person to the users dictionary
users["Alex"] = ["New person"]
print(users["Alex"])

#Exercise C:

united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
wales_capital = united_kingdom[1]["capital"] = ["Cardiff"]
print(wales_capital)
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list 
# (The capital is Belfast, and the population is 1,811,000).
northern_ireland = {"name" : "Northern Ireland",
                    "population" : 1811000,
                    "capital" : "Belfast"}
united_kingdom.append(northern_ireland)
print(united_kingdom)
# 3. Use a loop to print the names of all the countries in the UK.
for country in united_kingdom:
    print(country["name"])
# 4. Use a loop to find the total population of the UK.
total_population = 0
for country in united_kingdom:
    total_population += (country["population"])
    country["population"] = 0
print(f'{total_population}')