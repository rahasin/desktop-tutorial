#class Appointment
import requests
from db_connector import create_connection

class Appointment:
    def __init__(self):
        self.connection = create_connection()

    def reserve_appointment(self, clinic_id, reserved):
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
                    sql = "UPDATE patients SET patient_reserved_appointments = patient_reserved_appointments + %s WHERE clinic_id = %s"
                    cursor.execute(sql, (reserved, clinic_id))

                self.connection.commit()
            finally:
                self.connection.close()

        return result


    def cancel_appointment(self, clinic_id, cancelled):
        # Update MySQL database
        try:
            with self.connection.cursor() as cursor:
                # Update clinics table
                sql = "UPDATE clinics SET capacity = capacity + %s, clinic_reserved_appointments = clinic_reserved_appointments - %s WHERE clinic_id = %s"
                cursor.execute(sql, (cancelled, cancelled, clinic_id))

                # Update patients table
                sql = "UPDATE patients SET patient_reserved_appointments = patient_reserved_appointments - %s WHERE clinic_id = %s"
                cursor.execute(sql, (cancelled, clinic_id))

            self.connection.commit()
            # IF WE WANT IT TO SEND A MESSAGE LIKE IT DOES WITH MAKING RESERVATIONS
            #return {"success": True, "message": "Appointment cancelled successfully"}
        #except Exception as e:
            #return {"success": False, "message": str(e)}
        finally:
            self.connection.close()

appointment = Appointment()
result_reservation = appointment.reserve_appointment('<clinic_id>', '<number_of_appointments>')
print(result_reservation)
result_cancellation = appointment.cancel_appointment('<clinic_id>', '<number_of_appointments>')
print(result_cancellation)

