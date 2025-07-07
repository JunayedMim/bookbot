def word_counter(file_contents):
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count



def character_counter(book_text):
    character_dict = {}
    lowered_book_text = book_text.lower()
    for character in lowered_book_text:
        if character not in character_dict:
            character_dict[character] = 1
        elif character in character_dict:
            character_dict[character] += 1
    return character_dict


def list_converter(character_dict):
    list_of_dict = [ {"char": key, "num": value} for key, value in character_dict.items() ]
    return list_of_dict

def sort_on(items):
    return items["num"]



def sort_listed_dict(list_of_dict):
    list_of_dict.sort(reverse=True,key=sort_on)
    return list_of_dict