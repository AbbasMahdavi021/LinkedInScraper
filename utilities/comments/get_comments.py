"""
LinkedIn Comments Scraping

Author: Abbas Mahdavi
Date: 05/14/24
Description:
This script contains functions to scrape comments from LinkedIn posts using Selenium and BeautifulSoup. 
It includes functions to scrape all comments (including hidden ones) and public comments only. 
The scraped comments are then saved to a CSV file.

Usage:
1. Use 'get_all_comments' to scrape all comments from a LinkedIn post.
2. Use 'get_public_comments' to scrape public comments only, without authentication.

"""


import time
from bs4 import BeautifulSoup as BSoup
from selenium.webdriver.common.by import By

from ..save_comments_to_csv import save_comments_to_csv

comments_list = []


def get_all_comments(driver, target_post_url):
    # Open the target post URL
    driver.get(target_post_url)
    time.sleep(1)  # Wait for the comments to load initially

    # JavaScript to scroll down the page
    scroll_script = "window.scrollTo(0, document.body.scrollHeight);"

    def click_show_more_button():
        try:
            # Locate and click the "Show more" button for comments
            show_more_button = driver.find_element(By.CLASS_NAME, "comments-comments-list__load-more-comments-button")
            show_more_button.click()
            return True  # Return True if the button was clicked successfully
        except Exception:
            print("Found all comments!")
            return False  # Return False if all comments are already loaded

    # Keep scrolling and clicking "Show more" until all comments are loaded
    while True:
        driver.execute_script(scroll_script)  # Scroll down
        time.sleep(1)  # Wait for page to load after scrolling
        if not click_show_more_button():  # Break the loop if all comments are loaded
            break

    # Parse the page source using BeautifulSoup
    soup = BSoup(driver.page_source, "html.parser")
    comment_sections_all = soup.find_all(class_="comments-comment-item")

    comments_list = []  # Initialize an empty list to store comments

    # Extract information for each comment and store in a dictionary
    for comment in comment_sections_all:
        author_name = comment.find(class_="comments-post-meta__name-text").get_text(strip=True)
        linkedin_url = comment.find(class_="app-aware-link")['href']
        position = comment.find(class_="comments-post-meta__headline").get_text(strip=True)
        comment_text = comment.find(class_="comments-comment-item__main-content").get_text(strip=True)
        timestamp = comment.find(class_="comments-comment-item__timestamp").get_text(strip=True)

        comment_dict = {
            "Name": author_name,
            "LinkedIn URL": linkedin_url,
            "Position": position,
            "Comment": comment_text,
            "Timestamp": timestamp
        }

        comments_list.append(comment_dict)  # Add the comment to the list

        # Print the scraped comment in a readable format
        print(f"Scraped Comment:\n"
              f"Name: {comment_dict['Name']}\n"
              f"LinkedIn URL: {comment_dict['LinkedIn URL']}\n"
              f"Position: {comment_dict['Position']}\n"
              f"Comment: {comment_dict['Comment']}\n"
              f"Timestamp: {comment_dict['Timestamp']} ago\n"
              "----------------------------------")

    # Save the comments to a CSV file
    save_comments_to_csv(comments_list, "comments.csv")



def get_public_comments(driver, target_post_url):
    # Open the target post URL
    driver.get(target_post_url)
    time.sleep(3)  # Wait for the page to load
    
    # Parse the page source using BeautifulSoup
    soup = BSoup(driver.page_source, "html.parser")
    
    # Find all comment sections on the page
    comment_sections_public = soup.find_all(class_="comment")
    
    for section in comment_sections_public:
        comment_dict = {}  # Initialize an empty dictionary for each comment
        
        try:
            # Extract author information if available
            author_element = section.find(class_="comment__author")
            if author_element:
                comment_dict["Name"] = author_element.text.strip()
                comment_dict["LinkedIn URL"] = author_element["href"]
            
            # Extract author's position if available
            position_element = section.find(class_="comment__author-headline")
            if position_element:
                comment_dict["Position"] = position_element.text.strip()
            
            # Extract comment text if available
            comment_text_element = section.find(class_="comment__text")
            if comment_text_element:
                comment_dict["Comment"] = comment_text_element.text.strip()
            
            # Extract timestamp if available
            timestamp_element = section.find(class_="comment__duration-since")
            if timestamp_element:
                comment_dict["Timestamp"] = timestamp_element.text.strip()

            comments_list.append(comment_dict)  # Add the comment to the list

            # Print the scraped comment in a readable format
            print(f"Scraped Comment:\n"
                  f"Name: {comment_dict.get('Name', 'N/A')}\n"
                  f"LinkedIn URL: {comment_dict.get('LinkedIn URL', 'N/A')}\n"
                  f"Position: {comment_dict.get('Position', 'N/A')}\n"
                  f"Comment: {comment_dict.get('Comment', 'N/A')}\n"
                  f"Timestamp: {comment_dict.get('Timestamp', 'N/A')} ago\n"
                  "----------------------------------")
            
        except Exception:
            print(f"Error processing comment section!")

    # Save the comments to a CSV file
    save_comments_to_csv(comments_list, "comments.csv")
