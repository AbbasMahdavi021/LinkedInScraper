import csv

def save_comments_to_csv(comments_list, output_filename="comments.csv"):
    # Define CSV file headers
    fieldnames = ["Name", "LinkedIn URL", "Position", "Comment", "Timestamp"]

    # Write comments data to CSV file
    with open(output_filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(comments_list)

    print(f"Comments saved to {output_filename}")
