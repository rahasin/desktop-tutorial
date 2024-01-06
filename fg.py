import pymysql.cursors 
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='APterm3r@r@8304')

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE APclinics"
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
            clinic_id AUTO_INCREMENT PRIMARY KEY,
            capacity INTEGER,
            address VARCHAR(255) NOT NULL,
            service VARCHAR(255) NOT NULL,
            clinic_contact_info INTEGER NOT NULL,
            clinic_password INTEGER NOT NULL
        )
        """
        cursor.execute(sql)
    with connection.cursor() as cursor:
        
        sql = """
        CREATE TABLE previous_appointments (
            clinic_id AUTO_INCREMENT PRIMARY KEY,
            patient_natinal_code INTEGER NOT NULL,
            patient_name VARCHAR(255) NOT NULL,
            reserved_appointments INTEGER,
            service VARCHAR(255) NOT NULL,
            patient_contact_info INTEGER NOT NULL,
            address VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(sql)
    with connection.cursor() as cursor:
       
        sql = """
        CREATE TABLE new_appointments (
            clinic_id AUTO_INCREMENT PRIMARY KEY,
            appointments INTEGER,
            address VARCHAR(255) NOT NULL,
            clinic_contact_info INTEGER NOT NULL,
            service VARCHAR(255) NOT NULL,
        )
        """
        cursor.execute(sql)
    with connection.cursor() as cursor:
     
        sql = """
        CREATE TABLE patients (
            patient_natinal_code INTEGER NOT NULL,
            patient_name VARCHAR(255) NOT NULL,
            patient_contact_info INTEGER NOT NULL,
            age INTEGER NOT NULL,
            insurance VARCHAR(255),
            illness_history VARCHAR(255)
        )
        """
        cursor.execute(sql)
    with connection.cursor() as cursor:
     
        sql = """
        CREATE TABLE secretary (
            current_appointments INTEGER,
            capacity INTEGER,
            patient_natinal_code INTEGER NOT NULL,
            patient_name VARCHAR(255) NOT NULL,
            patient_contact_info INTEGER NOT NULL,
        )
        """
        cursor.execute(sql)
    
    connection.commit()
finally:
    connection.close()













