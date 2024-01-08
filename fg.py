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
            FOREIGN KEY (clinic_id) REFERENCES clinics(clinic_id),
            FOREIGN KEY (patient_natinal_code) REFERENCES patients(patient_natinal_code),
            FOREIGN KEY (patient_name) REFERENCES patients(patient_name),
            reserved_appointments INTEGER,
            FOREIGN KEY (service) REFERENCES clinics(service),
            FOREIGN KEY (clinic_contact_info) REFERENCES clinics(clinic_contact_info),
            FOREIGN KEY (address) REFERENCES clinics(address),
        )
        """
        cursor.execute(sql)
    with connection.cursor() as cursor:
       
        sql = """
        CREATE TABLE new_appointments (
            FOREIGN KEY (clinic_id) REFERENCES clinics(clinic_id),
            FOREIGN KEY (capacity) REFERENCES clinics(capacity),
            appointments INTEGER,
            FOREIGN KEY (address) REFERENCES clinics(address),
            FOREIGN KEY (clinic_contact_info) REFERENCES clinics(clinic_contact_info),
            FOREIGN KEY (service) REFERENCES clinics(service),
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
            illness_history VARCHAR(255),
        )
        """
        cursor.execute(sql)
    with connection.cursor() as cursor:
     
        sql = """
        CREATE TABLE secretary (
            FOREIGN KEY (reserved_appointments) REFERENCES previous_appointments(reserved_appointments),
            FOREIGN KEY (capacity) REFERENCES clinics(capacity),
            FOREIGN KEY (patient_natinal_code) REFERENCES patients(patient_natinal_code),
            FOREIGN KEY (patient_name) REFERENCES patients(patient_name),
            FOREIGN KEY (patient_contact_info) REFERENCES patients(patient_contact_info),
        )
        """
        cursor.execute(sql)
    
    connection.commit()
finally:
    connection.close()













