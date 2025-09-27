# how to connect to an api using python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response) # status code 200 = OK

    if response.status_code == 200:
        print("data was retrieved")
        pokemon_data = response.json()
        # prints dictionary of pokemon info
        # print(pokemon_data)
        return pokemon_data
    else:
        print(f"failed to retrieve data {response.status_code}")

# ask user to input pokemon name
pokemon_name = input("enter pokemon name: ")
# call get_pokemon_info function with name inputted
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]} ft")
    print(f"Weight: {pokemon_info["weight"]} lbs")