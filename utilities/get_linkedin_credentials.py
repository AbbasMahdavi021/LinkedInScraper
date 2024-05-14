import getpass


path = '../drivers/chromedriver.exe'


def get_linkedin_credentials():

    # Prompt for credentials
    while True:
        choice = input("Would you like to enter your LinkedIn credentials? (Y/N): ").strip().lower()
        if choice == 'n':
            print("Skipping login.")
            return None  # Skip login
        elif choice == 'y':
            username = input("Enter your LinkedIn Email/Login: ")
            password = getpass.getpass("Enter your password: ")
            # Validate credentials (optional)
            if len(username) > 0 and len(password) > 0:
                print("Credentials entered.")
                return (username, password)
            else:
                print("Error: Please enter valid credentials.")
        else:
            print("Error: Invalid choice. Please enter 'Y' to enter credentials or 'N' to skip.")