import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def linkedin_login(driver, linkedin_credentials):
    """
    Logs into LinkedIn using provided credentials.

    Parameters:
    - driver: Selenium WebDriver instance.
    - linkedin_credentials: Tuple containing (username, password).

    Returns:
    - bool: True if login is successful, False otherwise.
    """
    username, password = linkedin_credentials

    error = ''

    try:
        # Open LinkedIn login page
        driver.get("https://www.linkedin.com/login")

        time.sleep(2)

        #if already logged in and feedpage is accessed
        curr_url = driver.current_url
        if curr_url == 'https://www.linkedin.com/feed/':
            return True

        # Wait for the username field to be visible
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        password_field = driver.find_element(By.ID, "password")

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

        # Check for errors related to username and password
        try:

            # Check if the "challenge" element exists
            time.sleep(3)
            url = driver.current_url
            if "checkpoint" in url:
                error = "LinkedIn Challenge Verification Needed!"
                driver.maximize_window()  # Maximize the window for human verification
            error_username = driver.find_element(By.ID, "error-for-username")
            if error_username.is_displayed():
                error = error_username.text

            error_password = driver.find_element(By.ID, "error-for-password")
            if error_password.is_displayed():
                error = error_password.text

        except NoSuchElementException:
            pass  # No error message for username

        # Wait until redirected to the feed page (or any other desired page)
        WebDriverWait(driver, 5).until(
            EC.url_contains("/feed")
        )

        # Check if login was successful by waiting for the dashboard element
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "feed-identity-module"))
        )
        
        print("Logged Into LinkedIn via Credentials")
        driver.minimize_window()
        return True

    except Exception:
        print (error)
        driver.minimize_window()
        return False