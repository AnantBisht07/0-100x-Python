'''
Given sentence = "the cat sat on the mat the cat", build a dict counting how many times each
word appears, then print the most frequent word.
'''

sentence = "the cat sat on the mat the cat"
#split
sentences = sentence.split(" ")
word_frequency = {}
print(sentences)
for word in sentences:
    word_frequency[word] = word_frequency.get(word, 0) + 1
most = max(word_frequency, key=word_frequency.get)
print(word_frequency)
print(most)