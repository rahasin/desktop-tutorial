#class Secretary
from db_connector import create_connection

class Secretary:
   def __init__(self):
      self.connection = create_connection()
      self.secretary_special_code = 's1234567@c'
      self.clinic_ids = [1,2,3,4,5,6,7]
      #here you should add another atribute to make a dictionary for referring each clinic id to each table.

   def enter_code(self):
      code = input("Please enter the secretary special code: ")
      if code == self.secretary_special_code:
         return True
      else:
         return print('The secretary special code is wrong.')
      
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
    


        