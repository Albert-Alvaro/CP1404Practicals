"""
CP1404 - Practicals
"""

import wikipedia

user_search = input("Search: ")
while user_search != "":
    wiki_page = wikipedia.page(user_search)
    print("Title: " + wiki_page.title)
    print(wikipedia.summary(user_search))
    print("URL: " + wiki_page.url)
    user_search = input("Search: ")