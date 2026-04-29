from datetime import datetime

class ArrayList:
    def __init__(self, initialCapacity=2):
        self.MEMORY_SPACE = initialCapacity
        self.lastPosition = 0
        self.array = [None] * self.MEMORY_SPACE
        
    def capacity(self):
        return len(self.array)
    
    def size(self):
        return self.lastPosition 

    def resizeMemory(self):
        
        newArray = [None] * (self.capacity() * 2)
        for position in range(self.capacity()):
            newArray[position] = self.array[position]
        self.array = newArray

    def updateInsertArray(self, start, end):
        
        for index in range(start, end, -1):
            self.array[index] = self.array[index-1]
        self.lastPosition += 1

    def insertAt(self, value, position):
        if position < 0 or position > self.lastPosition:
            raise IndexError("Index out of bounds")
        if self.lastPosition == self.capacity():
            self.resizeMemory()
        
        self.updateInsertArray(self.lastPosition, position)
        self.array[position] = value

    def removeAt(self, position):
        if position < 0 or position >= self.lastPosition:
            raise IndexError("Index out of bounds")
        copy = self.array[position]
        for index in range(position, self.lastPosition - 1):
            self.array[index] = self.array[index + 1]
        self.lastPosition -= 1
        return copy

    def removeAll(self):
        self.lastPosition = 0

    def toList(self):
        return [self.array[i] for i in range(self.lastPosition)]

def addingSearch(historyObj):
    term = input("ENTER YOUR SEARCH: ").strip()

    if not term:
        print("Search is empty! No term added.")
        return

    if historyObj.size() > 0:
        first_item = historyObj.array[0]
        if first_item and first_item.lower().startswith(term.lower()):
            print("This term is already the most recent in history.")
            return

    timemark = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    termEntry = f"{term} - [Searched at {timemark}]"
    
    historyObj.insertAt(termEntry, 0)

    print(f"Search added!")
    print(f"DEBUG: Current size: {historyObj.size()} Real size: {historyObj.capacity()}")

def seeHistory(historyObj):
    if historyObj.size() == 0:
        print("History is empty.")
        return

    print(f"\nSEARCH HISTORY ({historyObj.size()})")
    for i in range(historyObj.size()):
        print(f"  {i+1}. {historyObj.array[i]}")

def cleanHistory(historyObj):
    confirm = input("\nClear history? (yes/no): ").strip().lower()
    if confirm == "yes":
        historyObj.removeAll()
        print("History cleared!")

def main():
    historySearch = ArrayList(2)

    while True:
        print("\n Menu")
        print("[1] New search")
        print("[2] View history")
        print("[3] Clear history")
        print("[0] Exit")
        option = input("Choose your option: ")

        match option:
            case "1":
                addingSearch(historySearch)
            case "2":
                seeHistory(historySearch)
            case "3":
                cleanHistory(historySearch)
            case "0":
                print("Exiting the system. See you later!")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()