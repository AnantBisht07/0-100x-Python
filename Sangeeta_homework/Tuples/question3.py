'''
Given a list of (name, score) tuples, sort it so the highest score comes first, and print the sorted list.
'''

records = [("Priya", 85), ("Arjun", 92), ("Neha", 78)]
sorted_record = sorted(records, key=lambda record: records[1], reverse=True)
print(sorted_record)