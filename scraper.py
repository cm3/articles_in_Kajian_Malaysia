# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
from bs4 import BeautifulSoup
import urllib.parse
import re
import os

#re_issue = re.compile("(?<=href\=\")issue-view.php\?id\=[^\"]+(?=\")")
re_issue = re.compile("issue-view.php\?id\=[^\"]+")
urlhead = "http://www.myjurnal.my/public/"
os.environ["SCRAPERWIKI_DATABASE_NAME"] = "sqlite:///data.sqlite"

# # Read in a page
html = scraperwiki.scrape("http://www.myjurnal.my/public/browse-journal-view.php?id=154")
#
# # Find something on the page using css selectors
soup = BeautifulSoup(html, "html.parser")

for a in soup.find_all(href=re_issue):
    #print(urlhead+a["href"])
    #print(a.get_text().strip())
    scraperwiki.sqlite.save(unique_keys=['uri'], data={"uri":urlhead+a["href"], "label": a.get_text().strip()}, table_name="data")

#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

scraperwiki.sql.select("* from data")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
