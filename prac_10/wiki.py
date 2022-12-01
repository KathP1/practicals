"""
CP1404 Practical 10
Wikipedia API & Python Library
"""

import wikipedia


def main():
    """Search for and display a wikipedia page summary and URL"""
    search_phrase = input("Enter page title or search phrase: ")
    while search_phrase != "":
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(f"Title: {page.title}")
            print(f"Summary: {wikipedia.summary(page)}")
            print(page.url)
            print("\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Is it one of these?: {e.options}")
        search_phrase = input("Enter page title or search phrase: ")


if __name__ == '__main__':
    main()
