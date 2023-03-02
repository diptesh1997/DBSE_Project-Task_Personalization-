def bag_of_words1():
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


    # queries for retrievint all rows
    retrive = "SELECT countries FROM `random countries` ORDER BY RAND() LIMIT 10"#To control the number of generated Questions for Countries
    #print(rows3)
        #"select vineyard from `producer"
        #"select typ from Flugzeugtyp"

    #executing the quires
    #executing the quires
    #cursor1.execute(retrive)
    cursor1.execute(retrive)
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

#a=bag_of_words1()
#print(a)
#print(a[6])