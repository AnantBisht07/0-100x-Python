#Given words = ["hi", "hello", "hey"], build a dict mapping each word to its length.
#Dict: { key: value for item in iterable if condition }
words = ["hi", "hello", "hey"]
dict_words = {word: len(word) for word in words}
print(dict_words)