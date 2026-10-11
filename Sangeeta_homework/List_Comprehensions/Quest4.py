#From the sentence "the quick brown fox", build a list of the words that are longer than 3 letters.
sentence = "the quick brown fox"
words = sentence.split()
new_list = [word for word in words if len(word) > 3]
print(new_list)