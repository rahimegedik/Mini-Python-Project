def start_end_letter(char):
    print("Looking for two \""+char+"\" words in a row.")
    word=input("Type a word: ")
    for i in word:
        
        word=input("Type a word: ")
        if word[0] == word[len(word)]:
            break
            


start_end_letter("l")
