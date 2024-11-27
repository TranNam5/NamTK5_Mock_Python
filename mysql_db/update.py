def update_hospital(cnx, cursor, id, name, phone, address, description=None):
    new_hospital = f"UPDATE hospital SET name=%s, phone=%s, address=%s"
    data_hospital = [name, phone, address]
    if description is not None:
        new_hospital += ', description=%s'
        data_hospital.append(description)

    new_hospital += f" WHERE id={id}"
    try:
        cursor.execute(new_hospital, data_hospital)
        cnx.commit()
        return True
    except:
        return False


def update_doctor(cnx, cursor, id, name, phone, email, address, hospital_id):
    new_doctor = "UPDATE doctor SET name=%s, phone=%s, email=%s, address=%s, hospital_id=%s" \
                 f" WHERE id={id}"
    data_doctor = [name, phone, email, address, hospital_id]
    try:
        cursor.execute(new_doctor, data_doctor)
        cnx.commit()
        return True
    except:
        return False


def update_patient(cnx, cursor, id, name, phone, email, address, hospital_id):
    new_patient = "UPDATE patient SET name=%s, phone=%s, email=%s, address=%s, hospital_id=%s" \
                  f" WHERE id={id}"
    data_patient = [name, phone, email, address, hospital_id]
    try:
        cursor.execute(new_patient, data_patient)
        cnx.commit()
        return True
    except:
        return False


def update_schedule(cnx, cursor, id, name, date, doctor_id, patient_id, result):
    new_schedule = "UPDATE schedule SET name=%s, `date`=%s, doctor_id=%s, patient_id=%s, result=%s" \
                   f" WHERE id={id}"
    data_schedule = [name, date, doctor_id, patient_id, result]
    try:
        cursor.execute(new_schedule, data_schedule)
        cnx.commit()
        return True
    except:
        return False
