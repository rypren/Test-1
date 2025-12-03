from gedcom.parser import Parser
from gedcom.element import individual

from gedcom.element.individual import IndividualElement

import gedcom.tags

# Path to your ".ged" file
file_path = ''

# Name of your ".ged" file
file_name = 'rypren Släktträd 251202 - may-oct.ged'

# Initialize the parser
parser = Parser()
parser.parse_file(file_path + file_name)

# Use criteria to find person.  Only one field is required.  The search returns the first match.
# criteria = "given_name=[first name]:surname=[last name]:birth=[birth year]:death=[death year]"
# criteria = "given_name=Stefan:birth=1987"
# criteria = "given_name=Peter:birth=1957"
# criteria = "given_name=Johan Oskar:birth=1872"
criteria = "given_name=Selma Elovina:birth=1886"
# criteria = "given_name=Eric:birth=1835"
#criteria = "given_name=Emanuel:birth=1849"
# criteria = "given_name=Jonas:birth=1798"
individual = parser.find_person(criteria)

if individual == "":
    print('Person not found')
    exit()

# Print found person's name and sources for the name.
given_name, last_name, suffix, sources = individual.get_name_data()
print("Selected person:")
print("  ", given_name, last_name, suffix)

# Print found person's spouse(s)
print("Spouse(s):")
for spouse in parser.get_spouses(individual):
    given_name, last_name, suffix, sources = spouse.get_name_data()
    print("  ",given_name, last_name, suffix)

print("\nTraverse:")

level = 1

def traverse(person):
    global level
    given_name, surname = person.get_name()
    birth_date, birth_place, birth_sources = person.get_birth_data()
    death_date, death_place, death_sources = person.get_death_data()
    hyphens = "-" * level
    print(f"{level} {hyphens} {given_name} {surname} ({birth_date} - {death_date})")
    children = parser.get_children(person)
    if len(children) == 0:
        return
    else:
        level += 1
        for child in children:
            traverse(child)
        level -= 1

traverse(individual)