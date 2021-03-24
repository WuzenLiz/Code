import json

data = {}
dataname = {}

def auto_keys_generator(n):
    sf = int(input("Key start from: "))
    if sf==0:
        for k in range(sf,n):
            value=input("Enter data: ")
            dataname[int(k)]=value
    else:
        for k in range(sf,n+1):
            value=input("Enter data: ")
            dataname[int(k)]=value
        
def manual_key_data(n):
    for NODs in range(n): #NODs aka number of Datas
        k=input("Enter key: ")
        value=input("Enter data: ")
        dataname[int(k)]=value

def Data_generator(n):
    print("1. Auto generator key\n2. Manual input")
    choice=int(input("Your choice: ")) 
    if choice == 1:
        auto_keys_generator(n)
    elif choice == 2:
        manual_key_data(n)
    else:
        print("You must choice:\n1. Auto generator key\n2.Manual input")

def Save_json(d,filename='base.json'):
    with open("base.json", 'w') as file:
        json.dump(d, file, sort_keys=True, indent=2) 

def define_info():
    base = int(input("What your list base on? "))
    d = {'base':base}
    dataname.update(d)

if __name__ == "__main__":
    data_name=input("Enter data name: ")
    key = int(input("Input number of key: "))
    define_info()
    Data_generator(key)
    data[data_name]=dataname
    with open("base.json") as file:
        jdata = json.load(file)
        if data_name in jdata:
            temp_data=jdata[data_name]
            temp_data.update(dataname)
            Save_json(jdata)
        else:
            temp_data=jdata
            temp_data.update(data)
            Save_json(jdata)