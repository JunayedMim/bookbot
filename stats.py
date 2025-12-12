def word_counter(book_contents):
    word_list = book_contents.split()
    num_words = len(word_list)
    return num_words


def character_counter(book_contents):
    char_dict = {}
    word_list = book_contents.split()

    for word in word_list:
        lowered_word = word.lower()
        
        for char in lowered_word:
            if char not in char_dict:
                char_dict[char] = 1
            elif char in char_dict:
                char_dict[char] += 1

    return char_dict

def sort_on(item):
    return item["num"]




def dict_sort(char_dict):
    sorted_list = []
    
    for char, num in char_dict.items():
        if not char.isalpha():
            continue

        single_char_dict = {
            "char": char,
            "num": num
        }
        sorted_list.append(single_char_dict)
    

        
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

