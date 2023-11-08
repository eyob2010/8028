# -*- encoding: utf-8 -*-


import os, random, string, psycopg2

try:
    con = psycopg2.connect(
    database="8028T",
    user="postgres",
    password="Pass#19",
    host="localhost",
    port='5432'
    )
    cursor_obj = con.cursor()

    postgres_insert_query = """ INSERT INTO name (fullname, email) VALUES (%s,%s)"""
    record_to_insert = ('Another Name', 'anothername@hotmail.com')
    cursor_obj.execute(postgres_insert_query, record_to_insert)

    con.commit()
    count = cursor_obj.rowcount
    print(count, "Record inserted successfully into name table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if con:
        cursor_obj.close()
        con.close()
        print("PostgreSQL connection is closed")

#SECRET_KEY = os.getenv('SECRET_KEY', None)
#cursor_obj.execute("insert into name (fullname, email) values ('Eyob Mersha', 'e.mersha@gmail.com');")
#cursor_obj.execute("select * from name")
#result = cursor_obj.fetchall()
#print("List of Names: \n", result)
