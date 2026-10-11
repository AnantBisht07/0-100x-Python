#Given names = ["Priya","Arjun"] and scores = [85,92], loop with zip and print each as "name: score".
names = ["Priya","Arjun"]
scores = [85,92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")