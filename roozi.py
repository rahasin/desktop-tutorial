import random
import string

#username is a "only_lowercase" string with length 5
#password is a "lowercase + digit" string with length 10

#password and username generator functions : 
def generate_password(length):
    characters = string.ascii_lowercase + string.digits 
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_username(length): 
    characters = string.ascii_lowercase
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


User_list = []


class Poeple :

    def __init__(self) : 
        self.users = {}

    def sign_in(self , email , name , national_code , age , insurance , sickness , user_type ):
        if name not in self.users :
            self.users[name] = User(email , name , national_code , age , insurance , sickness , user_type , generate_username(5) , generate_password(10))
        else : 
            raise Exception ("This name is already exist in our database")
    def log_in(self , username , password ) : 
        pass

    def refresh_profile(self , name , username , password) :
        pass

    def meetings(self , name , username , password) :  
        pass

class User :

    def __init__(self , email , name , national_code , age , insurance , sickness , user_type , username , password):
        self.name = name
        self.email = email
        self.national_code = national_code
        self.age = age
        self.insurance = insurance
        self.sickness = sickness
        self.user_type = user_type
        self.username = username
        self.password = password

