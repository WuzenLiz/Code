from tokenize import Number
from transmuter import *
from Extended_Euclid import *
import numpy as npy

def key_inv(k,t):
    """
    npy.linalg.det -> tinh det cua ma tran
    npy.linalg.inv -> tinh matran bu nghich dao cua matran goc
    """
    nt=int(get_Code_table(t)["base"])
    detk=int(npy.linalg.det(k))
    det_inv=EuclidE(detk,nt)%nt
    return  det_inv*npy.round(detk*npy.linalg.inv(k)).astype(int)%nt
    

def Encrypt(s,k,t): #S - string, k- key, l-TableName
    k=npy.array(k)
    String_Matrix = []
    Encrypt_String = ''
    nt=int(get_Code_table(t)["base"])
    for i in range(len(s)):
        String_Matrix.append(To_Numb(s[i],t))
    String_Matrix=npy.array(sum(String_Matrix,[])).astype(int)
    Split_Str_arr =[String_Matrix[i : i + int(k.shape[0])] for i in range(0, len(String_Matrix), int(k.shape[0]))] 
    for n in Split_Str_arr:
        n = npy.transpose(npy.asarray(n))[:, npy.newaxis]
        while n.shape[0] != k.shape[0]:
            n = npy.append(n, To_String('',t))[:, npy.newaxis]
        numbers = npy.dot(k, n) % nt
        n = numbers.shape[0] 
        for idx in range(n):
            number = int(numbers[idx, 0])
            Encrypt_String += To_String(number,t)
    return Encrypt_String.upper()

def Decrypt(s,k,t): #S - string, k- key, l-TableName
    k=npy.array(key_inv(k,t))
    String_Matrix = []
    Encrypt_String = ''
    nt=int(get_Code_table(t)["base"])
    for i in range(len(s)):
        String_Matrix.append(To_Numb(s[i],t))
    String_Matrix=npy.array(sum(String_Matrix,[])).astype(int)
    Split_Str_arr =[String_Matrix[i : i + int(k.shape[0])] for i in range(0, len(String_Matrix), int(k.shape[0]))] 
    for n in Split_Str_arr:
        n = npy.transpose(npy.asarray(n))[:, npy.newaxis]
        while n.shape[0] != k.shape[0]:
            n = npy.append(n, To_String('',t))[:, npy.newaxis]
        numbers = npy.dot(k, n) % nt
        n = numbers.shape[0] 
        for idx in range(n):
            number = int(numbers[idx, 0])
            Encrypt_String += To_String(number,t)
    return Encrypt_String.lower()