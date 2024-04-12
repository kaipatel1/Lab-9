#Kai Patel
def encode(password):
    result = ""
    for i in password:
        result += str(int(i) + 3)
    return result


def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        selection = input("Please enter an option: ")
        e = 1
        if selection == "1":
            password = encode(input("Please enter an option: "))
            print("Your password has been encoded and stored!")
        elif selection == "2":
            pass
        elif selection == "3":
            break

if __name__ == "__main__":
    main()
