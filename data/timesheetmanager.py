import datetime
from employeemanager import EmployeeManager
from employermanager import EmployerManager 

class TimesheetManager:
    def __init__(self, sheet_manager):
        """
        Initializes the TimesheetManager with a SheetManager instance.
        """
        self.sm = sheet_manager
        self.employee_manager = EmployeeManager(sheet_manager)
        self.employer_manager = EmployerManager(sheet_manager)


    """
    LOG worksheet columns: [Date, Employee, Employer, Type, Hours, Amount, Notes]
    Type can be "WORK" or "ADVANCE"
    Note: It would be cleaner to pass the date with each log method, but for simplicity we can default to current date if not provided.
    """

    # Logging methods

    def log_work(self, date, employee_name, employer_name, hours, note = ""):
        """Logs hours worked and calculates pay based on stored wage."""
        employee_data = self.employee_manager.get(employee_name)
        if not employee_data:
            print(f"Error: {employee_name} not found in system.")
            return

        # Clean wage string (e.g., "$20.00" -> 20.0)
        wage = float(employee_data['wage'].replace('$', '').replace(',', ''))
        amount = hours * wage
        if date is None:
            date = datetime.datetime.now().strftime("%m-%d-%Y")

        # Append: [Date, Employee, Employer, Type, Hours, Amount, Notes]
        self.sm.append_row("LOG", [date, employee_name, employer_name, "WORK", hours, amount, note])
        print(f"Logged ${amount} for {employee_name} at {employer_name}")


    def log_advance(self, date, employee_name, amount, note="Cash Advance"):
        """Logs a pay advance (deduction)."""
        if date is None:
            date = datetime.datetime.now().strftime("%m-%d-%Y")

        self.sm.append_row("LOG", [date, employee_name, "N/A", "ADVANCE", "", amount, note])
        print(f"Logged advance of ${amount} for {employee_name}")


    def get_summary(self, employee_name):
        if employee_name not in self.employee_manager.get_names():
            print(f"Error: {employee_name} not found in system.")
            return {}
        
        """Calculates total earned, total advances, and net owed."""
        all_records = self.sm.get_all_records("LOG")
        
        earned = 0
        advances = 0
        hours = 0
        
        for row in all_records:
            if row['Employee'] == employee_name:
                val = float(str(row['Amount']).replace('$', '').replace(',', ''))
                if row['Type'] == 'WORK':
                    earned += val
                    hours += float(str(row['Hours']).replace('$', '').replace(',', '')) if row['Hours'] else 0
                elif row['Type'] == 'ADVANCE':
                    advances += val

        return {
            "total_hours": hours,
            "total_earned": earned,
            "total_advances": advances,
            "net_owed": earned - advances
        }


    # Deletion methods - by row, by date, by employee, by job

    def _delete_by_filter(self, column_index, value):
        """
        Internal helper to delete rows where a specific column matches a value.
        Deletes in reverse to maintain index integrity.
        """
        # Get all values in that specific column
        col_values = self.sm.get_column_values("LOG", column_index)
        
        # Find all row indices that match (1-based)
        # We skip row 1 (header)
        rows_to_delete = [i + 1 for i, val in enumerate(col_values) if val == str(value) and i > 0]
        
        if not rows_to_delete:
            print(f"No logs found for '{value}'.")
            return

        # Delete in REVERSE order
        for row in reversed(rows_to_delete):
            self.sm.delete_rows("LOG", row)
            
        print(f"Deleted {len(rows_to_delete)} rows matching '{value}'.")


    def delete_by_row(self, row_index):
        """Deletes a single specific row and shifts others up."""
        # Note: gspread row indices are 1-based.
        self.sm.delete_rows("LOG", row_index)
        print(f"Row {row_index} deleted.")


    def delete_by_date(self, date_string):
        """Deletes all logs from a particular date (e.g., '03-31-2026')"""
        # Date is Column 1
        self._delete_by_filter(1, date_string)


    def delete_by_employee(self, employee_name):
        """Deletes all logs for a particular employee"""
        # Employee is Column 2
        self._delete_by_filter(2, employee_name)


    def delete_by_job(self, employer_name):
        """Deletes all logs for a particular job/employer"""
        # Employer is Column 3
        self._delete_by_filter(3, employer_name)


    def clear_all_logs(self):
        """Wipes the entire sheet except for the header row safely."""
        row_count = self.sm.get_row_count("LOG")
        
        # We only delete if there are more than 1 row total.
        # This prevents the 'delete all non-frozen rows' API error.
        if row_count > 1:
            try:
                # Delete starting from row 2 to the very last row
                self.sm.delete_rows("LOG", 2, row_count)
                print("All log entries have been cleared.")
            except Exception as e:
                # If it's a size error, we can just clear the cell values instead
                # of deleting the actual physical rows.
                self.sm.batch_clear("LOG", ["A2:Z"])
                print("Logs cleared via cell wipe.")
        else:
            print("Sheet is already empty.")


    def get_employees(self):
        return self.employee_manager.get_names()


    def get_employers(self):
        return self.employer_manager.get_names()


    def get_employers_data(self):
        return self.employer_manager.get_all_employers_data()