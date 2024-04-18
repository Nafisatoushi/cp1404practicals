import wikipedia

while True:
    # Prompt user for input
    search_phrase = input("Enter a page title or search phrase (or press Enter to exit): ")

    # Check if input is blank, if so, exit the loop
    if not search_phrase:
        break

    try:
        # Search for the page
        page = wikipedia.page(search_phrase, auto_suggest=False)

        # Print page title, summary, and URL
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.DisambiguationError as e:
        # Handle disambiguation page
        print("Disambiguation Error: Choose one of the following options:")
        for option in e.options:
            print("-", option)
    except wikipedia.PageError:
        # Handle page not found
        print("Page not found for the given search phrase.")
