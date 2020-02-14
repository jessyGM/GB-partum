import boleto

def loadFile(filename):
    file= open(filename, 'r')
    try:
        lines=file.readlines()
    finally:
        file.close()
    return lines

def loadObjects():
    boletos=[]
    for line in loadFile('data.txt'):
        boletos.append(boleto.boleto(line))
    return boletos

def savefile(filename):
    file=open(filename,'w')
    try:
        for obj in loadObjects():
            file.write(obj.toString())
    finally:
        file.close()
