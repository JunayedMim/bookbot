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


def dict_sort(char_dict):
    sorted_list = []
    single_char_dict = {"char": "char_value", "num": "num_value"}
    
    for char in char_dict:
        single_char_dict["char"] = char
        single_char_dict["num"] = char_dict[char]
        single_char_dict_sort = {single_char_dict["char"]: single_char_dict["num"]}

        sorted_list.append(single_char_dict_sort)
    
    return sorted_list

