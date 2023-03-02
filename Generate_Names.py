def Generate_Names(k):
    ans = []
    import names

    for i in range(k):
        a = names.get_first_name()
        li = list(a.split(" "))
        #print(li)
        ans.append(li)
        #print(ans)

    #return ans
    import pymysql
    from mysql.connector import Error

    #database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="begineer_db")
    #connection1 = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_master")
    cursor = connection.cursor()
    #import main
    #ans = main.main()
    #print(ans)

    """def execute_list_query(connection, sql, val):
        cursor = connection.cursor()
        try:
            cursor.executemany(sql, val)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
    sql="INSERT INTO `random names` (`names`) VALUES ( %s)"
    #val = [('hyhhhh')]
    j = 0
    for i in ans:
         val=ans[j]
         #print(val)
         j=j+1
         execute_list_query(connection, sql, val)

    connection.close()"""
    return ans

#a=Generate_Names(5)
#print(a)