import gspread

def get_data_worksheet():
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open("MosherMade_Sheet")
    return sh.worksheet("DATA")


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



# Employee Management Functions
def check_employee_exists(name):
    ws = get_data_worksheet()
    employees = ws.col_values(1)
    return name in employees


def get_employee(name):
    ws = get_data_worksheet()
    employees = ws.col_values(1)
    
    try:
        row_index = employees.index(name) + 1
        wage = ws.cell(row_index, 2).value
        return {"name": name, "wage": wage}
    except ValueError:
        print(f"Employee {name} not found.")
        return None




# Employer Management Functions
def check_employer_exists(name):
    ws = get_data_worksheet()
    employers = ws.col_values(5)
    return name in employers


def get_employer(name):
    ws = get_data_worksheet()
    employers = ws.col_values(5)
    
    try:
        row_index = employers.index(name) + 1
        location = ws.cell(row_index, 6).value
        return {"name": name, "location": location}
    except ValueError:
        print(f"Employer {name} not found.")
        return None



# Test function to print named ranges in the sheet
def test_named_ranges():
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open("MosherMade_Sheet")
    named_ranges = sh.fetch_sheet_metadata()['namedRanges']

    print("--- System Named Ranges ---")
    for r in named_ranges:
        print(f"Name: {r['name']}, Range: {r['range']}")



# Examples of how to call these:
if __name__ == "__main__":
    manage_employee('ADD', 'Dr.Test', "$45.00")
    manage_employer('ADD', 'New Job')
    print_lists()
    manage_employee('DELETE', 'Dr.Test')
    manage_employer('DELETE', 'New Job')

    print_lists()

   
