class Book: #capitalize first letter

    def __init__(self, word_count, cover_color, title, author, publisher):
        self.word_count=word_count
        self.cover_color=cover_color
        self.title=title
        self.author=author
        self.publisher=publisher
    
    def increase_word(self):
        self.word_count+=1

    def __str__(self):
        return"A book has {word_count}pages and the author is {author}."

harry_potter = Book(100000,"Orange","Harry Potter","J.K Rowling","Bloomsbury")
print(harry_potter)

class Car:

    def __init__(self, color, company, model, size, speed):
        self.color=color
        self.company=company
        self.model=model
        self.size=size
        self.speed=speed