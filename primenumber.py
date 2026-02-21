userinput = int(input("Enter a number: "))
if userinput > 1:
    for i in range(2, userinput):
        if (userinput % i) == 0:
            print(f"{userinput} is not a prime number")
            break
    else:
        print(f"{userinput} is a prime number")