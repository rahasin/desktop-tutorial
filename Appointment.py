import requests
from db_connector import create_connection

class Appointment:
    def __init__(self):
        self.connection = create_connection()

    def reserve_appointment(self, clinic_id, reserved, patient_national_code):
        # Send POST request to Flask API
        url = 'http://127.0.0.1:5000/reserve'
        data = {'id': clinic_id, 'reserved': reserved}
        response = requests.post(url, json=data)
        result = response.json()
        
        if result['success']:
            # Update SQLite database
            cursor = self.connection.cursor()
            # Update clinics table
            sql = "UPDATE clinics SET capacity = capacity - ?, clinic_reserved_appointments = clinic_reserved_appointments + ? WHERE clinic_id = ?"
            cursor.execute(sql, (reserved, reserved, clinic_id))

            # Update patients table
            sql = "UPDATE patients SET patient_reserved_appointments = patient_reserved_appointments + ? WHERE patient_national_code = ?"
            cursor.execute(sql, (reserved, patient_national_code))

            self.connection.commit()

        return result

    def cancel_appointment(self, clinic_id, cancelled, patient_national_code):
        # Update SQLite database
        cursor = self.connection.cursor()
        # Update clinics table
        sql = "UPDATE clinics SET capacity = capacity + ?, clinic_reserved_appointments = clinic_reserved_appointments - ? WHERE clinic_id = ?"
        cursor.execute(sql, (cancelled, cancelled, clinic_id))

        # Update patients table
        sql = "UPDATE patients SET patient_reserved_appointments = patient_reserved_appointments - ? WHERE patient_national_code = ?"
        cursor.execute(sql, (cancelled, patient_national_code))
        self.connection.commit()

        print({"success": True, "message": "Appointment cancelled successfully"}) 
        return True

    def increase_capacity(self, clinic_id, increase_amount):
        # Update SQLite database
        cursor = self.connection.cursor()
        # Update clinics table
        sql = "UPDATE clinics SET capacity = capacity + ? WHERE clinic_id = ?"
        cursor.execute(sql, (increase_amount, clinic_id))
        self.connection.commit()

        print({"success": True, "message": "Clinic capacity increased successfully"})
        return True

    def close_connection(self):
        self.connection.close()