import random
import string
from tkinter import _Cursor
from unittest import result
from colorama import Cursor
import pymysql

#password is a "lowercase + digit" string with length 10
#password generator functions : 

def generate_password(length) :
    characters = string.ascii_lowercase + string.digits 
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

class Patient :

    all_patient = {}

    def __init__(self , patient_natinal_code , patient_name , patient_contact_info , age , insurance , illness_history , permanent_password , temporary_password , appointment_obj , connection):
        self.patient_natinal_code = patient_natinal_code
        self.patient_name = patient_name
        self.patient_contact_info = patient_contact_info
        self.age = age
        self.insurance = insurance
        self.illness_history = illness_history
        self.permanent_password = permanent_password
        self.temporary_password = temporary_password
        self.appointment_obj = appointment_obj  # This should be an instance of the Appointment class
        self.connection = connection

    def sign_in(self , patient_national_code , patient_name , patient_contact_info , age , insurance , illness_history , temporary_password , appointment_obj , connection) :
        if patient_national_code not in Patient.all_patient :
            if temporary_password == 'No' : 
               Patient.all_patient[patient_national_code] = Patient(patient_national_code , patient_name , patient_contact_info , age , insurance , illness_history , generate_password(10) , 'No' , appointment_obj , connection)
            elif temporary_password == 'Yes' : 
                Patient.all_patient[patient_national_code] = Patient(patient_national_code , patient_name , patient_contact_info , age , insurance , illness_history , generate_password(10) , 'Yes' , appointment_obj , connection)
        else : 
            print('This name is already exist in our database')

    def log_in(self , patient_national_code , password) : 
        if patient_national_code in Patient.all_patient : 
            if Patient.all_patient[patient_national_code].temporary_password == 'No':
                if Patient.all_patient[patient_national_code].permanent_password == password : 
                    print('login succesfully')
                else : 
                    print('password is wrong')
            elif Patient.all_patient[patient_national_code].temporary_password == 'Yes':
                print(f'Your one-time password is {generate_password(10)}')
                print('Login succesfully')
        else : 
            print('This name does not exist in our database')

    # appointment_obj here is an istanse of class appointment:
    def book_appointment(self , appointment_obj):
        return appointment_obj.add_appointment(self.name)

    def cancel_appointment(self , appointment_obj):
        return appointment_obj.remove_appointment(self.name)

    def get_info(self):
        if len(self.patient_natinal_code) != 10:
            print("national code is incorrect")
        elif len(self.permanent_password) < 8 or not any (c.isdigit for c in self.permanent_password) :
            print('The password is weak.')
        elif len(self.patient_contact_info) != 8 :
            print("this phone number is incorrect")
        return {
            "patient_natinal_code" : self.patient_natinal_code,
            "patient_name" : self.patient_name,
            "patient_contact_info" : self.patient_contact_info,
            "patient_age" : self.age,
            "patient_insurance" : self.insurance,
            
            "patient_permanent_password" : self.permanent_password,
            "patient_temporary_password" : self.temporary_password,
        }
        
    # THIS IS NEW/THIS PART IS FOR DATABASE
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
                INSERT INTO patients (patient_national_code, patient_name , patient_contact_info , patient_age , patient_insurance , patient_permanent_password) 
                VALUES (%s , %s , %s , %s , %s , %s , %s , %s)
                """
                val = (data['patient_natinal_code'] , data['patient_name'] , data['patient_contact_info'] , data['patient_age'] , data['patient_insurance'] , data['patient_permanent_password'])
                cursor.execute(sql, val)
                self.connection.commit()
    # UNTIL HERE
      
#sign in and login patients with using sign_in and log_in methods using this test object that created in the code :
#example : p.sign_in("bla bla bla" ... )
p = Patient("0000000000" , "test" , "00000000" , "0" , "0" , "0" , "yes" , "0000" ,"0" , "0")

connection = pymysql.connect(host = 'localhost' ,
                             user = 'root' ,
                             password = 'APterm3r@r@8304' ,
                             database = 'APclinics')