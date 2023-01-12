def main():
    import bag_of_words

    ans = bag_of_words.bag_of_words()
    #print(type(ans))

    import original_question

    ans1 = original_question.original_question()
    #print(ans1[0])

    import noun_extractor
    #ans2 = noun_extractor.noun_extractor('<p>How many planes (not types) are stored in relation departure?</p>\r\n<hr>\r\n\r\n<p></p>\r\n\r\n<p>{hints}<br>\r\n&nbsp;&nbsp;{hint title:Departure}select * from departure{/hint}<br>\r\n{/hints}</p>')
    #print(ans2)

    row = []
    for r in ans1:
        #print(r)
        a = noun_extractor.noun_extractor(r)
        row.append(a)
    #print(row)

    #print(row[0][1])
    print

    #print(ans[0][0])
    """for i in ans:
      #k=0
      #for j in row:
            w=str(ans1[k])
            #print(w)
            x=w.replace(str(j),str(i))
            #print(str(i))
            #print(x)
            k = k + 1)"""
    def replace():
        answ=[]
        j = 0
        for i in (ans):
            x=str(ans1[0]).replace('types',str(ans[j][0]))
            j = j + 1
            #print(x)
            answ.append(x)
        return answ
    a=replace()
    return a
#a=main()
#print(a[1])
