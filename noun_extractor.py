def noun_extractor(text):
    import nltk

    #nltk.download('stopwords')
    #nltk.download('punkt')
    #nltk.download('averaged_perceptron_tagger')
    from nltk.corpus import stopwords

    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.append("Write")
    stopwords.append("=")
    stopwords.append("*")
    stopwords.append("Select")
    stopwords.append("AND")
    stopwords.append(">")
    stopwords.append("<")
    stopwords.append("/p")
    stopwords.append("(")
    stopwords.append(")")
    stopwords.append("'")
    stopwords.append(",")
    from nltk.tokenize import word_tokenize, sent_tokenize


    def ProperNounExtractor(text):
         #print('PROPER NOUNS EXTRACTED :')

        sentences = nltk.sent_tokenize(text)
        for sentence in sentences:
            words1 = []
            words = nltk.word_tokenize(sentence)
            words = [word for word in words if word not in set(stopwords)]
            tagged = nltk.pos_tag(words)
            for (word, tag) in tagged:
                if tag == 'NNP':  # If the word is a proper noun
                    words1.append(word)
                    # print(word)
        return(words1)
    a= ProperNounExtractor(text)
    return a


