import nltk
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
sentences = nltk.sent_tokenize(input()) #tokenize sentences
nouns = [] #empty to array to hold all nouns
verbs = []#empty array to hold verbs
adjective=[] #empty array to hold adjectives
for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if not word  in stop_words:

            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                 nouns.append(word)
            if ( pos=='VB' or  pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos =='VBZ'):
                 verbs.append(word)
            if (pos=='JJ' or pos == 'JJR' or  pos == 'JJS'):
                 adjective.append(word)



def combine(l1,l2):
     return (l1+"_"+l2)

