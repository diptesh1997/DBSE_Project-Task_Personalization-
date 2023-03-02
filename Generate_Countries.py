def Generate_Countries(k):
    import pycountry

    country = list(pycountry.countries)
    list_countries = []
    i=0
    #for x in country:
    for x in country:
        if (i<k):
          a=x.name
          li = list(a.split(","))
          #print(li)
          list_countries.append(li)
          i=i+1
    #print(list_countries)
    #return(list_countries)
    import pymysql
    from mysql.connector import Error

    # database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="begineer_db")
    # connection1 = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_master")
    cursor = connection.cursor()

    # import main

    def execute_list_query(connection, sql, val):
        cursor = connection.cursor()
        try:
            cursor.executemany(sql, val)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
    sql="INSERT INTO `random countries` (`countries`) VALUES ( %s)"
    j = 0
    for i in list_countries:
        val = list_countries[j]
        # print(val)
        j = j + 1
        execute_list_query(connection, sql, val)

    connection.close()

    return(list_countries)


#a=Generate_Countries(190)
#print(a[0])