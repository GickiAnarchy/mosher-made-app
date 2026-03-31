import datetime

import sys
import os

# 1. Add the parent directory (data) to the path so Python can see your modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 2. Now you can import your classes and utilities
from employeemanager import EmployeeManager
from employermanager import EmployerManager
from timesheetmanager import TimesheetManager
from sheet_utils import get_log_and_data_worksheets, print_lists



print_lists()

def get_timesheet_manager():
    # 1. Setup Worksheets
    data_ws, log_ws = get_log_and_data_worksheets()
    # 2. Initialize Managers
    emp_manager = EmployeeManager(data_ws)
    job_manager = EmployerManager(data_ws)
    ts_manager = TimesheetManager(log_ws, emp_manager, job_manager)
    return ts_manager


def test_time_manager():
    ts_manager = get_timesheet_manager()
    date = datetime.datetime.now().strftime("%m-%d-%Y")

    # 3. Use the app
    # Let's say Mark worked 8 hours for 'The Anthony House'
    ts_manager.log_work(date, "Mark", "The Anthony House", 8)
        
    ts_manager.log_work(date, "Corey", "Barbara Howell", 8)
    ts_manager.log_work(date, "Corey", "Barbara Howell", 8)
    ts_manager.log_work(date, "Corey", "Joe", 6)
    ts_manager.log_advance(date, "Corey", 100, "Partial advance for week of 10/1")

    ts_manager.log_advance(date, "Chad", 45, "Advance for food.")

    # Let's say Mark took a $50 advance
    ts_manager.log_advance(date, "Mark", 50)

    # 4. See what he's owed
    status_mark = ts_manager.get_summary("Mark")
    print(f"Mark's Net Owed: ${status_mark.get('net_owed', 0)}")
    print("\n")
    status_corey = ts_manager.get_summary("Corey")
    for k,v in status_corey.items():
        print(f"Corey's {k}: {v}")
    print("\n")
    status_chad = ts_manager.get_summary("Chad")
    for k,v in status_chad.items():
        print(f"Chad's {k}: {v}")



def clear_logs():
    ts_manager = get_timesheet_manager()
    ts_manager.clear_all_logs()




if __name__ == "__main__":
    # test timesheet manager functionality
    test_time_manager()

    # clear logs after testing
    clear_logs()