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
      
    #here another function must be added such as get database/table.