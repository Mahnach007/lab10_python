class Book:

    def __init__(self, name: str, author: str, publication_date: int, edition: str, price: float):
        self.name = name
        self.author = author
        self.publication_date = publication_date
        self.edition = edition
        self.price = price


    def __str__(self) -> str:
        return f"Name: {self.name}, Author: {self.author}, Date: {self.publication_date}, Edition: {self.edition}, Price: {self.price}"
    
        