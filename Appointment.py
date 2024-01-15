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
            return {"success": True, "message": "Appointment cancelled successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}
        finally:
            self.connection.close()




secretary = Secretary()
appointment = Appointment()  # Create an instance of the Appointment class

while True:
    if not secretary.enter_code():
        break
    clinic_id = secretary.choose_clinic()
    secretary.select_each_clinic_info(clinic_id)
    print ('1. Reserving an appointment')
    print('2. Canceling an appointment')
    print('3. Logout')
    option = int(input('Please choose an option: '))
    if option == 1:
        # Ask for the number of appointments to reserve
        number_of_appointments = int(input('Enter the number of appointments to reserve: '))
        # Ask for the patient's national code
        patient_national_code = input('Enter the patient\'s national code: ')
        # Call the reserve_appointment method
        result_reservation = appointment.reserve_appointment(clinic_id, number_of_appointments, patient_national_code)
        print(result_reservation)
    elif option == 2:
        # Ask for the number of appointments to cancel
        number_of_appointments = int(input('Enter the number of appointments to cancel: '))
        # Ask for the patient's national code
        patient_national_code = input('Enter the patient\'s national code: ')
        # Call the cancel_appointment method
        result_cancellation = appointment.cancel_appointment(clinic_id, number_of_appointments, patient_national_code)
        print(result_cancellation)
    elif option == 3:
        logout()
        break
    else :
        print("Invalid option. Please try again.")
