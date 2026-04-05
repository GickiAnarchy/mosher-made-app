import gspread


class SheetManager:
    """
    Centralized manager for Google Sheets API communication.
    Acts as the single source of truth for spreadsheet data.
    """
    def __init__(self, credentials_path='creds.json', spreadsheet_name="MosherMade_Sheet"):
        self.gc = gspread.service_account(filename=credentials_path)
        self.sh = self.gc.open(spreadsheet_name)
        self._worksheets = {}
        self._initialize_sheets()

    def _initialize_sheets(self):
        """Initializes DATA and LOG worksheets and applies freezing/header logic."""
        # DATA Worksheet setup
        data_ws = self.sh.worksheet("DATA")
        data_ws.freeze(rows=2)
        self._worksheets["DATA"] = data_ws
        print("DATA worksheet ready (frozen 2 rows).")

        # LOG Worksheet setup (with auto-creation if missing)
        try:
            log_ws = self.sh.worksheet("LOG")
        except gspread.exceptions.WorksheetNotFound:
            log_ws = self.sh.add_worksheet(title="LOG", rows="100", cols="20")
            headers = ["Date", "Employee", "Employer", "Type", "Hours", "Amount", "Notes"]
            log_ws.append_row(headers)    
            print("Created new 'LOG' worksheet with headers.")
        
        log_ws.freeze(rows=1)
        self._worksheets["LOG"] = log_ws
        print("LOG worksheet ready (frozen 1 row).")

    def _get_ws(self, ws_name):
        """Internal helper to retrieve worksheet object by name, using cache."""
        if ws_name not in self._worksheets:
            self._worksheets[ws_name] = self.sh.worksheet(ws_name)
        return self._worksheets[ws_name]

    # --- API Abstraction Layer ---

    def get_column_values(self, ws_name, column_index):
        """Gets all values from a specific column (1-indexed)."""
        return self._get_ws(ws_name).col_values(column_index)

    def get_values(self, ws_name, cell_range):
        """Gets values from a specific range or named range (e.g., 'A1:B2' or 'Employers')."""
        return self._get_ws(ws_name).get(cell_range)

    def get_cell_value(self, ws_name, row, col):
        """Gets the value of a single cell."""
        return self._get_ws(ws_name).cell(row, col).value

    def get_all_records(self, ws_name):
        """Gets all rows as a list of dictionaries using the header row."""
        return self._get_ws(ws_name).get_all_records()

    def update_range(self, ws_name, cell_range, values):
        """Updates a range with provided data (list of lists)."""
        return self._get_ws(ws_name).update(cell_range, values)

    def append_row(self, ws_name, values):
        """Appends a single row of data."""
        return self._get_ws(ws_name).append_row(values)

    def delete_rows(self, ws_name, start_index, end_index=None):
        """Deletes rows starting from the given index."""
        self._get_ws(ws_name).delete_rows(start_index, end_index)

    def batch_clear(self, ws_name, ranges):
        """Clears content in the specified cell ranges (e.g., ['A2:Z'])."""
        self._get_ws(ws_name).batch_clear(ranges)

    def get_row_count(self, ws_name):
        """Returns total physical rows in the sheet."""
        return self._get_ws(ws_name).row_count

    # --- Utility & Debug Methods ---

    def get_all_named_ranges(self):
        """Utility to print and return all named ranges in the sheet for debugging."""
        named_ranges = self.sh.fetch_sheet_metadata().get('namedRanges', [])
        print("--- System Named Ranges ---")
        for r in named_ranges:
            print(f"Name: {r['name']}, Range: {r['range']}")
        return named_ranges

    def print_lists(self):
        """Prints current employer and employee lists from the DATA sheet."""
        try:
            employer_list = self.get_values("DATA", "Employers")
            employee_list = self.get_values("DATA", "Employees")
            
            print("--- Current Data ---")
            print("Employers:", [name[0] for name in employer_list if name])
            print("Employees:", [name[0] for name in employee_list if name])
        except Exception as e:
            print(f"An error occurred: {e}")

    # --- Properties for Backward Compatibility ---

    @property
    def data_ws(self):
        """Direct access to DATA worksheet."""
        return self._get_ws("DATA")

    @property
    def log_ws(self):
        """Direct access to LOG worksheet."""
        return self._get_ws("LOG")


if __name__ == "__main__":
    manager = SheetManager()
    manager.print_lists()


   
