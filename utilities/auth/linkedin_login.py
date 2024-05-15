"""
LinkedIn Login and Credentials Error Handling

Author: Abbas Mahdavi
Date: 05/14/24

Description:
This script contains functions for logging into LinkedIn using provided credentials and handling login-related errors using Selenium. It also includes a function to check for credential errors during the login process.

Functions:
- linkedin_login(driver, linkedin_credentials): Logs into LinkedIn using provided credentials.
    - Returns:
        - True if login is successful.
        - False if login fails or encounters errors.

- credentials_error(driver): Checks for credential-related errors during the LinkedIn login process.
    - Returns:
        - Error message if credential errors are detected.
        - False if no credential errors are found.

"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def linkedin_login(driver, linkedin_credentials):
    
    """
    This function handles the LinkedIn login process, including entering credentials,
    handling challenges, and verifying successful login.

    Parameters:
    - driver: Selenium WebDriver instance.
    - linkedin_credentials: Tuple containing (username, password).

    Returns:
    - True if login is successful.
    - False or Error string if login fails or encounters errors.
    """
    username, password = linkedin_credentials
    try:
        # Open LinkedIn login page
        driver.get("https://www.linkedin.com/login")

        time.sleep(2)

        # Check if already logged in and feed page is accessed
        curr_url = driver.current_url
        if curr_url == 'https://www.linkedin.com/feed/':
            return True

        # Wait for the username field to be visible
        try:
            username_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "username"))
            )
            password_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "password"))
            )

            # Clear fields (in case they are pre-filled)
            username_field.clear()
            password_field.clear()

            # Enter credentials
            username_field.send_keys(username)
            password_field.send_keys(password)

            # Find and click the sign-in button
            sign_in_button = driver.find_element(By.XPATH, "//button[contains(@class, 'from__button--floating')]")
            sign_in_button.click()

            time.sleep(2)

            try:
                # Check if the "challenge" element exists
                url = driver.current_url
                if "checkpoint" in url:
                    print("LinkedIn Challenge Verification Required!")
                    print("Please Complete Verification, Re-Checking in 30 seconds!")
                    time.sleep(2)
                    driver.maximize_window()  # Maximize the window for human verification

                # Wait until redirected to the feed page
                WebDriverWait(driver, 10).until(EC.url_contains("/feed"))

                driver.minimize_window()
                print("Verification Complete!")

            except TimeoutException:
                driver.minimize_window()
                res = credentials_error(driver)
                if res == False:
                    return False
                else:
                    return res

            res = credentials_error(driver)

            if res == False:
                print("No Credential Errors!")
            else:
                return res

            # Wait until redirected to the feed page (or any other desired page)
            WebDriverWait(driver, 10).until(
                EC.url_contains("/feed")
            )

            # Check if login was successful by waiting for the dashboard element
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "feed-identity-module"))
            )

            print("Logged Into LinkedIn via Credentials")
            return True

        except TimeoutException:
            return False

        except NoSuchElementException:
            return False

        except Exception:
            return False

    except Exception:
        print("That didn't work!")
        return False
    

def credentials_error(driver):
    """
    Checks for credential-related errors during the LinkedIn login process.

    Returns:
    - Error message if credential errors are detected.
    - False if no credential errors are found.
    """
    try:
        # Check for errors related to username and password
        error_username = driver.find_element(By.ID, "error-for-username")
        if error_username.is_displayed():
            return error_username.text
        error_password = driver.find_element(By.ID, "error-for-password")
        if error_password.is_displayed():
            return error_password.text
    except NoSuchElementException:
        return False
    
    return False
