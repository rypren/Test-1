from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

import gedcom.tags

# Path to your GEDCOM file
gedcom_file = "rypren Släktträd 240310 - may-oct.ged"

# Initialize the parser
gedcom_parser = Parser()
gedcom_parser.parse_file(gedcom_file)

# Get the root element
root_elements = gedcom_parser.get_element_list()

# Iterate through root elements
count = 0
for element in root_elements:
    if isinstance(element, IndividualElement):
        name = element.get_name()
        birth_data = element.get_birth_data()
        death_data = element.get_death_data()

        print(f"Name: {name}")
        print(f"Birth: {birth_data}")
        if death_data[1] != "":
            print(f"Death: {death_data}")
        else:
            print("Death: Still alive")

        count = count + 1
print("Number of individuals: ", count)

print("======================================================")

for element in gedcom_parser.get_root_child_elements():
    if element.get_tag() == gedcom.tags.GEDCOM_TAG_INDIVIDUAL:
        for child in element.get_child_elements():
            if child.get_tag() == gedcom.tags.GEDCOM_TAG_NAME:
                print(child.get_value())