import re
def Function(a):
    dem,temp = 0,0
    # debg = [] //debug
    for item in a:
        if int(item)%10==0: #<=Nah dont ask me why pls
            dem+=1
            temp+=int(item)
            # debg.append(item) //debug
    # print(debg) //debug
    return temp/dem , dem
           
    
if __name__ == '__main__':
    a = input("Nhap vao mot mang: ")
    a = re.split(',| |;',a)
    print("So cac so chia het cho ca 2 va 5: ", Function(a)[1],"\nTBC: ",Function(a)[0])
    print
