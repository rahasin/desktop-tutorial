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
            service VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            clinic_password VARCHAR(255) NOT NULL,
            clinic_contact_info VARCHAR(255) NOT NULL
    )
        """
       cursor.execute(sql)
    
    with connection.cursor() as cursor:
     
        sql = """
        CREATE TABLE patients (
            patient_national_code INT PRIMARY KEY NOT NULL,
            patient_name VARCHAR(255) NOT NULL,
            patient_contact_info VARCHAR(255) NOT NULL,
            age INT,
            insurance VARCHAR(255) ,
            patient_password VARCHAR(255) 
    )
        """
        cursor.execute(sql)
    
    with connection.cursor() as cursor:
     
        sql = """
        CREATE TABLE appointments (
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
