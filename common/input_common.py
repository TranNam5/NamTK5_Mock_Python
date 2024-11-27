import re
import mysql_db
import datetime

PHONE_PATTERN = '(\+[0-9]{2,3} )?[0-9 ]{8,15}'
EMAIL_PATTERN = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
ID_PATTERN = '[1-9][0-9]*'
DATETIME_PATTERN = '^[1-9][0-9]{3}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'


def check_input_format(pattern, text):
    if re.search(pattern, text):
        return True
    return False


def check_hospital_input(name, phone, address):
    msg = ''
    if name == '':
        msg += 'Name can not be blank\n'
    if phone == '' or not check_input_format(
            '{}( - {})*'.format(PHONE_PATTERN, PHONE_PATTERN), phone):
        msg += 'Phone number invalid\n'
    if address == '':
        msg += 'Address can not be blank\n'

    return msg


def check_doctor_input(cursor, name, phone, email, address, hospital_id):
    msg = ''
    if name == '':
        msg += 'Name can not be blank\n'
    if phone == '' or not check_input_format(
            '{}( - {})*'.format(PHONE_PATTERN, PHONE_PATTERN), phone):
        msg += 'Phone number invalid\n'
    if email == '' or not check_input_format(EMAIL_PATTERN, email):
        msg += 'Email address invalid\n'
    if address == '':
        msg += 'Address can not be blank\n'
    if hospital_id == '' or not check_input_format(ID_PATTERN, hospital_id):
        msg += 'Hospital id must be an number\n'
    elif (int(hospital_id),) not in mysql_db.select_id(cursor, 'hospital'):
        msg += 'Hospital id is not in hospital table'
    return msg


def check_patient_input(cursor, name, phone, email, address, hospital_id):
    msg = ''
    if name == '':
        msg += 'Name can not be blank\n'
    if phone == '' or not check_input_format(
            '{}( - {})*'.format(PHONE_PATTERN, PHONE_PATTERN), phone):
        msg += 'Phone number invalid\n'
    if email == '' or not check_input_format(EMAIL_PATTERN, email):
        msg += 'Email address invalid\n'
    if address == '':
        msg += 'Address can not be blank\n'
    if hospital_id == '' or not check_input_format(ID_PATTERN, hospital_id):
        msg += 'Hospital id must be an number\n'
    elif (int(hospital_id),) not in mysql_db.select_id(cursor, 'hospital'):
        msg += 'Hospital id is not in hospital table'
    return msg


def check_schedule_input(cursor, name, doctor_id, patient_id, date_time=None):
    msg = ''
    if name == '':
        msg += 'Name can not be blank\n'
    if date_time == '':
        msg += 'Datetime can not be blank\n'
    elif date_time is not None:
        if check_input_format(DATETIME_PATTERN, date_time):
            date, time = date_time.strip().split(' ')
            date_list = date.strip().split('-')
            time_list = time.strip().split(':')
            try:
                datetime.datetime(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]),
                                  hour=int(time_list[0]), minute=int(time_list[1]), second=int(time_list[2]))
            except ValueError:
                msg += 'Datetime not exist'
        else:
            msg += 'Datetime much be in format YYYY-MM-DD hh:mm:ss'
    if doctor_id == '' or not check_input_format(ID_PATTERN, doctor_id):
        msg += 'Doctor id must be an number\n'
    elif (int(doctor_id),) not in mysql_db.select_id(cursor, 'doctor'):
        msg += 'Doctor id is not in doctor table\n'
    if patient_id == '' or not check_input_format(ID_PATTERN, patient_id):
        msg += 'Patient id must be an number\n'
    elif (int(patient_id),) not in mysql_db.select_id(cursor, 'patient'):
        msg += 'Patient id is not in patient table\n'
    return msg
