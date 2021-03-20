# Imports
from bs4 import BeautifulSoup
import requests

#Data Sources
with open("website.html", "r") as web:
    contents = web.read()

response = requests.get("http://news.ycombinator.com/news")
response_text = response.text
soup = BeautifulSoup(response_text, "html.parser")
story_link_raw = soup.find_all(name="a", class_="storylink")
story_link_score = soup.find_all(name="span", class_="score")

article_text = [story_link.getText() for story_link in story_link_raw]
article_link = [story_link.get("href") for story_link in story_link_raw]
article_score = [int(story_score.getText().split()[0]) for story_score in story_link_score]
print(article_text)
print(article_score)
largest_upvote_score = max(article_score)
print(largest_upvote_score)
article_index = article_score.index(largest_upvote_score)
print(article_index)
print(f"{article_text[article_index]} {article_link[article_index]} {article_score[article_index]} ")

