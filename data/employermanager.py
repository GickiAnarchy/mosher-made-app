class EmployerManager:
    def __init__(self, worksheet):
        self.ws = worksheet


    def _get_row_index(self, name):
        """Helper to find the row index of an employer."""
        # Employers are in Column E (index 5)
        names = self.ws.col_values(5)
        try:
            return names.index(name) + 1
        except ValueError:
            return None


    def add(self, name, location=""):
        # We find the first empty row in Col E to append
        current_employers = self.ws.col_values(5)
        next_row = len(current_employers) + 1
        self.ws.update(f"E{next_row}:F{next_row}", [[name, location]])
        print(f"Added Employer {name}")


    def update(self, name, new_name=None, new_location=None):
        row = self._get_row_index(name)
        if not row:
            return
        
        target_name = new_name if new_name else name
        target_loc = new_location if new_location else self.ws.cell(row, 6).value
        
        self.ws.update(f"E{row}:F{row}", [[target_name, target_loc]])
        print(f"Updated Employer {name}")


    def delete(self, name):
        row = self._get_row_index(name)
        if row:
            self.ws.update(f"E{row}:F{row}", [["", ""]])
            print(f"Deleted Employer {name}")


    def get_names(self):
        employer_list = self.ws.get("Employers")
        return [name[0] for name in employer_list if name]


    def _exists(self, name):
        """Helper to check if a employers name already exists."""
        names = self.get_names()
        return name in names