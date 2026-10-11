'''
You are given two dicts of scores from two tests. Combine them so each student's value is the
SUM of both tests. t1 = {"a": 10, "b": 20}, t2 = {"b": 5, "c": 15}.
'''
t1 = {"a": 10, "b": 20}
t2 = {"b": 5, "c": 15}
combined = dict(t1)
for student, mark in t2.items():
    combined[student] = combined.get(student, 0) + mark
print(combined)