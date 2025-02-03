class String():
    def __init__(self):
        self.text = ""
    
    def getString(self):
        self.text = input("Write a string:")

    def printString(self):
        print(self.text.upper())

s = String()
s.getString()
s.printString()