'''
Given students = {"Priya": [80, 90], "Arjun": [60, 70]} (each value is a list of marks), print each
student's average.
'''
students = {"Priya": [80, 90], "Arjun": [60, 70]} 
for student, marks in students.items():
    avg = sum(marks)/len(marks)
    print(f"{student} average is {avg}")
