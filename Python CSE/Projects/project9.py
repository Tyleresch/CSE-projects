'''
Main data structure is a dictionary
   word_dic[(i,ch)] = set of words with ch at index i
'''
import string

def open_file():
    while True:
        try:
            file_name = input("Enter a vocabulary file name: ")
            fp = open(file_name, encoding='UTF-8')
            return fp
        except FileNotFoundError:
            print("Error: file not found.")
    # Docstring
    pass

def read_file(fp):
    word_set = set()
    for line in fp:
        words = line.split()
        for word in words:
            # Remove punctuation
            cleaned_word = ''.join(c for c in word if c not in string.punctuation)

            # Check if the cleaned word has a length greater than 1 and the original word contains only alphabetic characters or punctuation
            if len(cleaned_word) > 1 and cleaned_word.isalpha() and all(c.isalpha() or c in string.punctuation for c in word):
                word_set.add(cleaned_word.lower())
    return word_set


def fill_completions(words):
    # Docstring
    word_dic = {}
    for word in words:
        for i, ch in enumerate(word):
            key = (i, ch)
            if key not in word_dic:
                word_dic[key] = set()
            word_dic[key].add(word)
    return word_dic

    pass

def find_completions(prefix,word_dic):
    if not prefix:
        return set()
    
    completions = set(word_dic[(0, prefix[0])]) if (0, prefix[0]) in word_dic else set()

    for i, ch in enumerate(prefix[1:], start=1):
        key = (i, ch)
        if key in word_dic:
            completions = completions.intersection(word_dic[key])
        else:
            return set()

    return completions

def main():  
    fp = open_file()
    words = read_file(fp)
    word_dic = fill_completions(words)

    while True:
        prefix = input("Enter a word prefix: ").strip().lower()
        if not prefix:
            break

        completions = find_completions(prefix, word_dic)
        if completions:
            print("The completions are:", ", ".join(sorted(completions)))
        else:
            print("No completions found.")     
    pass

if __name__ == '__main__':
    main()
