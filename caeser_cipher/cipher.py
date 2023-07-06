from caeser_cipher.corpus_loader import word_list, name_list
from caeser_cipher.is_english_word import count_words

def encrypt(plain_text, shift):
      encrypted_text = ""
      for char in plain_text:
            if char.isalpha(): #checks if the char is alpha letter
                base = ord('a') if char.islower() else ord('A') #if yes, determines base value based on if char is lower or upper
                shifted_char = chr((ord(char) - base + shift) % 26 + base) # calc shifted char by sub the base value from the ASCII value of the char, then adding shift value, then taking modulo of that and 26 to make sure it wraps around the alphabet range. result of this is added to the base value to get the equivalent shifted character
                encrypted_text += shifted_char # concat shifted char to encrypted_text string
            else: # if char is not alpha letter
                encrypted_text += char # concat to encrypted_text string
      return encrypted_text # return encrypted version of plain_text


def decrypt(encrypted_test, shift):
    return encrypt(encrypted_test, -shift) # returns result of encrypt fn called on the encrypted_text and NEGATION of the shift args, since decryption is shift in opposite direction

def crack(encrypted_text):
    potential_solutions = [] # empty list to store potential decrypted versions
    for shift in range(1, 27): # go through each possible shift value from 1-26
        potential_solutions.append(decrypt(encrypted_text, shift))
    for phrase in potential_solutions:
        word_count = count_words(phrase)
        percentage = int(word_count / len(phrase.split()) * 100)
        if percentage > 50: # if we have confidence that over 50% of the words match english, return, otherwise, if it's jibberish, return the string at line 28
             return phrase
    return ''



if __name__ == "__main__":
      print("cypher.py is showing")