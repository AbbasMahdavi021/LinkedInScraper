"""
CSV Comments Saving

Author: Abbas Mahdavi
Date: 05/14/24
Description:
This function takes a list of dictionaries containing comment data and saves it to a CSV file.

Usage:
1. Use the 'save_comments_to_csv' function to save comments to a CSV file.
2. Provide the comments list and an optional output filename.

"""

import csv

def save_comments_to_csv(comments_list, output_filename="comments.csv"):
    # Define CSV file headers
    fieldnames = ["Name", "LinkedIn URL", "Position", "Comment", "Timestamp"]

    # Write comments data to CSV file
    with open(output_filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(comments_list)

    print(f"Comments saved to ./{output_filename}")
