import wikipedia
def main():
    """Prompt the user for a page title or search phrase and display details."""
    print("Welcome to the Wikipedia search tool!")

    search_phrase = input("Enter page title (or press Enter to exit): ")
    while search_phrase:
        try:
            # Fetch the Wikipedia page with autosuggest disabled
            page = wikipedia.page(search_phrase, auto_suggest=False)

            # Display page details
            print("\nTitle:", page.title)
            print("Summary:", page.summary[:500], "...")  # Display a truncated summary
            print("URL:", page.url)

        except wikipedia.DisambiguationError as e:
            # Handle disambiguation pages
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(", ".join(e.options[:10]))  # Display up to 10 options for disambiguation


        except wikipedia.PageError:

            # Handle page not found error

            print(f'\nPage id "{search_phrase}" does not match any pages. Try another id!')

        except Exception as ex:
            # Handle unexpected exceptions
            print("\nAn unexpected error occurred:", str(ex))

            # Prompt again for a new search or exit
        search_phrase = input("\nEnter page title (or press Enter to exit): ")

    print("Thank you.")

if __name__ == "__main__":
    main()