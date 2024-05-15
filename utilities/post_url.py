"""
LinkedIn Post URL Validator

Author: Abbas M.
Date: 05/14/24
Description:
This function loops until a valid LinkedIn post URL is entered by the user.


"""

import re

def request_post_url():

    # Loop until a valid LinkedIn post URL is entered
    while True:
        post_url = input("Enter a valid LinkedIn Post URL: ")

        if is_valid_linkedin_url(post_url):
            return post_url
        else:
            print("Error: Invalid LinkedIn Post URL!")
            print(f"URL must start with:\nhttps://www.linkedin.com/feed/...\nor\nhttps://www.linkedin.com/post/...")


#   Checks if a URL is a valid LinkedIn post URL.
# URL must start with: https://www.linkedin.com/feed/... 
#                   or https://www.linkedin.com/post/...
def is_valid_linkedin_url(postURL):

    linkedin_pattern = r'^https:\/\/www\.linkedin\.com\/(?:posts|feed)\/.+'

    if re.match(linkedin_pattern, postURL):
        return True
    else: 
        return False