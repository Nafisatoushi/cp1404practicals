import wikipedia

while True:
    search_phrase = input("Enter a page title or search phrase (or blank to quit): ")
    if not search_phrase:
        break

    try:
        page = wikipedia.page(search_phrase)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        pass  # Handle disambiguation error here
