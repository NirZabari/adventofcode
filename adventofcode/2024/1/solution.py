file_path = "./input.txt"

# Open the file and process it
with open(file_path, 'r') as file:
    lines = [
        (l.split()[0], l.split()[1])  # Assuming each line has at least two space-separated items
        for l in file.readlines()
    ]

list_1 = sorted([float(x[0]) for x in lines])
list_2 = sorted([float(x[1]) for x in lines])
diff = sum([abs(list_1[i] - list_2[i]) for i in range(len(list_1))])
    
print(diff)

# a dictionary with each value as key and the number of times it appears as value

value_counts = {}
for x in list_2:
    value_counts[x] = value_counts.get(x, 0) + 1
    
similarity_score = 0
for x in list_1:
    if x in value_counts and value_counts[x] > 0:
        similarity_score += x * value_counts[x]

print(similarity_score)