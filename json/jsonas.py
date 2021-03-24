#import
import json as json

#Define 
data = None
key=None
INPUTfile = 'data.json'
OUTPUTJsonfile = 'Dumped.json'
OUTPUTJsonfile1 = 'Dumped1.json'
OUTPUTExelfile = 'Dumped.xlsx'

#file function
def Op_File(file):
    with open(file, encoding="utf8") as json_file:
        data = json.load(json_file)
    return data

def Sv_file(file,data):  
    with open(file, 'w'  ,encoding ="utf8") as outfile:
        json.dump(data, outfile)
        print(len(data))
def convert_to_exel(infile,outfile):
    import pandas as pd
    df_json = pd.read_json(infile)
    df_json.to_excel(outfile)

#Main function
def removeduplicate(data):
    seen = []
    for item in data:
        if item not in seen:
            seen.append(item)
    return seen

def removeduplicate_by_key_until(data,k):
    result = data
    dem = 0
    for i in range(0,len(data)-2):
        for j in range(i+1,len(result)-1):       
            if data[i][k]==data[j][k]:
                del result[j-dem]
                dem+=1
    return result

def removeduplicate_by_key(data,k):
    result = data
    for item in k:
       result = removeduplicate_by_key_until(result,item)
    return result

def main():
    data = Op_File(INPUTfile)
    opdata = removeduplicate(data)
    key=["title","author","content"]
    opdata2 = removeduplicate_by_key(data,key)
    Sv_file(OUTPUTJsonfile,opdata)
    Sv_file(OUTPUTJsonfile,opdata2)
    convert_to_exel(OUTPUTJsonfile1,OUTPUTExelfile)  

if __name__ == '__main__':
    main()
    print("DONE")
    
    
        
