def D_L_model(text):
    from transformers import pipeline

    classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
    labels = ["wine_names", "people", "places"]
    hypothesis_template = 'This text is about {}.'
    #sequence = "I am going to Berlin"
    #print(type(text))
    sequence = text
    prediction = classifier(sequence, labels, hypothesis_template=hypothesis_template, multi_label=True)

    #print(prediction)
    t = list(prediction.values())
    #print(t[1][0])
    return(t[1][0])

#a=D_L_model("3a Changing table Update all Red Wines by increasing their vintage by 1 yearhints\xa0\xa0hint titleWineselect  from Winehinthints")
#print(a)