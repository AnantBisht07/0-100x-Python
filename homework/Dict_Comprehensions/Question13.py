#From marks = {"Priya": 85, "Arjun": 40, "Neha": 92}, build a new dict keeping only students
#who scored 50 or above.

marks = {"Priya": 85, "Arjun": 40, "Neha": 92}
scored_above_50 = {student : mark for student, mark in marks.items() if mark >= 50}
print(scored_above_50)