class Pharmacy:
    def __init__(self, inventory):
        # Inventory is a dictionary with drug names as keys and quantities as values
        self.inventory = inventory

    def dispense_drug(self, drug):
        # Check if the drug is in stock
        if self._check_availability(drug):
            self._update_inventory(drug)
            print(f"Dispensed {drug}")
        else:
            print(f"Sorry, {drug} is currently out of stock.")

    def _check_availability(self, drug):
        # Check if the drug is in stock
        return drug in self.inventory and self.inventory[drug] > 0

    def _update_inventory(self, drug):
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

# Get the drug information
drug = input("Enter the drug: ")

# Use the Pharmacy instance to dispense the drug
pharmacy.dispense_drug(drug)
