'''
You are given two tuples names = ("Priya", "Arjun", "Neha") and scores = (85, 92, 78). Pair
them up into a list of (name, score) tuples using zip.
'''

names = ("Priya", "Arjun", "Neha")
scores = (85, 92, 78)
paired = list(zip(names, scores))
print(paired)