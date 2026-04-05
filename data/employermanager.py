"""
    Employer Columns: [Name] *Starts on row 3
        D(4): Employer Name
"""

class EmployerManager:
    def __init__(self, sheet_manager):
        """
        Initializes the EmployerManager with a SheetManager instance.
        """
        self.sm = sheet_manager

    def _get_row_index(self, name):
        """Helper to find the row index of an employer in Column D (4)."""
        names = self.sm.get_column_values("DATA", 4)
        try:
            return names.index(name) + 1
        except ValueError:
            return None

    def add(self, name):
        """Adds an employer name starting at Row 3."""
        # Find next empty row in Column D
        current_names = self.sm.get_column_values("DATA", 4)
        next_row = len(current_names) + 1
        
        # Safety: Never overwrite headers on Row 1 or 2
        if next_row < 3:
            next_row = 3
            
        self.sm.update_range("DATA", f"D{next_row}:D{next_row}", [[name]])
        print(f"Added Employer: {name}")

    def delete(self, name):
        """Clears name from the row in Column D."""
        row = self._get_row_index(name)
        if row:
            # We clear D to keep the list layout
            self.sm.update_range("DATA", f"D{row}:D{row}", [[""]])
            print(f"Removed Employer: {name}")

    def get_names(self):
        """Returns employer names from Column D, skipping the TWO header rows."""
        names = self.sm.get_column_values("DATA", 4)
        # names[2:] skips Row 1 (Title) and Row 2 (Labels)
        names_list = [n for n in names[2:] if n]
        return names_list

    def get_all_employers_data(self):
        """
        Returns a list of dictionaries with employer data.
        Currently just returns names, matching the requirements of TimesheetManager.
        """
        names = self.get_names()
        return [{"name": name} for name in names]

    def _exists(self, name):
        """Checks if an employer name already exists in the list."""
        return name in self.get_names()