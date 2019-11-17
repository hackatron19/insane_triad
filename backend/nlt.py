import nltk
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
 #tokenize sentences
nouns = [] #empty to array to hold all nouns
#verbs = []#empty array to hold verbs
#djective=[] #empty array to hold adjectives
l2=[]
nouns = [] #empty to array to hold all nouns
#verbs = []

adjective=[]
import nltk
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
for sentence1 in l1:

    sentences = nltk.sent_tokenize(sentence1) #tokenize sentences
#empty array to hold verbs
    #empty array to hold adjectives
    for sentence in sentences:
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if not word  in stop_words:

                if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                    nouns.append(word)
                if (pos=='JJ' or pos == 'JJR' or  pos == 'JJS'):
                    adjective.append(word)