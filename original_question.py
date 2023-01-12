def original_question():
    import pymysql
    import re
    from bs4 import BeautifulSoup
    #database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_data")
    #mysqli_connect('localhost','root','','beginner_db');
    cursor = connection.cursor()

    # queries for retrievint all rows
    retrive = "select tskl_description from task_localization where tskl_lang = 'en' and tskl_tsk_id in (select tskgl_id from task_group_localization where tskgl_tskg_id in (select tskg_id from task_group where tskg_sem_id='9'));"
    #select * from task_localization where tskl_tsk_id in (select tskgl_id from task_group_localization where tskgl_tskg_id in (select tskg_id from task_group where tskg_sem_id='10'))
    #1:- Flugzeugtyp and tskl_title = '(a) Number of Planes'
    #3: Flug

    #executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    row2 = []
    for row in rows:
        a=str(row)
        #print(row)
        cleantext = BeautifulSoup(a, "lxml").text
        a1 = re.sub(r'[^\w\s\r]', '', cleantext)
        #a1 = re.sub('(?is)</html>.+<p>', ' ', a)
        #print(a)
        row2.append(a1)
        #page = BeautifulSoup.find_all(cleantext,'p').text()
        #print(cleantext)
    return(row2)


    #commiting the connection then closing it.
    connection.commit()
    connection.close()

#original_question()