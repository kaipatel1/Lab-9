def encode(password):
    result = ""
    for i in password:
        result += str(int(i) + 3)
    return result


def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        selection = input("Please enter an option: ")
        if selection == "1":
            password = input("Please enter an option: ")
            print(encode(password))

if __name__ == "__main__":
    main()
