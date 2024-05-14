import getpass

def get_linkedin_credentials():
    while True:
        choice = input("Would you like to enter your LinkedIn credentials? (Y/N): ").strip().lower()
        if choice == 'n':
            print("Without logging in, only the first 10 comments per post will be retrieved.")
            confirm_skip = input("Are you sure you want to skip login? (Y/N): ").strip().lower()
            if confirm_skip == 'y':
                print("Skipping login.")
                return None
            else:
                print("Let's retry.")
        elif choice == 'y':
            username = input("Enter your LinkedIn Email/Login: ")
            password = getpass.getpass("Enter your password: ")
            if len(username) > 0 and len(password) > 0:
                print("Credentials entered.")
                return (username, password)
            else:
                print("Error: Please enter valid credentials.")
        else:
            print("Error: Invalid choice. Please enter 'Y' to enter credentials or 'N' to skip.")

