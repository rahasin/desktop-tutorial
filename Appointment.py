#class Appointment
import requests
from db_connector import create_connection


class Appointment:
    def __init__(self):
        self.connection = create_connection()

    def reserve_appointment(self, clinic_id, reserved, national_code):
        # Send POST request to Flask API
        url = 'http://127.0.0.1:5000/reserve'
        data = {'id': clinic_id, 'reserved': reserved}
        response = requests.post(url, json=data)
        result = response.json()

        if result['success']:
            # Update MySQL database
            try:
                with self.connection.cursor() as cursor:
                    # Update clinics table
                    sql = "UPDATE clinics SET capacity = capacity - %s, clinic_reserved_appointments = clinic_reserved_appointments + %s WHERE clinic_id = %s"
                    cursor.execute(sql, (reserved, reserved, clinic_id))

                    # Update patients table
                    sql = "UPDATE patients SET patient_reserved_appointments = patient_reserved_appointments + %s WHERE national_code = %s"
                    cursor.execute(sql, (reserved, national_code))

                self.connection.commit()
            finally:
                self.connection.close()

        return result



    def cancel_appointment(self, clinic_id, cancelled, patient_national_code):
        # Update MySQL database
        try:
            with self.connection.cursor() as cursor:
                # Update clinics table
                sql = "UPDATE clinics SET capacity = capacity + %s, clinic_reserved_appointments = clinic_reserved_appointments - %s WHERE clinic_id = %s"
                cursor.execute(sql, (cancelled, cancelled, clinic_id))

                # Update patients table
                sql = "UPDATE patients SET patient_reserved_appointments = patient_reserved_appointments - %s WHERE patient_national_code = %s"
                cursor.execute(sql, (cancelled, patient_national_code))

            self.connection.commit()
            print({"success": True, "message": "Appointment cancelled successfully"}) 
            return True
        except Exception as e:
            print({"success": False, "message": str(e)}) 
            return False
        finally:
            self.connection.close()





