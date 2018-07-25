from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "this is an example of stop word filteration."
stop_words = set(stopwords.words("english"))

print(stop_words) # all set of stop words

words = word_tokenize(example_sent)

print words # user's set of words

filtered_words = [i for i in words if i not in stop_words]

print(filtered_words) # filtered words with meaning.