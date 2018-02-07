#--------------------[Horalia Armas]------------------------------------
#---------------------[Problem 10]--------------------------------------
#----------[Answer: jackandjillwentupthehill]---------------------------

#import
import numpy as np
import numpy.linalg as num
from numpy.linalg import inv
from fractions import Fraction
import fractions

def lcm(num1, num2):
    return int(num1*num2/fractions.gcd(num1,num2))

def return_inverse(number):
    i = int(number)
    if i < 0:
        while i < 0:
            i = i + 26
        return (int(i))
    elif i >= 0 and i <26:
        i = 1
        while (i%number != 0):
            i += 26
        return (int(i/number))
    else:
        while i > 26:
            i = i -26
    return (int(i))
def main():
    #Open and Read "zirk.txt"
    cipher_object = open('zirk.txt','r')
    list_cipher = cipher_object.read()
    cipher_object.close() #closes "zirk.txt"

    #Given Key

    key = np.array([[1,2,3,4],[4,3,2,1],[11,2,4,6],[2,9,6,4]])

    #Get the Determinant of key

    determinant_key = num.det(key)
    print(determinant_key)


    #----Get the Inverse of the Key --------------------------------
    inv_det = return_inverse(27)
    inv_key = inv(key)
    inv_Key_list =[]
    for rows in inv_key:
        row = []
        for col in rows:
            b = Fraction(col).limit_denominator()
            row.append(b) 
        inv_Key_list.append(row)

    
    non_zero = []
    lcm_list = []
    for i in inv_Key_list:
        for j in i:
            if j != 0:
                lcm_list.append(j.denominator)
                
    current_lcm = lcm(lcm_list[0], lcm_list[1])
    for number in range(2, len(lcm_list)):
        current_lcm = lcm(current_lcm, lcm_list[number])

    for k in inv_Key_list:
        numerator_list = []
        for y in k:
            numerator_list.append((((current_lcm*y).numerator)*9)%26)
        non_zero.append(numerator_list)

    print(non_zero)
        
                
            
                
                
        
        

    

    print(len(list_cipher))
    list_cipher_num = []
    for items in list_cipher:
        list_cipher_num.append(ord(items)-97)

    print(list_cipher_num)
        
    list_cipher_num_matrix = []
    row = []
    for col in range(1, len(list_cipher_num) + 1):
        if col % 4 == 0:
            row.append(list_cipher_num[col - 1])
            list_cipher_num_matrix.append(row)
            row = []
        else:
            row.append(list_cipher_num[col - 1])

    print(list_cipher_num_matrix)
    #print(list_cipher_num_matrix)
    list_decrypt = []
 
    for row in range(0, len(list_cipher_num_matrix)):
        decrypt = (np.dot(list_cipher_num_matrix[row], non_zero))%26
        list_decrypt.append(decrypt)

    
    decrypted_string = ""
    for row in list_decrypt:
        for column in row:
            decrypted_string += chr(column + 97)

    print(decrypted_string)

            
        
                
    
        
   
        

if __name__ == "__main__":
    main()

        





       
 
