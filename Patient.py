#class Patient

import random
import string
import re

def generate_password(length) :
    characters = string.ascii_lowercase + string.digits 
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

class Patient :
    all_patient = {}
    def __init__ (self, patient_national_code, patient_name, patient_contact_info, age,insurance, password_type):
        self.patient_national_code = patient_national_code
        self.patient_name = patient_name
        self.patient_contact_info = patient_contact_info
        self.age = age
        self.insurance = insurance
        self.password_type = password_type
        if password_type == 'permanent':
            self.patient_password = input("Enter your permanent password: ")
        elif password_type == 'temporary':
            self.patient_password = generate_password(6)
        

    def get_info (self):
        if len(self.patient_national_code) != 10:
            return print("national code is incorrect")
        elif self.password_type == 'permanent':
            if len(self.patient_password) < 8 or not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[_]).+$', self.patient_password):
                    return print('The password is weak.')
        elif len(self.patient_contact_info) != 8 :
            return print("this phone number is incorrect")
        return {
            "patient_national_code" : self.patient_national_code,
            "patient_name" : self.patient_name,
            "patient_contact_info" : self.patient_contact_info,
            "patient_age" : self.age,
            "patient_insurance" : self.insurance,
            "patient_password" : self.patient_password
        }
    
    def sign_in(self):
        if self.patient_national_code not in Patient.all_patient:
            Patient.all_patient[self.patient_national_code] = self
        else:
            return print('This national code already exists in our database')
        
    def log_in(self, patient_national_code, password):
        if patient_national_code in Patient.all_patient:
            if Patient.all_patient[patient_national_code].password_type != 'permanent':
                print(f'Your temporary password is {Patient.all_patient[patient_national_code].patient_password}')
                
                return print('Login successfully')
                
            else:
                if Patient.all_patient[patient_national_code].patient_password == password:
                    return print('Login successfully')
                else:
                    return print('Password is wrong')
        else:
            return print('This national code does not exist in our database and you need signing up.')
        
    
    def insert_data(self):
     data = self.get_info()
     if data is not None:
        with self.connection.cursor() as cursor:
            # Check if the patient already exists in the 'patients' table
            sql = "SELECT * FROM patients WHERE patient_national_code = %s"
            val = (data['patient_natinal_code'])
            cursor.execute(sql , val)
            result = cursor.fetchone()

            # If the patient does not exist, insert the new data
            if result is None :
                sql = """
                INSERT INTO patients (patient_national_code, patient_name , patient_contact_info , patient_age , patient_insurance , patient_password) 
                VALUES (%s , %s , %s , %s , %s , %s , %s , %s)
                """
                val = (data['patient_natinal_code'] , data['patient_name'] , data['patient_contact_info'] , data['patient_age'] , data['patient_insurance'] , data['patient_password'])
                cursor.execute(sql, val)
                self.connection.commit()
                
                
    def execute_query(self, query, values=None):
        try:
            with self.connection.cursor() as cursor:
              if values is None:
                cursor.execute(query)
              else:
                cursor.execute(query, values)
            return cursor.fetchall()  # Return all rows of the result
        except Exception as e:
           print(f"An error occurred: {e}")


        
    
    def select_patient_info(self, patient_national_code, patient_name, age, insurance, patient_contact_info):
        query = "SELECT patient_national_code, patient_name, age, insurance, patient_contact_info FROM patients ORDER BY patient_national_code"
        values = (patient_national_code,)
        return self.execute_query(query, values)