class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        pass

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Name: {self.name}\nAuthor: {self.author}\nPage: {self.page_count} pages")


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        print(f"Name: {self.name}\nEditor: {self.editor}")

magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No.6", "Rosa Liksom", 192)
magazine1.print_information()
book1.print_information()
