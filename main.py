def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_chars = get_num_char(text)
    sorted_chars = dict(sorted(lowered_chars.items(), reverse=True, key=lambda x:x[1]))
    print(f"Creating report of" + " " + (book_path[6:]) + "....")
    print(f"===============================================================")
    print(f"{num_words} words were found in the book")
    print(f"")
    print_chars(sorted_chars)
    print(f"===============================================================")
    print(f"Report completed successfully!")
    
def print_chars(sorted):
    for key, value in sorted.items():
        if key.isalpha() == True:
            print(f"The '{key}' character was found {value} times")
    else:
        pass

def get_num_char(text):
    chars = {}
    for i in text.lower():
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()