# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    word = word.replace(" ", "").lower()
    anagram = anagram.replace(" ", "").lower()

    if (len(word) == len(anagram)):
        sorted_1 = sorted(word)
        sorted_2 = sorted(anagram)
        if (sorted_1 == sorted_2):
            print("\nTrue")
        else:
            print("\nFalse")


find_anagram("hello", "check")
find_anagram("below", "elbow")
