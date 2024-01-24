from  Secretary  import Secretary
from Appointment import Appointment
from Doctor import Doctor
from Patient import Patient
from Pharmacy import Pharmacy
from Clinic import Clinic
from prettytable import PrettyTable
# Logging out
def log_out():
        print('You have been logged out.')
        return None


def main():
    clinic = Clinic()
    try:
        clinic.get_info()
        clinic.insert_data()
    finally:
        clinic.close_connection()

    while True:
        print('1. Patient')
        print('2. Secretary')
        print('3. Doctor')
        print('4. Pharmacy')
        position = int(input('Please choose your position: '))
        if position == 1:
            patient = Patient()
            appointment = Appointment()
            while True:
                print('1. Sign up')
                print('2. Log in')
                print('3. Log out')
                option = int(input('Please choose an option: '))
                if option == 3 :
                    log_out()
                    break
                elif option == 1:
                    patient.insert_data()
                    patient.sign_up()
                    print('Now you are heading to home page.')
                elif option == 2:
                    if not patient.log_in() : 
                        break
                    else :
                        while True:
                            print('1. Your reserved appointments')
                            print('2. Available appointments')
                            print('3. Log out')
                            option1 = int(input('Please choose an option: '))
                            if option1 == 3:
                                log_out()
                                break
                            elif option1 == 1:
                                while True:
                                    result_patinet_reserved = patient.select_patient_reserved_appointments_info(patient_national_code=input('Please enter your national code.'))
                                    table = PrettyTable()
                                    table.field_names = ["Patient National Code", "Patient Name", "Clinic ID", "Reserved Appointments"]
                                    for row in result_patinet_reserved:
                                        table.add_row(row)
                                    print('\nPatient Reserved Appointments Info: ')
                                    print(table)
                                    print('Heading to previous menu.')
                                    break
                            elif option1 == 2:
                                while True:
                                        clinic_id = int(input('Choose a clinic id: '))
                                        result_view_capacity = patient.select_clinic_capacity_info(clinic_id)
                                        print('\nClinic Capacity Info: ')
                                        table = PrettyTable()
                                        table.field_names = ["Clinic ID", "Service", "Capacity", "Reserved Appointments", "Address", "Contact Info"]
                                        for row in result_view_capacity:
                                            table.add_row(row)
                                        print('\nClinic Capacity Info: ')
                                        print(table)
                                        print('1. Reserve an appointment')
                                        print('2. Cancel an appointment')
                                        print('3. Logout')
                                        option2 = int(input('Choose an option: '))
                                        if option2 == 1:
                                            clinic_id = int(input('Please choose a clinic id: '))
                                            number_of_appointments = int(input('Enter the number of appointments to reserve: '))
                                            patient_national_code = input('Enter the patient\'s national code: ')
                                            result_reservation = appointment.reserve_appointment(clinic_id, number_of_appointments, patient_national_code)
                                            input('For loging out, enter a word: ')
                                            log_out()
                                            print('Back to main menu.')
                                            break
                                        elif option2 == 2:
                                            clinic_id = int(input('Please choose a clinic id: '))
                                            number_of_appointments = int(input('Enter the number of appointments to cancel: '))
                                            patient_national_code = input('Enter the patient\'s national code: ')
                                            result_cancellation = appointment.cancel_appointment(clinic_id, number_of_appointments, patient_national_code)
                                            print(result_cancellation)
                                            input('For loging out, enter a word: ')
                                            log_out()
                                            print('Back to main menu.')
                                            break
                                        elif option2 == 3:
                                            log_out()
                                            print('Back to main menu.')
                                            break
        elif position == 2:
            secretary = Secretary()
            appointment = Appointment()
            while True:
                print('1. Login to secretary page')
                print('2. Exit')
                option1 = int(input('Choose an option: '))
                if option1 == 2 :
                    print('Heading to home page.')
                    break
                elif option1 == 1 :
                    if not secretary.enter_code():
                        break
                    clinic_id = secretary.choose_clinic()
                    result_secretary_view_info = secretary.select_each_clinic_info(clinic_id)
                    table = PrettyTable()
                    table.field_names = ["Patient National Code", "Patient Name", "Reserved Appointments", "Patient Age", "Patient Insurance", "Patient Contact Info"]
                    for row in result_secretary_view_info:
                        table.add_row(row)
                    print('\nEach Clinic Info: ')
                    print(table)
                    while True :
                        print('1. Reserving an appointment')
                        print('2. Canceling an appointment')
                        print('3. Increase clinic capacity')
                        print('4. Logout')
                        option = int(input('Please choose an option: '))
                        if option == 1:
                            clinic_id = int(input('Please choose a clinic id: '))                           
                            number_of_appointments = int(input('Enter the number of appointments to reserve: '))                           
                            patient_national_code = input('Enter the patient\'s national code: ')                           
                            result_reservation = appointment.reserve_appointment(clinic_id, number_of_appointments, patient_national_code)
                            print(result_reservation)
                        elif option == 2:
                            clinic_id = int(input('Please choose a clinic id: '))                          
                            number_of_appointments = int(input('Enter the number of appointments to cancel: '))                           
                            patient_national_code = input('Enter the patient\'s national code: ')                           
                            result_cancellation = appointment.cancel_appointment(clinic_id, number_of_appointments, patient_national_code)
                            print(result_cancellation)
                        elif option == 3:
                            clinic_id = int(input('Please choose a clinic id: '))                      
                            increase_amount = int(input('Enter the amount to increase the clinic capacity: '))                          
                            result_increase = appointment.increase_capacity(clinic_id, increase_amount)
                            if result_increase:
                                print('Clinic capacity increased successfully.')
                            else:
                                print('Failed to increase clinic capacity.')
                        elif option == 4:
                            log_out()
                            break
                        else :
                            print('Invalid option. Please try again.')

        elif position == 3:
            doctor = Doctor()
            while True:
                if not doctor.enter_code():
                    break

                print('1. View clinic table')
                print('2. View patient data')
                print('3. Logout')
                option = int(input('Please choose an option: '))
                if option == 1:
                    clinic_id = doctor.choose_clinic()
                    result_doctor_view_info = doctor.select_each_clinic_info(clinic_id)
                    table = PrettyTable()
                    table.field_names = ["Patient National Code", "Patient Name", "Patient Age", "Patient Insurance", "Patient Contact Info", "Reserved Appointments"]
                    for row in result_doctor_view_info:
                        table.add_row(row)
                    print('\nEach Clinic Info:')
                    print(table)
                elif option == 2:
                    if not doctor.view_patient_data():
                        break
                    result_view_patient = doctor.select_each_patient_info(patient_national_code=input('Please enter your national code.'))
                    table = PrettyTable()
                    table.field_names = ["Patient National Code", "Patient Name", "Patient Age", "Patient Insurance", "Patient Contact Info", "Reserved Appointments"]
                    for row in result_view_patient:
                        table.add_row(row)
                    print('\nEach Patient Info: ')
                    print(table)
                elif option == 3:
                    log_out()
                    break
                else:
                    print('Invalid option. Please try again.')

        elif position == 4:
            pharmacy = Pharmacy(inventory = {
                'Tetrahydrozoline': 25,
                'carbetocin': 15,
                'Mometasone': 15,
                'Amoxicillin': 20,
                'Diclofenac': 30,
                'Amiodarone': 9,
                'Articaine': 8
            })
            pharmacy.insert_inventory()
            while True :
                print('1. Tetrahydrozoline')
                print('2. carbetocin')
                print('3. Mometasone')
                print('4. Amoxicillin')
                print('5. Diclofenac')
                print('6. Amiodarone')
                print('7. Articaine')
                print('8. Log out')
                patient_national_code = input('Please enter your national code: ')
                option7 = int(input('Please Enter the drug name'))
                if option7 == 1: 
                    pharmacy.dispense_drug('Tetrahydrozoline', patient_national_code)
                    log_out()
                    break
                elif option7 == 2:
                    pharmacy.dispense_drug('carbetocin', patient_national_code)
                    log_out()
                    break
                elif option7 == 3:
                    pharmacy.dispense_drug('Mometasone', patient_national_code)
                    log_out()
                    break
                elif option7 == 4:
                    pharmacy.dispense_drug('Amoxicillin', patient_national_code)
                    log_out()
                    break
                elif option7 == 5:
                    pharmacy.dispense_drug('Diclofenac', patient_national_code)
                    log_out()
                    break
                elif option7 == 6:
                    pharmacy.dispense_drug('Amiodarone', patient_national_code)
                    log_out()
                    break
                elif option7 == 7:
                    pharmacy.dispense_drug('Articaine', patient_national_code)
                    log_out()
                    break
                elif option7 == 8:
                    log_out()
                    break

        

        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
