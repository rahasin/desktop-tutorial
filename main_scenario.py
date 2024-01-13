from  Secretary  import Secretary
from Appointment import Appointment
from Clinic import Clinic
from Doctor import Doctor
from Patient import Patient

def logout():
        print('You have been logged out.')
        return None

def main():
    while True:
        print('1. Patient')
        print('2. Secretary')
        print('3. Doctor')
        position = int(input("Please choose your position: "))
        if position == 1:
            pass
        elif position == 2:
            pass
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
                    doctor.logout()
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid option. Please try again.")

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Get user input to determine which character they want to be
    character_choice = input("Choose a character (Doctor, Patient, Secretary): ")
    
    if character_choice.lower() == "doctor":
        doctor = Doctor()
        if doctor.enter_code():
            clinic_id = doctor.choose_clinic()
            clinic_info = doctor.select_each_clinic_info(clinic_id)
            print(clinic_info)
            
    elif character_choice.lower() == "patient":
        patient_national_code = input("Enter your national code: ")
        patient_name = input("Enter your name: ")
        patient_contact_info = input("Enter your contact info: ")
        age = input("Enter your age: ")
        insurance = input("Do you have insurance (yes/no): ")
        password_type = input("Do you want a permanent or temporary password: ")
        patient = Patient(patient_national_code, patient_name, patient_contact_info, age, insurance, password_type)
        patient.sign_in()
        # Continue with the scenario as the patient
    elif character_choice.lower() == "secretary":
        secretary = Secretary()
        if secretary.enter_code():
            clinic_id = secretary.choose_clinic()
            # Continue with the scenario as the secretary
    else:
        print("Invalid choice. Please choose Doctor, Patient, or Secretary.")

if __name__ == "__main__":
    main()
