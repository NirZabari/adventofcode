import re

# ==============================================================================
# Part 1
# ==============================================================================

file = "./input.txt"
with open(file, 'r') as f:
    s = f.read()

regex = re.compile(r"mul\(\d*,\d*\)")

total_prod = 0
for match in regex.findall(s):
    match = match[4:-1]
    num1, num2 = [int(x) for x in match.split(",")]
    prod = num1 * num2
    total_prod += prod
print(total_prod)

# ==============================================================================
# Part 2
# ==============================================================================

regex = re.compile(r"mul\(\d*,\d*\)|don\'t\(\)|do\(\)")

total_prod = 0
mult = 1
for match in regex.findall(s):
    if match == "don't()":
        mult = 0
    elif match == "do()":
        mult = 1
    else:
        match = match[4:-1]
        num1, num2 = [int(x) for x in match.split(",")]
        prod = num1 * num2 * mult
        total_prod += prod
        
print(total_prod)
