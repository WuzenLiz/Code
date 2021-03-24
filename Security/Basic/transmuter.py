import json
def get_Code_table(tablename):
    dicts = {}
    with open('base.json','r') as base:
        bs=json.load(base)
        dicts = bs[tablename]
        return dicts

def To_Numb(S,tablename):
    if S==None:
        return
    tmp_String = S.lower()
    tmp_String = "".join(tmp_String.split())
    Table_Data = get_Code_table(tablename)
    Numb_arr=[]
    for pos in range(len(tmp_String)):
        for key,value in Table_Data.items():
            if tmp_String[pos]==value:
                Numb_arr.append(key)
    return Numb_arr

def To_String(S,tablename):
    if S== None:
        return
    Table_Data = get_Code_table(tablename)
    tmp_String =''
    if type(S) == int:
        for key,value in Table_Data.items():
            if str(S)==key:
                tmp_String+=value
    else:
        for pos in range(len(S)):
            for key,value in Table_Data.items():
                if str(S[pos])==key:
                    tmp_String+=value
    return tmp_String