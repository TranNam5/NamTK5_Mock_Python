import mysql_db
import common
from create import *
import os

DATABASE_CONFIG_PATH = '../database_config.json'

if __name__ == '__main__':
    config = common.load_json(DATABASE_CONFIG_PATH)
    connect_status, cnx = mysql_db.mysql_connect(config)
    while not connect_status:
        print(cnx)
        os.system('notepad.exe {}'.format(DATABASE_CONFIG_PATH))
        config = common.load_json(DATABASE_CONFIG_PATH)
        connect_status, cnx = mysql_db.mysql_connect(config)

    cursor = cnx.cursor()
    use_db = mysql_db.use_database(cursor, config['database_name'])
    if use_db is False:
        create_database(cursor, config['database_name'])

    # mysql_db.create_table
    create_table(cnx, cursor, 'hospital', hospital_table)
    create_table(cnx, cursor, 'doctor', doctor_table)
    create_table(cnx, cursor, 'patient', patient_table)
    create_table(cnx, cursor, 'schedule', schedule_table)

    with open('hospital_data.txt', 'r', encoding="utf8") as hospital_file:
        for line in hospital_file:
            data = line.strip().split('|')
            print(data)
            print(mysql_db.add_hospital(cnx, cursor, data[0], data[1], data[2], data[3]))

    with open('doctor_data.txt', 'r', encoding="utf8") as doctor_file:
        for line in doctor_file:
            data = line.strip().split('|')
            print(data)
            print(mysql_db.add_doctor(cnx, cursor, data[0], data[1], data[2], data[3], data[4]))

    with open('patient_data.txt', 'r', encoding="utf8") as patient_file:
        for line in patient_file:
            data = line.strip().split('|')
            print(data)
            print(mysql_db.add_patient(cnx, cursor, data[0], data[1], data[2], data[3], data[4]))
