#!/usr/bin/env python
# coding: utf-8

import random
import math
import os
import struct
'''
Author: ジョシュアモル
Date: March, 6, 2020
Contact: devr4ndom@gmail.com
Version: 1
'''

'''
Source:        Paul Nelson Baker
Source:        hivert
Website:       https://stackoverflow.com/questions/18940194/using-extended-euclidean-algorithm-to-create-rsa-private-key
Website:       https://stackoverflow.com/questions/42422921/multiple-subset-sum-calculation
'''
def egcd(a, b):
    modulus = a
    x, lastX = 0, 1
    y, lastY = 1, 0
    while (b != 0):
        q = a // b
        a, b = b, a % b
        x, lastX = lastX - q * x, x
        y, lastY = lastY - q * y, y
    if (lastY < 0):
        lastY = modulus + lastY
    return (lastY)

def subSetSum(array, target):
    res = {0 : []}
    for i in array:
        newres = dict(res)
        for v, l in res.items():
            if v+i < target:
                newres[v+i] = l+[i]
            elif v+i == target:
                return l+[i]
        res = newres
    return None

def decrypt(encryptedMessage, modulus, privateKey):
    inverseV = egcd(modulus, privateKey)
    decryptedMessage = []
    for element in encryptedMessage:
        decryptedMessage.append(element * inverseV % modulus)
    return decryptedMessage


def binaryOrder(array, message):
    bindumpArray = []
    for text in message:
        subSet = []
        subSet = subSetSum(array, text)
        print("subSetSum of %d: \n%s" % (text, subSet))
        bindump = ""
        for x in range(0, len(array)):
            bindump = bindump + "0"
        #print(bindump)
        for element in subSet:
            bindump = bindump[:array.index(element)] + '1' + bindump[array.index(element)+1:]
        bindumpArray.append(bindump)
    return bindumpArray

publicKey = {80086, 124209, 791676, 16445764, 1973255276, 272578856242022}
encryptedMessage = {272578873763843, 1989861212, 16730145, 16730145, 16525850}
modulus = 308147912
privateKey = 77216739

print("Question 1:  16-bit knapsack cipher has public key:\n")
decryptedA = decrypt(publicKey, modulus, privateKey)
decryptedA = sorted(decryptedA)

decryptedMessage = decrypt(encryptedMessage, modulus, privateKey)

print("Reversed Trap Door Set: \n%s\n\nDecrypted Message Sums: \n%s\n" % (decryptedA, decryptedMessage))

binaryMessage = binaryOrder(decryptedA, decryptedMessage)

print("\n\nBinary Message   \"Answer Key?\":\n%s\n\n\n\n\n" % (binaryMessage))