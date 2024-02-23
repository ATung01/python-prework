message = """My dog has fleas
and charm."""
print(message)

"""
testing commenting with delimiting with 3 quotes

yada yada

"""

message = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad 
minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(message)
message = "My dog has fleas\nand \"charm\"."

print(message)
shrug = "¯\\_(ツ)_/¯"
print(shrug) # ¯\_(ツ)_/¯

dozen = 12
message = f"{dozen} is a dozen."
print(message)

elements = "hydrogen helium lithium"
helium = "helium"
elements_contain_helium = helium in elements
print(elements_contain_helium) #True

value = "  \nnoodles\t  \r\n"
print(value)
#
# noodles<tab>
#

stripped = value.strip()
print(stripped)  # noodles

value = "aaanoodlesbbba"
print(value)  # aaanoodlesbbb

stripped = value.strip("ab")
print(stripped)  # noodles

strip_front = value.lstrip("ab")
print(strip_front)  # noodlesbbb

strip_back = value.rstrip("ab")
print(strip_back)  # aaanoodles

message = "baked apples"

# value[start:end:step]

substring = message[:5]
print(substring)  # baked

substring = message[6:]
print(substring)  # apples

substring = message[1:4]
print(substring)  # ake

substring = message[-5:-2]
print(substring)  # ppl


message = "Grouper, Halibut, and Trout"
vowels = "aeiou"
print(vowels.find("o"))