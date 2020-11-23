from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

url = r'https://www.its.co.uk/search.aspx?rs=dewalt-dcf887&directSearch=true#/embedded/query=dewalt%20dcf887&page=1&query_name=match_and'
page = urlopen(url)
html = page.read().decode("utf-8")
# start_index = html.find("<title>") + len("<title>")
# end_index = html.find("</title>")
# title = html[start_index:end_index]

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(f"Website title is '{title}'")

soup = BeautifulSoup(html, "html.parser")
# print(soup.get_text())
print(soup.find_all("img"))