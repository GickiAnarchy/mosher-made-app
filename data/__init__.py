from .models import Employer, Employee
from .sheet_utils import get_employees, get_employee, get_employers, get_employer, manage_employee, manage_employer, check_employee_exists, check_employer_exists, print_lists



MANAGEMENT_FUNCTIONS = [
    "sheet_utils.get_employees",
    "sheet_utils.get_employee",
    "sheet_utils.get_employers",
    "sheet_utils.get_employer",
    "sheet_utils.manage_employee",
    "sheet_utils.manage_employer",
    "sheet_utils.check_employee_exists",
    "sheet_utils.check_employer_exists",
]



__all__ = [
    "Employer",
    "Employee",
    "get_employees",
    "get_employee",
    "get_employers",
    "get_employer",
    "manage_employee",
    "manage_employer",
    "check_employee_exists",
    "check_employer_exists"
    "print_lists",
    ]