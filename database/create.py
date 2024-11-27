import mysql
from mysql.connector import errorcode
import mysql_db


def create_database(cursor, db_name):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        print("Database {} created successfully.".format(db_name))
        mysql_db.use_database(cursor, db_name)
    except mysql.connector.Error as err1:
        print("Failed creating mysql_db: {}".format(err1))
        exit(1)


def create_table(cnx, cursor, table_name, create_cmd):
    try:
        print("Creating table {}: ".format(table_name))
        cursor.execute(create_cmd)
        cnx.commit()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("Create successfully.")


hospital_table = """CREATE TABLE `hospital` (
                    id INT UNSIGNED auto_increment NOT NULL,
                    name varchar(200) NOT NULL,
                    phone varchar(100) NOT NULL,
                    address varchar(1000) NOT NULL,
                    description varchar(1000) NULL,
                    CONSTRAINT hospital_pk PRIMARY KEY (id))
                """

doctor_table = """CREATE TABLE `doctor` (
                id INT UNSIGNED auto_increment NOT NULL,
                name varchar(200) NOT NULL,
                phone varchar(100) NOT NULL,
                email varchar(100) NOT NULL,
                address varchar(1000) NOT NULL,
                hospital_id INT UNSIGNED NOT NULL,
                CONSTRAINT doctor_pk PRIMARY KEY (id),
                CONSTRAINT doctor_FK FOREIGN KEY (hospital_id) REFERENCES hospital(id) ON UPDATE CASCADE)
                """

patient_table = """CREATE TABLE patient (
                id INT UNSIGNED auto_increment NOT NULL,
                name varchar(200) NOT NULL,
                phone varchar(100) NOT NULL,
                email varchar(100) NOT NULL,
                address varchar(1000) NOT NULL,
                hospital_id INT UNSIGNED NOT NULL,
                CONSTRAINT patient_pk PRIMARY KEY (id),
                CONSTRAINT patient_FK FOREIGN KEY (hospital_id) REFERENCES hospital(id) ON UPDATE CASCADE)
                """

schedule_table = """CREATE TABLE schedule (
                id INT UNSIGNED auto_increment NOT NULL,
                name varchar(200) NOT NULL,
                `date` DATETIME NOT NULL,
                doctor_id INT UNSIGNED NOT NULL,
                patient_id INT UNSIGNED NOT NULL,
                `result` varchar(1000) NOT NULL,
                CONSTRAINT schedule_pk PRIMARY KEY (id),
                CONSTRAINT schedule_FK FOREIGN KEY (doctor_id) REFERENCES doctor(id) ON UPDATE CASCADE,
                CONSTRAINT schedule_FK_1 FOREIGN KEY (patient_id) REFERENCES patient(id) ON UPDATE CASCADE)
                """
