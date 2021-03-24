from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import Crypto_module as Module
from Crypto_module import clear
from Cryptodome.Util import number as Crypto_Number
from Cryptodome import Random as Crypto_Rand
import traceback
import pyfiglet
#define
##Folder
Private_file = 'key/RSA_private.key'
Public_file = 'key/RSA_public.key'
##Variable
bits = 60
custom_fig = pyfiglet.Figlet(font='standard')
banner = custom_fig.renderText("* R S A  T O O L *")
#Function
##Function for key
###KeyE
def ChooseE(n):
    """
    This function for choose E.
    """
    while True:
        e = Crypto_Number.getRandomRange(2,n)
        if(Module.gcd(e,n)==1):
            return e
###Private & Public key 
def ChooseKeys(choice=1,file=Private_file,file2=Public_file):
    """
    This function generate pubic key and private key
    """
    p,q = None,None
    if choice == 1:
        # Auto generate p, q then calculate n, totient (Choice 1)
        p = Crypto_Number.getPrime(bits, randfunc=Crypto_Rand.get_random_bytes)
        q = p
        while q == p:
            q = Crypto_Number.getPrime(bits, randfunc=Crypto_Rand.get_random_bytes)
    else:
        # Auto  calculate n, totient (Choice 2)
        p = int(input("p = "))
        q = p
        while p == q:
            q = int(input("q = "))
    
    n = p * q
    totient = (p - 1) * (q - 1)
    # generate e
    e = ChooseE(totient)
    # calculate d
    d = Module.egcd(e,totient)
    # save to file 
    ## Private key
    try:
        with open(file,'w+') as pri_file:
            pri_file.write(str(n)+'\n')
            pri_file.write(str(d)+'\n')
            pri_file.close()
    except IOError or FileExistsError or FileNotFoundError:
        print("Can't write to file!!!")
        print(traceback.format_exc()) # for debug
        
    ## Public key 
    try:
        with open(file2, 'w+') as pub_file:
            pub_file.write(str(n)+'\n')
            pub_file.write(str(e)+'\n')
            pub_file.close()
    except IOError or FileExistsError or FileNotFoundError:
        print("Can't write to file!!!")
        print(traceback.format_exc())
    

def encrypt(msg,fl=Public_file):
    """
    we not have docstring here
    """
    encrypted = None
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
        n = int(f.readline())
        e = int(f.readline())
        f.close()

        m = bytes_to_long(str(msg).encode('utf-8'))
        encrypted = pow(m,e,n)

    return encrypted

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
        n = int(f.readline())
        d = int(f.readline())
        f.close()

        decrypted = long_to_bytes(pow(int(encrypted),d,n))

    return decrypted

def key_menu(fl=Private_file,fl2=Public_file):
    choice = 0
    print("Select key generate mode:\n1. Auto\n2. Manual\n")
    while choice == 0:
        try:
            choice = int(input("Your Choice(default or None is 1): "))
        except ValueError :
            choice = 1
        if choice == 1:
            ChooseKeys(1,fl,fl2)
        else:
            choice2 = 0
            print("Select mode:\n\n1. auto calculate\n2. Manual private key file\n3. Manual public key file")
            while choice2 == 0:
                try:
                    choice2= int(input("Your Choice(default or None is 1): "))
                except ValueError :
                    choice2 = 1
                if choice2 == 1:
                    ChooseKeys(2)
                elif choice2 == 2:
                    n = int(input("n key: ")) 
                    d = int(input("d key: "))
                    try:
                        with open(fl,'w+') as pri_file:
                            pri_file.write(str(n)+'\n')
                            pri_file.write(str(d)+'\n')
                            pri_file.close()
                    except IOError or FileExistsError or FileNotFoundError:
                        print("Can't write to file!!!")
                        print(traceback.format_exc())
                elif choice2 == 3: 
                    n = int(input("n key: ")) 
                    e = int(input("e key: "))
                    try:
                        with open(fl2, 'w+') as pub_file:
                            pub_file.write(str(n)+'\n')
                            pub_file.write(str(e)+'\n')
                            pub_file.close()
                    except IOError or FileExistsError or FileNotFoundError:
                        print("Can't write to file!!!")
                        print(traceback.format_exc())
    else:
        r = input("Continue(y/n)? ")
        if r == "y" or r == "yes":
            clear()
            return 0
        else:
            return 4

def RSA_menu():
    """
    I created this function for rsa menu 
    """
    clear()
    choice_tool = 0
    while choice_tool > 5 or choice_tool < 1:
        print(banner)
        print("\n1. Create key file\n2. Encrypt\n3. Decrypt\n4. Quit")
        try:
            choice_tool = int(input("Your Choice(default is 4): "))
        except ValueError :
            choice_tool = 4
        if choice_tool == 1 :
            clear()
            choice_tool = key_menu()
        elif choice_tool == 2:
            msg = input("Input some thing for encrypt: ")
            print("Encrypted: ",encrypt(msg))
        elif choice_tool == 3:
            msg = input("Input some thing for decrypt: ")
            print("Decrypted: ",decrypt(msg))
        elif choice_tool == 4:
            print("Ok! Quitting...")
            raise SystemExit
        else:
            clear()
            print("Tool you choice not available!\nChoice below!")
    else:
        r = input("Continue(y/n)? ")
        if r == "y" or r == "yes":
            RSA_menu()
        else: 
            print("Ok! Quitting...")
            raise SystemExit
        
#Main for debug
# if __name__ == "__main__":
#     RSA_menu()