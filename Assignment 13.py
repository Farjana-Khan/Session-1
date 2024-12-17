# Assignment 13: Write a regex to find all the hashtags in a string.

import re

# Regex to find hashtags
text_with_hashtags = "This is a #great day to learn #regex in #Python!"
hashtag_regex = r"#\w+"
hashtags = re.findall(hashtag_regex, text_with_hashtags)
print("Hashtags found:", hashtags)
