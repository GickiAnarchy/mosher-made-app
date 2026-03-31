import gspread
from datetime import datetime


gc = gspread.service_account(filename='creds.json')

# Connect using your credentials
gc = gspread.service_account(filename='service_account.json')
sh = gc.open("MosherMade_Sheet").sheet1

def clock_in(employer_name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Appends [Date, Employer Name] to the first empty row
    sh.append_row([now, employer_name])
    print(f"Clocked in for {employer_name} at {now}")
