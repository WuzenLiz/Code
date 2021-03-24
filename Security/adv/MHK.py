from Cryptodome.Util.number import bytes_to_long
import Crypto_module as Module
from Crypto_module import clear
from Cryptodome.Util import number as Crypto_Number
from Cryptodome import Random as Crypto_Rand
from functools import reduce
#Define
##File
Private_file = 'key/MHK_private.key'
Public_file = 'key/MHK_public.key'
##Varialble
bits = 32
#Function
##Check S array
def Is_Superincreasing(S):
    """
    This function using for checking your array or auto-regenerated is Superincreasing
    """
    temp_var=0
    for n in S:
        if n<=temp_var:
            return False
            break
        temp_var += n
    return True

##Sum of elem in array
def Sum_elem(S):
    """
    This return sum of all elem in array S
    """
    SumE=0
    for n in S:
        SumE += n
    return SumE

##Choose P
def ChooseP(S):
    """
    This function for choose p.
    """
    P = 0
    while Is_Superincreasing(S) and P < Sum_elem(S):
        P = Crypto_Number.getRandomInteger(bits,randfunc=Crypto_Rand.get_random_bytes)
        return P 

##Choose a
def ChooseA(P):
    """
    This function for choose E.
    """
    while True:
        a = Crypto_Number.getRandomRange(2,P-1)
        if(Module.gcd(a,P)==1):
            return a

##Generate array S
def GenerateS(n):
    """
    Generate an array have n element
    """
    S = []
    i = 1
    while len(S) < n :
        elem = Crypto_Number.getRandomInteger(bits//2+i,randfunc=Crypto_Rand.get_random_bytes)
        while elem > Sum_elem(S):
            S.append(elem)
            i += 1
    else:
        return S

## Solve t
def Solve_t(a,S,p):
    """
    docstring? There is no docstring
    """
    t = []
    for elem in S:
        t.append((a*elem)% p)
    return t

##Keys function 
def KeysFunction(choice=1):
    """
    This function generate pubic key and private key and save to file
    """
    #Generate S
    S = []
    if choice == 1:
        # Auto generate elem for S array (Choice 1)
        n = int(input("Input number of element in S: "))
        S = GenerateS(n)
        print("Generated an S array")
    else:
        # Auto  calculate n, totient (Choice 2)
        n = int(input("Input number of element in S: "))
        while Is_Superincreasing(S): 
            for i in range(n):
                elem = int(input("Input elem ",i,": "))
                S.append(elem)

    # generate P
    p = ChooseP(S)
    # generate A
    a = ChooseA(p)
    # calculate d
    t = Solve_t(a,S,p)
    # save to file 
    ## Private key
    try:
        with open(Private_file,'w+') as pri_file:
            pri_file.write(str(a)+'\n')
            pri_file.write(str(p)+'\n')
            for elem in S:
                pri_file.write("{}_".format(elem))
            pri_file.close()
    except IOError or FileExistsError or FileNotFoundError:
        print("Can't write to file!!!")
        #print(traceback.format_exc()) # for debug
        
    ## Public key 
    try:
        with open(Public_file, 'w+') as pub_file:
            for elem in t:
                pub_file.write("{}_".format(elem))
            pub_file.close()
    except IOError or FileExistsError or FileNotFoundError:
        print("Can't write to file!!!")
        #print(traceback.format_exc())
##encry support
def sp_enc_func(n,k):
    temp = 0
    m = [char for char in n]
    for i in range(len(m)):
        if m[i]=='0':
            if i > len(k)-1:
                temp += int(k[i-(len(k))])
            else:
                temp += int(k[i])
    return temp
##decry support
def Sp_dec_func(y,a,p,k):
    C = (Module.egcd(a,p)*y)%p
    s = []
    temp = C
    rev_k = k[::-1]
    print('\ntemp\t\tk\t\tS')    
    for i in range(len(k)):
        if int(rev_k[i]) <= temp:
            temp -= int(rev_k[i])
            s.append("1")
            print(temp,"\t",int(rev_k[i]),"\t\t",s)
        else:
            s.append("0")
            print(temp,"\t",int(rev_k[i]),"\t\t",s)
    s = "".join(s)
    return s

#Encrypt & Decrypt
##Encrypt
def encrypt(msg,fl=Public_file):
    """
    we not have docstring here
    """
    encrypted = []
    try:
        f = open(fl,'r')
    except FileNotFoundError:
        print('Man! You not have file that have public key!')
        choice = None
        while choice == None:
            choice = input("Create(y/n)? ")
            if choice == 'y' or choice  == 'yes':
                key_menu()
            else:
                print("Warning! An error coming! Force Quit!!!!")
                raise SystemExit
    else:
        t = f.readline().split("_")
        t = t[:-1]
        f.close()
        m = (' '.join('{0:08b}'.format(ord(x), 'b') for x in msg)).split(' ')
        print(m)
        for elem in m:
            encrypted.append(sp_enc_func(elem,t))
    return encrypted

##Decrypt
def decrypt(encrypted,fl=Private_file):
    """
    we not have docstring here
    """
    decrypted = None
    try:
        f = open(fl,'r')
    except FileNotFoundError:
        print('Man! You not have file that have public key!')
        choice = None
        while choice == None:
            choice = input("Create(y/n)? ")
            if choice == 'y' or choice  == 'yes':
                key_menu()
            else:
                print("Warning! An error coming! Force Quit!!!!")
                raise SystemExit
    else:
        a = int(f.readline())
        p = int(f.readline())
        k = f.readline().split("_")
        k = k[:-1]
        f.close()

        if type(encrypted) == list:
            decrypted = []
            for taget in encrypted:
               decrypted.append(Sp_dec_func(taget,a,p,k)) 
        else:
            decrypted = Sp_dec_func(encrypted,a,p,k)

    return decrypted
    
##Menu
###Key menu
def key_menu():
    choice = 0
    print("Select key generate mode:\n1. Auto\n2. Manual\n")
    while choice == 0:
        try:
            choice = int(input("Your Choice(default or None is 1): "))
        except ValueError :
            choice = 1
        if choice == 1:
            KeysFunction(1)
        else:
            choice2 = 0
            print("Select mode:\n\n1. auto calculate\n2. Manual private key file\n3. Manual public key file")
            while choice2 == 0:
                try:
                    choice2= int(input("Your Choice(default or None is 1): "))
                except ValueError :
                    choice2 = 1
                if choice2 == 1:
                    KeysFunction(2)
                elif choice2 == 2:
                    n = int(input("n key: ")) 
                    d = int(input("d key: "))
                    try:
                        with open(Private_file,'w+') as pri_file:
                            pri_file.write(str(n)+'\n')
                            pri_file.write(str(d)+'\n')
                            pri_file.close()
                    except IOError or FileExistsError or FileNotFoundError:
                        print("Can't write to file!!!")
                        #print(traceback.format_exc())
                elif choice2 == 3: 
                    n = int(input("n key: ")) 
                    e = int(input("e key: "))
                    try:
                        with open(Public_file, 'w+') as pub_file:
                            pub_file.write(str(n)+'\n')
                            pub_file.write(str(e)+'\n')
                            pub_file.close()
                    except IOError or FileExistsError or FileNotFoundError:
                        print("Can't write to file!!!")
                        #print(traceback.format_exc())
    else:
        r = input("Continue(y/n)? ")
        if r == "y" or r == "yes":
            clear()
            return 0
        else:
            return 4

##Main for debug
if __name__ == "__main__":
    enc = encrypt('Hello')
    print(enc)
    print(decrypt(enc))
    