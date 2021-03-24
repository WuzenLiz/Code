"""
Hệ mã Vigenere
"""
from transmuter import *
def sync_key(s,k):
    """
    Tái tạo độ dài sao cho k == s
    """
    if len(k)==len(s):
        return k
    elif len(s)<len(k):
        k=k[:-(len(k)-len(s))]   
        return k;  
    else:
        for i in range(len(s) - 
                       len(k)): 
            k.append(k[i % len(k)]) 
        return("" . join(k))

def Encrypt(s,k,t):
    key=sync_key(s,k)
    key_NumArray=To_Numb(key,t)
    string_NumArray=To_Numb(s,t)
    nt=int(get_Code_table(t)["base"])
    encrypted_array = []
    for i in range(len(string_NumArray)):
        tmp = (int(string_NumArray[i])+int(key_NumArray[i]))%nt
        encrypted_array.append(tmp)
    return To_String(encrypted_array,t).upper()

def Decrypt(s,k,t):
    key=sync_key(s,k)
    key_NumArray=To_Numb(key,t)
    string_NumArray=To_Numb(s,t)
    nt=int(get_Code_table(t)["base"])
    decrypted_array = []
    for i in range(len(string_NumArray)):
        tmp = (int(string_NumArray[i])-int(key_NumArray[i])+26)%nt
        decrypted_array.append(tmp)
    return To_String(decrypted_array,t).lower()
