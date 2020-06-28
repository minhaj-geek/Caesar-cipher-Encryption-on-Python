
alphabet_list=["A","B","C","D","E","F",
               "G","H","I","J","K","L","M","N",
               "O","P","Q","R","S","T","U","V","W",
               "X","Y","Z"]

def string_converter(list1):
    var_01=""
    for i in list1:
        var_01=var_01+i
    return var_01

key=3
print("Enter Key Number: ")
key=input(": ")
key=int(key)

print("Enter Message//Plain Text: ")
print("But Make Sure message don't Contain any spaces: ")
text=input()
text=text.upper()
cipher_list=[]
print("Plain Text: ",text)

for i in text:
    position_in_list=alphabet_list.index(i)
    position_in_list=position_in_list+key

    if(position_in_list>25):
        while(position_in_list>25):
            position_in_list-=26

    cipher_list.append(alphabet_list[position_in_list])

cipher_message=""

cipher_message=string_converter(cipher_list)
#print(cipher_list)
#string_converter(cipher_list)
print("Cipher Text: ",cipher_message)
