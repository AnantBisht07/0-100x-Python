#Q8. Given subjects = ["math","art","science"] and marks = [80,40,65], build a list of only the subjects where the mark is 50 or above.
subjects = ["math","art","science"] 
marks = [80,40,65]
subjects_above_50 = [subject for subject, mark in zip(subjects, marks) if mark >= 50]
print(subjects_above_50)