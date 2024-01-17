import random
import string
import re
from db_connector import create_connection

def generate_password(length):
    characters = string.ascii_lowercase + string.digits 
    random_string = ''.join(random.choice(characters) for _ in range(length))
    print(random_string)
    return random_string

class Patient:
    all_patient = {}
    def __init__(self):
        self.connection = create_connection()

    def get_info(self):
        # needs while True/ try except
        self.patient_national_code = input("Enter your national code: ")
        if len(self.patient_national_code) != 10:
            print("national code is incorrect")
        self.patient_name = input("Enter your full name: ")
        # needs while True/ try except
        self.patient_contact_info = input("Enter your contact info: ")
        if len(self.patient_contact_info) != 11 :
            print("this phone number is incorrect")
        while True:
            self.age = input("Enter your age: ")
            if not self.age.isdigit():
                print('Please enter a number')
            else:
                self.age = int(self.age)
                break

        self.insurance = input("Do you have insurance (Yes/No): ")
        print("Choose a password type:")
        print('1. Temporary')
        print('2. Permanent')
        self.password_type = int(input('Please choose an option: '))
        if self.password_type == 1:
            self.patient_password = generate_password(8)
        elif self.password_type == 2:
            self.patient_password = input('Enter your password: ')
        # needs while True/ try except
        # don't send temporary password in sign up, only in login
        if len(self.patient_password) < 8 or not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[_]).+$', self.patient_password) and self.password_type == 2:
            print('The password is weak.')

        self.patient_info = {
            "patient_national_code" : self.patient_national_code,
            "patient_name" : self.patient_name,
            "patient_contact_info" : self.patient_contact_info,
            "patient_age" : self.age,
            "patient_insurance" : self.insurance,
            "patient_password" : self.patient_password
        }

        return self.patient_info
    
    def sign_up(self):
        if self.patient_national_code not in Patient.all_patient:
            Patient.all_patient[self.patient_national_code] = self
            print('Sign up successfully. Now you need logging in to be able to reserve or cancel an appointment.')
            return True
        else:
            print('This national code already exists in the database, please choose the log in option')
            return False
        
    def log_in(self, patient_national_code, password):
        max_attempts = 3
        attempts = 0
        patient_national_code = input('Enter your national code.')
        if patient_national_code in Patient.all_patient:
            if Patient.all_patient[patient_national_code].password_type == 1:
                print(f'Your temporary password is {generate_password(8)}')
                print('Log in successfully')
                return True
                
            else:
                while attempts < max_attempts:
                    password = input('Enter your password: ')
                    if Patient.all_patient[patient_national_code].patient_password == password:
                        print('Log in successfully')
                    else:
                        attempts += 1
                        print('Password is wrong!')
                        if attempts == max_attempts:
                            print('You have been logged out due to too many incorrect attempts.')
                            return None
                        
        else:
            print('This national code does not exist in our database and you needs signing up.')
            return False

        
    
    def insert_data(self):
        data = self.get_info()
        if data is not None:
            cursor = self.connection.cursor()
            # Check if the patient already exists in the 'patients' table
            sql = "SELECT * FROM patients WHERE patient_national_code = ?"
            val = (data['patient_national_code'],)  # corrected here
            cursor.execute(sql , val)
            result = cursor.fetchone()

            # If the patient does not exist, insert the new data
            if result is None:  # changed here
                sql = """
                INSERT INTO patients (patient_national_code, patient_name , patient_contact_info , patient_age , patient_insurance , patient_password) 
                VALUES (?, ?, ?, ?, ?, ?)
                """
                val = (data['patient_national_code'] , data['patient_name'] , data['patient_contact_info'] , data['patient_age'] , data['patient_insurance'] , data['patient_password'])
                cursor.execute(sql, val)
                self.connection.commit()
    
    def execute_query(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            if values is None:
                cursor.execute(query)
            else:
                cursor.execute(query, values)
            return cursor.fetchall()  # Return all rows of the result
        except Exception as e:
           print(f"An error occurred: {e}")

    def select_clinic_capacity_info(self, clinic_id):
        query = """
        SELECT 
        clinic_id,
        service,
        address,
        capacity ,
        clinic_reserved_appointments,
        clinic_contact_info
        FROM clinics
        WHERE clinic_id = ?
        ORDER BY clinic_id ASC
        """
        values = (clinic_id,)
        return self.execute_query(query, values)
    
    def select_patient_reserved_appointments_info(self, patient_national_code):
        query ="""
        SELECT 
        patient_national_code, 
        patient_name ,
        clinic_id,
        patient_reserved_appointments
        FROM patients
        WHERE patient_reserved_appointments > 0 
        AND patient_national_code = ?
        ORDER BY clinic_id
        """
        values = (patient_national_code,)
        return self.execute_query(query, values)
    
    def close_connection(self):
        self.connection.close()