class FelineTerror(object):
    legs = 4
    fur = "short"


class HouseCat(FelineTerror):
    def __init__(self, fur="black"):
        self.fur = fur

    def anger(self):
        print("Hiss!")

    def startle(self):
        print("Meow!")


class Tiger(FelineTerror):
    def __init__(self, fur="orange"):
        self.fur = fur

    def anger(self):
        print("Roar!")

    def startle(self):
        print("Snarl!")


tiger = Tiger()
tiger.startle()
tiger.anger()

otherTiger = Tiger()
otherTiger.startle()
otherTiger.anger()

print(tiger.fur + " fur")
tiger.fur = "white"
print(tiger.fur + " fur")
print(otherTiger.fur + " fur")

whiteTiger = Tiger("white")
print(whiteTiger.fur + " fur")

standardIssueIndianTiger = Tiger()
print(standardIssueIndianTiger.fur + " fur")

blackCat = HouseCat()
tortyCat = HouseCat("tortoiseShell")

print(tortyCat.fur, blackCat.fur)
