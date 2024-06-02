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
        chars[i] = chars.get(i, 0) + 1
    return chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(f"The word count is: {word_count}")
    print(f"The character counts are: {char_count}")

main()