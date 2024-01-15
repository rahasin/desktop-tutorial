from  Secretary  import Secretary
from Appointment import Appointment
from Clinic import Clinic
from Doctor import Doctor
from Patient import Patient
from Patient import generate_password
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
                  while True:
                    patient.get_info()
                    patient.sign_in()
                    patient.insert_data()
                    print('1. Log in')
                    print('2. Log out')
                    option2 = int(input('Please choose an option: '))
                    if option2 == 1:
                      while True:
                        patient.log_in()
                        print('1. Your reserved appointments')
                        print('2. Available appointments')
                        print('3. Log out')
                        option3 = int(input('Please choose an option: '))
                        if option3 == 1:
                            while True:
                                patient.select_patient_reserved_appointments_info(patient_national_code=input('Please enter your national code.'))
                                print('1. Available appointments')
                                print('2. Log out')
                                option4 = int(input('Please choose an option: '))
                                if option4 == 1:
                                  while True:
                                    clinic_id = int(input('Choose a clinic id'))
                                    patient.select_clinic_capacity_info(clinic_id)
                                    print('1. Reserve an appointment')
                                    print('2. Cancel an appointment')
                                    print('3. Log out')
                                    option5 = int(input('Choose an option: '))
                                    if option5 == 1:
                                        Appointment.reserve_appointment(clinic_id,patient_national_code = input('Please enter your national code.'))
                                    elif option5 == 2:
                                        Appointment.cancel_appointment(clinic_id,patient_national_code=input('Please enter your national code.'))
                                    elif option5 == 3:
                                        logout()
                                        break
                                    else:
                                        ("Invalid option. Please try again.")
                                elif option4 == 2:
                                    logout()
                                    break
                                else:
                                    print("Invalid option. Please try again.")
                        elif option3 == 2:
                            while True:
                                    clinic_id = int(input('Choose a clinic id'))
                                    patient.select_clinic_capacity_info(clinic_id)
                                    print('1. Reserve an appointment')
                                    print('2. Cancel an appointment')
                                    print('3. Log out')
                                    option6 = int(input('Choose an option: '))
                                    if option6 == 1:
                                        Appointment.reserve_appointment(clinic_id,patient_national_code=input('Please enter your national code.'))
                                    elif option6 == 2:
                                        Appointment.cancel_appointment(clinic_id,patient_national_code=input('Please enter your national code.'))
                                    elif option6 == 3:
                                        logout()
                                        break
                                    else:
                                        ("Invalid option. Please try again.")
                        elif option3 == 3:
                            logout()
                            break
                        else :
                            print("Invalid option. Please try again.")
                        
                    elif option2 == 2:
                        logout()
                        break
                    else:
                        print("Invalid option. Please try again.")
                elif option == 2:
                    patient.log_in()
                elif option == 3:
                    logout()
                    break
                else:
                    print("Invalid option. Please try again.")


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

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
