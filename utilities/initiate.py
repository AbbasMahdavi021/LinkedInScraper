from .auth.linkedin_login import linkedin_login
from .auth.get_linkedin_credentials import get_linkedin_credentials

def initiate(driver):

    linkedin_credentials = get_linkedin_credentials()

    error_count = 0

    while True:

        if error_count > 3:
            skip_login = input("There is an issue logging in right now! Skip login (Y/N)? ").strip().lower()
            if skip_login == 'y':
                print("Skipping login.")
                return False
            else:
                error_count = 0
                print("Continuing login attempt...")

        if linkedin_credentials:
            is_logged_in = linkedin_login(driver, linkedin_credentials)

            if isinstance(is_logged_in, str):
                error_count += 1
                print(is_logged_in)
                linkedin_credentials = get_linkedin_credentials()
            elif is_logged_in:
                print("Login successful. Now we can retrive more data!")
                return True
            else:
                print("Couldn't log in. Retrying...")
                error_count += 1
        else:
            print("Proceeding without LinkedIn credentials.")
            return False
            