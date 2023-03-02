def bag_of_words():
    import pymysql
    import nltk
    #nltk.download('punkt')
    from bs4 import BeautifulSoup
    #database connection

    #connection1 = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_master")
    connection1 = pymysql.connect(host="localhost", user="root", passwd="", database="begineer_db")
    #mysqli_connect('localhost','root','','beginner_db');
    cursor1 = connection1.cursor()
    #cursor2 = connection1.cursor()

    retrive = "SELECT names FROM `random names` ORDER BY RAND() LIMIT 10" #To control the number of generated Questions for Names
    cursor1.execute(retrive)
    rows3 = cursor1.fetchall()
    row2 = []
    #return rows1
    for row in rows3:
        row2.append(row)
    return(row2)
        #print(row)
        #return(row)


    connection1.commit()
    connection1.close()

#a=bag_of_words()
#print(a)
#print(a[6])