import random
import string
import pymysql

#password is a "lowercase + digit" string with length 10
#password generator functions : 

def generate_password(length) :
    characters = string.ascii_lowercase + string.digits 
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

class People :

#This class generate several objects from diffrent classes
     
    all_people = {}

    def __init__(self , connection) : 
        self.connection = connection
        
    def sign_in_patient(self , patient_national_code , patient_name , patient_contact_info , age , insurance , illness_history , one_time_password , appointment_obj , connection) :
        if patient_name not in People.all_people :
            if one_time_password == 'No' : 
                People.all_people[patient_name] = Patient(patient_national_code , patient_name , patient_contact_info , age , insurance , illness_history , generate_password(10) , 'No' , appointment_obj , connection)
            elif one_time_password == 'Yes' : 
                People.all_people[patient_name] = Patient(patient_national_code , patient_name , patient_contact_info , age , insurance , illness_history , generate_password(10) , 'Yes' , appointment_obj , connection)
        else : 
            print('This name is already exist in our database')

    def log_in_patient(self , patient_name , password) : 
        if patient_name in People.all_people : 
            if People.all_people[patient_name].one_time_password == 'No':
                if People.all_people[patient_name].password == password : 
                    print('login succesfully')
                else : 
                    print('password is wrong')
            elif People.all_people[patient_name].one_time_password == 'Yes':
                print(f'Your one-time password is {generate_password(10)}')
                print('Login succesfully')
        else : 
            print('This name does not exist in our database')
    # a get_info function should be created, returning a dictionary of all the necessary info like the other classes
    def insert_data_patient(self):
        data = self.get_info()
        if data is not None:    
            with self.conn.cursor() as cursor:
                sql = """
                INSERT INTO patients (patient_natinal_code , patient_name , patient_contact_info , age , insurance , illness_history)
                VALUES (%s , %s , %s , %s , %s , %s , %s)
                """
                cursor.execute(sql , (data['patient_natinal_code'] , data['patient_name'] , data['patient_contact_info'] , data['age'] , data['insurance'] , data['illness_history']))
            self.connection.commit()
    
    def sign_in_secretary(self , secretary_name , clinic_id , clinic_password , appointment):
        if secretary_name in People.all_people : 
            print("this name is already exist in our database")
        else :
            People.all_people[secretary_name] = Secretary(secretary_name , clinic_id , clinic_password , appointment)
        
    def log_in_secretary(self , secretary_name , clinic_id , clinic_password):
        if secretary_name not in People.all_people : 
            print("the username/secretary name is wrong")
        elif clinic_password != People.all_people[clinic_id].clinic_password : 
            print("password is wrong")
        else : 
            print("login succesfully")

    def sign_in_clinic(self , clinic_id , address , clinic_contact_info , clinic_password , capacity , service , connection) : 
        if clinic_id in People.all_people : 
            print("this clinic id is already exist in our database")
        else : 
            People.all_people[clinic_id] = Clinic(clinic_id , address , clinic_contact_info , clinic_password , capacity , service , connection)           
        




class Patient :

    def __init__(self , patient_natinal_code , patient_name , patient_contact_info , age , insurance , illness_history , fixed_password , one_time_password , appointment_obj , connection):
        self.patient_natinal_code = patient_natinal_code
        self.patient_name = patient_name
        self.patient_contact_info = patient_contact_info
        self.age = age
        self.insurance = insurance
        self.illness_history = illness_history
        self.fixed_password = fixed_password
        self.one_time_password = one_time_password
        self.appointment_obj = appointment_obj  # This should be an instance of the Appointment class
        self.connection = connection
    # appointment_obj here is an istanse of class appointment:
    def book_appointment(self , appointment_obj):
        return appointment_obj.add_appointment(self.name)

    def cancel_appointment(self , appointment_obj):
        return appointment_obj.remove_appointment(self.name)

    # a get_info function should be created, returning a dictionary of all the necessary info like the other classes
    def insert_data(self):
        data = self.get_info()
        if data is not None:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO secretary (reserved_appointments , capacity, patient_natinal_code , patient_name , patient_contact_info) 
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql , (self.appointment_obj.reserved_appointments , self.appointment_obj.capacity , data['patient_natinal_code'] , data['patient_name'] , data['patient_contact_info']))
            self.connection.commit()

    def get_info(self):
        if len(self.patient_natinal_code) != 10:
            print("national code is incorrect")
        elif len(self.fixed_password) < 8 or not any (c.isdigit for c in self.fixed_password) :
            print('The password is weak.')
        elif len(self.patient_contact_info) != 8 :
            print("this phone number is incorrect")
        return {
            "patient_natinal_code" : self.patient_natinal_code,
            "patient_name" : self.patient_name,
            "patient_contact_info" : self.patient_contact_info,
            "patient_age" : self.age,
            "patient_insurance" : self.insurance,
            "patient_illness_history" : self.illness_history,
            "patient_fixed_password" : self.fixed_password,
            "patient_one_time_password" : self.one_time_password,
            "patient_appointment_obj" : self.appointment_obj,
            "patient_connection" : self.connection
        }



connection = pymysql.connect(host = 'localhost' ,
                             user = 'root' ,
                             password = 'APterm3r@r@8304' ,
                             database = 'APclinics')