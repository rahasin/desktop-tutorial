#class doctor
class Doctor:
    def __init__(self):
      self.doctor_special_code = 'd7654321_doc*'
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
        query = f"""
        SELECT  clinic_id, service, capacity, reserved_appointments 
        FROM clinics 
        WHERE clinic_id = ? 
        ORDER BY clinic_id
        """
        values = (clinic_id,)
        return self.execute_query(query, values)

doctor = Doctor()
if doctor.enter_code():
    clinic_id = doctor.choose_clinic()
    clinic_info = doctor.select_each_clinic_info(clinic_id)
    print(clinic_info)