from datetime import date
from entry import entry

class bibliography:
    def __init__(self) -> None:
        self.items = set()

    def add_entry(self, url:str, date:date = date.today()) -> None:
        e = entry(url, date)
        if e in self.items:
            self.items.remove(e)
        self.items.add(e)

    def __str__(self) -> str:
        return(str(self.items))
    
    def pretty_print(self) -> str:
        for elem in sorted(self.items):
            print(elem.pretty_print())