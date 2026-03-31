import sqlite3
from datetime import datetime

class DataManager:
     def __init__(self, db_name="data/mosher_work.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()


    def create_tables(self):
        cursor = self.conn.cursor()
        # Employee Table
        cursor.execute('''CREATE TABLE IF NOT EXISTS employees 
                          (id INTEGER PRIMARY KEY, name TEXT, wage REAL)''')
        # Employer/Location Table
        cursor.execute('''CREATE TABLE IF NOT EXISTS employers 
                          (id INTEGER PRIMARY KEY, name TEXT, location TEXT)''')
        # Updated Time Logs Table with 'job_type' and 'notes'
        cursor.execute('''CREATE TABLE IF NOT EXISTS timelogs 
                          (id INTEGER PRIMARY KEY, 
                           employee_id INTEGER, 
                           employer_id INTEGER, 
                           job_type TEXT,
                           notes TEXT,
                           start_time TEXT, 
                           end_time TEXT,
                           FOREIGN KEY(employee_id) REFERENCES employees(id),
                           FOREIGN KEY(employer_id) REFERENCES employers(id))''')
        self.conn.commit()


    def clock_in(self, employee_id, employer_id, job_type="General", notes=""):
        """Starts a log with specific job details."""
        cursor = self.conn.cursor()
        start_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''INSERT INTO timelogs 
                          (employee_id, employer_id, job_type, notes, start_time) 
                          VALUES (?, ?, ?, ?, ?)''',
                       (employee_id, employer_id, job_type, notes, start_now))
        self.conn.commit()


    def clock_out_or_switch(self, employee_id, new_employer_id=None, new_job_type="General", new_notes=""):
        """Closes current task. If switching, opens the next one with new details."""
        cursor = self.conn.cursor()
        end_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''UPDATE timelogs SET end_time = ? 
                          WHERE employee_id = ? AND end_time IS NULL''', 
                       (end_now, employee_id))
        
        if new_employer_id:
            self.clock_in(employee_id, new_employer_id, new_job_type, new_notes)
            
        self.conn.commit()

    def get_active_workers(self):
        """Returns a list of employees currently on a clock."""
        cursor = self.conn.cursor()
        cursor.execute('''SELECT employees.name, employers.name, timelogs.start_time 
                          FROM timelogs 
                          JOIN employees ON timelogs.employee_id = employees.id
                          JOIN employers ON timelogs.employer_id = employers.id
                          WHERE timelogs.end_time IS NULL''')
        return cursor.fetchall()

    def get_employee_logs(self, employee_id):
        """Returns all logs for a specific employee."""
        cursor = self.conn.cursor()
        cursor.execute('''SELECT employers.name, timelogs.job_type, timelogs.notes, 
                          timelogs.start_time, timelogs.end_time 
                          FROM timelogs 
                          JOIN employers ON timelogs.employer_id = employers.id
                          WHERE timelogs.employee_id = ?''', 
                       (employee_id,))
        return cursor.fetchall()

    import sqlite3


    def get_job_report(self, employer_id):
        """Calculates total site hours and breaks down work by employee."""
        cursor = self.conn.cursor()

        # 1. Fetch Site Info
        cursor.execute("SELECT name, location FROM employers WHERE id = ?", (employer_id,))
        site = cursor.fetchone()
        if not site:
            return {"error": "Site not found"}

        # 2. Fetch all completed logs for this site
        query = """
            SELECT 
                employees.name, 
                timelogs.job_type,
                timelogs.notes,
                timelogs.start_time,
                (strftime('%s', end_time) - strftime('%s', start_time)) / 3600.0 as hours
            FROM timelogs
            JOIN employees ON timelogs.employee_id = employees.id
            WHERE timelogs.employer_id = ? AND timelogs.end_time IS NOT NULL
            ORDER BY timelogs.start_time ASC
        """
        cursor.execute(query, (employer_id,))
        rows = cursor.fetchall()

        # 3. Structure the Data
        total_hours = 0
        breakdown = {}

        for name, job, notes, start, hours in rows:
            total_hours += hours
            if name not in breakdown:
                breakdown[name] = []
            
            breakdown[name].append({
                "date": start.split(" ")[0],
                "job": job,
                "hours": round(hours, 2),
                "notes": notes
            })

        return {
            "site_name": site[0],
            "location": site[1],
            "total_company_hours": round(total_hours, 2),
            "employee_data": breakdown
        }


    def get_all_employers(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name FROM employers")
        return cursor.fetchall()