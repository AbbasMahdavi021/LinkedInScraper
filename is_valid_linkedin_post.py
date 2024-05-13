import re

def is_valid_linkedin_post(url):

    # Define a regular expression pattern for LinkedIn post URLs
    linkedin_pattern = r'^https:\/\/www\.linkedin\.com\/(?:posts|feed)\/.+'

    if re.match(linkedin_pattern, url):
        return True
    else: 
        return False