"""
LinkedIn Post Comments Scraper

This script allows users to enter a valid LinkedIn post URL and 
then retrieves comments for that post. 
The comments along with their details are stored in a CSV file.

main():
- The main function loops until a valid LinkedIn post URL is entered.
- It checks the validity of the URL using the is_valid_linkedin_post function.
- If the URL is valid, it retrieves comments using the get_comments function and stores them in a CSV file.


Author: Abbas Mahdavi
Date: 05/14/24

"""
from utilities.is_valid_linkedin_post import is_valid_linkedin_post
from utilities.get_comments import get_comments


def main():
    # Loop until a valid LinkedIn post URL is entered
    while True:
        postURL = input("Enter a valid LinkedIn Post URL: ")

        # Check if the entered URL is a valid LinkedIn post
        # return True or False
        # URL must start with: https://www.linkedin.com/feed/... 
        #                   or https://www.linkedin.com/post/...


        if is_valid_linkedin_post(postURL):
            break
        else:
            print("Error: Invalid LinkedIn Post URL!")

    # Once a valid URL is entered, get comments for the post
    get_comments(postURL)

if __name__ == '__main__':
    main()