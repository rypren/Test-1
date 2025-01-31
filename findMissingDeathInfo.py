from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

import gedcom.tags

# Path to your GEDCOM file
gedcom_file = "rypren Släktträd 250131.ged"

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

        (bdate, bplace, bextra) = birth_data
        (ddate, dplace, dextra) = death_data

        if (death_data[0] == "" and death_data[1] != "") or (death_data[0] != "" and death_data[1] == "") or (name[1] == "Okänd"):
            print(f"Name: {name}")
            print("Birth: ", bdate, " ", bplace)
            print("Death: ", ddate, " ", dplace)
            count = count + 1

print("Number of individuals: ", count)