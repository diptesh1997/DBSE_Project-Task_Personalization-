import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import jaccard_score

#nltk.download('punkt') # if necessary...


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

#def jaccard_score(text1, text2):
    #return jaccard_score(text1, text2)


print(cosine_sim('a little bird', 'a little bird'))
#print(jaccard_score('a little bird', 'a little boy'))
