def main():
    #import Generate_Names
    #ans2 = Generate_Names.Generate_Names(10)#put half the number of what u want to generate
    #print(ans2)
    import bag_of_words#random names
    ans = bag_of_words.bag_of_words()
    print(ans)
    ans_ = bag_of_words.bag_of_words()
    print(ans_)
    ans__ = bag_of_words.bag_of_words()
    print(ans__)

    import bag_of_words1#random countries
    ans4 = bag_of_words1.bag_of_words1()
    print(ans4)
    ans4_ = bag_of_words1.bag_of_words1()
    print(ans4_)
    ans4__ = bag_of_words1.bag_of_words1()
    print(ans4__)

    import bag_of_words2  # random wine_names
    ans5 = bag_of_words2.bag_of_words2()
    print(ans5)
    ans5_ = bag_of_words2.bag_of_words2()
    print(ans5_)
    ans5__ = bag_of_words2.bag_of_words2()
    print(ans5__)
    #print(ans[0][0])

    import original_question

    ans1 = original_question.original_question() #For importing original questions from Original Database
    """"#ans1=[] #For selecting any random questions
    string1='3a Changing table Update all Red Wines by increasing their vintage by 1 yearhints\xa0\xa0hint titleWineselect  from Winehinthints'
    ans1=list(string1)"""
    #print(type(ans1))
    #print(ans1[1])
    #print(ans2)

    import D_L_model
    ans3=D_L_model.D_L_model(str(ans1))
    print(ans3)

    import noun_extractor

    #ans2 = noun_extractor.noun_extractor('<p>How many planes (not types) are stored in relation departure?</p>\r\n<hr>\r\n\r\n<p></p>\r\n\r\n<p>{hints}<br>\r\n&nbsp;&nbsp;{hint title:Departure}select * from departure{/hint}<br>\r\n{/hints}</p>')
    #print(ans2)

    row = []
    for r in ans1:
        #print(r)
        a = noun_extractor.noun_extractor(r)
        #print(a)
        row.append(a)
    print(len(row[0]))
    print(row[0])

    #def replace():
    answ = []
    def replace(t): #It can handle upto 3 proper Nouns in a sentences
        #answ = []
        #for p in range(len(row)):
        #for p in row[0]:#extracted proper nouns
           k=0
           w = str(ans1[k])  # original_questions
           if(t==1):#For Names
               if (len(row[0]) == 1):
                   for i in ans:
                       x = w.replace(str(row[0][0]), str(i[0]))
                       print(x)
                       answ.append(x)
               elif (len(row[0]) == 2):
                   for i, j in zip(ans, ans_):  # bag of words for names
                       x = w.replace(str(row[0][0]), str(i[0]))
                       x1 = x.replace(str(row[0][1]), str(j[0]))
                       print(x1)
                       answ.append(x1)
                       # print(answ)
               elif (len(row[0]) >= 3):
                   for i, j, y in zip(ans, ans_, ans__):  # bag of words for names
                       x = w.replace(str(row[0][0]), str(i[0]))
                       x1 = x.replace(str(row[0][1]), str(j[0]))
                       x2 = x1.replace(str(row[0][2]), str(y[0]))
                       print(x2)
                       answ.append(x2)
           if (t == 2):#For places
               # for j in row[0]:#for p in range(len(row)):
               if (len(row[0]) == 1):
                   for i in ans4:
                       x = w.replace(str(row[0][0]), str(i[0]))
                       print(x)
                       answ.append(x)
               elif (len(row[0]) == 2):
                   for i, j in zip(ans4, ans4_):  # bag of words for names
                       x = w.replace(str(row[0][0]), str(i[0]))
                       x1 = x.replace(str(row[0][1]), str(j[0]))
                       print(x1)
                       answ.append(x1)
                       # print(answ)
               elif (len(row[0]) >= 3):
                   for i, j, y in zip(ans4, ans4_, ans4__):  # bag of words for names
                       x = w.replace(str(row[0][0]), str(i[0]))
                       x1 = x.replace(str(row[0][1]), str(j[0]))
                       x2 = x1.replace(str(row[0][2]), str(y[0]))
                       print(x2)
                       answ.append(x2)
                   # print(answ)
           if (t == 3):#For wines
               # for j in row[0]:#for p in range(len(row)):
                 if(len(row[0])==1):
                   for i in ans5:
                       x = w.replace(str(row[0][0]), str(i[0]))
                       print(x)
                       answ.append(x)
                 elif(len(row[0])==2):
                   for i, j in zip(ans5, ans5_):  # bag of words for names
                       x = w.replace(str(row[0][0]), str(i[0]))
                       x1 = x.replace(str(row[0][1]), str(j[0]))
                       print(x1)
                       answ.append(x1)
                       # print(answ)
                 elif (len(row[0]) >= 3):
                   for i, j,y in zip(ans5, ans5_,ans5__):  # bag of words for names
                       x = w.replace(str(row[0][0]), str(i[0]))
                       x1 = x.replace(str(row[0][1]), str(j[0]))
                       x2 = x1.replace(str(row[0][2]), str(y[0]))
                       print(x2)
                       answ.append(x2)

           k = k + 1
           return answ

    if ans3 == "wine_names":
        a = replace(3)
        return a
    elif ans3 == "people":
        a = replace(1)
        return a
    elif ans3 == "places":
        a = replace(2)
        return a

    #a=replace()
    #return a
a=main()
#print(a)
