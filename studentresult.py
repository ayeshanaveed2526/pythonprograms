subject1 = int(input("Enter marks of subject 1:"))
subject2 = int(input("Enter marks of subject 2:"))
subject3 = int(input("Enter marks of subject 3:"))
totalmarks=[subject1, subject2, subject3]
average = sum(totalmarks)/3
print("The average marks is", average)
if average >= 80:
    print("Congratulations! You got Distinction")
elif average >= 60:
    print("Congratulations! You are pass")
elif average < 50:
    print("Oops! You are fail")