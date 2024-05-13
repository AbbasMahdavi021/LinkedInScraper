

from is_valid_linkedin_post import is_valid_linkedin_post
from get_comments import get_comments

while True:

    url = input("Enter a valid LinkedIn Post URL: ")

    if is_valid_linkedin_post(url):
        break
    else:
        print("URL NOT A VALID POST!")

get_comments(url)


