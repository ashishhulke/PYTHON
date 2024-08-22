# 6. Write a python function which converts inches to cms. 

def inches_to_cm(inches):
    centimeters = inches * 2.54
    return centimeters


inches_value = float(input("Enter measurement in inches: "))
cm_value = inches_to_cm(inches_value)
print(f"{inches_value} inches is equal to {cm_value} cm.")