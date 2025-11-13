import requests
import click

@click.command()
@click.argument("title")
@click.option('--count', default=6, help="number of books")

def title_search(title, count):
    """search book by its title."""

    URL = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        book = data.get("docs", [])
        if not book:
            print("No books found")
            return
        for books in book[:count]:
            print("Title:", books.get("title"))
            print("Author Name:", books["author_name"][0])
            print("Author Key:", books["author_key"][0])
            print("first publish year:", books["first_publish_year"],"\n")
        click.echo(f"The book name has been fetched successfully by {title}")
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    title_search()
    






