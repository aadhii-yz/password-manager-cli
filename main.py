def welcome():
    print(" _______________________________")
    print("|       PASSWORD MANAGER        |")
    print("|===============================|")
    print("|Options:                       |")
    print("| Init  - initialize a database |")
    print("| Login - login to a database   |")
    print("| Exit  - exit password manager |")
    print("| Help  - to see this message   |")
    print("|_______________________________|")

def initDB():
    pass

def login():
    pass

def main():
    welcome()
    option = input("password-manager -> ").lower()
    while option != 'exit':
        match option:
            case 'init':
                print('initializing')
            case 'login':
                print('logging in')
            case 'help':
                print('Help :')
                welcome()
            case _:
                print("Invalid option. 'Help' for help")
        option = input("password-manager -> ").lower()
        

if __name__ == '__main__':
    main()