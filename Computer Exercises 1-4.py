#-----------[HORALIA ARMAS]-------------------------------------------
#HOMEWORK 1: PROBLEM 4
#ANSWER: twentysixpossibilities = twenty six possibilities
def return_inverse(number):
    i = 1
    while (i%number != 0):
        i += 26
    return (int(i/number))



def Decrypting_String(list_object, shift):
    letter_val_list = [] 
    for letter in list_object:
        letter = ord(letter)
        #if letter is out of bound when shift is made
        if letter >= 97 and letter < (97 + shift):
            letter = letter - 97
            letter = (9*letter + (26 - shift))%26
            letter_val_list.append(letter+97)
        else:
            letter = letter - 97
            letter = ( 9*letter - shift) %26
            letter_val_list.append(letter+97)
    return (letter_val_list)
def Plaintext(plaintext_values):
    plaintext = ""
    for value in range(0, len(plaintext_values)):
        letter = chr(plaintext_values[value])
        plaintext += letter
    return (plaintext)

def main():
    
    tcab_file = open('tcab.txt','r')
    cyphertext_list = tcab_file.read()
    tcab_file.close()
    shift = 1
    while shift < 27:
        plaintext_values = Decrypting_String(cyphertext_list, shift)
        plaintext = Plaintext(plaintext_values)
        print(" The plaintext is: ", plaintext, "Shift: ", shift)
        shift += 1
        
        

# encryption_function = 3x + beta for some beta
#Decrypt function = y = 3x + beta = y-beta = 3 alpha
#= alpha = return_inverse(3) *(y-beta)
#9(y-beta) = 9y - 9*beta = alpha
#alpha = 9*cipher





if __name__ == "__main__":
    main()
