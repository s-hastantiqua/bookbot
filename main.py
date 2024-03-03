def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    report(book_path, num_words, chars_dict)

def report(path, num_words, chars_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = [{'char': key, 'num': value} for key, value in chars_dict.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

def get_chars_dict(text):
    alphabet = "abcdefghijklmnoprqstuvwxyz"
    text = text.lower()
    chars = {}
    for letter in alphabet:
        chars[letter] = text.count(letter)
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()