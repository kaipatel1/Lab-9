#Kai Patel

def encode(password):
    result = ""
    for i in password:
        result += str(int(i) + 3)
    return result

def decode(password):
    result = ""
    for j in password:
        result += str(int(j) - 3)
    return result

def main():
    password = ""
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        selection = input("Please enter an option: ")
        e = 1
        if selection == "1":
            password = encode(input("Please enter an option: "))
            print("Your password has been encoded and stored!")
        elif selection == "2":
            result = decode(password)
            print(f"The encoded password is {password}, and the original password is {result}.")
        elif selection == "3":
            break

if __name__ == "__main__":
    main()
