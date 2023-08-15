import re
import nltk
from nltk.corpus import stopwords

with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()

# Find all sentences containing the word "love"
pattern_love = re.compile("[A-Z][^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.", re.UNICODE)
findings_love = re.findall(pattern_love, book)


pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

# Filter by stop words
d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)

english_stopwords = stopwords.words("english")

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))




