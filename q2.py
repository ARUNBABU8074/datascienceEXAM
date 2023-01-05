import nltk
from nltk.corpus import stopwords

stop_words=set(stopwords.words('English'))
txt="This is the data science lab " \
    "Here we do lots of programs in python for our improvenment in meachine learing and data science." \
    "Proper utilization of this lab will help you in this sem exam." \
    "Otherwise you will be fail in exam." \
    "So be carefull and study well." \
    "Frist you need to concentrate in lecture."

tokenized=nltk.sent_tokenize(txt)

for i in tokenized:
    wordlist=nltk.word_tokenize(i)
    wordlist=[w for w in wordlist if w not in stop_words]

tagged=nltk.pos_tag(wordlist)
print(tagged)
