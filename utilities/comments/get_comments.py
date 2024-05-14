import time
from bs4 import BeautifulSoup as BSoup
from selenium.webdriver.common.by import By

from ..save_comments_to_csv import save_comments_to_csv

comments_list = []

def get_all_comments(driver, target_post_url):
    driver.get(target_post_url)
    time.sleep(1)  # Wait for the comments to load
    scroll_script = "window.scrollTo(0, document.body.scrollHeight);"

    def click_show_more_button():
        try:
            show_more_button = driver.find_element(By.CLASS_NAME, "comments-comments-list__load-more-comments-button")
            show_more_button.click()
            return True
        except Exception as e:
            print(f"Error clicking 'Show more' button: {e}")
            return False
        
    while True:
        driver.execute_script(scroll_script)
        time.sleep(1)
        if not click_show_more_button():
            break

    soup = BSoup(driver.page_source, "html.parser")
    comment_sections_all = soup.find_all(class_="comments-comment-item")
    for comment in comment_sections_all:
        author_name = comment.find(class_="comments-post-meta__name-text").get_text(strip=True)
        linkedin_url = comment.find(class_="app-aware-link")['href']
        position = comment.find(class_="comments-post-meta__headline").get_text(strip=True)
        comment_text = comment.find(class_="comments-comment-item__main-content").get_text(strip=True)
        Timestamp = comment.find(class_="comments-comment-item__timestamp").get_text(strip=True)
        comments_list.append({
            "Name": author_name,
            "LinkedIn URL": linkedin_url,
            "Position": position,
            "Comment": comment_text,
            "Timestamp": Timestamp
        })
    
    save_comments_to_csv(comments_list, "comments.csv")

def get_public_comments(driver, target_post_url):
    driver.get(target_post_url)
    time.sleep(3)
    soup = BSoup(driver.page_source, "html.parser")
    comment_sections_public = soup.find_all(class_="comment")
    
    for section in comment_sections_public:
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

            comments_list.append(comment_data)
        except Exception as e:
            print(f"Error processing comment section: {e}")

    save_comments_to_csv(comments_list, "comments.csv")
