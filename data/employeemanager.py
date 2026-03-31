

class EmployeeManager:
    def __init__(self, worksheet):
        self.ws = worksheet


    def _get_row_index(self, name):
        """Helper to find the row index of an employee."""
        names = self.ws.col_values(1)
        try:
            return names.index(name) + 1
        except ValueError:
            return None


    def add(self, name, wage="$0.00"):
        self.ws.append_row([name, wage])
        print(f"Added Employee {name} with wage {wage}")


    def update(self, name, new_name=None, new_wage=None):
        row = self._get_row_index(name)
        if not row:
            print(f"Employee {name} not found.")
            return

        # Fetch current values if updates aren't provided
        current_name = new_name if new_name else name
        # If updating name but not wage, we need the existing wage from the sheet
        current_wage = new_wage if new_wage else self.ws.cell(row, 2).value
        
        self.ws.update(f"A{row}:B{row}", [[current_name, current_wage]])
        print(f"Updated {name}'s details.")


    def delete(self, name):
        row = self._get_row_index(name)
        if row:
            self.ws.update(f"A{row}:B{row}", [["", ""]])
            print(f"Removed {name} and their wage data.")


    def list_all(self):
        # Assumes a named range "Employees" exists or fetches Col A
        return [name[0] for name in self.ws.get("Employees") if name]


    def get(self, name):
        row = self._get_row_index(name)
        if row:
            wage = self.ws.cell(row, 2).value
            return {"name": name, "wage": wage}
        return None


    def get_names(self):
        names = self.ws.get("Employees")
        return names


    def _exists(self, name):
        """Helper to check if a employees name already exists."""
        names = self.get_names()
        return name in names