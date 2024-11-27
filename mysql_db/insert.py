def add_hospital(cnx, cursor, name, phone, address, description=''):
    new_hospital = "INSERT INTO hospital(name, phone, address, description)" \
                   "VALUES(%s, %s, %s, %s)"
    data_hospital = [name, phone, address, description]
    try:
        cursor.execute(new_hospital, data_hospital)
        cnx.commit()
        return True
    except:
        return False


def add_doctor(cnx, cursor, name, phone, email, address, hospital_id):
    new_doctor = "INSERT INTO doctor(name, phone, email, address, hospital_id)" \
                 "VALUES(%s, %s, %s, %s, %s)"
    data_doctor = [name, phone, email, address, hospital_id]
    try:
        cursor.execute(new_doctor, data_doctor)
        cnx.commit()
        return True
    except:
        return False


def add_patient(cnx, cursor, name, phone, email, address, hospital_id):
    new_patient = "INSERT INTO patient(name, phone, email, address, hospital_id)" \
                  "VALUES(%s, %s, %s, %s, %s)"
    data_patient = [name, phone, email, address, hospital_id]
    try:
        cursor.execute(new_patient, data_patient)
        cnx.commit()
        return True
    except:
        return False


def add_schedule(cnx, cursor, name, date, doctor_id, patient_id, result=''):
    new_schedule = "INSERT INTO schedule(name, `date`, doctor_id, patient_id, `result`)" \
                   "VALUES(%s, %s, %s, %s, %s)"
    data_schedule = [name, date, doctor_id, patient_id, result]
    try:
        cursor.execute(new_schedule, data_schedule)
        cnx.commit()
        return True
    except:
        return False
