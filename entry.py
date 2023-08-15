from datetime import date
from functools import total_ordering

@total_ordering
class entry:
    def __init__(self, url:str, date:date) -> None:
        self.path = url
        self.date = date
        sliced_path = self.path.split(".")
        try:
            self.name = sliced_path[0] if sliced_path[0] != "www" else sliced_path[1]
            self.name = self.name.capitalize()
        except:
            self.name = None
            
    def pprint(self):
        return f"{self.name} \t {self.path} \t {self.date}"

    def __hash__(self):
        return hash(self.path)
    def __repr__(self) -> str:
        return f"{self.name}: {self.path}, {self.date}"
    def __str__(self) -> str:
        return f"{self.name}: {self.path}, {self.date}"
    def __gt__(self, other):
        return self.name > other.name if self.name != self.name else self.path > self.path
    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.path == __value.path