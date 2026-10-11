#Print a numbered menu from menu = ["tea","coffee","juice"] starting the count at 1 (use enumerate's start)
menu = ["tea","coffee","juice"]
for item, index in enumerate(menu, start=1):
    print(f"{index}. {item}")