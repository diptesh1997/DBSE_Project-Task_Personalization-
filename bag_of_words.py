def bag_of_words():
    import pymysql
    import nltk
    #nltk.download('punkt')
    from bs4 import BeautifulSoup
    #database connection

    connection1 = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_master")
    #mysqli_connect('localhost','root','','beginner_db');
    cursor1 = connection1.cursor()

    # queries for retrievint all rows

    retrive1 = "select typ from Flugzeugtyp"

    #executing the quires
    #executing the quires
    cursor1.execute(retrive1)
    rows1 = cursor1.fetchall()
    row2 = []
    #return rows1
    for row in rows1:
        row2.append(row)
    return(row2)
        #print(row)
        #return(row)


    connection1.commit()
    connection1.close()

#a=bag_of_words()
#print(a)
#print(a[6][0])