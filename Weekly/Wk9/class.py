class Book:
    def __init__(self, title, author, year, url):
        self.title = title
        self.author = author
        self.year = year
        self.url = url


book1 = Book("Harvard", "Michael", "2019", "google.com")
book2 = Book("Sydney", "Jesus", "2014", "facebook.com")

b1_author = book1.author
b1_title = book1.title
b1_year = book1.year
b1_url = book1.url

b2_author = book2.author
b2_title = book2.title
b2_year = book2.year
b2_url = book2.url

print(b1_author)
print(b1_title)
print(b1_url)
print(b1_year)

print(b2_author)
print(b2_title)
print(b2_url)
print(b2_year)