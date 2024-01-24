import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('APclinics.db')

try:
    cursor = connection.cursor()

    # Create 'clinics' table
    sql = """
    CREATE TABLE IF NOT EXISTS clinics (
        clinic_id INTEGER PRIMARY KEY,
        capacity INTEGER,
        service TEXT NOT NULL,
        clinic_reserved_appointments INTEGER,
        address TEXT NOT NULL,
        clinic_contact_info TEXT NOT NULL
    )
    """
    cursor.execute(sql)

    # Create 'patient_info' table
    sql = """
    CREATE TABLE IF NOT EXISTS patient_info (
        patient_national_code TEXT PRIMARY KEY,
        patient_name TEXT NOT NULL,
        patient_contact_info TEXT NOT NULL,
        patient_password TEXT
    )
    """
    cursor.execute(sql)

    # Create 'patient_health' table
    sql = """
    CREATE TABLE IF NOT EXISTS patient_health (
        patient_national_code TEXT NOT NULL,
        patient_age INTEGER,
        patient_insurance TEXT,
        FOREIGN KEY (patient_national_code) REFERENCES patient_info(patient_national_code)
    )
    """
    cursor.execute(sql)

    # Create 'patient_appointments' table
    sql = """
    CREATE TABLE IF NOT EXISTS patient_appointments (
        patient_national_code TEXT NOT NULL,
        patient_reserved_appointments INTEGER,
        clinic_id INTEGER,
        FOREIGN KEY (patient_national_code) REFERENCES patient_info(patient_national_code),
        FOREIGN KEY (clinic_id) REFERENCES clinics(clinic_id)
    )
    """
    cursor.execute(sql)
    
    # Create 'pharmacy' table
    sql = """
    CREATE TABLE IF NOT EXISTS pharmacy (
    drug_name TEXT PRIMARY KEY,
    quantity INTEGER
    )
    """
    cursor.execute(sql)


    connection.commit()
finally:
    connection.close()
