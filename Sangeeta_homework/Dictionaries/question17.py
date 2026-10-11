'''
Group a list of words by their first letter. From words = ["apple", "banana", "avocado",
"cherry", "blueberry"], build a dict like {"a": [...], "b": [...], ...}.
'''

words = ["apple", "banana", "avocado", "cherry", "blueberry"]
groups = {}
for word in words:
    first = word[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(word)
print(groups)