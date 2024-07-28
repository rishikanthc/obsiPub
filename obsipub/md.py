import os

import frontmatter
import markdown

__all__ = ["parse_md_file"]
# read markdown files from md folder in project root.
# parse yaml front matter  and separate it from rest
# parse markdown content and convert it to html


def parse_md_file(md_file_path):
    # Check if the file exists
    if os.path.exists(md_file_path) and md_file_path.endswith(".md"):
        # Read the markdown file
        with open(md_file_path, "r", encoding="utf-8") as file:
            # Parse the front matter and content
            post = frontmatter.load(file)
            front_matter = post.metadata
            content = post.content

            # Convert markdown content to HTML
            html_content = markdown.markdown(content)

            # Return the parsed data
            return {
                "file_name": os.path.basename(md_file_path),
                "front_matter": front_matter,
                "html_content": html_content,
            }
    else:
        print("File not found or not a markdown file.")
        return None
