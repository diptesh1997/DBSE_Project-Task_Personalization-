def Insert_Wine_Names():
    #ans = []
    import pandas as pd
    data = pd.read_csv(r'C:\xampp\htdocs\Begineer\wine_name.csv')
    # print(type(data_list))
    ans1 = data.iloc[:, 1:2].values.tolist()
    ans = []
    for i in ans1:
        li1 = str(i).replace("]", "")
        li2 = str(li1).replace("[", "")
        li3 = str(li2).replace("'", "")
        li = list(li3.split(","))
        print(li)
        ans.append(li)

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

    def execute_list_query(connection, sql, val):
        cursor = connection.cursor()
        try:
            cursor.executemany(sql, val)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
    sql="INSERT INTO `wine_names` (`names`) VALUES ( %s)"
    #val = [('hyhhhh')]
    j = 0
    for i in ans:
         val=ans[j]
         #print(val)
         j=j+1
         execute_list_query(connection, sql, val)

    connection.close()
    return ans

#a=Insert_Wine_Names()
