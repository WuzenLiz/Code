from transmuter import *
"""
Hệ mã Dịch Vòng
"""
def Encrypt(s,k,t): #S - string, k- key, l-TableName
    temp_arr=To_Numb(s,t)
    enc_Numb_arr = []
    nt=int(get_Code_table(t)["base"])
    for n in temp_arr:
        tmp=(int(n)+k)%nt  
        enc_Numb_arr.append(tmp)
    return To_String(enc_Numb_arr,t).upper()

def Decrypt(s,k,t): #S - string, k- key, l-TableName
    temp_arr=To_Numb(s,t)
    enc_Numb_arr = []
    nt=int(get_Code_table(t)["base"])
    for n in temp_arr:
        tmp=(int(n)-k)%nt  
        enc_Numb_arr.append(tmp)
    return To_String(enc_Numb_arr,t).lower()
