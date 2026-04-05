import json


class Employer:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name","")
        self.location = kwargs.get("location","")


    def to_dict(self):
        return {
            "name":self.name,
            "location":self.location,
        }


    @classmethod
    def from_dict(cls, data):
        name = data.get("name", "")
        location = data.get("location", "")
        return cls(name = name, location = location)