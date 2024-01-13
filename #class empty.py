# class empty
class Patient:
    def __init__(self, national_code, has_insurance):
        self.national_code = national_code
        self.has_insurance = has_insurance

class Pharmacy:
    def __init__(self, inventory):
        self.inventory = inventory

    def fill_prescription(self, prescription, patient):
        if self._validate_prescription(prescription) and patient.has_insurance:
            drug = prescription['drug']
            if self._check_availability(drug):
                self._dispense_drug(drug)
                print(f"Dispensed {drug} to patient {prescription['patient_national_code']}")
            else:
                print(f"Sorry, {drug} is currently out of stock.")
        elif not patient.has_insurance:
            print("The patient does not have insurance and cannot purchase the drug.")
        else:
            print("Invalid prescription")

    def _validate_prescription(self, prescription):
        # Check if the prescription has all the necessary fields
        required_fields = ['patient_national_code', 'drug']
        return all(field in prescription for field in required_fields)

    def _check_availability(self, drug):
        # Check if the drug is in stock
        return drug in self.inventory and self.inventory[drug] > 0

    def _dispense_drug(self, drug):
        # Dispense the drug and update the inventory
        self.inventory[drug] -= 1
        
# Create an instance of the Pharmacy class
inventory = {
    'DrugA': 10,
    'DrugB': 20,
    'DrugC': 15,
    'DrugD': 30
}
pharmacy = Pharmacy(inventory)

# Get the patient's information
national_code = input("Enter the patient's national code: ")
has_insurance = input("Does the patient have insurance? (yes/no): ").lower() == 'yes'

# Create a Patient instance
patient = Patient(national_code, has_insurance)

# Get the drug information
drug = input("Enter the drug: ")

# Create a prescription
prescription = {
    'patient_national_code': national_code,
    'drug': drug
}

# Use the Pharmacy instance to fill the prescription
pharmacy.fill_prescription(prescription, patient)
