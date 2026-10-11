#Q13. From items = ["x","y","z"], build a list of (index, value) tuples using enumerate.
items = ["x","y","z"]
positions = [(index, val) for index, val in enumerate(items)]
print(positions)