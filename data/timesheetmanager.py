import datetime

class TimesheetManager:
    def __init__(self, log_worksheet, employee_manager, employer_mananger):
        self.ws = log_worksheet
        self.employee_manager = employee_manager
        self.employer_manager = employer_mananger


    """
    LOG worksheet columns: [Date, Employee, Employer, Type, Hours, Amount, Notes]
    Type can be "WORK" or "ADVANCE"
    """

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
        self.ws.append_row([date, employee_name, employer_name, "WORK", hours, amount, note])
        print(f"Logged ${amount} for {employee_name} at {employer_name}")


    def log_advance(self, date, employee_name, amount, note="Cash Advance"):
        """Logs a pay advance (deduction)."""
        if date is None:
            date = datetime.datetime.now().strftime("%m-%d-%Y")

        self.ws.append_row([date, employee_name, "N/A", "ADVANCE", "", amount, note])
        print(f"Logged advance of ${amount} for {employee_name}")


    def get_summary(self, employee_name):
        if employee_name not in self.employee_manager.get_names():
            print(f"Error: {employee_name} not found in system.")
            return {}
        
        """Calculates total earned, total advances, and net owed."""
        all_records = self.ws.get_all_records()
        
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