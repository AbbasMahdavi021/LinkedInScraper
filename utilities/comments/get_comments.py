import time
from bs4 import BeautifulSoup as BSoup

from ..save_comments_to_csv import save_comments_to_csv

comments_list = []

def get_all_comments(driver, target_post_url):
        print(target_post_url)


def get_public_comments(driver, target_post_url):

    driver.get(target_post_url)
    time.sleep(3)
    soup = BSoup(driver.page_source, "html.parser")
    # Find all comment sections
    comment_sections = soup.find_all(class_="comment")
    # Loop through each comment section and extract relevant information

    # Loop through each comment section and extract relevant information
    for section in comment_sections:
        comment_data = {}
        try:
            author_element = section.find(class_="comment__author")
            if author_element:
                comment_data["Name"] = author_element.text.strip()
                comment_data["LinkedIn URL"] = author_element["href"]
            
            position_element = section.find(class_="comment__author-headline")
            if position_element:
                comment_data["Position"] = position_element.text.strip()
            
            comment_text_element = section.find(class_="comment__text")
            if comment_text_element:
                comment_data["Comment"] = comment_text_element.text.strip()
            
            timestamp_element = section.find(class_="comment__duration-since")
            if timestamp_element:
                comment_data["Timestamp"] = timestamp_element.text.strip()

            # Append the comment details to the comments_list
            comments_list.append(comment_data)
        except Exception as e:
            # Handle any other exceptions that might occur
            print(f"Error processing comment section: {e}")

    save_comments_to_csv(comments_list, "comments.csv")