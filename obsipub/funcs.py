import os
from obsipub import config


def list_posts():
    """
    List all post names in the directory.
    All markdown files in the path should be listed as titles.
    The list of titles should be cleaned to replace <space> with hyphens.
    """
    # Define the path to the markdown files directory
    md_folder_path = config.POSTS_PATH  # assuming the path is set in the config

    # Check if the directory exists
    if not os.path.exists(md_folder_path):
        print("Directory does not exist.")
        return

    # List to store cleaned titles
    cleaned_titles = []

    # Iterate through all files in the directory
    for md_file in os.listdir(md_folder_path):
        if md_file.endswith(".md"):
            # Remove the file extension
            title = os.path.splitext(md_file)[0]
            # Replace spaces with hyphens
            cleaned_title = title.replace(" ", "-")
            cleaned_titles.append(cleaned_title)

    return cleaned_titles
