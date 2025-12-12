import sys
from stats import word_counter, character_counter, dict_sort

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1] 

def get_book_text(file_path):
    with open(file_path) as book:
        book_contents = book.read()
        return book_contents
    



    


    
def main():
    book_contents = get_book_text(file_path)
    word_count = word_counter(book_contents)
    char_count = character_counter(book_contents)
    sorted_count = dict_sort(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    for dict in sorted_count:
        print(f"{dict['char']}: {dict['num']}")
    
    print("============= END ===============")


main()