


class Employee:
    def __init__(self, name, wage=None, **kwargs):
        self.name = name
        self.wage = wage
        try:
            self.pay_advances = kwargs.get("pay_advances", [])
        except KeyError:
            self.pay_advances = []
    





class Employer:
    def __init__(self, name, location=None):
        self.name = name
        self.location = location




