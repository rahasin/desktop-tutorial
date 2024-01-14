from  Secretary  import Secretary
from Appointment import Appointment
from Clinic import Clinic
from Doctor import Doctor
from Patient import Patient
from Patient import generate_password()
import string
import random
def logout():
        print('You have been logged out.')
        return None



def main():
    while True:
        print('1. Patient')
        print('2. Secretary')
        print('3. Doctor')
        print('4. Logout')
        position = int(input("Please choose your position: "))

        if position == 1:
            patient = Patient()
            while True:
                print('1. Sign in')
                print('2. Log in')
                print('3. Log out')
                option = int(input('Please choose an option: '))
                if option == 1:
                    patient.get_info()
                    patient.sign_in()
                    patient.insert_data()
                if option == 2:
                    pass
                    patient.log_in()
                if option == 3:
                    logout()
                    break

                

        elif position == 2:
            secretary = Secretary()
            while True:
                if not secretary.enter_code():
                    break
                clinic_id = secretary.choose_clinic()
                secretary.select_each_clinic_info(clinic_id)
                # we can change the place of upper line with the prints!
                print ('1. Reserving an appointment')
                print('2. Canceling an appointment')
                print('3. Logout')
                option = int(input('Please choose an option: '))
                if option == 1:
                    pass
                elif option == 2:
                    pass
                elif option == 3:
                    logout()
                    break
                else :
                    print("Invalid option. Please try again.")


        elif position == 3:
            doctor = Doctor()
            while True:
                if not doctor.enter_code():
                    break

                print("1. View clinic table")
                print("2. View patient data")
                print("3. Logout")
                option = int(input("Please choose an option: "))
                if option == 1:
                    clinic_id = doctor.choose_clinic()
                    doctor.select_each_clinic_info(clinic_id)
                elif option == 2:
                    if not doctor.view_patient_data():
                        break
                    doctor.select_each_patient_info()
                elif option == 3:
                    logout()
                    break
                else:
                    print("Invalid option. Please try again.")


        elif position == 4:
            break
        else:
            print("Invalid option. Please try again.")

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
