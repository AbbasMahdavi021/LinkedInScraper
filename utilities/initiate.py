from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from .linkedin_login import linkedin_login
from .get_linkedin_credentials import get_linkedin_credentials

path_to_driver = './drivers/chromedriver.exe'

def initiate():

    service = Service(executable_path=path_to_driver)
    driver = webdriver.Chrome(service=service)
    driver.minimize_window()

    is_logged_in = False

    while True:
        linkedin_credentials = get_linkedin_credentials()
        if linkedin_credentials:
            is_logged_in = linkedin_login(driver, linkedin_credentials)
            if is_logged_in:
                print("Login successful. Now we can retrive more data!")
                break
            else:
                print("Couldn't log in. Retrying...")
        else:
            print("Failed to get LinkedIn credentials. Skipping login process.")
            break
    

    
