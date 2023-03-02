def original_question():
    import pymysql
    import re
    from bs4 import BeautifulSoup
    #database connection
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="sqlvali_data")
    #mysqli_connect('localhost','root','','beginner_db');
    cursor = connection.cursor()

    # queries for retrievint all rows
    retrive = "select tskl_title, tskl_description from task_localization where tskl_lang = 'en' and tskl_id = '578' and tskl_tsk_id in (SELECT tsk_id FROM `task` WHERE tsk_sem_id = '9');" #Different tskl ids:612,616,606,610,(572),580,(578),576,574,(583),(563),559,561,565,556,566,568,570,535
    #retrive = "select tskl_description from task_localization where tskl_lang = 'en' and tskl_tsk_id in (select tskgl_id from task_group_localization where tskgl_tskg_id in (select tskg_id from task_group where tskg_sem_id='9'));"
    #select * from task_localization where tskl_tsk_id in (select tskgl_id from task_group_localization where tskgl_tskg_id in (select tskg_id from task_group where tskg_sem_id='10'))

    #1:- Flugzeugtyp and tskl_title = '(a) Number of Planes'
    #3: Flug

    #executing the quires
    cursor.execute(retrive)
    rows = cursor.fetchall()
    row2 = []
    for row in rows:
        #print(row)
        soup = BeautifulSoup(str(row), features="html.parser")
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        a1 = re.sub(r'[^\w\s\r]', '', text)
        x = a1.replace('rn', ' ')
        x = x.replace('tttt', ' ')
        #print(x)
        row2.append(x)
        #print(row2)
    return(row2)


    #commiting the connection then closing it.
    connection.commit()
    connection.close()

#a=original_question()
#print(a)