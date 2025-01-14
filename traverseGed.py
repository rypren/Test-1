from gedcom.parser import Parser
from gedcom.element import individual

from gedcom.element.individual import IndividualElement

import gedcom.tags

# Path to your ".ged" file
file_path = ''

# Name of your ".ged" file
file_name = 'rypren Släktträd 250107.ged'

# Initialize the parser
parser = Parser()
parser.parse_file(file_path + file_name)

# Use criteria to find person.  Only one field is required.  The search returns the first match.
# criteria = "given_name=[first name]:surname=[last name]:birth=[birth year]:death=[death year]"
# criteria = "given_name=Stefan:birth=1987"
criteria = "given_name=Peter:birth=1957"
# criteria = "given_name=Johan Oskar:birth=1872"
# criteria = "given_name=Selma Elovina:birth=1886"
# criteria = "given_name=Jonas:birth=1798"
individual = parser.find_person(criteria)

if individual == "":
    print('Person not found')
    exit()

# Print found person's name and sources for the name.
given_name, last_name, suffix, sources = individual.get_name_data()
print("Selected person:")
print("  ", given_name, last_name, suffix)

# Print found person's children.
print("Children:")
for child in parser.get_children(individual):
    given_name, surname = child.get_name()
    print("  ", given_name, surname)
print(" ")

no_of_individuals = 1

def traverse(person):
    global no_of_individuals
    given_name, surname = person.get_name()
    spaces = "-" * no_of_individuals
    print(no_of_individuals, spaces, given_name, surname)
    parents = parser.get_parents(person)
    if len(parents) == 0:
        return
    else:
        no_of_individuals += 1
        for parent in parents:
            traverse(parent)
        no_of_individuals -= 1

traverse(individual)

print(no_of_individuals)

exit()
