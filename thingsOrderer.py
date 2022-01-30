# Goal: Help me make a ranked list of a collection of random items
# Algorithm:
# 	- Have a dictionary with as key a random item and as value 0
# 	- Pick two random keys from dictionary
# 	- Print them out for user
# 	- Have user input choose between them
# 	- If user chose an item, add +1 to item
# 	- If user didn't choose an item, add -1 to item
# 	- Loop until user input = done
# 	- If done, print dictionary ordered by value of values.

# Helpers:
# 	- pickRandomKeys: input: dictionary, output: two random keys in dictionary
# 	- getOrderedListFromDict: returns an ordered list from dictionary
#   - getDictionary: input: list, output: dictionary with list item as key and 0 as value

from pickle import TRUE
import random as rand

RANDOM_THINGS = [
"Brononderzoek doen",
"Onderzoeksverslag schrijven",
"Informerende kaart maken",
"Studeren van natuurlijke geografie",
"Studeren van sociale geografie",
"Statistiek gebruiken",
"Infographic maken",
"Data verzamelen",
"Met design bezig",
"Website maken",
"Interactieve kaart maken",
"Focus op klimaatverandering",
"Storymaps",
"Datagericht onderzoek uitvoeren",
"Met software ruimtelijke voorspellingen maken",
"Onderzoek naar Nederlands landschap",
"Op basis van ruimtelijke eigenschappen advies geven",
"Interpolatietechnieken",
"Onderzoek in het veld",
"Werken met echte klant",
"Python scripting",
"App design",
"Data kritisch analyseren",
"Leiderschap",
"In groepsverband werken",
"Individueel werken",
]

def get_dictionary(input_list):
    output_dict = {}
    for item in input_list:
        output_dict[item] = 0
    return output_dict

def get_random_items(input_list):
    item_1 = rand.choice(input_list)
    item_2 = item_1
    while item_1 == item_2:
        item_2 = rand.choice(input_list)
    return item_1, item_2

def get_ordered_list(input_dict):
    output_list = []
    for item in sorted(input_dict, key=input_dict.get, reverse=True):
        output_list.append(item)
    return output_list

values_dict = get_dictionary(RANDOM_THINGS)


def main():
    while True:
        item_1, item_2 = get_random_items(RANDOM_THINGS)
        print (f'Item 1: {item_1}')
        print (f'Item 2: {item_2}')
        user_choice = input('Enter either 1, 2 or done: ')
        print ('')
        
        # 	- If user chose an item, add +1 to item
        if user_choice == '1':
            values_dict[item_1] += 1
            values_dict[item_2] -= 1

        if user_choice == '2':
            values_dict[item_1] -= 1
            values_dict[item_2] += 1
        
        if user_choice == 'done':
            break

    result = get_ordered_list(values_dict)
    ranking = 0
    for item in result:
        ranking += 1
        print (f'{ranking}: {item}. Score: {values_dict[item]}')

main()

