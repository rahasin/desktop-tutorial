from db_connector import create_connection

class Pharmacy:

    def __init__(self,inventory):
        # Inventory is a dictionary with drug names as keys and quantities as values
        self.inventory = inventory
        self.connection = create_connection()

    def dispense_drug(self, drug):
        # Check if the drug is in stock
        if self.check_availability(drug):
            self.update_inventory(drug)
            print("We have your drug in stock.\nThanks for your shopping!")
            return True
        else:
            print(f"Sorry, {drug} is currently out of stock.\n")
            return False

    def check_availability(self, drug):
        # Check if the drug is in stock
        if drug in self.inventory and self.inventory[drug] > 0 : 
            return True
        else : 
            return False

    def insert_inventory(self):
        cursor = self.connection.cursor()
        sql = "INSERT OR REPLACE INTO pharmacy (drug_name, quantity) VALUES (?, ?)"
        values = [(drug, quantity) for drug, quantity in self.inventory.items()]
        cursor.executemany(sql, values)
        self.connection.commit()
    
    def update_inventory(self, drug):
        # Dispense the drug and update the inventory
        self.inventory[drug] -= 1

        # Update the quantity in the database
        cursor = self.connection.cursor()
        sql = "UPDATE pharmacy SET quantity = ? WHERE drug_name = ?"
        values = (self.inventory[drug], drug)
        cursor.execute(sql, values)
        self.connection.commit()
    

