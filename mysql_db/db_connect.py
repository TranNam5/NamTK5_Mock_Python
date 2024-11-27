import mysql.connector
from mysql.connector import errorcode


def mysql_connect(config):
    try:
        cnx = mysql.connector.connect(user=config['user'],
                                      password=config['password'],
                                      host=config['host'],
                                      port=config['port'])
        print("Connect to MySQL successfully.")
        return True, cnx

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return False, "Something is wrong with your username or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return False, "Database does not exist"
        else:
            return False, err


def use_database(cursor, db_name):
    try:
        cursor.execute("USE {}".format(db_name))
        print("Connect to database {} successfully.".format(db_name))
        return True
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            return False
        else:
            print(err)
            exit(1)
