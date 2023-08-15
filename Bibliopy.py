import sys
import constants
from bibliography import bibliography
import pickle

def badUsageHandle() -> None:
    print(constants.BAD_USAGE)
    exit(-1)

def addEntry(url: str) -> bibliography:
    data = load_from_file()
    data.add_entry(url)
    return data

def load_from_file() -> bibliography:
    try:
        with open(constants.FILENAME, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return bibliography()

def save_to_file(data:bibliography) -> None:
    with open(constants.FILENAME, "wb") as file:
        pickle.dump(data, file)

def list_entries() -> None:
    data = load_from_file()
    print(data.pretty_print())

if __name__ == '__main__':
    argv = sys.argv

    if len(argv) < 2:
        badUsageHandle()
    if argv[1] == constants.ARGV_LIST_ENTRIES:
        list_entries()
    elif argv[1] == constants.ARGV_ADD_NEW_ENTRY:
        if len(argv) < 3:
            badUsageHandle()
        save_to_file(addEntry(argv[2]))
        list_entries()
