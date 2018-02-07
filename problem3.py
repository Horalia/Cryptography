#---------[HORALIA ARMAS]------------------------
#---------[Homework 1: Problem 3]------------------------
#ANSWER: ifyoucanreadthisthankateacher = if you can read this thank a teacher
from fractions import gcd
#Open and read "edsg.txt"
def return_inverse(number):
    i = 1
    while (i%number != 0):
        i += 26
    return (int(i/number))

edsg_file  = open('edsg.txt','r')
plaintext_file = open('plaintext_attack.txt')
list_cypher = edsg_file.read()
list_plaintext = plaintext_file.read()
plaintext_file.close()
edsg_file.close() #Close file
if_list = []
edsg_list = []
for items in list_cypher:
    edsg_list.append(ord(items)-97)
for letters in list_plaintext:
    if_list.append(ord(letters)-97)

#cypher_key = alpha*plaintext + Beta
##4 = 8*alpha + beta
##3 = 5*alpha + beta
##1 = 3*alpha
##1 * inv(3) = alpha

cypher_key_one = edsg_list[0]
cypher_key_two = edsg_list[1]
plaintext_one = if_list[0]
plaintext_two = if_list[1]

subtract_cypher = cypher_key_one - cypher_key_two
subtract_plaintext = plaintext_one - plaintext_two

alpha = subtract_cypher * return_inverse(subtract_plaintext)
beta = (cypher_key_one - (plaintext_one * alpha))%26

Decryption = ""
for cypher in edsg_list:
    Decryption += chr(((cypher-beta)*return_inverse(alpha)%26) +97)


print(Decryption)
#Euclideans Algorithm
##gcd(3,26)= 1

# 1=26+1 = 27
#check if number is divisible by 3
#if true
#27%3 = 9
#inv(3) = 9

##alpha = 1*inv(3) = 1*9 = 9 mod 26
# 4 = 8*9 + Beta
#4 - 72 = beta
# -68 = beta = -68%26 = 10mod26
#y = 9x + 10
# (y-10)*inv(9) = x
#gcd(9,26) = 1
#1=26+1
#27%9 = 0
#27/9 = 3
#(y-10)*3 = x decrypting equation
#(4-10)*3 = -18mod26 = 8 = i
#(3-10)*3== -21 mod26 = 5 = f


##cypher_letter_value = alpha*plaintext_letter +Beta
##cypher[0]= alpha*plaintextletter[0] + Beta
##cypher[1]= alpha*plaintextletter[1] + Beta
##
##-1 = 3*alpha
##25 = 3*alpha
##-----------------
