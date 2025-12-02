# fruits = ["Apples", "Bananas", "Pears"]

# book1 = {"title": "Great Expectations", "author": "Charles Dickens"}
# book2 = {"title": "Bleak House", "author": "Charles Dickens"}
# book3 = {"title": "An Book By No Author"}
# book4 = {"title": "Moby Dick", "author": "Herman Melville"}

# books = [book1, book2, book3, book4]

# # Simple enough to start

# fruit_mapping = {fruit: fruit.upper() for fruit in fruits}
# fruit_mapping

# print(fruit_mapping)

class BookShelf:
    def __init__(self, books):
        self.books = books

    def unique_authors(self):
        seen = set()
        for book in self.books:
            author = book["author"]
            if author not in seen:
                seen.add(author)
                yield author


# Example usage
books = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "Animal Farm", "author": "George Orwell"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"title": "The Silmarillion", "author": "J.R.R. Tolkien"},
    {"title": "Dune", "author": "Frank Herbert"},
]

shelf = BookShelf(books)

for author in shelf.unique_authors():
    print(author)
