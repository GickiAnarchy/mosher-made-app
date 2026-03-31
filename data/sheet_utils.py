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
def manage_employee(action, name, wage=None, new_name=None):
    """
    action: 'ADD', 'EDIT_NAME', 'EDIT_WAGE', 'DELETE'
    """
    ws = get_data_worksheet()
    
    # Column A (1) is Names, Column B (2) is Wages
    names = ws.col_values(1)
    
    try:
        # Find which row the employee is on (1-based index)
        current_row = names.index(name) + 1
    except ValueError:
        current_row = None

    action = action.upper()

    if action == 'ADD':
        # Add Name to Col A and Wage to Col B
        next_row = len(names) + 1
        ws.update_cell(next_row, 1, name)
        ws.update_cell(next_row, 2, wage if wage else "$0.00")
        print(f"Added Employee {name} with wage {wage}")

    elif action == 'EDIT_NAME' and current_row:
        ws.update_cell(current_row, 1, new_name)
        print(f"Changed name from {name} to {new_name}")

    elif action == 'EDIT_WAGE' and current_row:
        ws.update_cell(current_row, 2, wage)
        print(f"Updated {name}'s wage to {wage}")

    elif action == 'DELETE' and current_row:
        # Clears both the Name and the Wage cell
        ws.update_cell(current_row, 1, "")
        ws.update_cell(current_row, 2, "")
        print(f"Removed {name} and their wage data.")


def get_employees():
    ws = get_data_worksheet()
    return [name[0] for name in ws.get("Employees") if name]


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
def manage_employer(action, name, location=None, new_name=None):
    """
    action: 'ADD', 'EDIT_NAME', 'EDIT_LOCATION', 'DELETE'
    """
    ws = get_data_worksheet()

    #Column F(5) is Employers, Column G(6) is Locations
    employers = ws.col_values(5)

    try:
        # Find row the employer is on
        current_row = employers.index(name) + 1
    except ValueError as e:
        current_row = None
        print(e)
    
    action = action.upper()
    
    if action == 'ADD':
        next_row = len(employers) + 1
        ws.update_cell(next_row,5,name)
        ws.update_cell(next_row,6,location if location else "")
        print(f"Added Employer {name} with location {location}")
    elif action == 'EDIT_NAME' and current_row:
        ws.update_cell(current_row,5,new_name)
        print(f"Changed name from {name} to {new_name}")
    elif action == 'EDIT_LOCATION' and current_row:
        ws.update_cell(current_row,6,location)
        print(f"Updated {name}'s location to {location}")
    elif action == 'DELETE' and current_row:
        ws.update_cell(current_row,5,"")
        ws.update_cell(current_row,6,"")
        print(f"Removed {name} and their location data")


def get_employers():
    ws = get_data_worksheet()
    return [name[0] for name in ws.get("Employers") if name]


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

   
