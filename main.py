def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_dict = dict_list(char_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} found in the document")
    print("")
    for i in char_dict:
        if not i["char"].isalpha():
            continue
        print(f"The {i["char"]} character was found {i["num"]} times")
    print("--- End report ---")

def get_char_count(words):
    char_count = {}
    lowered_words = words.lower()
    for char in lowered_words:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_word_count(words):
    word = words.split()
    return len(word)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_dict(dict):
    return

def sort_on(key):
    return key["num"]

def dict_list(dict):
    list = []
    for ch in dict:
        list.append({"char" : ch, "num" : dict[ch]})
    list.sort(reverse=True, key=sort_on)
    return list

main()