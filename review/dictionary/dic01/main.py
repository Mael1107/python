book = {
    "title": "Palf",
    "author": "Araujuh",
    "year": 9
}

print(book["title"])

if "year" in book:
    print(book["year"])
else:
    print("year not reported")

print(book.get("publisher", "Not reported"))
print(book.get("author", "Autor desconhecido"))