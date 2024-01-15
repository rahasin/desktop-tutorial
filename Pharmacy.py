class Pharmacy:

    def __init__(self,inventory):
        # Inventory is a dictionary with drug names as keys and quantities as values
        self.inventory = inventory

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

    def update_inventory(self, drug):
        # Dispense the drug and update the inventory
        self.inventory[drug] -= 1

# Create an instance of the Pharmacy class



# Get the drug information
#drug = input("Enter the drug: ")

# Use the Pharmacy instance to dispense the drug
#pharmacy.dispense_drug(drug)

