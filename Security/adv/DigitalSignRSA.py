import RSA as rsa
import pyfiglet
import Crypto_module as Module
from Crypto_module import clear
#Define
Private_file = 'key/RSA_ds_private.key'
Public_file = 'key/RSA_ds_public.key'
custom_fig = pyfiglet.Figlet(font='standard',width=175)
banner = custom_fig.renderText("R S A  D I G I T A L  S I G N E R  T O O L")
#Function
##Sign
def sign_function(x,fl=Private_file):
    signed = None
    try:
        f = open(fl,'r')
    except FileNotFoundError:
        print('Man! You not have file that have public key!')
        choice = None
        while choice == None:
            choice = input("Create(y/n)? ")
            if choice == 'y' or choice  == 'yes':
                rsa.key_menu()
            else:
                print("Warning! An error coming! Force Quit!!!!")
                raise SystemExit
    else:
        n = int(f.readline())
        d = int(f.readline())
        f.close()
        signed = pow(int(x),d,n)
    return x, signed
##Check sign
def check_function(x,y,e,n):
    return x == pow(y,e,n)
##Menu
def rsa_ds_menu():
    clear()
    choice_tool = 0
    while choice_tool > 5 or choice_tool < 1:
        print(banner)
        print("\n1. Create key file\n2. Sign\n3. check\n4. Quit")
        try:
            choice_tool = int(input("Your Choice(default is 4): "))
        except ValueError :
            choice_tool = 4
        if choice_tool == 1 :
            clear()
            choice_tool = rsa.key_menu(Private_file,Public_file)
        elif choice_tool == 2:
            msg = input("Input some thing for Sign: ")
            print("signed: (%s,%s)" % sign_function(msg))
        elif choice_tool == 3:
            print("\nInsert public key for checking sign\n1. From created file\n2. Manual\n")
            choice = 0
            n,d = 0,0 
            while choice == 0:
                try:
                    choice = int(input("Your Choice(default is 1): "))
                except ValueError :
                    choice = 1
            else:
                if choice == 1:
                    try:
                        f = open(Public_file,'r')
                    except FileNotFoundError:
                        print('Man! You not have file that have public key!')
                        choice = None
                        while choice == None:
                            choice = input("Create(y/n)? ")
                            if choice == 'y' or choice  == 'yes':
                                rsa.key_menu()
                            else:
                                print("Warning! An error coming! Force Quit!!!!")
                                raise SystemExit
                    else:
                        n = int(f.readline())
                        e = int(f.readline())
                        f.close()
                        print("Please input your Sign!")
                        x = int(input("x: "))
                        y = int(input("y: "))
                        print("Checked: ",check_function(x,y,e,n))
                else:
                    print("Please input your key!")
                    e = int(input("e: "))
                    n = int(input("n: "))
                    print("Please input your Sign!")
                    x = int(input("x: "))
                    y = int(input("y: "))
                    print("Checked: ",check_function(x,y,e,n))
            
        elif choice_tool == 4:
            print("Ok! Quitting...")
            raise SystemExit
        else:
            clear()
            print("Tool you choice not available!\nChoice below!")
    else:
        r = input("Continue(y/n)? ")
        if r == "y" or r == "yes":
            rsa_ds_menu()
        else: 
            print("Ok! Quitting...")
            raise SystemExit

if __name__ == "__main__":
    rsa_ds_menu()