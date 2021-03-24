import Caesar_cipher as Caesar
import Vigenere_cipher as Vigenere
import Affine_cipher as Affine
import Hill_cipher as hillc
from Extended_Euclid import EuclidE

if __name__ == "__main__":
    test_String = 'Lemon'
    test_key = 'Lemonade'
    table='A0Z26'
    hs_test = 'zene'
    Hkey = [[7,8],[5,9]]
    PKey=[11,22]
    print("Test result\nDecrypt\t\tEncrypt")
    Caesar_DEString = Caesar.Decrypt(test_String,5,table)
    Caesar_ENString = Caesar.Encrypt(Caesar_DEString,5,table)
    print(Caesar_DEString,'\t\t',Caesar_ENString)
    Vigenere_ENString = Vigenere.Encrypt(test_String,test_key,table)  
    Vigenere_DEString = Vigenere.Decrypt('wiyca',test_key,table)
    print(Vigenere_DEString,'\t\t',Vigenere_ENString)
    Affine_ENString = Affine.Encrypt(test_String,PKey,table)  
    Affine_DEString = Affine.Decrypt('WZZGJO',PKey,table)
    print(Affine_DEString,'\t\t',Affine_ENString)
    Hill_ENString = hillc.Encrypt(hs_test,Hkey,table)  
    Hill_DEString = hillc.Decrypt(Hill_ENString,Hkey,table)
    print(Hill_DEString,'\t\t',Hill_ENString)