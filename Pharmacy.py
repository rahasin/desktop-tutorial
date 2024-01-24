from db_connector import create_connection


class Pharmacy:

    def __init__(self, inventory):
        # Inventory is a dictionary with drug names as keys and quantities as values
        self.inventory = inventory
        self.connection = create_connection()

    def check_patient(self, patient_national_code):
        # Check if the patient exists in the database
        cursor = self.connection.cursor()
        sql = "SELECT * FROM patient_info WHERE patient_national_code = ?"
        cursor.execute(sql, (patient_national_code,))
        result = cursor.fetchone()
        if result is None:
            print('Please sign up first.')
            return False
        else:
            return True

    def check_insurance(self, patient_national_code):
        # Check if the patient has insurance
        cursor = self.connection.cursor()
        sql = "SELECT patient_insurance FROM patient_health WHERE patient_national_code = ?"
        cursor.execute(sql, (patient_national_code,))
        result = cursor.fetchone()
        if result is not None and result[0] == 'Yes':
            return True
        else:
            return False

    def dispense_drug(self, drug, patient_national_code):
        # Check if the patient exists
        if not self.check_patient(patient_national_code):
            return False

        # Check if the drug is in stock
        if not self.check_availability(drug):
            print(f'Sorry, {drug} is currently out of stock.\n')
            return False

        # Dispense the drug and update the inventory
        self.update_inventory(drug)

        # Check the patient's insurance status and print the appropriate message
        if self.check_insurance(patient_national_code):
            print('You have 70 percent discount as you have insurance.')
        else:
            print('You have to pay full price as you do not have insurance.')

        print('We have your drug in stock.\nThanks for your shopping!')
        return True

    def check_availability(self, drug):
        # Check if the drug is in stock
        if drug in self.inventory and self.inventory[drug] > 0 : 
            return True
        else : 
            return False

    def insert_inventory(self):
            # Inserting inventory
            cursor = self.connection.cursor()
            sql = "INSERT OR REPLACE INTO pharmacy (drug_name, quantity) VALUES (?, ?)"
            values = [(drug, quantity) for drug, quantity in self.inventory.items()]
            cursor.executemany(sql, values)
            self.connection.commit()
            
    def update_inventory(self, drug):
            try:
                # Dispense the drug and update the inventory
                self.inventory[drug] -= 1

                # Update the quantity in the database
                cursor = self.connection.cursor()
                sql = "UPDATE pharmacy SET quantity = ? WHERE drug_name = ?"
                values = (self.inventory[drug], drug)
                cursor.execute(sql, values)
                self.connection.commit()
            except Exception as e:
                print(f'An error occurred: {e}')
        

