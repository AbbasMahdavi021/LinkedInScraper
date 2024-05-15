"""
LinkedIn Credentials Retrieval

Author: Abbas M.
Date: 05/13/24

Description:
This script contains a function to retrieve LinkedIn login credentials securely,
using stdiomask to hide the password input. It prompts the user to choose 
whether to log in to LinkedIn or skip the login process, providing options for 
handling the login or skip confirmation.

Returns:
- Tuple containing (username, password) if credentials are provided.
- None if the user chooses to skip login.

"""

from stdiomask import getpass

def get_linkedin_credentials():

    while True:
        choice = input("Would you like to log in to LinkedIn to access all available comments? (Y/N): ").strip().lower()
        if choice == 'n':
            print("Without logging in, only the first 10 comments per post will be retrieved.")
            confirm_skip = input("Are you sure you want to skip login? (Y/N): ").strip().lower()
            if confirm_skip == 'y':
                print("No problem, skipping login...")
                return None
            else:
                print("Great, let's retry.")
        elif choice == 'y':
            username = input("Enter your LinkedIn Login Email: ")
            password = getpass("Enter your password: ")
            if len(username) > 0 and len(password) > 0:
                print("Got it! Trying to log in...")
                return (username, password)
            else:
                print("Error: Please enter valid credentials.")
        else:
            print("Error: Invalid choice. Please enter 'Y' to enter credentials or 'N' to skip.")
