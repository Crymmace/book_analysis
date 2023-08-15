import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

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

# Determine most positive/ negative chapters

analyzer = SentimentIntensityAnalyzer()

pattern2 = re.compile("Chapter [0-9]+")
chapters = re.split(pattern2, book)
chapters = chapters[1:]

for chapter in chapters:
    scores = analyzer.polarity_scores(chapter)

    if scores["pos"] > scores["neg"]:
        print("This chapter is a positive text.")
    else:
        print("This chapter is a negative text.")

