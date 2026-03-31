import datetime
from data import EmployeeManager, EmployerManager, TimesheetManager, get_log_and_data_worksheets, print_lists


print_lists()

# 1. Setup Worksheets
data_ws, log_ws = get_log_and_data_worksheets()

# 2. Initialize Managers
emp_manager = EmployeeManager(data_ws)
job_manager = EmployerManager(data_ws)
ts_manager = TimesheetManager(log_ws, emp_manager, job_manager)

date = datetime.datetime.now().strftime("%m-%d-%Y")

# 3. Use the app
# Let's say Mark worked 8 hours for 'The Anthony House'
ts_manager.log_work(date, "Mark", "The Anthony House", 8)
    
ts_manager.log_work(date, "Corey", "Barbara Howell", 8)
ts_manager.log_work(date, "Corey", "Barbara Howell", 8)
ts_manager.log_work(date, "Corey", "Joe", 6)
ts_manager.log_advance(date, "Corey", 100, "Partial advance for week of 10/1")

# Let's say Mark took a $50 advance
ts_manager.log_advance(date, "Mark", 50)

# 4. See what he's owed
status_mark = ts_manager.get_summary("Mark")
print(f"Mark's Net Owed: ${status_mark.get('net_owed', 0)}")

status_corey = ts_manager.get_summary("Corey")

for k,v in status_corey.items():
    print(f"Corey's {k}: {v}")
