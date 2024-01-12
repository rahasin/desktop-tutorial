import pymysql.cursors 

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='APterm3r@r@8304')

try:
    with connection.cursor() as cursor:
        sql = 'CREATE DATABASE IF NOT EXISTS APclinics'
        cursor.execute(sql)
    
    connection.commit()
finally:
    connection.close()

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='APterm3r@r@8304',
                             database='APclinics')

try:
    with connection.cursor() as cursor:
       sql = """
       CREATE TABLE clinics (
            clinic_id INT PRIMARY KEY,
            capacity INT,
            service VARCHAR(255),
            clinic_contact_info VARCHAR(255),
            address VARCHAR(255),
            clinic_password VARCHAR(255)
    )
        """
       cursor.execute(sql)
    
    with connection.cursor() as cursor:
     
        sql = """
        CREATE TABLE patients (
            patient_national_code INT PRIMARY KEY,
            patient_name VARCHAR(255),
            patient_contact_info VARCHAR(255),
            age INT,
            insurance VARCHAR(255)
    )
        """
        cursor.execute(sql)
    
    with connection.cursor() as cursor:
     
        sql = """
        CREATE TABLE appointments (
            appointment_id INT AUTO_INCREMENT PRIMARY KEY,
            clinic_id INT,
            patient_national_code INT,
            reserved_appointments INT,
            FOREIGN KEY (clinic_id) REFERENCES clinics(clinic_id),
            FOREIGN KEY (patient_national_code) REFERENCES patients(patient_national_code)
    )
        """
        cursor.execute(sql)
    
    connection.commit()
finally:
    connection.close()
