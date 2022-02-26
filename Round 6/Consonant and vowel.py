"""VU TU PHUONG NGUYEN
PROGRAMMING 1 spring 2021"""

def main():
    vowel_list = ["a", "e", "i", "o", "u", "y"]
    vowel = 0
    consonant = 0
    word = str(input("Enter a word: "))
    for letter in word:
        if letter in vowel_list:
            vowel +=1
        else:
            consonant += 1
    print(f"The word \"{word}\" contains",vowel, "vowels and",consonant, "consonants.",end = "")


if __name__ == "__main__":
    main()
