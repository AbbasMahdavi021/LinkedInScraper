import time
import re
import pandas as pd
from bs4 import BeautifulSoup as BSoup

from save_comments_to_csv import save_comments_to_csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = 'chromedriver.exe'

def get_comments(url):
    
    service = Service(executable_path = path)
    driver = webdriver.Chrome(service = service)
    driver.maximize_window()

    driver.get(url)

    time.sleep(1)

    soup = BSoup(driver.page_source, "html.parser")
    # Find all comment sections
    comment_sections = soup.find_all(class_="comment")

    # Initialize an empty list to store formatted comments
    commenters_list = []

    # Loop through each comment section and extract relevant information
    for comment in comment_sections:
        # Extract author name and LinkedIn URL
        author_element = comment.find(class_="comment__author")
        if author_element:
            author_name = author_element.get_text(strip=True)
            linkedin_url = author_element['href'] if 'href' in author_element.attrs else None

        # Extract author position
        position_element = comment.find(class_="comment__author-headline")
        position = position_element.get_text(strip=True) if position_element else None

        # Extract comment text
        comment_text_element = comment.find(class_="comment__text")
        comment_text = comment_text_element.get_text(strip=True) if comment_text_element else None

        # Append commenter details to the list
        commenters_list.append({
            "Name": author_name,
            "LinkedIn URL": linkedin_url,
            "Position": position,
            "Comment": comment_text
        })

    save_comments_to_csv(commenters_list, "comments_output.csv")
