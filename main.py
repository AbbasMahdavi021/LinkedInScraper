"""
LinkedIn Post Comments Scraper

This script allows users to enter a valid LinkedIn post URL and 
then retrieves comments for that post. 
The comments along with their details are stored in a CSV file.

main():
- The main function loops until a valid LinkedIn post URL is entered.
- It checks the validity of the URL using the is_valid_linkedin_post function.
- If the URL is valid, it retrieves comments using the get_comments function and stores them in a CSV file.


Author: Abbas Mahdavi
Date: 05/14/24

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from utilities.post_url import request_post_url
from utilities.comments.get_comments import get_public_comments, get_all_comments


from utilities.initiate import initiate


path_to_driver = './drivers/chromedriver.exe'


def main():

    options = Options()
    # Keeps the browser open after the script ends
    options.add_experimental_option("detach", True)  

    service = Service(executable_path=path_to_driver)
    driver = webdriver.Chrome(service=service, options=options)
    driver.minimize_window()

    is_authenticated = initiate(driver)

    target_post_url = request_post_url()

    if is_authenticated:
        get_all_comments(driver, target_post_url)
    else:
        get_public_comments(driver, target_post_url)






if __name__ == '__main__':
    main()