from stats import word_counter, character_counter, dict_sort


def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        return book_contents
    



    


    
def main():
    book_contents = get_book_text("books/frankenstein.txt")
    word_count = word_counter(book_contents)
    char_count = character_counter(book_contents)
    sorted_count = dict_sort(char_count)
    
    print(f"Found {word_count} total words")
    print(sorted_count)


main()