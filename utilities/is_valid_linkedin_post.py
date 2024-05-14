"""
LinkedIn Post URL Validator

This function checks whether a given URL is a valid LinkedIn post URL according to the defined pattern.

Author: Abbas M.
Date: 05/14/24

is_valid_linkedin_post():
- Call the is_valid_linkedin_post function and pass a URL string to check its validity.
- Returns True if the URL matches the LinkedIn post URL pattern, False otherwise.

"""


import re

def is_valid_linkedin_post(postURL):

    # Define a regular expression pattern for LinkedIn post URLs
    # URL must start with: https://www.linkedin.com/feed/... 
    #                   or https://www.linkedin.com/post/...

    linkedin_pattern = r'^https:\/\/www\.linkedin\.com\/(?:posts|feed)\/.+'

    if re.match(linkedin_pattern, postURL):
        return True
    else: 
        return False