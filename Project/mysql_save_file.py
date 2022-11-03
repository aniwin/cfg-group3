# pip install mysql-connector-python

import mysql.connector
from config import USER, PASSWORD, HOST
import pathlib
import csv
import sys
import os

csv_path1 = pathlib.Path.cwd() / "date.csv"
csv_path2 = pathlib.Path.cwd() / "daily_scores.csv"




class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

import datetime as dt

save_data = {}

with csv_path1.open(mode="r") as csv_reader1:
    csv_reader1 = csv.reader(csv_reader1)
    for rows in csv_reader1:
        save_data.update({'date_created':rows[0]})

with csv_path2.open(mode="r") as csv_reader2:
    csv_reader2 = csv.reader(csv_reader2, delimiter=',')
    for rows in csv_reader2:
        save_data.update({'weather_score':rows[0], 'feed_pet_score':rows[1], 'rock_paper_scissors_score':rows[2]})
        break



def insert_new_record(save_data):
    global db_connection
    try:
        db_name = 'pet_database'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """INSERT INTO character_game_save ({}) VALUES ('{}', {}, {}, {})""".format(
            ', '.join(save_data.keys()),
            save_data['date_created'],
            save_data['weather_score'],
            save_data['feed_pet_score'],
            save_data['rock_paper_scissors_score']
        )
        cur.execute(query)
        db_connection.commit()  # VERY IMPORTANT, otherwise, rows would not be added or reflected in the DB!
        cur.close()


    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
        print("Record added to DB")



insert_new_record(save_data)


