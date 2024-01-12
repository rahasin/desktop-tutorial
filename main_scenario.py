from  Secretary  import Secretary
from Appointment import Appointment
from Clinic import Clinic
from Doctor import Doctor
from Patient import Patient

def main():
    # Get user input to determine which character they want to be
    character_choice = input("Choose a character (Doctor, Patient, Secretary): ")
    
    if character_choice.lower() == "doctor":
        doctor = Doctor()
        if doctor.enter_code():
            clinic_id = doctor.choose_clinic()
            # Continue with the scenario as the doctor
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
