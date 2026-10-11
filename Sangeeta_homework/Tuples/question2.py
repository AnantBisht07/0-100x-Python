'''
Given records = [("Priya", 85), ("Arjun", 92), ("Neha", 78)], find the name of the person with the
highest score. Do it without sorting.
'''

records = [("Priya", 85), ("Arjun", 92), ("Neha", 78)]
best_score = -1
best_name = ""
for name, score in records:
    if score > best_score:
        best_name , best_score = name, score

print(f"Best scorer is {best_name}")
        