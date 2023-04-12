'''
Main data structure is a dictionary
   word_dic[(i,ch)] = set of words with ch at index i
'''
import string

def open_file():
    while True:
        try:
            file_name = input("\nInput a file name: ")
            fp = open(file_name, encoding='UTF-8')
            return fp
        except FileNotFoundError:
            print("\n[Error]: no such file")
    # Docstring
    pass

def read_file(fp):
    word_set = set()
    for line in fp:
        words = line.strip().split()
        for word in words:
            cleaned_word = ''.join(c for c in word if c not in string.punctuation)
            subwords = cleaned_word.split('-')
            for subword in subwords:
                if len(subword) > 1 and subword.isalpha() and "'" not in word and "-" not in word:
                    word_set.add(subword.lower())
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
        prefix = input("\nEnter a prefix (# to quit): ")
        
        if prefix == '#':
            print("\nBye")
            break
        
        completions = find_completions(prefix, word_dic)
        
        if completions:
            completions_str = ", ".join(sorted(list(completions)))
            print(f"\nThe words that completes {prefix} are: {completions_str}")
        else:
            print("\nThere are no completions.")

if __name__ == '__main__':
    main()
