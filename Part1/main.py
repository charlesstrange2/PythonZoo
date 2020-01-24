class FelineTerror(object):
    # See that this `inherits` from the base `object` class python provides
    # Technically it isn't necessary to specify.

    # All FelineTerrors and descendents have 4 legs ...
    legs = 4
    # ... and have some kind of fur
    fur = "short"


class HouseCat(FelineTerror):
    # See that this `inherits` all the properties and methods of the FelineTerror

    # __init__ is magical, called by python when we make a new instance of this class
    # note the use if `self` - python expects objects to reference themselves in method definitions.
    # note that we add a parameter of fur, and we set a default of "black" - this makes it "optional"

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

# we can call methods on the tiger
tiger.startle()
tiger.anger()

otherTiger = Tiger()
otherTiger.startle()
otherTiger.anger()

# we can get properties on the tiger
print(tiger.fur + " fur")

# we can set properties on the tiger
tiger.fur = "white"
print(tiger.fur + " fur")

# which wont affect other tigers.
print(otherTiger.fur + " fur")

# or we can just make a white tiger to start with
whiteTiger = Tiger("white")
print(whiteTiger.fur + " fur")

# which is different from our standard tiger (no parameter)
standardIssueIndianTiger = Tiger()
print(standardIssueIndianTiger.fur + " fur")

# cats are Felines too!
blackCat = HouseCat()
tortyCat = HouseCat("tortoiseShell")

# print can "join" text automatically when it's passed like this.
print(tortyCat.fur, blackCat.fur)
