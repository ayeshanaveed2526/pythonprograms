password = "ayesha2004"
attempts = 0
while attempts < 3:
    usercheck = input("Enter your password: ")
    if usercheck == password:
        print("You have successfully logged in")
        break
    else:
        print(f"Wrong password. Attempts left: {2 - attempts}")
    attempts += 1
else:
    print("You have entered the wrong password 3 times. Please try again later.")