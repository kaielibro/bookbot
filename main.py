def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    chars = {}
    lc_text = text.lower()
    for i in lc_text:
        if i.isalpha():
            chars[i] = chars.get(i, 0) + 1
    return chars

def sort_on(dict):
    return dict["num"]

def dict_to_list_dict(dict):
    list_dict = []
    for key, value in dict.items():
        list_dict.append({"char": key, "num": value})
    return list_dict

def print_report(book_path):
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_list = dict_to_list_dict(char_count)
    char_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for char in char_list:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)

main()