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

def listParents(parents, indent):
    print("Parents:")
    for parent in parents:
        given_name, surname = parent.get_name()
        print(indent, given_name, surname)

def getParents(person):
    parents = parser.get_parents(person)
    if len(parents) > 0:
        listParents(parents, "1 ")
        return parents
    else:
        return None

parents = getParents(individual)

# Print found person's parents.
# parents = parser.get_parents(individual)
# if len(parents) > 0:
#     listParents(parents, "1 ")

# Print found person's grandparents
if len(parents) > 0:
    for parent in parents:
        grandparents = parser.get_parents(parent)
        listParents(grandparents, "2 ")
        if len(grandparents) > 0:
            for grandparent in grandparents:
                grand_grandparents = parser.get_parents(grandparent)
                listParents(grand_grandparents, "3 ")
                if len(grand_grandparents) > 0:
                    for grand_grandparent in grand_grandparents:
                        grand_grand_grandparents = parser.get_parents(grand_grandparent)
                        listParents(grand_grand_grandparents, "4 ")
