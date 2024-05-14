from .linkedin_login import linkedin_login
from .get_linkedin_credentials import get_linkedin_credentials

def initiate(driver):


    while True:
        linkedin_credentials = get_linkedin_credentials()
        if linkedin_credentials:
            is_logged_in = linkedin_login(driver, linkedin_credentials)
            if is_logged_in:
                print("Login successful. Now we can retrive more data!")
                return True
            else:
                print("Couldn't log in. Retrying...")
        else:
            print("Proceeding without LinkedIn credentials.")
            return False