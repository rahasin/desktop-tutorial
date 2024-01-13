#class doctor
from Patient import Patient
class Doctor:
    def __init__(self):
      self.doctor_special_code = 'd7654321_doc*'
      self.clinic_ids = [1,2,3,4,5,6,7]
      #here you should add another atribute to make a dictionary for referring each clinic id to each table.

    def enter_code(self):
      while True:
        code = input("Please enter the doctor special code: ")
        if code == self.doctor_special_code:
          return True
        else:
          print('The doctor special code is wrong.')
          return False
      
    def choose_clinic(self):
        while True:
            clinic_id = int(input('Please choose your clinic id.'))
            if clinic_id in self.clinic_ids:
                return clinic_id
            else:
                print('No clinic exists with this id. Please try again.')
         
      
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
    
    def view_patient_data(self):
        
          patient_national_code = input("Please enter the patient's national code: ")
          if patient_national_code in Patient.all_patient:
              return patient_national_code
          else:
              print('No patient exists with this national code.')
              return False
        
    #if the join is needed
    def select_each_patient_info(self, patient_national_code):
        sql_query = """
        SELECT 
        patient_national_code, 
        patient_name, 
        patient_contact_info, 
        patient_age, 
        patient_insurance, 
        patients_reserved_appointments
        FROM patients 
        WHERE patients_reserved_appointments > 0 AND
        patient_national_code = %s
        """

        values = ( patient_national_code)
        return self.execute_query(sql_query, values)
        
    

    

    

