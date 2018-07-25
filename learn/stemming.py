from nltk.stem import PorterStemmer

from nltk import word_tokenize

ps = PorterStemmer()

example_words = ['python','pythoning','pythoned','pythoner']
op = [ ps.stem(i)  for i in example_words]

print(op)