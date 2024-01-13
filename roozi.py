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



class Doctor:
   def __init__(self):
      self.doctor_special_code = 'abcd123'
      self.clinic_ids = [1,2,3,4,5,6,7]
      #here you should add another atribute to make a dictionary for referring each clinic id to each table.

   def enter_code(self):
      code = input("Please enter the doctor special code: ")
      if code == self.doctor_special_code:
         return True
      else:
         return print('The doctor special code is wrong.')
      
   def choose_clinic(self):
      clinic_id = int(input('Please choose your clinic id.'))
      if clinic_id in self.clinic_ids:
         return clinic_id
      else:
         return print('No clinic exists with this id.')
      
      
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

   def select_each_clinic_info(self, clinic_id):
        query = "SELECT  clinic_id, service, capacity, reserved_appointments FROM clinics WHERE clinic_id = ? ORDER BY clinic_id"
        values = (clinic_id,)
        return self.execute_query(query, values)

doctor = Doctor()

if doctor.enter_code():
    clinic_id = doctor.choose_clinic()
    clinic_info = doctor.select_each_clinic_info(clinic_id)
    print(clinic_info)






#doctor sql code: 
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


#if the join is needed 
def select_each_clinic_info(self, clinic_id):
        query = """
        SELECT 
        patient_national_code, 
        patient_name, 
        patient_contact_info, 
        patient_age, 
        patient_insurance, 
        patients_reserved_appointments
        FROM patients 
        WHERE clinic_id = ? AND 
        patients_reserved_appointments > 0 
        """

        values = (clinic_id,)
        return self.execute_query(query, values)
    
#if the join is needed
def select_each_patient_info(self, clinic_id, patient_national_code):
    sql_query = """
    SELECT 
    patient_national_code, 
    patient_name, 
    patient_contact_info, 
    patient_age, 
    patient_insurance, 
    patients_reserved_appointments
    FROM patients 
    WHERE clinic_id = %s AND 
    patients_reserved_appointments > 0 AND
    patient_national_code = %s
    """

    values = (clinic_id, patient_national_code)
    return self.execute_query(sql_query, values)
    
    
