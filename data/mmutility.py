import gspread
from datetime import datetime, timedelta


CREDS_FILE = "creds.json"
SPREADSHEET = "MosherMade_Sheet"

class MMSpreadUtility:
    def __init__(self):
        self.sh = None
        self.fetch_time = None
        self.fetch_sheet()
    
    
    def fetch_sheet(self):
        gc = gspread.service_account(filename=CREDS_FILE)
        self.sh = gc.open(SPREADSHEET)
        self.fetch_time = datetime.now()


    @property
    def needs_update(self):
        now = datetime.now()
        elapsed = now - self.fetch_time
        return elapsed > timedelta(minutes = 10)