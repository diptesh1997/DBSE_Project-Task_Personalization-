import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="begineer_db")
#connection1 = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_master")
cursor = connection.cursor()
import main
ans = main.main()
#print(ans)
# queries for inserting values
"""j=0
for i in ans:
    #print(type(i))
    insert1 = "INSERT INTO  transformed_question (questions) VALUES (%s);" % ','(tuple(ans[j]));
    #print "INSERT INTO table VALUES %r;" % (tuple(varlist),)
    j=j+1
params = ['?' for item in ans]
sql = 'INSERT INTO transformed_question (questions) VALUES (%s);' % ','.join(params)
cursor.execute(sql,params)"""
for i in ans:
    print(i)

#executing the quires
#cursor.execute(insert1)



#commiting the connection then closing it.
connection.commit()
connection.close()