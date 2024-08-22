#Functions with arguments
def goodDay(name, ending):
    print(f"Good Day, {name} , {ending}")

goodDay("Ashish", "Thank you!")

# Functions with default arguments values
def goodDay1(name, ending = "Thank you!"):
    print(f"Good Day, {name} , {ending}")

goodDay1("Ashish","Thanks")

# Function with a return value
def goodDay2(name, ending = "Thank you!"):
    print(f"Good Day, {name} , {ending}")
    return True

a = goodDay2("Ashish")
print(a)
