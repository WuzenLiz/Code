
from Cryptodome.Util.number import bytes_to_long, long_to_bytes
import Crypto_module as Module
from Crypto_module import clear
from Cryptodome.Util import number as Crypto_Number
from Cryptodome import Random as Crypto_Rand
#Define
bits = 10
p = Crypto_Number.getPrime(bits,randfunc=Crypto_Rand.get_random_bytes)
alpha = 2
a = Crypto_Number.getRandomInteger(bits-1,randfunc=Crypto_Rand.get_random_bytes)
beta = pow(alpha,a,p)
#encrypt
def encrypt(x):
    """
    docstring
    """
    k = Crypto_Number.getPrime(bits-1,randfunc=Crypto_Rand.get_random_bytes)
    y1 = pow(alpha,k,p)
    y2 = (x*pow(beta,k))%p

    return y1,y2

def Decrypt(y1,y2):
    """
    docstring
    """
    t1  = pow(y1,alpha,p)
    t2  = Module.egcd(t1,p)

    x = (y2*t2)%p

    return x

if __name__ == "__main__":
    e,f = encrypt(10)
    d = Decrypt(e,f)
    print(e,f, d)   