"""
    Employee Columns: [Name, Wage] *Starts on row 3
        A(1): Employee Name
        B(2): Wage (e.g., "$15.00")
"""

class EmployeeManager:
    def __init__(self, sheet_manager):
        self.sm = sheet_manager


    def _get_row_index(self, name):
        """Helper to find the row index of an employee in Column A (1)."""
        names = self.sm.get_column_values("DATA", 1)
        try:
            return names.index(name) + 1
        except ValueError:
            return None


    def add(self, name, wage="$0.00"):
        """Adds name and wage starting at Row 3."""
        # Find next empty row in Column A
        current_names = self.sm.get_column_values("DATA", 1)
        next_row = len(current_names) + 1
        
        # Safety: Never overwrite headers on Row 1 or 2
        if next_row < 3:
            next_row = 3
            
        self.sm.update_range("DATA", f"A{next_row}:B{next_row}", [[name, wage]])
        print(f"Added Employee {name} with wage {wage}")


    def update(self, name, new_name=None, new_wage=None):
        row = self._get_row_index(name)
        if not row:
            print(f"Employee {name} not found.")
            return

        current_name = new_name if new_name else name
        current_wage = new_wage if new_wage is not None else self.sm.get_cell_value("DATA", row, 2)
        
        self.sm.update_range("DATA", f"A{row}:B{row}", [[current_name, current_wage]])
        print(f"Updated {name}'s details.")


    def delete(self, name):
        """Clears name and wage from the row."""
        row = self._get_row_index(name)
        if row:
            # We clear A and B to keep the list layout
            self.sm.update_range("DATA", f"A{row}:B{row}", [["", ""]])
            print(f"Removed {name} and their wage data.")


    def get(self, name):
        row = self._get_row_index(name)
        if row:
            wage = self.sm.get_cell_value("DATA", row, 2)
            return {"name": name, "wage": wage}
        return None


    def get_names(self):
        """Returns names from Column A, skipping the TWO header rows."""
        names = self.sm.get_column_values("DATA", 1)
        # names[2:] skips Row 1 (Title) and Row 2 (Labels)
        
        names_list = [n for n in names[2:] if n]
        print(f"Employee names: {names_list}")
        return names_list


    def _exists(self, name):
        """Checks if a name already exists in the list."""
        return name in self.get_names()