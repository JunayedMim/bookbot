import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>:")
    sys.exit(1)
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

from stats import word_counter
from stats import character_counter    
from stats import list_converter
from stats import sort_listed_dict

def main():
    book_contents = get_book_text(sys.argv[1])
    
    word_number = word_counter(book_contents)
    
    char_counts = character_counter(book_contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_number} total words")
    
    dict_list = list_converter(char_counts)
    sorted_list = sort_listed_dict(dict_list)
    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
   
    

   
    print("============= END ===============")

main()
