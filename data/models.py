from datetime import datetime

class Employee:
    def __init__(self, id=None, name="", wage=0):
        self.id = id
        self.name = name
        self.wage = wage


class Employer:
    def __init__(self, id=None, name="", location=""):
        self.id = id
        self.name = name
        self.location = location


class TimeLog:
    def __init__(self, id=None, employee_id=None, employer_id=None, 
                 job_type="General", notes="", start_time=None, end_time=None):
        self.id = id
        self.employee_id = employee_id
        self.employer_id = employer_id
        self.job_type = job_type
        self.notes = notes
        # Sets start_time to 'now' if no time is provided
        self.start_time = start_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = end_time


class MMData:
    def __init__(self):
        pass