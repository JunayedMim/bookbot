def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        print(book_contents)
        return
    
def main():
    get_book_text("books/frankenstein.txt")



main()