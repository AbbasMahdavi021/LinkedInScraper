import time
import re
import pandas as pd
from bs4 import BeautifulSoup as BSoup

from save_comments_to_csv import save_comments_to_csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = 'chromedriver.exe'

def get_comments(url):

    isLoggedIn = False

    comments_list = []


    # Enter your credentials
    username = input("Enter your LinkedIn Email Login (or s to skip login): ")
    if username != 's':
        password = input("Enter your password: ")

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.minimize_window()

    if username and username != 's':
        # Open LinkedIn sign-in page
        driver.get("https://www.linkedin.com")

        # Find username and password input fields
        username_field = driver.find_element(By.ID, "session_key")
        password_field = driver.find_element(By.ID, "session_password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        # Find and click the sign-in button
        sign_in_button = driver.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn']")
        sign_in_button.click()
        
        # It's a good practice to add a delay to ensure the page fully loads
        time.sleep(2)

        isLoggedIn = True

    if isLoggedIn:

        driver.get(url)
        time.sleep(1)  # Wait for the comments to load

        # Define a JavaScript script to scroll to the bottom of the page
        scroll_script = "window.scrollTo(0, document.body.scrollHeight);"

        # Execute the JavaScript to scroll to the bottom of the page
        driver.execute_script(scroll_script)

        # Wait for some time after scrolling to allow content to load (adjust as needed)
        time.sleep(2)

        # Define a function to check if the "Show 10 more comments" button exists and click it
        def click_show_more_button():
            try:
                show_more_button = driver.find_element(By.CLASS_NAME, "comments-comments-list__load-more-comments-button")
                show_more_button.click()
                return True
            except Exception as e:
                print(f"Error clicking 'Show more' button: {e}")
                return False

        # Keep scrolling and clicking the button until it's no longer available
        while True:
            driver.execute_script(scroll_script)  # Scroll again to load more content
            time.sleep(3)  # Wait for the scroll action and content to load
            if not click_show_more_button():
                break  # Exit loop if the button is no longer available

        soup = BSoup(driver.page_source, "html.parser")
        comment_sections = soup.find_all(class_="comments-comment-item")

        for comment in comment_sections:
            author_name = comment.find(class_="comments-post-meta__name-text").get_text(strip=True)
            linkedin_url = comment.find(class_="app-aware-link")['href']
            position = comment.find(class_="comments-post-meta__headline").get_text(strip=True)
            comment_text = comment.find(class_="comments-comment-item__main-content").get_text(strip=True)
            comment_timestamp = comment.find(class_="comments-comment-item__timestamp").get_text(strip=True)

            comments_list.append({
                "Name": author_name,
                "LinkedIn URL": linkedin_url,
                "Position": position,
                "Comment": comment_text,
                "Timestamp": comment_timestamp
            })

    else:
        driver.get(url)
        time.sleep(3)
        soup = BSoup(driver.page_source, "html.parser")
        # Find all comment sections
        comment_sections = soup.find_all(class_="comment")

        # Loop through each comment section and extract relevant information
        for comment in comment_sections:
            # Extract author name and LinkedIn URL
            author_element = comment.find(class_="comment__author")
            if author_element:
                author_name = author_element.get_text(strip=True)
                linkedin_url = author_element['href'] if 'href' in author_element.attrs else None
            else:
                author_name = None
                linkedin_url = None
            
            # Extract author position
            position_element = comment.find(class_="comment__author-headline")
            position = position_element.get_text(strip=True) if position_element else None
            
            # Extract comment text
            comment_text_element = comment.find(class_="comment__text")
            comment_text = comment_text_element.get_text(strip=True) if comment_text_element else None
            
            # Extract comment timestamp if available
            timestamp_element = comment.find(class_="comment__duration-since")
            comment_timestamp = timestamp_element.get_text(strip=True) if timestamp_element else None
            
            # Append commenter details to the list
            comments_list.append({
                "Name": author_name,
                "LinkedIn URL": linkedin_url,
                "Position": position,
                "Comment": comment_text,
                "Timestamp": comment_timestamp  # Add the timestamp to the dictionary
            })

    if len(comments_list) > 0:
        save_comments_to_csv(comments_list, "comments_output.csv")
    else:
        print("Could not find comments on this post!")

        
