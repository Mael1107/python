class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def description(self):
        return f"{self.title} - {self.author}" 

book01 = Book("The Little Prince", "Antoine de Saint-Exupéry")

print(book01.description())