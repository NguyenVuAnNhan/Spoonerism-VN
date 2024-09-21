import re

def generate_regex_from_file(file_path):
    # Read the file and split lines
    with open(file_path, 'r', encoding='utf-8') as file:
        syllables = file.read().splitlines()
    
    # Escape any special characters in the syllables
    escaped_syllables = [re.escape(syllable) for syllable in syllables]
    
    # Combine syllables using '|' and ensure exact match
    pattern = r'^(?:' + '|'.join(escaped_syllables) + r')$'
    
    return pattern

# Usage
file_path = "LuomTV-amtiet-tiengViet.txt"
regex_pattern = generate_regex_from_file(file_path)

# string = "nứng"
#
# print(bool(re.match(regex_pattern, string)))

