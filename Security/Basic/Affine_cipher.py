from transmuter import *
from Extended_Euclid import *
"""
Hệ mã Affine 
"""
def Encrypt(s,k,t): #S - string, k- pair key, l-TableName
    temp_arr=To_Numb(s,t)
    enc_Numb_arr = []
    nt=int(get_Code_table(t)["base"])
    for n in temp_arr:
        tmp=(k[0]*int(n)+k[1])%nt  #Công thức mã hóa
        enc_Numb_arr.append(tmp)
    return To_String(enc_Numb_arr,t).upper()

def Decrypt(s,k,t): #S - string, k- pair key, l-TableName
    temp_arr=To_Numb(s,t)
    enc_Numb_arr = []
    nt=int(get_Code_table(t)["base"])
    euclidA=EuclidE(k[0],nt)
    for n in temp_arr:
        tmp=(euclidA*(int(n)-k[1]))%nt  
        enc_Numb_arr.append(tmp)
    return To_String(enc_Numb_arr,t).lower()