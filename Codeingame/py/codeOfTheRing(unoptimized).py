magicPhrase = str(input()).upper()
validSequence = ""

def charToBrainFck(chr=" ",chr2=" "):
    if (chr == " " and chr2 == " ") or chr == chr2:
        return ".>"
    elif chr == " " or chr2 == " ":
        if chr != " ": # chr2 is space and chr is not space convert chr to space move to after Z or before A
            if ord(chr) < 77:
                return "-" * (ord(chr) - 64) + ".>"
            else:
                return "+" * (91 - ord(chr)) + ".>"
        elif chr2 != " ": # chr is space and chr2 is not space convert chr2 to space move to after Z or before A
            if ord(chr2) < 77:
                return "+" * (ord(chr2) - 64) + ".>"
            else:
                return "-" * (91 - ord(chr2)) + ".>"
    else:
        if ord(chr) <= ord(chr2):
            return "+" * (ord(chr2) - ord(chr)) + ".>"
        else:
            return "-" * -(ord(chr2) - ord(chr)) + ".>"

last_str = ''

if len(magicPhrase) < 30:
    validSequence = "".join([charToBrainFck(" ",magicPhrase[i]) for i in range(len(magicPhrase))])
else:
    arr = [magicPhrase[i:i+30] for i in range(0,len(magicPhrase),30)] # split magicPhrase into chunks of 30
    validSequence = "".join([charToBrainFck(" ",arr[0][i]) for i in range(len(arr[0]))]) # calculate offset of first 30 characters
    last_str = arr[0]
    for i in range(1,len(arr)):
        for j in range(len(arr[i])):
            validSequence += charToBrainFck(last_str[j],arr[i][j])
        last_str = arr[i]
print(validSequence)