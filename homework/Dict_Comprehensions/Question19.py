#Given records = [("Priya", 85), ("Arjun", 40), ("Neha", 92)], build a dict {name: score}, keeping only scores of 50 or above.

records = [("Priya", 85), ("Arjun", 40), ("Neha", 92)]
score_above50 = {name: score for name, score in records.it }