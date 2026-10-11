#Q16. Number the words in sentence = "the quick brown fox" as "1. the", "2. quick", and so on.
sentence = "the quick brown fox"
words = sentence.split()
for i, word in enumerate(sentence.split(), start=1):
    print(f"{i}. {word}")