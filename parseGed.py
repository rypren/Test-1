from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

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
        print(f"Death: {death_data}")

        count = count + 1
print("Number of individuals: ", count)