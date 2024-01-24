
import random
import string
import re
from db_connector import create_connection
# Logging out
def log_out():
        print('You have been logged out.')
        return None

# Generating temporary password
def generate_password(length):
    characters = string.ascii_lowercase + string.digits 
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

class Patient:
    all_patient = {}
    def __init__(self):
        self.connection = create_connection()
        self.patient_password = None
        

    def get_info(self):
        # Getting patient's information
        while True:
            self.patient_national_code = input('Enter your national code: ')
            if len(self.patient_national_code) != 10:
                print('National code is incorrect, it must contain 10 digits. Please try again.')
                continue
            break

        self.patient_name = input('Enter your full name: ')

        while True:
            self.patient_contact_info = input('Enter your contact info: ')
            if len(self.patient_contact_info) != 11 :
                print('This phone number is incorrect, it must contain 11 digits. Please try again.')
                continue
            break

        while True:
            self.age = input('Enter your age: ')
            if not self.age.isdigit():
                print('Please enter a number.')
                continue
            else:
                self.age = int(self.age)
                break

        self.insurance = input('Do you have insurance (Yes/No): ')

        while True:
            print('Choose a password type: ')
            print('1. Temporary')
            print('2. Permanent')
            try:
                self.password_type = int(input('Please choose an option: '))
                if self.password_type not in [1, 2]:
                    print('Invalid option. Please try again.')
                    continue
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            break

        if self.password_type == 2:
            self.patient_password = input('Enter your password: ')

        while True:
            if self.patient_password is not None and (len(self.patient_password) < 8 or not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[_]).+$', self.patient_password)) and self.password_type == 2:
                print('The password is weak, it must be more than 8 chracters and must contain at least one digit, capital and small letter and the character in the bracket [_]. Please try again.')
                self.patient_password = input('Enter your password: ')
                continue
            break

        while True:
            try:
                self.clinic_id = int(input('Please choose a clinic id(1 , 2 , 3 , 4 , 5 , 6 , 7): '))
                if self.clinic_id not in [1, 2, 3, 4, 5, 6, 7]:
                    print('Invalid clinic id. Please try again.')
                    continue
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            break
        # Returning patient's information
        self.patient_info = {
            "patient_national_code" : self.patient_national_code,
            "patient_name" : self.patient_name,
            "patient_contact_info" : self.patient_contact_info,
            "patient_age" : self.age,
            "patient_insurance" : self.insurance,
            "patient_password" : self.patient_password,
            "clinic_id" : self.clinic_id
        }

        return self.patient_info
    
    def sign_up(self):
            # Check if the patient's national code is already in the database
            if self.patient_national_code in Patient.all_patient:
                print('This national code already exists in the database')
                return False
            else:
                # If not, add the patient to the database and complete the sign-up process
                Patient.all_patient[self.patient_national_code] = self
                print('Sign up successfully. Now you need to log in to be able to reserve or cancel an appointment.')
                return True
        
    def log_in(self):
        # Logging in
        max_attempts = 3
        attempts = 0
        while True:
            self.patient_national_code = input('Enter your national code: ')
            if self.patient_national_code in Patient.all_patient:
                if Patient.all_patient[self.patient_national_code].password_type == 1:
                    print(f'Your temporary password is {generate_password(8)}')
                    print('Log in successfully!')
                    return True
                    
                else:
                    while attempts < max_attempts:
                        self.password = input('Enter your password: ')
                        if Patient.all_patient[self.patient_national_code].patient_password == self.password:
                            print('Log in successfully!')
                            return True
                        else:
                            attempts += 1
                            print('Password is wrong!')
                            if attempts == max_attempts:
                                print('You have been logged out due to too many incorrect attempts.')
                                log_out()
                                return False 
            else:
                print('National code not found. Would you like to sign up? (Yes/No)')
                choice = input()
                if choice.lower() == 'yes':
                    self.insert_data()
                    self.sign_up()
                    return True
                else:
                    print('Please try again.')
            
    
    def insert_data(self):
        data = self.get_info()
        if data is not None:
            cursor = self.connection.cursor()
            # Check if the patient already exists in the 'patient_info' table
            sql = "SELECT * FROM patient_info WHERE patient_national_code = ?"
            val = (data['patient_national_code'],)
            cursor.execute(sql , val)
            result = cursor.fetchone()

            # If the patient does not exist, insert the new data
            if result is None:  
                # Insert into 'patient_info' table
                sql = """
                INSERT INTO patient_info (patient_national_code, patient_name , patient_contact_info , patient_password) 
                VALUES (?, ?, ?, ?)
                """
                val = (data['patient_national_code'] , data['patient_name'] , data['patient_contact_info'] , data['patient_password'])
                cursor.execute(sql, val)

                # Insert into 'patient_health' table
                sql = """
                INSERT INTO patient_health (patient_national_code, patient_age , patient_insurance) 
                VALUES (?, ?, ?)
                """
                val = (data['patient_national_code'] , data['patient_age'] , data['patient_insurance'])
                cursor.execute(sql, val)

                # Insert into 'patient_appointments' table
                sql = """
                INSERT INTO patient_appointments (patient_national_code, patient_reserved_appointments , clinic_id) 
                VALUES (?, ?, ?)
                """
                val = (data['patient_national_code'] , 0 , data['clinic_id'])
                cursor.execute(sql, val)

                self.connection.commit()

    
    def execute_query(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            if values is None:
                cursor.execute(query)
            else:
                cursor.execute(query, values)
            # Return all rows of the result
            return cursor.fetchall() 
        except Exception as e:
           print(f"An error occurred: {e}")

    def select_clinic_capacity_info(self, clinic_id):
        # Viewing clinics and their capacities
        query = """
        SELECT 
        clinic_id,
        service,
        capacity,
        clinic_reserved_appointments,
        address,
        clinic_contact_info
        FROM clinics
        WHERE clinic_id = ?
        ORDER BY clinic_id ASC
        """
        values = (clinic_id,)
        return self.execute_query(query, values)

    def select_patient_reserved_appointments_info(self, patient_national_code):
        # Viewing reserved appointments
        query ="""
        SELECT 
        patient_info.patient_national_code, 
        patient_info.patient_name,
        patient_appointments.clinic_id,
        patient_appointments.patient_reserved_appointments
        FROM patient_info
        JOIN patient_appointments ON patient_info.patient_national_code = patient_appointments.patient_national_code
        WHERE patient_appointments.patient_reserved_appointments > 0 
        AND patient_info.patient_national_code = ?
        ORDER BY patient_appointments.clinic_id
        """
        values = (patient_national_code,)
        return self.execute_query(query, values)

    def close_connection(self):
        self.connection.close()
