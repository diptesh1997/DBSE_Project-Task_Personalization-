import pymysql
from mysql.connector import Error

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="begineer_db")
#connection1 = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_master")
cursor = connection.cursor()
import main
ans = main.main()
print(ans)
# queries for inserting values

"""def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
sql="INSERT INTO `3a changing red wines` (`tskl_description`) VALUES ( %s)"
val = [('hyhhhh')]
j = 0
for i in ans:
     val=[(ans[j])]
     #print(val)
     j=j+1
     execute_list_query(connection, sql, val)"""



#query = "select name from studens where id IN {}".format(t)
"""for i in t:
  #print(t)
  insert1 = "INSERT INTO `2a insertions to producer` ( `tskl_title`,`tskl_description`) VALUES ()".format(t);"""

#Add the following entries to the example tables from the appendix using SQL The Johannishof Winery settled in the area Rheingau which is in the Hessen region hint title Creekselect  from Creek')
"""for i in ans:
    print(i)"""

#executing the quires
#cursor.execute(insert1)



#commiting the connection then closing it.
#connection.commit()
connection.close()