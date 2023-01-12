import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="begineer_db")
#connection1 = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_master")
cursor = connection.cursor()
#insert1 = "INSERT INTO  transformed_question (questions) VALUES ('List all plane   A-318  Thereby all first letters must be capitalized the rest must be uncapitalized Return the length of the type name in a second column The columns are called name und length');"
#insert1 = "INSERT INTO  transformed_question (questions) VALUES ('List all plane  boeing 747-400  Thereby all first letters must be capitalized the rest must be uncapitalized Return the length of the type name in a second column The columns are called name und length');"
#insert1 = "INSERT INTO  transformed_question (questions) VALUES ('List all plane A-340 Thereby all first letters must be capitalized the rest must be uncapitalized Return the length of the type name in a second column The columns are called name und length');"
#insert1 = "INSERT INTO  transformed_question (questions) VALUES ('List all plane A-380 Thereby all first letters must be capitalized the rest must be uncapitalized Return the length of the type name in a second column The columns are called name und length');"
#insert1 = "INSERT INTO  transformed_question (questions) VALUES ('List all plane Boeing 747-300 Thereby all first letters must be capitalized the rest must be uncapitalized Return the length of the type name in a second column The columns are called name und length');"
#insert1 = "INSERT INTO  transformed_question (questions) VALUES ('List all plane Boeing 777 Thereby all first letters must be capitalized the rest must be uncapitalized Return the length of the type name in a second column The columns are called name und length');"
#insert1 = "INSERT INTO  transformed_question (questions) VALUES ('List all plane TRIDENT Thereby all first letters must be capitalized the rest must be uncapitalized Return the length of the type name in a second column The columns are called name und length');"
insert1 = "INSERT INTO  questions (questions) VALUES ('List all plane types Thereby all first letters must be capitalized the rest must be uncapitalized Return the length of the type name in a second column The columns are called name und length');"

cursor.execute(insert1)


#commiting the connection then closing it.
connection.commit()
connection.close()