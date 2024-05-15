"""
LinkedIn Login Initialization

Author: Abbas Mahdavi
Date: 05/14/24

Description:
This script contains functions for initializing the LinkedIn login process. 
It provides the ability to authenticate a user's LinkedIn account using provided credentials or 
proceed without authentication if credentials are not available.

Usage:
1. Ensure the required modules are installed.
2. Use the 'initiate' function to start the LinkedIn login process.
3. The function prompts for LinkedIn credentials if available.
4. It handles login errors and allows skipping login after multiple failed attempts.

Returns:
    - True if login is successful.
    - False if login is skipped or unsuccessful.

"""

from .auth.linkedin_login import linkedin_login
from .auth.get_linkedin_credentials import get_linkedin_credentials


def initiate(driver):
    #return tuple username,password, or None if skipped login
    linkedin_credentials = get_linkedin_credentials()
    error_count = 0

    while True:

        #if 3 errors occur, give option of login skip
        if error_count > 3:
            skip_login = input("Few Attempts Failed! Skip login (Y/N)? ").strip().lower()
            if skip_login == 'y':
                print("Skipping login.")
                return False
            else:
                error_count = 0
                print("Continuing login attempt...")

        #attempt login with credentials
        if linkedin_credentials:

            #tries to login to linkedin
            #return True, False, or credentials error string
            is_logged_in = linkedin_login(driver, linkedin_credentials)

            if isinstance(is_logged_in, str):
                error_count += 1
                print(is_logged_in)
                linkedin_credentials = get_linkedin_credentials()
            elif is_logged_in:
                print("Login successful. Now we can retrieve more data!")
                return True
            else:
                print("Couldn't log in. Retrying...")
                error_count += 1
        else:
            print("Proceeding without LinkedIn credentials.")
            return False
