import random

#open list
#[Expression for item in iterable]

pets = ('dog','Cat','turtle', 'bird', 'snake')

uppercase_pets = []

for pet in pets:
    uppercase_pets.append(pet.upper())

print(uppercase_pets)



uppercased_pets = [pet.upper() for pet in pets]

print(uppercased_pets)

#[expression for item in iterable if condition]

uppercased_pets_upd = [pet.upper() for pet in pets if pet == 'Cat']
print(uppercased_pets_upd)

def four_legged_pet(pet):
    return pet in ('Cat', 'dog','horse')


four_legged_pets = [pet.capitalize() for pet in pets if four_legged_pet(pet)]
print(four_legged_pets)


#[expression0 if condition else expression1 for item in iterables]

max_num = 10
numbers = (5,8,15,11,6)

values_out = [number if number < max_num else max_num for number in numbers]
print(values_out)

# map(function,iterable)

uppercase_pts = list(map(str.upper,pets))
print(uppercase_pts)


# [expression for sublist in outer_list for item in sublist]

nested_number = ((1,3,5,7),(2,4,6,8))

outvalue = [x*x for numbers in nested_number for x in numbers]
print(outvalue)

letters = list('this is a test print')
print(letters)

#vowels = [letter.upper() for _ in range(0,10) if (letter := random.choice(letters)) in list('aeiou')]
vowels = [letter.upper() for _ in range(0, 10) if (letter := random.choice(letters)) in list('aeoui')]
print(vowels)