def Edge_cases(ans1,row):#row[0]=extracted nouns,ans1=original questions,ans3_1= DL Tags
        import nltk
        #print(row)
        #print(ans1)
        #print(len(row))
        from nltk import pos_tag, word_tokenize
        from nltk.corpus import stopwords
        #stopwords = stopwords.words('english')
        #stopwords = []
        sentences = nltk.sent_tokenize(ans1)
        for sentence in sentences:
            a = []
            words = nltk.word_tokenize(sentence)
            #words = [word for word in words if word not in set(stopwords)]
            tagged = nltk.pos_tag(words)
            for i in tagged:
               #print(i)````````````````````````````
               a.append(i)
        #text = word_tokenize(str(ans1))#original questions
        #a=pos_tag(text)
        #print(row)
        #print(len(row))
        a1=[]
        k=0
        #print(len(ans1))
        p=0
        for i in a:
            #print(1)
            if(a[k][1]=='NNP'):

                #for t in row:
                    #p=0
                    if((a[k][0])==row[p]):
                      if (p <= len(row)):
                          #print(p)
                          #print(row[0][p])
                          #print(a[k][0])
                          import D_L_model
                          ans3 = D_L_model.D_L_model(row[p])
                          if(ans3=="people"):
                              import bag_of_words  # random names
                              ans = bag_of_words.bag_of_words()
                              a1_1 = str(a[k][0]).replace(a[k][0],str(ans[0][0]))
                              a1.append(a1_1)
                              #print(a1)
                              #k=k+1
                              #break
                          if (ans3 == "places"):
                              import bag_of_words1  # random countries
                              ans4 = bag_of_words1.bag_of_words1()
                              a1_1 = str(a[k][0]).replace(a[k][0],str(ans4[0][0]))
                              a1.append(a1_1)
                              #p=p+1
                              #print(a1)
                          if (ans3 == "wine_names"):
                              import bag_of_words2  # random wine_names
                              ans5 = bag_of_words2.bag_of_words2()
                              a1_1 = str(a[k][0]).replace(a[k][0], str(ans5[0][0]))
                              a1.append(a1_1)
                          k=k+1
                          p=p+1
                    else:
                      a1.append(a[k][0])
                      k=k+1
                      #p=p+1



            else:
                      a1.append(a[k][0])
                      k=k+1
                      #p=p+1
            #p=0

        print(list(a1))
        return(list(a1))


#for i in range(2):#how much questions u want to generate
  #a=Edge_cases('2a Insertions to Producer         Add the following entries to the example tables from the appendix using SQL              The Johannishof Winery settled in the area Rheingau which is in the Hessen region     hints\xa0\xa0hint titleProducerselect  from Producerhinthints ',['Producer', 'Johannishof', 'Rheingau', 'Hessen'])
  #i=i+1