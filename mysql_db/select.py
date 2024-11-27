# use for 3.2,  3.3,  3.8
#         3.9,  3.10, 3.15
#         3.16, 3.17, 3.22
def search_all_name(cursor, table, search_name=''):
    select_cmd = f"SELECT * FROM {table}"
    if search_name != '':
        select_cmd += f" WHERE name LIKE \'%{search_name}%\'"

    try:
        cursor.execute(select_cmd)
        return cursor.fetchall()
    except:
        return None


def select_id(cursor, table):
    select_cmd = f"SELECT id FROM {table}"
    try:
        cursor.execute(select_cmd)
        return cursor.fetchall()
        # tuple_id = cursor.fetchall()
        # int_id = []
        # for i in tuple_id:
        #     int_id.append(i[0])
        # return int_id
    except:
        return None


def select_schedule(cursor, search_name, date_from, date_to):
    select_cmd = f"SELECT * FROM schedule WHERE name LIKE \'%{search_name}%\' " \
                 f"AND `date` >= \'{date_from}\' AND `date` <= \'{date_to}\'"
    try:
        cursor.execute(select_cmd)
        return cursor.fetchall()
    except:
        return None
