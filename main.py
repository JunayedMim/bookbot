def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        return book_contents
    

def word_counter(book_contents):
    word_list = book_contents.split()
    num_words = len(word_list)
    return num_words

    


    
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    word_count = word_counter(book_contents)
    print(f"Found {word_count} total words")


main()