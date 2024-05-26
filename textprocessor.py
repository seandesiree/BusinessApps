import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

key_to_extract = "Occupation"

pattern = rf"{key_to_extract}: (.*?)(?=;|$)"  

match = re.search(pattern, text)

if match:
    extracted_value = match.group()
    print(f"The value for the key '{key_to_extract}' is: {extracted_value}")
else:
    print(f"No information found for the key '{key_to_extract}'")

