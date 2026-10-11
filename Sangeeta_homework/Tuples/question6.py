'''
A function should return a student's (total, average) from a tuple of marks. Write it, then call it and
print the average only.
'''
def summarize(marks):
    total = sum(marks)
    average = total/len(marks)
    return total, average

_, avg = summarize((80, 50, 90))
print(avg)