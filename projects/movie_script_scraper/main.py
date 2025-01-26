from projects.movie_script_scraper.scraper.movie_script_scraper import MovieScriptScraper



def main():
    movie_script_scraper = MovieScriptScraper()
    # print(movie_script_scraper.fetch_data(1))
    raw_html = None

    try:
        raw_html = movie_script_scraper.fetch_data(1)
    except Exception as e:
        print(f"Error: {e}")

    try:
        print(movie_script_scraper.parse_data(raw_html))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()