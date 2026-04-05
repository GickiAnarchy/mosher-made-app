import json

class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.wage = kwargs.get("wage", "")


    def to_dict(self):
        return {
            "name":self.name,
            "wage":self.wage,
        }


    @classmethod
    def from_dict(cls, data):
        name = data.get("name", "")
        wage = data.get("wage", "")
        return cls(name, wage)