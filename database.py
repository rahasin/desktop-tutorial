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
        clinic_password TEXT NOT NULL,
        clinic_contact_info TEXT NOT NULL
    )
    """
    cursor.execute(sql)

    # Create 'patients' table
    sql = """
    CREATE TABLE IF NOT EXISTS patients (
        patient_national_code INTEGER NOT NULL,
        patient_name TEXT NOT NULL,
        patient_contact_info TEXT NOT NULL,
        patient_age INTEGER,
        patient_insurance TEXT,
        patient_password TEXT,
        patient_reserved_appointments INTEGER,
        clinic_id INTEGER,
        FOREIGN KEY (clinic_id) REFERENCES clinics(clinic_id)
    )
    """
    cursor.execute(sql)

    connection.commit()
finally:
    connection.close()
