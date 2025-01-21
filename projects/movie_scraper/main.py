from projects.movie_scraper.scraper.movie_scraper import MovieScraper
from projects.movie_scraper.utils.settings import OUTPUT_FOLDER


def main():

    total_pages = int(input("Enter the number of pages you want to scrape (e.g., 1, 2, 3): "))
    file_name = input("Enter the desired file name: ")

    scraper = MovieScraper()

    all_movies = []

    for page in range(1, total_pages + 1):
        print(f"Scraping page {page}...")
        try:
            raw_html = scraper.fetch_data(page)
            movies = scraper.parse_data(raw_html)
            all_movies.extend(movies)
        except Exception as e:
            print(f"Error on page {page}: {e}")

    try:
        scraper.save_to_csv(all_movies, file_name + ".csv")
        print(f"\nScraping completed successfully! The data has been saved to '{OUTPUT_FOLDER + file_name}.csv'.")
    except Exception as e:
        print(f"\nAn error occurred while saving the file: {e}")

if __name__ == "__main__":
    main()