import random
import string
import pymysql

#password is a "lowercase + digit" string with length 10
#password and username generator functions : 

def generate_password(length):
    characters = string.ascii_lowercase + string.digits 
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

class People :

    all_people = {}

    def __init__(self) : 
        self.conn = pymysql.connect(host='localhost', user='root', password='APterm3r@r@8304', database='APclinics') 
        self.cursor = self.conn.cursor()

    def sign_in(self , email , name , national_code , age , insurance , sickness , user_type , yekbar_masraf):
        
        if name not in People.all_people :
            if yekbar_masraf == "no" : 
                People.all_people[name] = Patient(email , name , national_code , age , insurance , sickness , user_type  , generate_password(10) , "no")
            elif yekbar_masraf == "yes" : 
                People.all_people[name] = Patient(email , name , national_code , age , insurance , sickness , user_type  , generate_password(10) , "yes")
        else : 
            print("This name is already exist in our database")

    def log_in(self , name , password ) : 
        if name in People.all_people : 
            if People.all_people[name].yekbar_masraf == "no":
                if People.all_people[name].password == password : 
                    print("login succesfully")
                else : 
                    print("password is wrong")
            elif People.all_people[name].yekbar_masraf == "yes":
                print(f"your one-time password is {generate_password(10)}")
                print("login succesfully")
        else : 
            print("username is wrong")

    
    def insert_data(self, user):
            with self.conn.cursor() as cursor:
                sql = """
                INSERT INTO patients (email, name, national_code, age, insurance, sickness, user_type, username, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (user.email, user.name, user.national_code, user.age, user.insurance, user.sickness, user.user_type, user.password))
            self.conn.commit()
        
        
class Patient :

    def __init__(self , email , name , national_code , age , insurance , sickness , user_type , password , yekbar_masraf):
        self.name = name
        self.email = email
        self.national_code = national_code
        self.age = age
        self.insurance = insurance
        self.sickness = sickness
        self.user_type = user_type
        self.password = password
        self.yekbar_masraf = yekbar_masraf

    # appointment_obj here is an istanse of class appointment:
    def book_appointment(self, appointment_obj):
        return appointment_obj.add_appointment(self.name)

    def cancel_appointment(self, appointment_obj):
        return appointment_obj.remove_appointment(self.name)

