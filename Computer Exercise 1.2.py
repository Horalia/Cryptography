#_________________[HORALIA ARMAS]__________________________________
#HOMEWORK 1: PROBLEM 2
#ANSWER: EVEEXPECTSEGGSFORBREAFAST = EVE EXPECTS EGGS FOR BREAKFAST
#IMPORT
from collections import Counter


#Opens and Read "lcll.txt"
decrypt_object = open('lcll.txt','r')
list_encrypted = decrypt_object.read() #Reads lcll.txt and copies its content into list encrypted
decrypt_object.close() #closes lcll.txt
#Makes empty string 
letters = ""
#loops through the string read from file, and each individual item gets added to a string and a space to be used in Counter
for item in list_encrypted:
    letters += item + " "

Frequency = Counter(letters.split())#Makes a dictionary with letters and their frequency i.e., a appears 3 times so it will be seen in the dictionary as {'a':2,...etc.}


for most_Freq in Frequency:
    Most_Frequent = most_Freq
    break
plaintext = ord(Most_Frequent) - 97

most_com_Let = 4
distance = plaintext - 4

plaintext_ans = ""

for letter in list_encrypted:
    letter = ord(letter)
    if letter >= 97 and letter < 97 + 7:
        letter = letter + (26 - 7)
        #else its in bounds
    else:
        letter = letter - 7

    plaintext_ans += chr(letter)
print(plaintext_ans )


#Makes Vector of all Zeroes, since not all letters are in the cypher text
#vector = [0] * 26
#Gets all the values from the Frequency keys.
#The keys are then turned into digits using ascii and subtracted by 98 in order to get the numbers fro 0-25
#A is 0, After it goes to the Vector that was originally all zeroes finds the letters index
#In the correct index the frequency of the letter divided by the total number of letters counted.
##for items in Frequency.keys():
##    index = ord(items) -97
##    vector[index] = Frequency.get(items)/length_Num_letters
##print(vector)
##   

