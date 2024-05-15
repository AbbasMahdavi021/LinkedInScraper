"""
LinkedIn Post Comments Scraper

Author: Abbas Mahdavi
Date: 05/14/24
Description: This script utilizes Selenium to scrape comments from a LinkedIn post. It allows for scraping all comments if authenticated or public comments otherwise.

Usage:
1. Run the python main.py.
2. Follow authentication prompts if required.
3. Provide the URL of the LinkedIn post when prompted.

"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from utilities.initiate import initiate
from utilities.post_url import request_post_url
from utilities.comments.get_comments import get_public_comments, get_all_comments

path_to_driver = './drivers/chromedriver.exe'

def main():
    """
    Scrapes comments from a LinkedIn post using Selenium.

    This function initiates a Selenium-driven browser, prompts for authentication if required,
    and then prompts for the URL of the LinkedIn post to scrape comments from.
    
    If authenticated, it scrapes all comments; otherwise, it scrapes public comments only.
    
    The browser remains open after execution.

    Returns:
    None
    """
    options = Options()
    # Keeps the browser open after the script ends
    options.add_experimental_option("detach", True)  


    service = Service(executable_path=path_to_driver)
    driver = webdriver.Chrome(service=service, options=options)
    driver.minimize_window()

    #initiates process, such as login, returns True/False
    is_authenticated = initiate(driver)

    #Promps the user for a linkedin post URL, return valid URL
    target_post_url = request_post_url()


    if is_authenticated:
        #prints all avaliable comments on a post, saves data to csv
        get_all_comments(driver, target_post_url)

        #quit or ask for another URL
        driver.quit()
    else:
        #prints top 10 public comments, saves data to csv
        get_public_comments(driver, target_post_url)
        driver.quit()

if __name__ == '__main__':
    main()
