def delete_row_by_id(cnx, cursor, table, id):
    delete_cmd = f"DELETE FROM {table} WHERE id={id}"

    try:
        cursor.execute(delete_cmd)
        cnx.commit()
        return True
    except:
        return False
