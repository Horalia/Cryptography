#-------------[HORALIA ARMAS] ------------
#HOMEWORK 1: PROBLEM 1
#ANSWER: watchoutforbrutus = watch out for brutus
def string_encrypted(decrypt_object):
    list_encrypted = decrypt_object.read()
    return list_encrypted

def Decrypting_String(list_object,shift):
    letter_val_list = []
    for letter in list_object:
        letter = ord(letter)
        #if letter is out of bound when shift is made
        if letter >= 97 and letter < (97 +shift):
            letter = letter + (26- shift)
            letter_val_list.append(letter)
        else:
            letter = letter - shift
            letter_val_list.append(letter)
       
       

    return (letter_val_list)
def Plaintext(plaintext_values):
    plaintext = ""
    for value in plaintext_values:
        letter = chr(value)
        plaintext += letter
    return (plaintext)

    
def main():    
    decrypt_object = open('ycve.txt','r')
    list_object = string_encrypted(decrypt_object)
    decrypt_object.close()
    shift = 1
    while shift <= 26:
        plaintext_values = Decrypting_String(list_object, shift)
        plaintext = Plaintext(plaintext_values)
        print(" The plaintext is: ", plaintext, "Shift: ", shift)
        shift += 1

    
    
    
    
    
    
    
    

if __name__ == "__main__":
    main()

