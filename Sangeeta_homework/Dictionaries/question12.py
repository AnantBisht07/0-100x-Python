'''
You have marks = {"Priya": 85, "Arjun": 40, "Neha": 92, "Raj": 33}. Build a new dict containing
only the students who scored 50 or above.
'''
marks = {"Priya": 85, "Arjun": 40, "Neha": 92, "Raj": 33}
students_above_50 = {}
for name, mark in marks.items():
    if mark >= 50:
        students_above_50[name] = mark
#students_above_50 = {name: m for name, m in marks.items() if m >= 50}

print(students_above_50)