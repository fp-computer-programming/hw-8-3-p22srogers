# Author: SMR (AMDG) 12/10/21
def three_letter_words(words):
    leng = 0
    x = 0
    while x <  len(words):
        if(len(words[x]) == 3):
            leng += 1
            x += 1
        else:
            x += 1
            continue
    return leng
print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)