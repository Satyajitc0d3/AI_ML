# import nltk
#
# nltk.download()

from nltk.tokenize import sent_tokenize,word_tokenize
#
example_text = "Hello Mr. Smith, How are you doing today? the weather is greate today and python is awesome. The sky is pinkish-blue."
sentarr = sent_tokenize(example_text)
wordarr = word_tokenize(example_text) #by default is recognize ponctuation as a word.
print sentarr
print wordarr







