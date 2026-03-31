"""
    Employer Columns:
        F(6): Employer Name
        G(7): Location (optional)
        H(8): Notes (optional)
"""

class EmployerManager:
    def __init__(self, worksheet):
        self.ws = worksheet


    def _get_row_index(self, name):
        # Column F is index 6
        names = self.ws.col_values(6)
        try:
            return names.index(name) + 1
        except ValueError:
            return None


    def add(self, name, location="", notes=""):
        # Column F is index 6
        current_employers = self.ws.col_values(6)
        next_row = len(current_employers) + 1
        # Update F, G, and H
        self.ws.update(f"F{next_row}:H{next_row}", [[name, location, notes]])


    def get_all_employers_data(self, as_dict=True):
        # Starts at F3 because F1 and F2 are headers in your CSV
        data = self.ws.get("F3:H")
        clean_data = [row for row in data if row and row[0]]

        if not as_dict:
            return clean_data

        employer_list = []
        for row in clean_data:
            employer_list.append({
                "name": row[0],
                "location": row[1] if len(row) > 1 else "",
                "notes": row[2] if len(row) > 2 else ""
            })
        return employer_list


    def update(self, name, new_name=None, new_location=None, new_notes=None):
        row = self._get_row_index(name)
        if not row:
            print(f"Employer {name} not found.")
            return
        
        # Logic to keep existing values if new ones aren't provided
        target_name = new_name if new_name else name
        target_loc = new_location if new_location is not None else self.ws.cell(row, 7).value
        target_notes = new_notes if new_notes is not None else self.ws.cell(row, 8).value
        
        self.ws.update(f"F{row}:H{row}", [[target_name, target_loc, target_notes]])
        print(f"Updated Employer {name}")


    def delete(self, name):
        row = self._get_row_index(name)
        if row:
            # Clears columns F, G, and H for that row
            self.ws.update(f"F{row}:H{row}", [["", "", ""]])
            print(f"Deleted Employer {name}")


    def get_names(self):
        """Returns a list of all employer names from Column F."""
        names = self.ws.col_values(6)
        # Skip the header row
        return [name for name in names[1:] if name]


    def _exists(self, name):
        """Helper to check if an employer name already exists."""
        return name in self.get_names()


    def get_locations(self):
        """Returns a list of all locations only (Column G / 7)."""
        locations = self.ws.col_values(7)
        return [loc for loc in locations[1:] if loc]


    def get_notes(self, name):
        """Returns the notes (Column H / 8) for a given employer."""
        row = self._get_row_index(name)
        if row:
            return self.ws.cell(row, 8).value 
        return None