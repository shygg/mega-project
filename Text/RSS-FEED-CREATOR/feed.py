"""
    RSS Feed Creator
        Given a link to RSS/Atom Feed, get all posts and display them
"""

import feedparser

d = feedparser.parse('http://feeds.gawker.com/lifehacker/full')
print(d['feed']['title'])
print(d.entries[3].title)
x = 0

#check for title, if there are no titles then f it
while True:
    try:
        print(x)
        print(d.entries[x].title)
        x += 1
    except:
        print("thats all")
        break
#check for description
    try:
        print(d.entries[x].description)
    except:
        print("no description")
#check for publication date
    try:
        print(d.entries[x].published)
    except:
        print("no date")
#check for url
    try:
        print(d.entries[x].link)
    except:
        print("no link available")

input("input anything to quit...")
