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
from gensim.scripts.glove2word2vec import glove2word2vec
def glovesim(text1,text2):
    import torch
    import torchtext
    a = list(text1)
    b = list(text2)
    # The first time you run this will download a ~823MB file
    glove = torchtext.vocab.GloVe(name="6B", # trained on Wikipedia 2014 corpus
                              dim=100)
    t=0
    for i in a:
          tensor1=glove[i]+t
          t=tensor1
    t1=0
    for i in b:
         tensor2=glove[b]+t1
         t1 = tensor2
    cos = torch.nn.CosineSimilarity(dim=0)
    print(tensor1)
    output=cos(tensor1, tensor2)
    return output
    #print(output)
from transformers import logging
logging.set_verbosity_error()
def bertembedding():
    import torch
    import torchtext
    from sent2vec.vectorizer import Vectorizer
    a=Vectorizer(pretrained_weights='distilbert-base-uncased', ensemble_method='average')
    sentences1= [
        "3a Changing table Update all Red Wines by increasing their vintage by 1 yearhints\xa0\xa0hint titleWineselect  from Winehinthints", #Original Question
        "3a Changing table Update all Aux Malconsorts Vosne-Romanee Premier Cru by increasing their vintage by 1 yearhints  hint titleVosne-Romanee Premier Cruelect  from Winehinthints" #Transformed Question
    ]
    vectorizer = Vectorizer()
    vectorizer.run(sentences1)
    vector1 = vectorizer.vectors
    #cos = torch.nn.CosineSimilarity(dim=0)
    from scipy import spatial
    output=1 - spatial.distance.cosine(vector1[0], vector1[1])
    print('The BertCosine similarity is:',output)


print('The cosine similarity is:', cosine_sim('3a Changing table Update all Red Wines by increasing their vintage by 1 yearhints\xa0\xa0hint titleWineselect  from Winehinthints" #Original Question', '3a Changing table Update all Aux Malconsorts Vosne-Romanee Premier Cru by increasing their vintage by 1 yearhints  hint titleVosne-Romanee Premier Cruelect  from Winehinthints'))#Original Question and #Transformed Question
#print('The gloveCosine similarity is:',glovesim('3a Changing table Update all Cappellano Cariad by increasing their vintage by 1 yearhints  hint titleCariadelect  from Winehinthints', '3a Changing table Update all Cappellano  Cariad by increasing their vintage by 1 yearhints  hint title Cariadelect  from Winehinthints'))
bertembedding()