#Pierce Berardi
#Lab_09

def displayMenu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

def encode_password(password):

    new_password = ""
    for i in password:
        n = (int(i)+ 3) % 10
        new_password += str(n)
    return new_password
def decode_password(new_password):
    pass


def main():
    while True:
        displayMenu()
        choice = int(input("Please enter an option: "))
        encoded_password = ''
        if choice == 1:
            og_password = str(input("Please enter your password to encode: "))
            new_password = encode_password(og_password)


            print("Your password has been encoded and stored!")
        elif choice == 2:
            print(f"The encoded password is {new_password}, and the original is {decode_password(new_password)}")

        elif choice == 3:
            break


if __name__ == "__main__":
    main()