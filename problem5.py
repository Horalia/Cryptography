#---------[Horalia Armas]------------------------
#---------[Homework 1: Problem 5]------------------------
#ANSWER: IF M CHANGES AND THE SHIFT STAYS THE SAME THE ENCRYPTION ISNT AFFECTED
#FOR EXAMPLE IF M = 1 THEN M 27 AND M = 53 WILL BE THE SAME MEANWHILE THEY ARE CONGRUENT
#in this example we print M values 0-52 if we see them in half from M < 26 and M > 26 we see that they repeat in encryption while congruent.
#EXPLANATION OF ANSWER AND CODE EXAMPLE
#The example in this program is "bread" if the equation is Mx + n where N = 4
# then we see that when m is o we get [w,w,w,w,w] and when m is 26 [w,w,w,w,w]
#we can notice 1 is congruent to 27 as 27 mod26 is 1
#when m = 25 we get = [v,f,s,w,t] and when m is 51 we get [v,f,s,w,t]
#we can notice 25 is congruent to 51 as 51 mod26 is 25

def Encrypt_list(list_object, shift,m):
    letter_val_list = [] 
    for letter in list_object:
        letter = ord(letter)
        #if letter is out of bound when shift is made
        if letter >= 97 and letter < (97 + shift):
            letter = letter - 97
            letter = (m*letter +(26- shift))%26
            letter_val_list.append(chr(letter+97))
        else:
            letter = letter - 97
            letter = ( m*letter - shift ) %26
            letter_val_list.append(chr(letter+97))
    return (letter_val_list)        
    
def main():
    
    bread_file = open('bread.txt','r')
    list_plaintext = bread_file.read()
    bread_file.close()
    list_less_twentysix = []
    list_greater_twentysix = []
    shift = 4
 #   encrypt = mx+n
    m = 0
    while m < 26 and m>=0 :
         encrypted = Encrypt_list(list_plaintext,shift,m)
         list_less_twentysix.append(encrypted)
         m +=1
    print(list_less_twentysix)
    print("-----------------------------------------------")
    m = 26
    while m > 25 and m < 52:
         encrypted = Encrypt_list(list_plaintext,4,m)
         list_greater_twentysix.append(encrypted)
         m +=1
    print(list_greater_twentysix)
    print("please note the printed list on top are the same as the one below marked by '-------'")

    
    
    

if __name__ == "__main__":
    main()



