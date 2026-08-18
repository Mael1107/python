# Desafio 054 em CursoemVideo

phrase = input("Enter a phrase: ").strip().upper()
words = phrase.split()
new_phrase = "".join(words)
inverse_phrase = new_phrase[::-1]

if new_phrase == inverse_phrase:
    print("The typed phrase is a \033[1;32mpalindrome!\033[m")
else:
    print("The typed phrase is \033[1;31mNOT\033[m palindrome!")