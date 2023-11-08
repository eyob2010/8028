# -*- encoding: utf-8 -*-


import os, random, string, psycopg2

con = psycopg2.connect(
    database="8028T",
    user="postgres",
    password="Pass#19",
    host="localhost",
    port='5432'
)
cursor_obj = con.cursor()

SECRET_KEY = os.getenv('SECRET_KEY', None)
