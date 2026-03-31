import gspread


def get_log_and_data_worksheets():
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open("MosherMade_Sheet")
    
    # Get or create LOG worksheet
    try:
        log_ws = sh.worksheet("LOG")
    except gspread.exceptions.WorksheetNotFound:
        log_ws = sh.add_worksheet(title="LOG", rows="100", cols="20")
        headers = ["Date", "Employee", "Employer", "Type", "Hours", "Amount", "Notes"]
        log_ws.append_row(headers)    
        print("Created new 'LOG' worksheet with headers.")
    
    # Get DATA worksheet
    data_ws = sh.worksheet("DATA")
    
    return data_ws, log_ws


def get_data_worksheet():
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open("MosherMade_Sheet")
    return sh.worksheet("DATA")


def get_log_worksheet():
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open("MosherMade_Sheet")

    try:
        return sh.worksheet("LOG")
    except gspread.exceptions.WorksheetNotFound:
        # If it's missing, create it and add the headers
        log_ws = sh.add_worksheet(title="LOG", rows="100", cols="20")

        # Define your standard headers for the ledger
        headers = ["Date", "Employee", "Employer", "Type", "Hours", "Amount", "Notes"]
        log_ws.append_row(headers)    
        print("Created new 'LOG' worksheet with headers.")
        return log_ws


def print_lists():
    try:
        data_sheet = get_data_worksheet()
        employer_list = data_sheet.get("Employers")
        employee_list = data_sheet.get("Employees")
        
        print("--- Current Data ---")
        print("Employers:", [name[0] for name in employer_list if name])
        print("Employees:", [name[0] for name in employee_list if name])
           
    except Exception as e:
        print(f"An error occurred: {e}")


# Utility to print all named ranges in the sheet for debugging
def get_all_named_ranges():
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open("MosherMade_Sheet")
    named_ranges = sh.fetch_sheet_metadata()['namedRanges']

    print("--- System Named Ranges ---")
    for r in named_ranges:
        print(f"Name: {r['name']}, Range: {r['range']}")



# Examples of how to call these:
if __name__ == "__main__":
    print_lists()

   
