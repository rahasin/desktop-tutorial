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
       CREATE TABLE IF NOT EXISTS clinics (
            clinic_id INT PRIMARY KEY,
            capacity INT,
            service VARCHAR(255) NOT NULL,
            clinic_reserved_appointments INT,
            address VARCHAR(255) NOT NULL,
            clinic_password VARCHAR(255) NOT NULL,
            clinic_contact_info VARCHAR(255) NOT NULL
    )
        """
       cursor.execute(sql)
    
    with connection.cursor() as cursor:
     
        sql = """
        CREATE TABLE IF NOT EXISTS patients (
            patient_national_code INT NOT NULL,
            patient_name VARCHAR(255) NOT NULL,
            patient_contact_info VARCHAR(255) NOT NULL,
            patient_age INT,
            patient_insurance VARCHAR(255),
            patient_permanent_password VARCHAR(255),
            patient_reserved_appointments INT,
            clinic_id INT,
            FOREIGN KEY (clinic_id) REFERENCES clinics(clinic_id)
    )
        """
        cursor.execute(sql)
    
    connection.commit()
finally:
    connection.close()
