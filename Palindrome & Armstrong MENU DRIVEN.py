while True:
    print("Below are the available choices")
    print("1. Check for Palindrome")
    print("2. Check for Armstrong")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("YOU OPTED TO CHECK FOR PALINDROME")
        try:
            a = int(input("Enter the number: "))
            if str(a) == str(a)[::-1]:
                print(a, "is a palindrome number")
            else:
                print(a, "is not a palindrome number")
        except:
            print("Please enter a valid number type")

    elif ch == 2:
        print("YOU OPTED TO CHECK FOR ARMSTRONG")
        try:
            a = int(input("Enter the number: "))
            sum = 0
            temp = a
            while temp > 0:
                digit = temp % 10
                sum += digit ** len(str(a))
                temp //= 10
            if a == sum:
                print(a, "is an Armstrong number")
            else:
                print(a, "is not an Armstrong number")
        except:
            print("Please enter a valid number type")

    else:
        print("Invalid choice")

    more = input("IF YOU WANT TO CHECK MORE DATA'S [Yes(Y)/NO(N)]: ")
    if more.lower() in ["y", "yes"]:
        continue
    else:
        break
