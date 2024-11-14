import pyshorteners

def shorten_url(url):
    """Shorten a given URL."""
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

def main():
    while True:
        url = input("Enter a URL to shorten (or type 'exit' to quit): ")
        if url.lower() == 'exit':
            print("Exiting the application.")
            break
        try:
            short_url = shorten_url(url)
            print(f"Shortened URL: {short_url}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
