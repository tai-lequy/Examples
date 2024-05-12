class TextBook():
    def __init__(self, pages_number):
        self.pages_number = pages_number
    def print_book_title(self, book_title):
        print(book_title)
    def print_book_pages_number(self):
        print("The number of pages is: {}".format(self.pages_number))
def main():
    pages_number = 300
    # object text_book is the instant of the class TextBook():
    text_book = TextBook(pages_number)
    book_title = "Programming with Python"
    # calling print_book_title() method
    text_book.print_book_title(book_title)
    # calling print_book_pages_number method
    text_book.print_book_pages_number()
    #print("The number of pages is: ",text_book.pages_number)
if __name__ == '__main__':
    main()