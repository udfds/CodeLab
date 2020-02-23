import json

# ------------------------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------------------------

path_lang_target = '../WebApp/src/assets/i18n/en-lang.json'
path_lang_x0 = '../WebApp/src/assets/i18n/x0-lang.json'

# ------------------------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------------------------

def text_to_x0(text):
    ### Convert a text to the 0x format
    x0 = 'x'
    previous_char = ''
    for index, char in enumerate(text, start=1):
        if char is '{':
            x0 += '{'
        elif char is '}':
            x0 += '}'
        elif previous_char is '{':
            x0 += char
        else:
            x0 += '0'
        previous_char = char

    return x0

def convert_value(json_data):
    ### Read the json values to convert the text in 0x
    for key in json_data:
        value = json_data[key]
        type_data = type(value)
        if type_data is dict:
            convert_value(value)
        else:
            json_data[key] = text_to_x0(value)

# ------------------------------------------------------------------------------------------------
# Execution
# ------------------------------------------------------------------------------------------------

# Step 1 - Load the target - lang json
with open(path_lang_target) as file:
    json_data = json.load(file)

# Step 2 - Convert the text to x0
convert_value(json_data)

# Step 3 - Dump the x0 - lang json
with open(path_lang_x0, 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

print("")
print("..ciao!")
