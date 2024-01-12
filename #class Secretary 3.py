#class Secretary
class Secretary:
   def __init__(self):
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
      
    #here another function must be added such as get database/table.


        