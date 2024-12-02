import numpy as np

file_path = "./input.txt"

def is_safe(list):
    deltas = np.diff(list)
    if 0 in deltas:
        return False
    mixed_signes = np.any(deltas > 0) and np.any(deltas < 0) 
    min_abs = np.min(np.abs(deltas))
    max_abs = np.max(np.abs(deltas))
    safe = not mixed_signes and min_abs >= 1 and max_abs <= 3
    return safe

num_safe = 0
maybe_safe = 0
# Open the file and process it
with open(file_path, 'r') as file:
    for line in file.readlines():
        l = np.array([int(x) for x in line.split()])
        # print(min_abs, max_abs)
        if is_safe(l):
            num_safe += 1
        else:
            lists_without_i = [np.concatenate((l[:i], l[i+1:])) for i in range(0, len(l))]
            for l_i in lists_without_i:
                if is_safe(l_i):
                    maybe_safe += 1
                    break
                
                
print(num_safe)
print(num_safe + maybe_safe)