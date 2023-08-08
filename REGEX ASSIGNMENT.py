#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
string = 'Python Exercises, PHP exercises.'
pattern="[ ,.]"
replace= ":"
result=re.sub(pattern,replace,string)
print(result)


# In[10]:


import re
string='The age of this element is age of the effect of work'
pattern="[ae]\w+"
result=re.findall(pattern,string)
print(result)


# In[17]:


import re

def word_lenght(string):
    pattern = re.compile(r'\b\w{4,}\b')
    result = pattern.findall(string)
    return result

string= 'The age of this element is age of the effect of work'
result = find_long_words(string)
print(result)


# In[18]:


import re

def word_lenght(string):
    pattern = re.compile(r'\b\w{3,5}\b')
    result = pattern.findall(string)
    return result

string = 'The age of this element is age of the effect of work'
result = find_words_by_length(string)
print(result)


# In[30]:


import re

def remover(strings_list):
    pattern = re.compile(r'\s*\([^)]*\)\s*')
    cleaned = [pattern.sub('', string) for string in strings_list]
    return cleaned

strings =  ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
output_strings = remover(strings)
for output_string in output_strings:
    print(output_string)


# In[52]:


import re

def remove_parentheses(text):
    pattern = re.compile(r'\s*\([^)]*\)\s*')
    cleaned_text = pattern.sub('', text)
    return cleaned_text

input_file = "input_text.txt"
output_file = "output_text.txt"

with open(input_file, 'r') as file:
    input_text = file.read()

cleaned_text = remove_parentheses(input_text)

with open(output_file, 'w') as file:
    file.write(cleaned_text)

print("Parentheses removed and cleaned text saved to", output_file)


# In[49]:


import re

string = "ImportanceOfRegularExpressionsInPython"
pattern = '[A-Z][^A-Z]*'
uppercase= re.findall(pattern,string)

print(uppercase)


# In[90]:


import re

def spaces(text):
    code = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)
    return code

string = "RegularExpression1IsAn2ImportantTopic3InPython"
result = spaces(string)
print(result)


# In[96]:


import re

def spaces(text):
    pattern= re.sub(r'([A-Z\d])([a-z])',r'\1 \2', text)
    return pattern

string= "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces(string)
print(result)


# In[ ]:


import re
with open("C:\Users\user\Desktop\input_text.txt") as file:
        for line in file:
            ty=re.findall('http?://(?:[-\w.]|(?:%[\da-zA-z0-9]{2}))+',line)
            print(ty)


# In[82]:


import re

def string (input):
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    return bool(pattern.match(input))

test_strings = [
    "Valid_String_123",
    "Invalid!@String",
    "Another_Valid_String",
    "123_456",
    "_Underscore_Start",
    "Ends_With_Underscore_",
]

for string in strings:
    if is_valid_string(string):
        print(f'"{string}" is a valid string.')
    else:
        print(f'"{string}" is not a valid string.')


# In[81]:


def starts(input_string, specific_number):
    return input_string.startswith(str(specific_number))

test_strings = [
    "55892Good",
    "50506Light",
    "890How",
    "Zinos123",
    "26304Python",
]

number = 411

for string in test_strings:
    if starts_with_number(string, number):
        print(f'"{string}" nice specail number {number}.')
    else:
        print(f'"{string}" nice specail number {number}.')


# In[97]:


def zeros(ip_address):
    components = ip_address.split('.')
    cleaned= [str(int(component)) for component in components]
    clear_ip = '.'.join(cleaned)
    return clear_ip

addresses = [
    "172.158.001.001",
    "020.020.020.010",
    "000.234.066.009",
    "004.003.002.002",
]

for ip in addresses:
    clear_ip = zeros(ip)
    print(f'Original IP: {ip} | Cleaned IP: {clear_ip}')


# In[104]:


import re

sample_text = 'On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country'

result = re.findall(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}\b', sample_text)

print(result)


# In[115]:


def search_words(text, words):
   found_words = [word for word in searched_words if word in text]
   return found_words

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

found_words = search_words(sample_text, searched_words)

for word in found_words:
   print(f'Found: "{word}"')


# In[117]:


def search_literal_with_location(text, search_string):
    found_locations = []
    start = 0      
    while start < len(text):
        index = text.find(search_string, start)
        if index == -1:
            break
        found_locations.append(index)
        start = index + 1

    return found_locations

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

found_locations = search_literal_with_location(sample_text, searched_word)

if found_locations:
    print(f'Found "{searched_word}" at locations: {found_locations}')
else:
    print(f'"{searched_word}" not found in the text.')


# In[118]:


def find_substrings(text, pattern):
    substrings = []
    index = text.find(pattern)
    
    while index != -1:
        substrings.append(index)
        index = text.find(pattern, index + 1)
    
    return substrings

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
substring_positions = find_substrings(sample_text, pattern)

if substring_positions:
    print(f'Pattern "{pattern}" found at positions: {substring_positions}')
else:
    print(f'Pattern "{pattern}" not found in the text.')


# In[119]:


def find_substrings_with_positions(text, substring):
   occurrences = []
   index = text.find(substring)
   while index != -1:
       occurrences.append((substring, index))
       index = text.find(substring, index + 1)
   
   return occurrences

sample_text = 'Python exercises, PHP exercises, C# exercises'
substrings = ['exercises', 'Python', 'C#']

for substring in substrings:
   occurrences = find_substrings_with_positions(sample_text, substring)
   
   if occurrences:
       print(f'Substring "{substring}" found at:')
       for occurrence in occurrences:
           print(f' - Position: {occurrence[1]}')
   else:
       print(f'Substring "{substring}" not found in the text.')


# In[120]:


def convert_date(input_date):
    parts = input_date.split('-')
    if len(parts) == 3:
        year, month, day = parts
        output_date = f'{day}-{month}-{year}'
        return output_date
    else:
        return "Invalid date format"

input_date = "2023-08-07"
converted_date = convert_date(input_date)
print(f'Original date: {input_date} | Converted date: {converted_date}')


# In[123]:


import re

def numbers(input_string):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    decimal_numbers = pattern.findall(input_string)
    return decimal_numbers

input_string = "The prices are 1.2, 7.6, 5.8, and 17.2 dollars."
result = numbers(input_string)
print(result)


# In[ ]:




