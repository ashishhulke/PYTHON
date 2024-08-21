# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

subject1 = float(input("Enter marks for subjects 1: "))
subject2 = float(input("Enter marks for subjects 2: "))
subject3 = float(input("Enter marks for subjects 3: "))

Total_marks = subject1 + subject2 + subject3
percentage = (Total_marks / 300)*100

if(subject1 >= 33 and subject2 >= 33 and subject3 >= 33 and percentage >= 40):
    print("The student has passed.")

else:
    print("The student has failed.")

print(f"Your marks are {subject1}\t{subject2}\t{subject3}\nyour percentage is {percentage}")        