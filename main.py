# Ethan Lawrence
# nov 19 2024
# return statements

# Project 1: Destination Europe
def describe_vacation(destination, activity, season='summer'):
    return f'I will go to {destination}, to {activity}, in {season}'

description1 = describe_vacation('Mars', 'look at rocks')
description2 = describe_vacation('Michigan', 'be cold', 'winter')
print(description1 + '\n' + description2)

# Project 2: Student Major
def show_major(first_name, university, major='Sports Medicine'):
    return f'{first_name}, attends {university} and is majoring {major}'

print(show_major('Brian', 'NMC', 'Bug Medicine'))
print(show_major('David', 'NMC'))